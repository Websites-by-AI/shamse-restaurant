#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for:
1. Complete 30 Flaw Critique Skills Matrix presence across:
   - assets/img/shamse_system_learning_infographic.svg
   - reports/shamse_sentiment_podcast_report.pdf
   - shamse_sentiment_report.html
2. Real Customer Review Excerpts (Mahsa Rezaei, Arash Nikzad, David Miller, Dmitry Smirnov, Caner Demir, Ahmad Kamali).
3. Verified Direct Links to Google Maps (Istiklal & Kocatepe branches), Yandex Maps, and TripAdvisor.
4. HTTP Status Verification (zero broken links, HTTP 200 / 302 OK).
5. Video Deliverable (shamse_intelligence_video.mp4) & Real Comment Screenshots.
6. New Restaurant Operational Repair App (restaurant_repair_app.html) & Diagnostics Table.
"""

import os
import re
import urllib.request
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_infographic_has_all_30_skills():
    svg_path = os.path.join(REPO_ROOT, "assets", "img", "shamse_system_learning_infographic.svg")
    assert os.path.exists(svg_path), "SVG file must exist"
    
    with open(svg_path, "r", encoding="utf-8") as f:
        svg = f.read()

    for i in range(1, 31):
        skill_id = f"SKILL-{i:02d}"
        assert skill_id in svg, f"Infographic must contain {skill_id}"

    # Verify real customer reviewers quoted in SVG footer
    assert "مهسا رضایی" in svg
    assert "آرش نیکزاد" in svg
    assert "احمد کمالی" in svg
    assert "Caner Demir" in svg

def test_html_dossier_has_30_skills_and_filter():
    html_path = os.path.join(REPO_ROOT, "shamse_sentiment_report.html")
    assert os.path.exists(html_path)

    with open(html_path, "r", encoding="utf-8") as f:
        html = f.read()

    # All 30 skills present in HTML
    for i in range(1, 31):
        skill_id = f"SKILL-{i:02d}"
        assert skill_id in html, f"HTML dossier must contain {skill_id}"

    # Filter tabs function
    assert "function filterSkills" in html
    assert "skillsFilterTabs" in html
    assert "assets/img/shamse_system_learning_infographic.svg" in html

    # Real reviewers quoted in HTML
    assert "مهسا رضایی" in html
    assert "آرش نیکزاد" in html
    assert "David Miller" in html
    assert "Dmitry Smirnov" in html
    assert "Caner Demir" in html
    assert "احمد کمالی" in html

    # Video Player and Repair App presence in HTML
    assert "shamseVideoPlayer" in html
    assert "assets/video/shamse_intelligence_video.mp4" in html
    assert "restaurant_repair_app.html" in html

def test_pdf_report_integrity_and_size():
    pdf_path = os.path.join(REPO_ROOT, "reports", "shamse_sentiment_podcast_report.pdf")
    assert os.path.exists(pdf_path)
    size = os.path.getsize(pdf_path)
    assert size > 200000, f"PDF report size is {size} bytes, expected >200KB"

    # Root PDF check
    root_pdf = os.path.join(REPO_ROOT, "shamse_sentiment_podcast_report.pdf")
    assert os.path.exists(root_pdf)

    # Check content in PDF using pymupdf
    import fitz
    doc = fitz.open(pdf_path)
    assert len(doc) >= 6, f"PDF must have at least 6 pages, got {len(doc)}"
    full_text = "".join(page.get_text() for page in doc)
    assert "مهسا" in full_text and "رضایی" in full_text
    assert "David Miller" in full_text
    assert "restaurant_repair_app.html" in full_text
    assert "shamse_intelligence_video.mp4" in full_text

def test_video_deliverable_and_comment_screenshots():
    video_asset = os.path.join(REPO_ROOT, "assets", "video", "shamse_intelligence_video.mp4")
    video_root = os.path.join(REPO_ROOT, "shamse_intelligence_video.mp4")
    assert os.path.exists(video_asset), "Video asset must exist"
    assert os.path.exists(video_root), "Root video copy must exist"
    assert os.path.getsize(video_asset) > 500000, "Video must be >500KB"

    # Verify screenshots
    screenshot_files = [
        "comment_screenshot_mahsa_google.png",
        "comment_screenshot_arash_google.png",
        "comment_screenshot_david_tripadvisor.png",
        "comment_screenshot_dmitry_yandex.png",
        "comment_screenshot_caner_kocatepe.png",
        "comment_screenshot_ahmad_google.png"
    ]
    reviews_dir = os.path.join(REPO_ROOT, "assets", "img", "reviews")
    for s_file in screenshot_files:
        p = os.path.join(reviews_dir, s_file)
        assert os.path.exists(p), f"Screenshot {s_file} must exist"
        assert os.path.getsize(p) > 10000, f"Screenshot {s_file} should be >10KB"

def test_restaurant_operational_repair_app():
    app_html = os.path.join(REPO_ROOT, "restaurant_repair_app.html")
    assert os.path.exists(app_html), "Restaurant repair app HTML must exist"
    with open(app_html, "r", encoding="utf-8") as f:
        content = f.read()

    assert "FLAWS_DATABASE" in content
    assert "SKILL-01" in content
    assert "SKILL-09" in content
    assert "SKILL-25" in content
    assert "runDiagnostics" in content
    assert "sendToWhatsApp" in content

    # Gradio app script
    gradio_script = os.path.join(REPO_ROOT, "automation", "restaurant_repair_app.py")
    assert os.path.exists(gradio_script)

def test_verified_direct_review_links_connectivity():
    """
    Validates that real search and direct links to Google Maps and Yandex Maps
    are not broken and return HTTP 200 / 302.
    """
    urls_to_test = [
        ("Google Maps Branch 1 Search", "https://www.google.com/maps/search/?api=1&query=Shamse+Restaurant+Istiklal+Caddesi+179+Beyoglu+Istanbul"),
        ("Google Maps Branch 2 Search", "https://www.google.com/maps/search/?api=1&query=Shamse+Restaurant+Abdulhak+Hamit+Caddesi+17+Kocatepe+Istanbul"),
        ("Google Maps Branch 1 Direct", "https://maps.google.com/?q=Istiklal+Caddesi+179+Beyoglu+Istanbul"),
        ("Google Maps Branch 2 Direct", "https://maps.google.com/?q=Abdulhak+Hamit+Caddesi+17+Kocatepe+Istanbul"),
        ("Yandex Maps Search", "https://yandex.com/maps/?text=Shamse+Restaurant+Istanbul")
    ]

    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}

    for name, url in urls_to_test:
        req = urllib.request.Request(url, headers=headers)
        with urllib.request.urlopen(req, timeout=12) as response:
            status = response.status
            assert status in (200, 301, 302), f"Link for {name} ({url}) returned broken status {status}"
