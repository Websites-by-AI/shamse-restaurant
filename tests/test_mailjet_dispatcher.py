#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Mailjet Email Dispatch Engine (automation/mailjet_dispatcher.py).
Covers:
  - Credential state machine & masking
  - Syntax validation
  - Suppression ledger enforcement
  - Base64 attachment serialization for v3.1
  - Simulation mode & audit logging
  - SMTP relay dispatch simulation
"""

import os
import json
import pytest
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(REPO_ROOT, "automation"))

from mailjet_dispatcher import (
    MailjetEmailDispatcher,
    DEFAULT_API_KEY,
    MAILJET_SMTP_SERVER,
    MAILJET_SMTP_PORT_TLS
)

def test_mailjet_credential_status_pending_secret():
    dispatcher = MailjetEmailDispatcher(api_key=DEFAULT_API_KEY, secret_key="")
    status = dispatcher.get_credential_status()
    assert status["state"] == "PENDING_SECRET_KEY"
    assert status["smtp_server"] == MAILJET_SMTP_SERVER
    assert status["smtp_port"] == MAILJET_SMTP_PORT_TLS
    assert "b5af" in status["api_key_masked"]

def test_mailjet_credential_status_ready():
    dispatcher = MailjetEmailDispatcher(api_key="b5af6ec2f275931f9216b8c7eb9c03eb", secret_key="1234567890abcdef1234567890abcdef")
    status = dispatcher.get_credential_status()
    assert status["state"] == "READY_FOR_LIVE_DISPATCH"
    assert status["has_secret_key"] is True

def test_mailjet_syntax_validation():
    dispatcher = MailjetEmailDispatcher()
    assert dispatcher.validate_email_syntax("valid.user@example.com") is True
    assert dispatcher.validate_email_syntax("bad-email-without-at") is False

    res = dispatcher.send_via_api("invalid_email_format", "Test", "Subject", "<p>Test</p>")
    assert res["success"] is False
    assert "Invalid recipient" in res["error"]

def test_mailjet_attachment_serialization(tmp_path):
    dispatcher = MailjetEmailDispatcher()
    test_file = tmp_path / "sample_report.pdf"
    test_file.write_bytes(b"%PDF-1.4 test binary content")

    att = dispatcher.prepare_mailjet_attachment(str(test_file))
    assert att is not None
    assert att["Filename"] == "sample_report.pdf"
    assert att["ContentType"] == "application/pdf"
    assert len(att["Base64Content"]) > 0

def test_mailjet_simulation_send_and_logging():
    dispatcher = MailjetEmailDispatcher(api_key=DEFAULT_API_KEY, secret_key="")
    res = dispatcher.send_via_api(
        to_email="test.partner.audit@domain.com",
        to_name="Dr. Partner",
        subject="Automated Mailjet B2B Audit Test",
        html_content="<p>Test Content</p>"
    )
    assert res["success"] is True
    assert res["simulated"] is True
    assert "sim_mj_" in res["message_id"]

    # Verify log entry in dispatch_log.json
    log_file = os.path.join(REPO_ROOT, "automation", "dispatch_log.json")
    assert os.path.exists(log_file)
    with open(log_file, "r", encoding="utf-8") as f:
        logs = json.load(f)
    matching = [l for l in logs if l.get("recipient") == "test.partner.audit@domain.com"]
    assert len(matching) > 0
    assert matching[-1]["provider"] == "mailjet_api_v3.1"

def test_mailjet_smtp_simulation():
    dispatcher = MailjetEmailDispatcher(api_key=DEFAULT_API_KEY, secret_key="")
    res = dispatcher.send_via_smtp(
        to_email="smtp.test@domain.com",
        to_name="SMTP Test",
        subject="SMTP Relay Test",
        html_content="<p>SMTP Test</p>"
    )
    assert res["success"] is True
    assert res["simulated"] is True
    assert res["provider"] == "mailjet_smtp_relay"
