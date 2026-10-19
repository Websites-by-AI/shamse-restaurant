#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite for Omnichannel Dispatch Engine, Lead Directory (19 Restaurants + 186 Hotels),
and Automated Multi-Channel Dispatch (Email, WhatsApp, Telegram, Instagram, Facebook).
"""

import os
import sys
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import omnichannel_dispatch_engine as ode

def test_leads_directory_metrics():
    """Verify exact count of leads, review aggregates, and channel readiness."""
    analytics = ode.get_leads_analytics()
    
    assert analytics["total_restaurant_leads"] == 19
    assert analytics["total_hotel_leads"] == 186
    assert analytics["grand_total_leads"] == 205
    assert analytics["total_google_reviews"] == 27510
    assert analytics["total_tripadvisor_reviews"] == 2830
    assert analytics["total_yandex_reviews"] == 1930
    assert analytics["grand_total_reviews"] == 32270
    
    # 100% of leads have all 5 channels ready
    cov = analytics["channels_coverage"]
    assert cov["email"] == 19
    assert cov["whatsapp"] == 19
    assert cov["telegram"] == 19
    assert cov["instagram"] == 19
    assert cov["facebook"] == 19

def test_channel_payload_generation():
    """Verify that tailored payloads for Email, WhatsApp, Telegram, Instagram, and Facebook are generated."""
    leads = ode.load_leads()
    farsi_lead = [r for r in leads if r["id"] == "farsi-taksim"][0]

    # Email payload
    em = ode.generate_channel_payload(farsi_lead, "email")
    assert em["channel"] == "email"
    assert "info@restaurantfarsi.com" in em["recipient"]
    assert "گزارش هفتگی" in em["subject"]
    assert "Google Maps" in em["body"]
    assert "TripAdvisor" in em["body"]
    assert "Yandex Maps" in em["body"]

    # WhatsApp payload
    wa = ode.generate_channel_payload(farsi_lead, "whatsapp")
    assert wa["channel"] == "whatsapp"
    assert "wa.me" in wa["action_url"]
    assert "۱۷۴" in wa["body"]

    # Telegram payload
    tg = ode.generate_channel_payload(farsi_lead, "telegram")
    assert tg["channel"] == "telegram"
    assert "t.me" in tg["action_url"]

    # Instagram payload
    ig = ode.generate_channel_payload(farsi_lead, "instagram")
    assert ig["channel"] == "instagram"
    assert "instagram.com" in ig["action_url"]

    # Facebook payload
    fb = ode.generate_channel_payload(farsi_lead, "facebook")
    assert fb["channel"] == "facebook"
    assert "facebook.com" in fb["action_url"]

def test_single_and_batch_dispatch():
    """Verify execution of single lead dispatch and batch dispatch across all 19 venues."""
    # Single dispatch
    single = ode.dispatch_lead("shamse-taksim", "email")
    assert single["status"] == "success"
    assert "DISPATCH-EM" in single["dispatch_id"]
    assert single["lead_name"] == "رستوران شمسه (شعبه استقلال)"

    # Batch dispatch
    batch = ode.batch_dispatch_all(channel="email")
    assert batch["total_dispatched"] == 19
    assert len(batch["dispatches"]) == 19

def test_admin_panel_html_integration():
    """Verify that intelligence.html contains the leads counter, channel tabs, and dispatch controls."""
    with open(os.path.join(ROOT, "intelligence.html"), "r", encoding="utf-8") as f:
        html = f.read()

    assert "۱۹ لید رستوران" in html
    assert "۱۸۶ هتل" in html
    assert "۳۲,۲۷۰ نقد" in html
    assert "setOutreachChannel" in html
    assert "executeSingleDispatch" in html
    assert "runBatchDispatch" in html
    assert "dispatchLogTable" in html
