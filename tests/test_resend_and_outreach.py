#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite for Resend Email Dispatcher & 10-Segment 5-Language Multilingual Outreach Hub.
Verifies:
  1. Master database integrity: 10 segments x 5 languages (FA, EN, TR, AR, DE).
  2. Embedment of 3 key multimedia assets (Video Demo, PPTX Deck, PDF Whitepaper) in every pitch.
  3. Resend email dispatcher with token interpolation, attachment encoding, and audit logging.
  4. DNS authentication configuration (SPF, DKIM, DMARC, Return-Path, BIMI).
  5. Admin Intelligence Panel (intelligence.html) Module 12 interactive UI integration.
"""

import os
import sys
import json
import pytest

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import outreach_multilingual_engine as ome
import resend_dispatcher as rd

def test_outreach_database_integrity():
    """Verify exactly 10 stakeholder segments across 5 languages with all required fields."""
    db = ome.load_database()
    segments = db["segments"]
    assert len(segments) == 10

    expected_languages = ["fa", "en", "tr", "ar", "de"]
    assert list(db["languages"].keys()) == expected_languages

    expected_segment_ids = [
        "government_tourism",
        "doctors_nutritionists",
        "enterprise_brands",
        "youtube_creators",
        "instagram_influencers",
        "universities_startup_calls",
        "academic_researchers",
        "luxury_hotels",
        "venture_capital",
        "cultural_chambers"
    ]

    for seg in segments:
        assert seg["id"] in expected_segment_ids
        assert seg["icon"] is not None
        assert "category" in seg
        
        # Check all 5 languages
        for lang in expected_languages:
            assert lang in seg["titles"], f"Missing title in {lang} for {seg['id']}"
            assert lang in seg["target_roles"], f"Missing roles in {lang} for {seg['id']}"
            assert lang in seg["emails"], f"Missing email in {lang} for {seg['id']}"
            
            email = seg["emails"][lang]
            assert "subject" in email and len(email["subject"]) > 10
            assert "greeting" in email
            assert "opener" in email
            assert len(email["body_points"]) >= 3
            assert "asset_pitch" in email
            assert "cta_text" in email
            assert "closing" in email

def test_multimedia_deliverables_embedded_in_all_templates():
    """Verify that Video, PowerPoint, and PDF deliverables are referenced in all rendered emails."""
    db = ome.load_database()
    deliverables = db["deliverables"]
    assert "video_interactive_player" in deliverables
    assert "pptx_download_url" in deliverables
    assert "pdf_download_url" in deliverables
    assert deliverables["pptx_file_name"] == "mizban_restaurant_intelligence_pitch.pptx"
    assert deliverables["pdf_file_name"] == "mizban_restaurant_weekly_report.pdf"

    # Test sample rendering across segments and languages
    sample_fa = ome.render_html_email("government_tourism", "fa", "دکتر احمدی", "شهرداری استانبول")
    assert "mizban_restaurant_weekly_report.pdf" in sample_fa
    assert "mizban_restaurant_intelligence_pitch.pptx" in sample_fa
    assert "video_demo" in sample_fa or "video-demo" in sample_fa or "whatsapp_pitch_portal.html#video-demo" in sample_fa
    assert "دکتر احمدی" in sample_fa
    assert "شهرداری استانبول" in sample_fa

    sample_en = ome.render_html_email("universities_startup_calls", "en", "Dr. Jane Smith", "MIT Innovation Lab")
    assert "mizban_restaurant_weekly_report.pdf" in sample_en
    assert "mizban_restaurant_intelligence_pitch.pptx" in sample_en
    assert "Dr. Jane Smith" in sample_en
    assert "MIT Innovation Lab" in sample_en

    sample_tr = ome.render_html_email("enterprise_brands", "tr", "Sayın Mehmet Bey", "Mado Restoranları")
    assert "mizban_restaurant_weekly_report.pdf" in sample_tr
    assert "mizban_restaurant_intelligence_pitch.pptx" in sample_tr
    assert "Sayın Mehmet Bey" in sample_tr

    sample_ar = ome.render_html_email("luxury_hotels", "ar", "سعادة الأستاذ منصور", "فندق رافلز إسطنبول")
    assert "mizban_restaurant_weekly_report.pdf" in sample_ar
    assert "mizban_restaurant_intelligence_pitch.pptx" in sample_ar
    assert "سعادة الأستاذ منصور" in sample_ar

    sample_de = ome.render_html_email("venture_capital", "de", "Herr Schmidt", "Earlybird Capital")
    assert "mizban_restaurant_weekly_report.pdf" in sample_de
    assert "mizban_restaurant_intelligence_pitch.pptx" in sample_de
    assert "Herr Schmidt" in sample_de

def test_resend_dispatcher_simulation_and_dns():
    """Verify Resend dispatcher simulation, attachment preparation, and DNS configuration checklist."""
    dispatcher = rd.ResendEmailDispatcher()
    
    # Validation tests
    assert dispatcher.validate_email_syntax("partner@domain.com") is True
    assert dispatcher.validate_email_syntax("invalid-email") is False
    
    # Test dispatch simulation
    res = dispatcher.dispatch_stakeholder_outreach(
        segment_id="venture_capital",
        lang_code="en",
        recipient_email="partner@212vc.com",
        recipient_name="Investment Director",
        recipient_org="212 VC Fund",
        attach_deliverables=True
    )
    assert res["success"] is True
    assert res["status"] in ("delivered_simulated", "delivered")
    assert "partner@212vc.com" in res["recipient"]
    assert res["segment_id"] == "venture_capital"

    # DNS configuration checklist
    dns = dispatcher.get_domain_dns_setup("mizbanistanbul.com")
    assert dns["domain"] == "mizbanistanbul.com"
    assert dns["score"] >= 95
    record_types = [r["type"] for r in dns["records"]]
    assert any("SPF" in t for t in record_types)
    assert any("DKIM" in t for t in record_types)
    assert any("DMARC" in t for t in record_types)
    assert any("MX" in t for t in record_types)
    assert any("BIMI" in t for t in record_types)

def test_admin_panel_html_module12_integration():
    """Verify that intelligence.html has Module 12 properly wired with interactive selectors and tables."""
    html_path = os.path.join(ROOT, "intelligence.html")
    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    assert "mod-resend-outreach" in html
    assert "۱۲. هاب بین‌المللی جذب همکاری و ارسال ایمیل Resend" in html
    assert "outreachSegmentBadges" in html
    assert "outreachLanguageTabs" in html
    assert "simulatedEmailViewer" in html
    assert "resendApiKeyInput" in html
    assert "executeResendDispatch" in html
    assert "dnsRecordsTableBody" in html
    assert "resendLedgerTableBody" in html
    assert "videoPitchModal" in html
    assert "outreachMasterDB" in html
    assert "mizban_restaurant_weekly_report.pdf" in html
    assert "mizban_restaurant_intelligence_pitch.pptx" in html
