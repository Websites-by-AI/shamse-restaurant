#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Mailjet Email Dispatch & Automated Relay Engine
Supports:
  1. Mailjet Send API v3.1 (https://api.mailjet.com/v3.1/send)
  2. Mailjet SMTP Relay (in-v3.mailjet.com:587 TLS / 465 SSL)
  3. Deliverable attachments (PDF Dossier, PPTX Pitch Deck) Base64 encoded
  4. Suppression list compliance (automation/suppression.jsonl)
  5. Simulation / Dry-run sandbox when Secret Key is pending generation or account in review
  6. Audit logging into automation/dispatch_log.json
"""

import os
import sys
import json
import base64
import re
import smtplib
import ssl
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from datetime import datetime, timezone

try:
    import requests
    REQUESTS_AVAILABLE = True
except ImportError:
    REQUESTS_AVAILABLE = False

ROOT = os.path.dirname(os.path.abspath(__file__))
LOG_FILE = os.path.join(ROOT, "dispatch_log.json")
SUPPRESSION_FILE = os.path.join(ROOT, "suppression.jsonl")
REPO_ROOT = os.path.dirname(ROOT)

MAILJET_API_URL = "https://api.mailjet.com/v3.1/send"
MAILJET_SMTP_SERVER = "in-v3.mailjet.com"
MAILJET_SMTP_PORT_TLS = 587
MAILJET_SMTP_PORT_SSL = 465

DEFAULT_API_KEY = "b5af6ec2f275931f9216b8c7eb9c03eb"
DEFAULT_FROM_EMAIL = "partnership@mizbanistanbul.com"
DEFAULT_FROM_NAME = "Mizban Istanbul & Shamse"
DEFAULT_REPLY_TO = "concierge@mizbanistanbul.com"


class MailjetEmailDispatcher:
    def __init__(self, api_key=None, secret_key=None, from_email=DEFAULT_FROM_EMAIL, from_name=DEFAULT_FROM_NAME):
        self.api_key = api_key or os.environ.get("MAILJET_API_KEY", DEFAULT_API_KEY)
        self.secret_key = secret_key or os.environ.get("MAILJET_SECRET_KEY", "")
        self.from_email = from_email
        self.from_name = from_name

    def get_credential_status(self):
        """
        Analyzes the state of the Mailjet configuration.
        """
        has_api_key = bool(self.api_key and len(self.api_key) >= 20)
        has_secret_key = bool(self.secret_key and len(self.secret_key) >= 16 and self.secret_key.lower() != "not generated")

        if has_api_key and has_secret_key:
            state = "READY_FOR_LIVE_DISPATCH"
            msg = "Both API Key and Secret Key are present. Live dispatch is unlocked."
        elif has_api_key and not has_secret_key:
            state = "PENDING_SECRET_KEY"
            msg = "API Key is configured (b5af...), but Secret Key is 'Not generated' or in account review. Simulation mode active."
        else:
            state = "UNCONFIGURED"
            msg = "Missing Mailjet API credentials."

        return {
            "state": state,
            "api_key_masked": f"{self.api_key[:6]}...{self.api_key[-4:]}" if self.api_key else "None",
            "has_secret_key": has_secret_key,
            "smtp_server": MAILJET_SMTP_SERVER,
            "smtp_port": MAILJET_SMTP_PORT_TLS,
            "message": msg
        }

    def is_suppressed(self, email):
        """Check against suppression ledger."""
        if not os.path.exists(SUPPRESSION_FILE):
            return False
        clean = email.strip().lower()
        try:
            with open(SUPPRESSION_FILE, "r", encoding="utf-8") as f:
                for line in f:
                    line = line.strip()
                    if not line:
                        continue
                    rec = json.loads(line)
                    if rec.get("email", "").strip().lower() == clean:
                        return True
        except Exception:
            pass
        return False

    @staticmethod
    def validate_email_syntax(email):
        pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        return bool(re.match(pattern, str(email).strip()))

    def prepare_mailjet_attachment(self, file_path, custom_filename=None):
        """Encodes local deliverable file to Mailjet v3.1 attachment format."""
        if not os.path.exists(file_path):
            return None
        filename = custom_filename or os.path.basename(file_path)
        ext = os.path.splitext(filename)[1].lower()

        content_type_map = {
            ".pdf": "application/pdf",
            ".pptx": "application/vnd.openxmlformats-officedocument.presentationml.presentation",
            ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document",
            ".png": "image/png",
            ".jpg": "image/jpeg",
            ".jpeg": "image/jpeg",
            ".json": "application/json"
        }
        content_type = content_type_map.get(ext, "application/octet-stream")

        with open(file_path, "rb") as f:
            content_b64 = base64.b64encode(f.read()).decode("utf-8")

        return {
            "ContentType": content_type,
            "Filename": filename,
            "Base64Content": content_b64
        }

    def send_via_api(self, to_email, to_name, subject, html_content, text_content=None, attachments=None, reply_to=DEFAULT_REPLY_TO):
        """
        Sends email using Mailjet Send API v3.1 (HTTP Basic Auth).
        Falls back to simulation mode if Secret Key is not configured.
        """
        to_email = to_email.strip()
        status_info = self.get_credential_status()

        if not self.validate_email_syntax(to_email):
            return {
                "success": False,
                "error": f"Invalid recipient email syntax: {to_email}",
                "simulated": False
            }

        if self.is_suppressed(to_email):
            return {
                "success": False,
                "error": f"Recipient {to_email} is on the suppression list (KVKK/GDPR opt-out).",
                "suppressed": True
            }

        # Check if live dispatch is possible
        if status_info["state"] != "READY_FOR_LIVE_DISPATCH" or not REQUESTS_AVAILABLE:
            # Execute simulation / audit mode
            simulated_id = f"sim_mj_{int(datetime.now(timezone.utc).timestamp())}_{abs(hash(to_email)) % 10000}"
            log_entry = {
                "message_id": simulated_id,
                "provider": "mailjet_api_v3.1",
                "mode": "simulation",
                "recipient": to_email,
                "recipient_name": to_name,
                "sender": f"{self.from_name} <{self.from_email}>",
                "subject": subject,
                "attachments_count": len(attachments) if attachments else 0,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "status": "simulated_success",
                "reason": status_info["message"]
            }
            self._write_log(log_entry)
            return {
                "success": True,
                "simulated": True,
                "message_id": simulated_id,
                "status": "simulated_success",
                "detail": status_info["message"],
                "provider": "mailjet_v3.1"
            }

        # Live dispatch with Mailjet v3.1 API
        message_dict = {
            "From": {
                "Email": self.from_email,
                "Name": self.from_name
            },
            "To": [
                {
                    "Email": to_email,
                    "Name": to_name or to_email
                }
            ],
            "Subject": subject,
            "HTMLPart": html_content,
            "TextPart": text_content or ""
        }

        if reply_to:
            message_dict["ReplyTo"] = {"Email": reply_to}

        if attachments:
            message_dict["Attachments"] = attachments

        payload = {"Messages": [message_dict]}

        try:
            resp = requests.post(
                MAILJET_API_URL,
                auth=(self.api_key, self.secret_key),
                headers={"Content-Type": "application/json"},
                json=payload,
                timeout=15
            )

            resp_json = resp.json() if resp.text else {}
            if resp.status_code in (200, 201):
                msg_status = resp_json.get("Messages", [{}])[0].get("Status", "success")
                msg_id = str(resp_json.get("Messages", [{}])[0].get("To", [{}])[0].get("MessageID", "mj_live"))
                result = {
                    "success": True,
                    "simulated": False,
                    "message_id": msg_id,
                    "status": msg_status,
                    "raw_response": resp_json
                }
            else:
                result = {
                    "success": False,
                    "simulated": False,
                    "status_code": resp.status_code,
                    "error": resp_json.get("ErrorMessage", resp.text)
                }

        except Exception as e:
            result = {
                "success": False,
                "simulated": False,
                "error": f"Mailjet HTTP connection error: {str(e)}"
            }

        # Log audit entry
        log_entry = {
            "message_id": result.get("message_id", "failed"),
            "provider": "mailjet_api_v3.1",
            "mode": "live",
            "recipient": to_email,
            "sender": f"{self.from_name} <{self.from_email}>",
            "subject": subject,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "status": "success" if result["success"] else "failed",
            "details": result
        }
        self._write_log(log_entry)
        return result

    def send_via_smtp(self, to_email, to_name, subject, html_content, text_content=None, attachment_paths=None):
        """
        Sends email via Mailjet SMTP Relay (in-v3.mailjet.com:587 TLS).
        """
        to_email = to_email.strip()
        status_info = self.get_credential_status()

        if not self.validate_email_syntax(to_email):
            return {"success": False, "error": f"Invalid recipient syntax: {to_email}"}

        if self.is_suppressed(to_email):
            return {"success": False, "error": f"Recipient {to_email} is suppressed."}

        if status_info["state"] != "READY_FOR_LIVE_DISPATCH":
            simulated_id = f"sim_smtp_{int(datetime.now(timezone.utc).timestamp())}_{abs(hash(to_email)) % 10000}"
            log_entry = {
                "message_id": simulated_id,
                "provider": "mailjet_smtp_relay",
                "mode": "simulation",
                "recipient": to_email,
                "sender": self.from_email,
                "subject": subject,
                "timestamp": datetime.now(timezone.utc).isoformat(),
                "status": "simulated_success",
                "reason": status_info["message"]
            }
            self._write_log(log_entry)
            return {
                "success": True,
                "simulated": True,
                "message_id": simulated_id,
                "provider": "mailjet_smtp_relay",
                "detail": status_info["message"]
            }

        # Build MIME Message
        msg = MIMEMultipart("alternative")
        msg["From"] = f"{self.from_name} <{self.from_email}>"
        msg["To"] = f"{to_name} <{to_email}>" if to_name else to_email
        msg["Subject"] = subject

        if text_content:
            msg.attach(MIMEText(text_content, "plain", "utf-8"))
        if html_content:
            msg.attach(MIMEText(html_content, "html", "utf-8"))

        # Attach local files
        if attachment_paths:
            for p in attachment_paths:
                if os.path.exists(p):
                    filename = os.path.basename(p)
                    part = MIMEBase("application", "octet-stream")
                    with open(p, "rb") as af:
                        part.set_payload(af.read())
                    encoders.encode_base64(part)
                    part.add_header("Content-Disposition", f'attachment; filename="{filename}"')
                    msg.attach(part)

        try:
            context = ssl.create_default_context()
            with smtplib.SMTP(MAILJET_SMTP_SERVER, MAILJET_SMTP_PORT_TLS, timeout=15) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(self.api_key, self.secret_key)
                server.sendmail(self.from_email, [to_email], msg.as_string())

            result = {
                "success": True,
                "simulated": False,
                "provider": "mailjet_smtp_relay",
                "server": f"{MAILJET_SMTP_SERVER}:{MAILJET_SMTP_PORT_TLS}",
                "status": "delivered_to_relay"
            }
        except Exception as e:
            result = {
                "success": False,
                "simulated": False,
                "provider": "mailjet_smtp_relay",
                "error": str(e)
            }

        log_entry = {
            "message_id": f"smtp_{int(datetime.now(timezone.utc).timestamp())}",
            "provider": "mailjet_smtp_relay",
            "mode": "live",
            "recipient": to_email,
            "sender": self.from_email,
            "subject": subject,
            "timestamp": datetime.now(timezone.utc).isoformat(),
            "status": "success" if result["success"] else "failed",
            "details": result
        }
        self._write_log(log_entry)
        return result

    def _write_log(self, entry):
        records = []
        if os.path.exists(LOG_FILE):
            try:
                with open(LOG_FILE, "r", encoding="utf-8") as f:
                    records = json.load(f)
            except Exception:
                records = []
        records.append(entry)
        try:
            with open(LOG_FILE, "w", encoding="utf-8") as f:
                json.dump(records, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f"Log write error: {e}", file=sys.stderr)


if __name__ == "__main__":
    dispatcher = MailjetEmailDispatcher()
    status = dispatcher.get_credential_status()
    print("=== MAILJET CONFIGURATION STATUS ===")
    print(json.dumps(status, indent=2, ensure_ascii=False))

    # Test simulation dispatch
    test_result = dispatcher.send_via_api(
        to_email="test.partner@example.com",
        to_name="Dr. Gastronomy Partner",
        subject="[Test] Partnership Proposal — Mizban Istanbul & Shamse",
        html_content="<h1>Partnership Proposal</h1><p>Automatic email dispatch test via Mailjet engine.</p>"
    )
    print("\n=== TEST DISPATCH RESULT ===")
    print(json.dumps(test_result, indent=2, ensure_ascii=False))
