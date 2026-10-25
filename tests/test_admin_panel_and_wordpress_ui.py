#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for:
  1. WordPress-like UI/UX enhancements in index.html (Hero Slider, WooCommerce Menu Filter, Header language switch).
  2. Telegram Bot & Channel integrity (@shamse_restaurant_bot & @shamse_istanbul).
  3. WordPress WP-Admin style Dashboard (admin_panel.html).
"""

import os
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
INDEX_HTML = os.path.join(REPO_ROOT, "index.html")
ADMIN_HTML = os.path.join(REPO_ROOT, "admin_panel.html")
TG_BOT_PY = os.path.join(REPO_ROOT, "automation", "telegram_bot.py")

def test_wordpress_ui_hero_slider_in_index():
    assert os.path.exists(INDEX_HTML), "index.html must exist"
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # Verify Hero Slider structure
    assert "wp-hero-slider" in html, "Must contain WordPress luxury hero slider"
    assert "wp-slide" in html, "Must contain slides"
    assert "wp-slider-ctrl" in html, "Must contain slider navigation controls"
    assert "wp-slider-dots" in html, "Must contain slider pagination dots"
    assert "changeWpSlide" in html, "Must contain slide transition logic"

def test_wordpress_woocommerce_menu_filter_in_index():
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # Verify Menu Filter Bar
    assert "wp-menu-filter-bar" in html, "Must contain WooCommerce-style menu filter bar"
    assert "wpMenuSearch" in html, "Must contain live search box"
    assert "wp-dietary-tags" in html, "Must contain dietary tags"
    assert "wpMenuSort" in html, "Must contain sorting selector"
    assert "applyWpMenuFilter" in html, "Must contain live filtering function"

def test_wordpress_header_and_admin_link():
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    assert "admin_panel.html" in html, "Header must link to admin panel"
    assert "lang-switch" in html, "Header must have language switcher"
    assert "🇮🇷 FA" in html
    assert "🇬🇧 EN" in html
    assert "🇹🇷 TR" in html

def test_admin_panel_wp_style_structure():
    assert os.path.exists(ADMIN_HTML), "admin_panel.html must exist"
    with open(ADMIN_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # Verify WP Topbar & Sidebar
    assert "wp-admin-bar" in html, "Must have WordPress admin topbar"
    assert "wp-sidebar" in html, "Must have WordPress left sidebar"
    assert "tab-dashboard" in html, "Must have Dashboard tab"
    assert "tab-menu-manager" in html, "Must have Menu Manager tab"
    assert "tab-slider-manager" in html, "Must have Slider Manager tab"
    assert "tab-telegram-channel" in html, "Must have Telegram Channel tab"
    assert "tab-leads-crm" in html, "Must have 100 Leads CRM tab"
    assert "tab-reviews-triage" in html, "Must have Reviews Triage tab"
    assert "@shamse_istanbul" in html, "Must integrate Telegram channel @shamse_istanbul"
    assert "@shamse_restaurant_bot" in html, "Must reference official bot"

    # Mailjet Relay & API Integration
    assert "b5af6ec2f275931f9216b8c7eb9c03eb" in html, "Must contain Mailjet Primary API Key"
    assert "in-v3.mailjet.com" in html, "Must configure Mailjet SMTP relay host"
    assert "cfgMailjetSecretKey" in html, "Must provide secret key input"

    # Multi-format Deliverables & Branch Google Maps Dossier
    assert "reports/mizban_restaurant_intelligence_pitch.pptx" in html, "Must link to PPTX deliverable"
    assert "reports/shamse_sentiment_podcast_report.pdf" in html, "Must link to PDF deliverable"
    assert "İstiklal Caddesi No:179" in html, "Must contain İstiklal branch address"
    assert "Abdülhak Hamit Cad" in html, "Must contain Kocatepe branch address"
    assert "10 İyileştirme Stratejisi" in html, "Must contain 10 Improvement Strategies table"
    assert "10 Hesaplama Alanı" in html, "Must contain 10 Calculators table"



def test_telegram_bot_file_and_channel_verification():
    assert os.path.exists(TG_BOT_PY), "telegram_bot.py must exist"
    with open(TG_BOT_PY, "r", encoding="utf-8") as f:
        code = f.read()

    assert "shamse_restaurant_bot" in code or "shamse_restaurant" in code
    assert "inline_keyboard" in code, "Bot must use inline keyboards"
    assert "area_keyboard" in code, "Bot must support area keyboards"

def test_amazon_conversion_skills_in_index():
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # Amazon 5-star to 1-star histogram breakdown
    assert "amazon-reviews-box" in html, "Must contain Amazon rating breakdown box"
    assert "amz-hist-row" in html, "Must contain rating histogram rows"
    assert "۸۲٪" in html or "82%" in html, "5-star percentage must be shown"
    assert "amz-rating-left" in html, "Must show aggregate rating summary"
    assert "amz-keywords-cloud" in html, "Must show customer sentiment keywords"

    # Amazon Frequently Paired Together Bundle
    assert "amz-bundle-card" in html, "Must contain Amazon signature bundle card"
    assert "amz-bundle-plus" in html, "Must show plus signs connecting bundled items"
    assert "Frequently Paired Together" in html, "Must reference Amazon bundle pattern"

def test_opentable_conversion_skills_in_index():
    with open(INDEX_HTML, "r", encoding="utf-8") as f:
        html = f.read()

    # OpenTable 1-click interactive time-slot pills
    assert "ot-slot-pills" in html, "Must contain OpenTable time slot pills"
    assert "ot-pill" in html, "Must contain time slot buttons"
    assert "selectOtTimeSlot" in html, "Must contain JavaScript time selection function"

    # OpenTable seating preference & real-time urgency banner
    assert "ot-seating-pills" in html, "Must contain seating preference selector"
    assert "ot-urgency-banner" in html, "Must contain real-time booking urgency banner"
    assert "تقاضای بالا در تکسیم" in html, "Must display hot booking urgency tag"


