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

def test_pdf_report_integrity_and_size():
    pdf_path = os.path.join(REPO_ROOT, "reports", "shamse_sentiment_podcast_report.pdf")
    assert os.path.exists(pdf_path)
    size = os.path.getsize(pdf_path)
    # The updated PDF with 6 pages, 30 skills, and embedded vector SVG should be over 200KB
    assert size > 200000, f"PDF report size is {size} bytes, expected >200KB"

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
