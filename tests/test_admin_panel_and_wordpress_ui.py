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

def test_telegram_bot_file_and_channel_verification():
    assert os.path.exists(TG_BOT_PY), "telegram_bot.py must exist"
    with open(TG_BOT_PY, "r", encoding="utf-8") as f:
        code = f.read()

    assert "shamse_restaurant_bot" in code or "shamse_restaurant" in code
    assert "inline_keyboard" in code, "Bot must use inline keyboards"
    assert "area_keyboard" in code, "Bot must support area keyboards"
