#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for:
1. Shamse System Learning Infographic (SVG): Closed-loop reinforcement, 5 stages, delta metrics.
2. Index.html Executive Credentials Bar, Card, Direct Access Links, Passwords, and 1-Click WhatsApp Copy.
3. System Learning Tab 5 in #ecosystem-infographic and switchEcoTab functionality.
"""

import os
import pytest

def test_system_learning_infographic_file():
    svg_path = "assets/img/shamse_system_learning_infographic.svg"
    assert os.path.exists(svg_path), "SVG file must exist"
    
    with open(svg_path, "r", encoding="utf-8") as f:
        svg = f.read()

    assert "<svg" in svg and "</svg>" in svg
    assert "Continuous Closed-Loop Learning" in svg or "یادگیری پیوسته" in svg
    assert "Google Maps" in svg
    assert "TripAdvisor" in svg
    assert "Yandex Maps" in svg
    assert "Dimer Engine" in svg
    assert "RLOF Core" in svg or "یادگیری تقویتی" in svg
    assert "+0.28★" in svg
    assert "-۴۲٪" in svg or "کاهش ۴۲٪" in svg
    assert "حلقهٔ بسته خودآموز" in svg

def test_index_html_executive_credentials_and_learning_tab():
    index_path = "index.html"
    assert os.path.exists(index_path)

    with open(index_path, "r", encoding="utf-8") as f:
        html = f.read()

    # Top Announcement Banner
    assert 'id="siteExecutiveCredentialsBanner"' in html
    assert "shamse_manager" in html
    assert "Shamse#Taksim2026" in html
    assert "shamse_admin" in html
    assert "Shamse@2026!Istiklal" in html

    # Executive Deliverables Card
    assert 'id="executiveCredentialsCard"' in html
    assert "SHAMSE-TAK-2026" in html
    assert "reports/shamse_sentiment_podcast_report.pdf" in html
    assert "reports/mizban_restaurant_intelligence_pitch.pptx" in html
    assert "assets/audio/shamse_intelligence_podcast.mp3" in html
    assert "shamse_sentiment_report.html" in html
    assert "copyIndexExecutiveWhatsApp" in html

    # Ecosystem Infographic Tab 5: System Learning
    assert "switchEcoTab('learning'" in html
    assert 'id="ecoTab-learning"' in html
    assert "shamse_system_learning_infographic.svg" in html
    assert "function switchEcoTab" in html
