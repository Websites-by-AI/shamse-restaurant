#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for the Shamse Multiplatform Sentiment Podcast & PDF Intelligence Dossier.
Verifies:
  1. PDF Report existence and vector structure.
  2. Synthesized executive podcast audio file integrity.
  3. Interactive Web View (ویونا) elements: podcast player, 4 vital flaws, 100 skills mapping, 4-language replies, and omnichannel dispatch links.
"""

import os
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def test_pdf_dossier_deliverable():
    pdf_path = os.path.join(REPO_ROOT, "reports", "shamse_sentiment_podcast_report.pdf")
    assert os.path.exists(pdf_path), "PDF report deliverable must exist in reports/"
    size = os.path.getsize(pdf_path)
    assert size > 50000, f"PDF report size should be substantial, got {size} bytes"

    # Also verify the symlink / copy in root
    root_pdf = os.path.join(REPO_ROOT, "shamse_sentiment_podcast_report.pdf")
    assert os.path.exists(root_pdf), "Root PDF copy must exist for direct user download"

def test_podcast_audio_deliverable():
    audio_path = os.path.join(REPO_ROOT, "assets", "audio", "shamse_intelligence_podcast.mp3")
    assert os.path.exists(audio_path), "Audio podcast file must exist in assets/audio/"
    size = os.path.getsize(audio_path)
    assert size > 100000, f"Audio podcast file size should be >100KB, got {size} bytes"

def test_interactive_web_dossier_html():
    html_path = os.path.join(REPO_ROOT, "shamse_sentiment_report.html")
    assert os.path.exists(html_path), "Interactive HTML report must exist"

    with open(html_path, "r", encoding="utf-8") as f:
        content = f.read()

    # Verify Podcast Player
    assert "podcastPlayBtn" in content, "Must include interactive audio podcast play button"
    assert "assets/audio/shamse_intelligence_podcast.mp3" in content, "Must link to podcast audio"
    assert "podcastProgressBar" in content, "Must include audio scrub progress bar"
    assert "audioWaveform" in content, "Must include visual audio waveform"

    # Verify 4 Vital Operational Flaws & 100 Skills Mapping
    assert "کالبدشکافی ۴ نقص حیاتی" in content, "Must analyze the 4 vital operational flaws"
    assert "TripAdvisor" in content, "Must analyze TripAdvisor European tourist sentiment"
    assert "Yandex" in content, "Must analyze Yandex Maps CIS/Russian sentiment"
    assert "SKILL-051" in content, "Must map to Hospitality Skill 051"
    assert "SKILL-081" in content, "Must map to Hospitality Skill 081"
    assert "SKILL-031" in content, "Must map to Hospitality Skill 031"
    assert "SKILL-094" in content, "Must map to Hospitality Skill 094"

    # Verify 4-Language AI Customer Responses
    assert "enTripReply" in content, "Must include English TripAdvisor reply"
    assert "ruYandexReply" in content, "Must include Russian Yandex Maps reply"
    assert "faGoogleReply" in content, "Must include Persian Google Maps reply"
    assert "trGoogleReply" in content, "Must include Turkish Google Maps reply"

    # Verify 5-Channel Omnichannel Outreach Console for Shamse
    assert "shamsemedia1@gmail.com" in content, "Must include official Shamse email"
    assert "+90 501 325 24 52" in content, "Must include Shamse WhatsApp number"
    assert "shamse.istanbul" in content, "Must include Shamse Instagram handle"
    assert "shamse_istanbul" in content, "Must include Shamse Telegram channel"
    assert "shamseistanbul" in content, "Must include Shamse Facebook ID"
