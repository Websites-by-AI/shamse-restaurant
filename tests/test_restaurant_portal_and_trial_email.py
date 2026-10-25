#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite for Restaurant User Portal (Dual Auth & 1-Month Trial License)
and Admin Panel Sample Outreach Email Report.
"""

import os
import json
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_taksim_restaurants_trial_metadata():
    """Verify all Taksim restaurants have 1-month trial license metadata."""
    json_path = os.path.join(ROOT, "automation", "taksim_restaurants_intel.json")
    with open(json_path, "r", encoding="utf-8") as f:
        data = json.load(f)

    assert len(data) >= 10
    shamse = next((r for r in data if r["id"] == "shamse-taksim"), None)
    assert shamse is not None

    assert shamse["trial_status"] == "active"
    assert shamse["trial_days"] == 30
    assert shamse["trial_expires"] == "2026-11-25"
    assert "۴ آذر ۱۴۰۵" in shamse["trial_expires_fa"]
    assert shamse["tenant_username"] == "shamse_manager"
    assert shamse["temp_password"] == "Shamse#Taksim2026"
    assert shamse["magic_token"] == "SHAMSE-TAK-2026"

def test_restaurant_portal_html_trial_and_dual_login():
    """Verify restaurant_portal.html has dual login, 1-month trial banner, and credentials."""
    portal_path = os.path.join(ROOT, "restaurant_portal.html")
    with open(portal_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Dual login methods
    assert "tabBtnToken" in html
    assert "tabBtnUser" in html
    assert "loginMethodToken" in html
    assert "loginMethodUser" in html
    assert "switchLoginMethod" in html
    assert "submitLoginUserPass" in html
    assert "submitLoginToken" in html

    # 1-Month Trial Banner & details
    assert "trialLicenseBanner" in html
    assert "۳۰ روز باقی‌مانده" in html
    assert "trialExpiresDate" in html
    assert "۲۵ نوامبر ۲۰۲۶" in html
    assert "۴ آذر ۱۴۰۵" in html
    assert "shamse_manager" in html
    assert "Shamse#Taksim2026" in html
    assert "SHAMSE-TAK-2026" in html

    # Multimedia deliverables inside portal
    assert "shamse_sentiment_podcast_report.pdf" in html
    assert "mizban_restaurant_intelligence_pitch.pptx" in html
    assert "shamse_intelligence_podcast.mp3" in html
    assert "shamse_intelligence_podcast_tr.mp3" in html
    assert "sentiment_candlestick_chart.svg" in html
    assert "shamse_system_learning_infographic.svg" in html

def test_admin_panel_sample_email_and_trial_credentials():
    """Verify admin_panel.html includes the sample email report card and trial credentials."""
    admin_path = os.path.join(ROOT, "admin_panel.html")
    with open(admin_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Credentials with 1-Month Trial
    assert "مجوز آزمایشی ۱ ماهه (30-Day Pro Trial)" in html
    assert "۲۶ اکتبر ۲۰۲۶ تا ۲۵ نوامبر ۲۰۲۶" in html
    assert "۳۰ روز کامل (30 Days Remaining)" in html
    assert "shamse_manager" in html
    assert "Shamse#Taksim2026" in html
    assert "SHAMSE-TAK-2026" in html

    # Sample Email Report Card
    assert "نمونه ایمیل ارسالی گزارش هفتگی به رستوران شمسه" in html
    assert "Sample Executive Audit Email Report" in html
    assert "taksim@shamserestaurants.com" in html
    assert "shamsemedia1@gmail.com" in html
    assert "intelligence@mizbanistanbul.com" in html
    assert "Shamse_Executive_Report_2026.pdf" in html
    assert "Shamse_Pitch_Deck_2026.pptx" in html

    # Email Body Content
    assert "Google Maps" in html
    assert "۲,۴۵۰" in html
    assert "★ ۴٫۸" in html
    assert "TripAdvisor" in html
    assert "Yandex Maps" in html
    assert "Dimer Intelligence Engine v2.0" in html
    assert "+۱۷۴,۰۰۰ لیر" in html
    assert "sampleEmailRenderContainer" in html

    # Dispatch & Copy Functions
    assert "sendSampleMailjetDispatch" in html
    assert "copySampleEmailHtml" in html
    assert "copySampleEmailText" in html
    assert "copyFullWhatsAppPitch" in html
