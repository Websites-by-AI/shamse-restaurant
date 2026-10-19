#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite for B2B WhatsApp Outreach Pitch, Multi-Platform Weekly Reports,
and Deliverables: Web View (HTML), PDF Document, and PowerPoint Presentation (PPTX).
"""

import os
import sys
import pytest
import zipfile
try:
    import pptx
    HAS_PPTX = True
except ImportError:
    HAS_PPTX = False

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_deliverable_files_existence_and_integrity():
    """Verify that Web View, PDF, and PowerPoint deliverables exist and have valid structure."""
    # 1. Web View
    view_path = os.path.join(ROOT, "whatsapp_pitch_portal.html")
    assert os.path.exists(view_path), "Web View HTML must exist in root"
    with open(view_path, "r", encoding="utf-8") as f:
        html = f.read()
    assert "<!DOCTYPE html>" in html
    assert "واتس‌اپ" in html
    assert "mizban_restaurant_weekly_report.pdf" in html
    assert "mizban_restaurant_intelligence_pitch.pptx" in html
    assert "copyWhatsAppMessage" in html

    # 2. PDF Report
    pdf_path = os.path.join(ROOT, "reports", "mizban_restaurant_weekly_report.pdf")
    assert os.path.exists(pdf_path), "PDF report must exist"
    assert os.path.getsize(pdf_path) > 10000, "PDF size must be > 10KB"
    with open(pdf_path, "rb") as f:
        header = f.read(5)
    assert header == b"%PDF-", "File must have valid PDF signature"

    # 3. PowerPoint Presentation
    pptx_path = os.path.join(ROOT, "reports", "mizban_restaurant_intelligence_pitch.pptx")
    assert os.path.exists(pptx_path), "PowerPoint presentation must exist"
    assert os.path.getsize(pptx_path) > 10000, "PPTX size must be > 10KB"
    
    # Verify valid OOXML ZIP archive containing slides
    with zipfile.ZipFile(pptx_path, "r") as z:
        names = z.namelist()
        assert "[Content_Types].xml" in names
        assert "ppt/presentation.xml" in names
        slide_xmls = [n for n in names if n.startswith("ppt/slides/slide")]
        assert len(slide_xmls) >= 6, f"Expected at least 6 slides, found {len(slide_xmls)}"
        
        # Check text in slide XMLs
        all_xml_content = " ".join([z.read(n).decode("utf-8", errors="ignore") for n in slide_xmls])
        assert "Google Maps" in all_xml_content
        assert "TripAdvisor" in all_xml_content
        assert "Yandex Maps" in all_xml_content
        assert "RevPASH" in all_xml_content

    if HAS_PPTX:
        prs = pptx.Presentation(pptx_path)
        assert len(prs.slides) >= 6

def test_whatsapp_message_content_and_onboarding_sequence():
    """Verify that the WhatsApp pitch contains the required onboarding elements and weekly report promise."""
    view_path = os.path.join(ROOT, "whatsapp_pitch_portal.html")
    with open(view_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Must contain greeting & recognition of ratings
    assert "مدیریت محترم رستوران" in html
    assert "گوگل مپ" in html
    assert "تریپ‌ادوایزر" in html
    assert "یاندکس مپ" in html

    # Must mention weekly report promise
    assert "هر هفته گزارش" in html
    assert "ثبت‌نام" in html

    # Must mention step-by-step services
    assert "پاسخ‌دهی خودکار ۴ زبانه" in html
    assert "۱۷۴٬۰۰۰" in html
    assert "۱۸۶ هتل" in html
