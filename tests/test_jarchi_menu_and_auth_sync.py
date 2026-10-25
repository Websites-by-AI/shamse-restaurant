#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
آزمون‌های جامع سیستم جارچی استقلال، ۱۰ حوزه هوش مصنوعی، مهندسی منو و احراز هویت همگام ۳۶۵ روزه
Unit & Integration Tests for Street Barker Slogans, AI Menu Engine, and 1-Year Auth Sync
"""

import json
import os
import sys
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "automation"))

import jarchi_ai_engine as jarchi
import auth_sync_manager as auth_sync
import telegram_bot as tb
import content


def test_10_street_barker_slogans_and_techniques():
    """بررسی جامع ۱۰ شعار میدانی دادزن استقلال، تنوع زبان‌ها، محرک‌های روانشناختی و تکنیک‌های جذب"""
    slogans = jarchi.get_street_barker_slogans()
    assert len(slogans) == 10, f"Expected exactly 10 street barker slogans, got {len(slogans)}"

    languages = set()
    for s in slogans:
        assert s["id"].startswith("SLOGAN-"), f"Invalid slogan ID: {s['id']}"
        assert len(s["hook_text"]) > 15, "Hook text must be substantial"
        assert len(s["action_technique"]) > 15, "Action technique must be described"
        assert len(s["psychological_trigger"]) > 10, "Psychological trigger required"
        assert "%" in s["conversion_metric"] or "٪" in s["conversion_metric"], "Conversion metric required"
        languages.add(s["language"])

    # بررسی پوشش ۵ زبان کلیدی
    lang_str = " ".join(languages)
    assert "fa" in lang_str, "Persian slogans must exist"
    assert "en" in lang_str, "English slogans must exist"
    assert "ru" in lang_str, "Russian slogans must exist"
    assert "ar" in lang_str, "Arabic slogans must exist"
    assert "tr" in lang_str, "Turkish slogans must exist"

    # بررسی کلمات کلیدی هویتی
    full_text = " ".join(s["hook_text"] for s in slogans)
    assert "زعفرون" in full_text or "زعفران" in full_text
    assert "حلال" in full_text or "لحم" in full_text
    assert "UNESCO" in full_text or "Cover Charge" in full_text
    assert "шашлык" in full_text or "шафрановый" in full_text
    assert "بالکن" in full_text
    assert "ته‌دیگ" in full_text


def test_10_ai_improvement_domains_and_seasons():
    """بررسی ۱۰ حوزه ارتقای هوش مصنوعی، انطباق فصلی ۴ گانه و تفکیک دو شعبه"""
    domains = jarchi.get_ai_improvement_domains()
    assert len(domains) == 10, f"Expected 10 AI domains, got {len(domains)}"

    dom_ids = [d["domain_id"] for d in domains]
    assert len(dom_ids) == len(set(dom_ids)), "Domain IDs must be unique"

    # بررسی حوزه فصلی (AI-DOM-01)
    d1 = domains[0]
    assert d1["domain_id"] == "AI-DOM-01"
    seasons = d1["seasonal_logic"]
    assert all(k in seasons for k in ["spring", "summer", "autumn", "winter"]), "All 4 seasons must be covered"
    assert "فسنجان" in seasons["autumn"]
    assert "ماهیچه" in seasons["winter"]
    assert "دوغ" in seasons["summer"]

    # بررسی حوزه تفکیک جغرافیایی شعب (AI-DOM-02)
    d2 = domains[1]
    assert "istiklal" in d2["branch_logic"] and "kocatepe" in d2["branch_logic"]
    assert "اکسپرس" in d2["branch_logic"]["istiklal"]
    assert "همایونی" in d2["branch_logic"]["kocatepe"]

    # بررسی چرخه حل نقدها (AI-DOM-03)
    d3 = domains[2]
    fixes = " ".join(d3["fixes_applied"])
    assert "مهسا" in fixes and "۱۰ دقیقه" in fixes
    assert "دیوید" in fixes or "David" in fixes or "چای" in fixes
    assert "دیمیتری" in fixes or "سیریلیک" in fixes or "روسی" in fixes

    # بررسی مدل‌های هدف هوش مصنوعی
    models = [d["target_ai_model"] for d in domains]
    assert any("Prophet" in m for m in models)
    assert any("LSTM" in m for m in models)
    assert any("ABSA" in m for m in models)
    assert any("DeepL" in m or "Whisper" in m for m in models)


def test_new_optimized_menu_pricing_and_margins():
    """بررسی منوی جدید شمسه، نسبت هزینه مواد (Food Cost) و حاشیه سود بالای ۶۰٪"""
    menu = jarchi.get_new_optimized_menu()
    assert len(menu) >= 3, "Menu must have at least 3 categories"

    all_items = [item for cat in menu for item in cat["items"]]
    assert len(all_items) >= 10, "At least 10 items in optimized menu"

    for it in all_items:
        assert it["proposed_price_try"] >= it["current_price_try"], "Proposed price should be optimized"
        assert it["price_usd"] > 0
        assert it["margin_try"] > 0
        # محاسبه حاشیه سود
        margin_pct = (it["margin_try"] / it["proposed_price_try"]) * 100
        assert margin_pct > 55, f"Gross margin should be healthy (>55%), got {margin_pct}% for {it['name']}"


def test_unified_365_day_auth_sync_database():
    """بررسی پایگاه داده احراز هویت همگام و اعتبار نشست ۳۶۵ روزه (یکساله)"""
    db = auth_sync.load_auth_db()
    assert "metadata" in db
    assert "users" in db
    assert "sessions" in db
    assert "sync_state" in db

    # احراز هویت موفق با رمز و کاربری مدیر
    auth_res = auth_sync.authenticate_user("shamse_admin", "Shamse@2026!Istiklal", origin="telegram", chat_id=98765)
    assert auth_res["ok"] is True
    token = auth_res["token"]
    assert auth_res["validity_days"] == 365, "Validity must be 365 days (1 year)"

    # تایید اعتبار توکن
    v = auth_sync.verify_session_token(token)
    assert v["valid"] is True
    assert v["is_one_year_valid"] is True
    assert v["remaining_days"] in (364, 365)

    # رد ورود با پسورد اشتباه
    bad_res = auth_sync.authenticate_user("shamse_admin", "WrongPassword!2026")
    assert bad_res["ok"] is False

    # بررسی وضعیت هماهنگ
    sync_header = auth_sync.get_current_sync_header_info()
    assert sync_header["is_synced"] is True
    assert sync_header["active_user"] == "shamse_admin"
    assert sync_header["expires_in_days"] == 365
    assert "۳۶۵ روزه" in sync_header["header_badge_text"]


def test_telegram_bot_admin_panel_and_commands():
    """بررسی پاسخ‌دهی ربات تلگرام به دستور /login، /panel و Callbackهای پنل ادمین"""
    # تست تابع‌های کمکی
    markup = tb.admin_panel_markup()
    buttons = [b["callback_data"] for row in markup["inline_keyboard"] for b in row if "callback_data" in b]
    assert "panel:barker" in buttons
    assert "panel:menu" in buttons
    assert "panel:pricing" in buttons
    assert "panel:ai" in buttons
    assert "panel:reviews" in buttons
    assert "panel:sync" in buttons
    assert "panel:logout" in buttons

    welcome_text = tb.get_panel_welcome_text("مدیر ارشد")
    assert "۳۶۵ روز" in welcome_text or "یکساله" in welcome_text

    # تست پردازش Callback با Mock API
    calls = []
    def fake_api(method, payload=None, retries=3):
        calls.append((method, payload))
        return {"ok": True, "result": {"message_id": 999}}

    real_api = tb.api
    tb.api = fake_api

    try:
        db = {"users": {}, "rsvps": {}, "reminders": {}, "counters": {}}
        test_actions = ["main", "barker", "menu", "pricing", "ai", "reviews", "sync", "logout"]

        for action in test_actions:
            upd = {
                "callback_query": {
                    "id": f"cq_{action}",
                    "data": f"panel:{action}",
                    "from": {"id": 111, "first_name": "ShamseManager"},
                    "message": {"chat": {"id": 111}, "message_id": 100}
                }
            }
            handled = tb.handle_callback(upd, db)
            assert handled is True, f"Callback panel:{action} must be handled"
    finally:
        tb.api = real_api


def test_html_headers_and_admin_panel_jarchi_tab():
    """بررسی وجود نشانگر ورود یکپارچه در هدر سایت اصلی و پنل ادمین و تب اختصاصی جارچی"""
    # Index.html header check
    index_path = os.path.join(REPO_ROOT, "index.html")
    with open(index_path, "r", encoding="utf-8") as f:
        index_html = f.read()

    assert "siteUnifiedAuthSyncBadge" in index_html, "Index header must have unified auth sync badge"
    assert "۳۶۵ روزه" in index_html, "Index header badge must state 365-day validity"
    assert "shamse_admin" in index_html, "Index must show admin user"

    # Admin_panel.html check
    admin_path = os.path.join(REPO_ROOT, "admin_panel.html")
    with open(admin_path, "r", encoding="utf-8") as f:
        admin_html = f.read()

    assert "adminSyncBadge" in admin_html, "Admin top bar must have adminSyncBadge"
    assert "tab-jarchi-menu" in admin_html, "Admin panel must have tab-jarchi-menu"
    assert "SLOGAN-01" in admin_html, "Admin panel must list SLOGAN-01"
    assert "SLOGAN-10" in admin_html, "Admin panel must list SLOGAN-10"
    assert "AI-DOM-01" in admin_html, "Admin panel must list AI-DOM-01"
    assert "AI-DOM-10" in admin_html, "Admin panel must list AI-DOM-10"
    assert "چلو کباب کوبیده مخصوص شمسه" in admin_html, "Admin panel must list optimized menu"
