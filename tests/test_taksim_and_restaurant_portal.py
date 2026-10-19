#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite for Taksim Gastronomy Intelligence, Multi-Tenant Restaurant Portal,
and Atikova Dispatch & Follow-Up Control Room.
"""

import os
import sys
import json
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import taksim_portal_engine as tpe

def test_taksim_restaurants_data():
    """Verify Taksim restaurants dataset integrity, ratings, ABSA dimensions, and magic tokens."""
    restaurants = tpe.load_taksim_restaurants()
    assert len(restaurants) == 10

    required_keys = [
        "id", "name_fa", "district", "google_rating", "google_review_count",
        "tripadvisor_rating", "yandex_rating", "absa_scores", "magic_token",
        "seat_capacity", "monthly_unlocked_revenue_try", "temp_password"
    ]

    for r in restaurants:
        for k in required_keys:
            assert k in r, f"Missing key {k} in restaurant {r.get('id')}"
        assert r["google_rating"] >= 4.0
        assert r["google_review_count"] > 500
        assert r["magic_token"].endswith("-2026")
        assert len(r["absa_scores"]) == 5

def test_taksim_district_summary():
    """Verify aggregated metrics across the Taksim district."""
    summary = tpe.get_taksim_district_summary()
    assert summary["district"] == "Taksim / Beyoğlu"
    assert summary["total_venues_tracked"] == 10
    assert summary["grand_total_reviews"] == 56905
    assert summary["average_google_rating"] >= 4.5
    assert summary["district_monthly_unlocked_revenue_try"] >= 1800000

def test_restaurant_outreach_package():
    """Verify generation of personalized Email, Magic Token URL, and WhatsApp 1-Touch message."""
    pkg = tpe.generate_restaurant_outreach_package("reyhun-taksim")
    assert pkg is not None
    assert pkg["magic_token"] == "REYHUN-TAK-2026"
    assert "token=REYHUN-TAK-2026" in pkg["magic_url"]
    assert "رستوران ریحون" in pkg["email_subject"]
    assert "REYHUN-TAK-2026" in pkg["email_html"]
    assert "wa.me/905312627526" in pkg["whatsapp_action_url"]
    assert "Mizban@Taksim2026" in pkg["whatsapp_text"]

def test_atikova_dispatch_db():
    """Verify the 43-entity Atikova outreach database and Telegram audit categories."""
    db = tpe.load_atikova_db()
    assert db["system"] == "Atikova & Mizban Dispatch Control Room"
    assert db["stats"]["total_dispatched"] == 43
    assert db["stats"]["replied"] == 4
    assert db["stats"]["pending"] == 19
    assert db["stats"]["reminded"] == 20
    assert db["whatsapp_sender_number"] == "+98 920 626 3218"
    assert len(db["entities"]) == 43

    # Check Telegram stats
    tg_stats = db["telegram_audit_stats"]
    assert tg_stats["official"] >= 1
    assert tg_stats["not_found"] == 36

def test_restaurant_portal_html():
    """Verify customer-facing restaurant_portal.html contains token authentication and multi-tenant views."""
    portal_path = os.path.join(ROOT, "restaurant_portal.html")
    assert os.path.exists(portal_path)
    with open(portal_path, "r", encoding="utf-8") as f:
        html = f.read()

    assert "loginCard" in html
    assert "dashboardView" in html
    assert "absaBarsContainer" in html
    assert "sampleReviewsContainer" in html
    assert "SHAMSE-TAK-2026" in html
    assert "REYHUN-TAK-2026" in html

def test_intelligence_html_modules_13_and_14():
    """Verify intelligence.html contains Modules 13 and 14 with subnav links and controllers."""
    intel_path = os.path.join(ROOT, "intelligence.html")
    with open(intel_path, "r", encoding="utf-8") as f:
        html = f.read()

    assert "mod-atikova-control" in html
    assert "mod-taksim-multitenant" in html
    assert "۱۳. اتاق کنترل دیسپچ و پیگیری‌ها" in html
    assert "۱۴. تحلیل گوگل مپ برای کل رستوران‌های منطقه تکسیم" in html
    assert "atikovaEntitiesTableBody" in html
    assert "taksimRestaurantSelect" in html
    assert "taksimRestaurantsTableBody" in html
