#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مدیریت همگام‌سازی احراز هویت کاربران (وب‌سایت و ربات تلگرام)
Unified Auth & 1-Year Session Sync Manager for Shamse Restaurant

این سیستم تضمین می‌کند:
۱. احراز هویت با نام کاربری و رمز عبور یکپارچه (shamse_admin / Shamse@2026!Istiklal).
۲. صدور نشست امن با انقضای ۳۶۵ روزه (یکساله / 1 Year Validity).
۳. همگام‌سازی بلادرنگ وضعیت ورود بین وب و بات تلگرام در auth_sync_db.json.
۴. امکان استعلام وضعیت لاگین جهت نمایش در هدر وب‌سایت و پیام‌های تلگرام.
"""

import datetime as dt
import hashlib
import json
import os
import uuid
from typing import Dict, Any, Optional

HERE = os.path.dirname(os.path.abspath(__file__))
AUTH_DB_FILE = os.path.join(HERE, "auth_sync_db.json")

VALID_USERS = {
    "shamse_admin": "Shamse@2026!Istiklal",
    "admin": "Shamse@2026!Istiklal",
    "demo_admin": "admin123"
}

TOKEN_VALIDITY_DAYS = 365  # اعتبار دقیقاً یک ساله


def _get_default_db() -> Dict[str, Any]:
    """ساختار پیش‌فرض پایگاه داده همگام احراز هویت"""
    now = dt.datetime.now(dt.timezone.utc)
    one_year_later = now + dt.timedelta(days=TOKEN_VALIDITY_DAYS)
    
    # توکن پیش‌فرض فعال یکساله برای مدیر
    default_token = "SHAMSE-365D-" + hashlib.sha256(f"shamse_admin_{now.year}".encode()).hexdigest()[:24].upper()
    
    return {
        "metadata": {
            "platform": "میزبان استانبول (Mizban Istanbul) - سامانه یکپارچه ورود شمسه",
            "version": "2.4.0",
            "session_policy": "365_DAYS_ONE_YEAR_STABLE",
            "last_updated": now.isoformat()
        },
        "users": {
            "shamse_admin": {
                "username": "shamse_admin",
                "role": "Chief Operating Executive & Restaurant Manager",
                "display_name": "مدیریت اجرایی شمسه",
                "created_at": now.isoformat(),
                "status": "active"
            },
            "admin": {
                "username": "admin",
                "role": "System Administrator",
                "display_name": "مدیر سیستم",
                "created_at": now.isoformat(),
                "status": "active"
            }
        },
        "sessions": {
            default_token: {
                "token": default_token,
                "username": "shamse_admin",
                "issued_at": now.isoformat(),
                "expires_at": one_year_later.isoformat(),
                "validity_days": TOKEN_VALIDITY_DAYS,
                "web_authenticated": True,
                "telegram_authenticated": True,
                "telegram_chat_id": 198117936491,
                "telegram_username": "shamse_manager",
                "client_ip": "127.0.0.1",
                "device": "Unified Sync (Web & Telegram)",
                "status": "active"
            }
        },
        "sync_state": {
            "active_user": "shamse_admin",
            "is_synced": True,
            "session_token": default_token,
            "web_status": "AUTHENTICATED",
            "telegram_status": "AUTHENTICATED",
            "expires_at": one_year_later.isoformat(),
            "expires_in_days": TOKEN_VALIDITY_DAYS,
            "header_badge_text": f"✓ ورود یکپارچه فعال • کاربر: shamse_admin • اعتبار سشن: ۳۶۵ روزه (تا {one_year_later.strftime('%Y-%m-%d')}) • سینک با تلگرام @shamse_restaurant_bot"
        }
    }


def load_auth_db() -> Dict[str, Any]:
    """بارگذاری دیتابیس هماهنگ احراز هویت"""
    if not os.path.exists(AUTH_DB_FILE):
        db = _get_default_db()
        save_auth_db(db)
        return db
    try:
        with open(AUTH_DB_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except Exception:
        db = _get_default_db()
        save_auth_db(db)
        return db


def save_auth_db(db: Dict[str, Any]) -> None:
    """ذخیره دیتابیس هماهنگ احراز هویت"""
    db.setdefault("metadata", {})["last_updated"] = dt.datetime.now(dt.timezone.utc).isoformat()
    with open(AUTH_DB_FILE, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)


def authenticate_user(username: str, password: str, origin: str = "web", chat_id: Optional[int] = None, tg_user: Optional[str] = None) -> Dict[str, Any]:
    """
    احراز هویت کاربر و صدور توکن یکساله (۳۶۵ روزه) با قابلیت سینک بین تلگرام و وب.
    """
    username = (username or "").strip().lower()
    password = (password or "").strip()
    
    expected_pass = VALID_USERS.get(username)
    if not expected_pass or expected_pass != password:
        return {
            "ok": False,
            "error": "نام کاربری یا رمز عبور نامعتبر است.",
            "code": 401
        }
    
    db = load_auth_db()
    now = dt.datetime.now(dt.timezone.utc)
    one_year_later = now + dt.timedelta(days=TOKEN_VALIDITY_DAYS)
    
    # تولید توکن نشست پایدار ۳۶۵ روزه
    random_part = uuid.uuid4().hex[:12].upper()
    token = f"SHAMSE-365D-{username.upper()}-{random_part}"
    
    session_data = {
        "token": token,
        "username": username,
        "issued_at": now.isoformat(),
        "expires_at": one_year_later.isoformat(),
        "validity_days": TOKEN_VALIDITY_DAYS,
        "web_authenticated": True if origin == "web" else False,
        "telegram_authenticated": True if origin == "telegram" else False,
        "telegram_chat_id": chat_id,
        "telegram_username": tg_user,
        "device": f"Client ({origin.capitalize()})",
        "status": "active"
    }
    
    db["sessions"][token] = session_data
    
    # به‌روزرسانی وضعیت همگام سراسری
    db["sync_state"] = {
        "active_user": username,
        "is_synced": True,
        "session_token": token,
        "web_status": "AUTHENTICATED",
        "telegram_status": "AUTHENTICATED" if origin == "telegram" else "READY_TO_PAIR",
        "expires_at": one_year_later.isoformat(),
        "expires_in_days": TOKEN_VALIDITY_DAYS,
        "header_badge_text": f"✓ ورود یکپارچه فعال • کاربر: {username} • اعتبار سشن: ۳۶۵ روزه (تا {one_year_later.strftime('%Y-%m-%d')}) • سینک با تلگرام @shamse_restaurant_bot"
    }
    
    save_auth_db(db)
    
    return {
        "ok": True,
        "token": token,
        "username": username,
        "expires_at": one_year_later.isoformat(),
        "validity_days": TOKEN_VALIDITY_DAYS,
        "sync_state": db["sync_state"]
    }


def sync_telegram_session(token: str, chat_id: int, tg_username: Optional[str] = None) -> bool:
    """
    پیوند دادن نشست وب موجود با حساب تلگرام کاربر جهت تکمیل سینک دوطرفه.
    """
    db = load_auth_db()
    if token not in db["sessions"]:
        return False
    
    session = db["sessions"][token]
    session["telegram_authenticated"] = True
    session["telegram_chat_id"] = chat_id
    if tg_username:
        session["telegram_username"] = tg_username
    
    db["sync_state"]["telegram_status"] = "AUTHENTICATED"
    db["sync_state"]["is_synced"] = True
    save_auth_db(db)
    return True


def verify_session_token(token: str) -> Dict[str, Any]:
    """
    بررسی اعتبار یک‌ساله توکن نشست.
    """
    db = load_auth_db()
    if not token or token not in db["sessions"]:
        return {"valid": False, "reason": "TOKEN_NOT_FOUND"}
    
    session = db["sessions"][token]
    if session.get("status") != "active":
        return {"valid": False, "reason": "TOKEN_REVOKED"}
    
    expires_str = session.get("expires_at")
    try:
        expires_at = dt.datetime.fromisoformat(expires_str)
        now = dt.datetime.now(dt.timezone.utc)
        if now > expires_at:
            session["status"] = "expired"
            save_auth_db(db)
            return {"valid": False, "reason": "TOKEN_EXPIRED"}
        
        remaining_days = (expires_at - now).days
        return {
            "valid": True,
            "username": session.get("username"),
            "expires_at": expires_str,
            "remaining_days": remaining_days,
            "is_one_year_valid": session.get("validity_days") == TOKEN_VALIDITY_DAYS
        }
    except Exception as e:
        return {"valid": False, "reason": f"DATE_PARSE_ERROR: {e}"}


def get_current_sync_header_info() -> Dict[str, Any]:
    """دریافت آخرین اطلاعات هدر جهت نمایش یکپارچه در سایت و تلگرام"""
    db = load_auth_db()
    return db.get("sync_state", {})


if __name__ == "__main__":
    # Test authentication
    res = authenticate_user("shamse_admin", "Shamse@2026!Istiklal", origin="telegram", chat_id=123456)
    print("Auth Result:", res["ok"], "Token:", res.get("token"))
    v = verify_session_token(res["token"])
    print("Verify Result:", v)
