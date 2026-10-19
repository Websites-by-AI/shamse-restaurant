#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite for Shamse Restaurant Multi-Platform Reviews:
Google Maps, TripAdvisor (3padviser), and Yandex Maps Analytics,
Aspect-Based Sentiment Analysis (ABSA), and Artifact Verification.
"""

import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "automation"))
import shamse_sentiment_analyzer as ssa

def test_branch_metrics_and_multiplatform_ratings():
    """Verify metrics for both Shamse branches across Google, TripAdvisor, and Yandex."""
    metrics = ssa.get_shamse_aggregate_metrics()
    branches = metrics["branches"]
    
    # Branch 1: Taksim İstiklal
    assert "shamse-taksim" in branches
    taksim = branches["shamse-taksim"]
    assert taksim["google_rating"] == 4.8
    assert taksim["google_review_count"] == 2450
    assert taksim["tripadvisor_rating"] == 4.6
    assert taksim["tripadvisor_review_count"] == 185
    assert "Travelers' Choice" in taksim["tripadvisor_award"]
    assert taksim["yandex_rating"] == 4.7
    assert taksim["yandex_review_count"] == 145
    
    # Branch 2: Kocatepe
    assert "shamse-kocatepe" in branches
    kocatepe = branches["shamse-kocatepe"]
    assert kocatepe["google_rating"] == 4.7
    assert kocatepe["google_review_count"] == 1620
    assert kocatepe["tripadvisor_rating"] == 4.5
    assert kocatepe["tripadvisor_review_count"] == 110
    assert kocatepe["yandex_rating"] == 4.6
    assert kocatepe["yandex_review_count"] == 95

    # Aggregates across channels
    assert metrics["total_google_reviews"] == 4070
    assert metrics["weighted_google_rating"] == 4.76
    assert metrics["total_tripadvisor_reviews"] == 295
    assert metrics["weighted_tripadvisor_rating"] == 4.56
    assert metrics["total_yandex_reviews"] == 240
    assert metrics["weighted_yandex_rating"] == 4.66
    assert metrics["total_direct_surveys"] == 450
    assert metrics["grand_total_feedback"] == 5055
    assert metrics["omnichannel_rating"] == 4.75

def test_channel_breakdown_dictionary():
    """Verify channel breakdown stats for Google, TripAdvisor, Yandex, and Surveys."""
    metrics = ssa.get_shamse_aggregate_metrics()
    cb = metrics["channel_breakdown"]
    
    assert "google" in cb
    assert "tripadvisor" in cb
    assert "yandex" in cb
    assert "direct_survey" in cb
    
    assert cb["tripadvisor"]["count"] == 295
    assert "Travelers' Choice" in cb["tripadvisor"]["badge"]
    assert cb["yandex"]["count"] == 240
    assert "Yandex Navi" in cb["yandex"]["highlight"]
    
    total_share = sum(ch["share_pct"] for ch in cb.values())
    assert 99.5 <= total_share <= 100.5

def test_sentiment_polarity_distribution():
    """Verify polarity percentages sum to 100% and indicate dominant guest satisfaction."""
    metrics = ssa.get_shamse_aggregate_metrics()
    polarity = metrics["sentiment_polarity"]
    
    pos = polarity["positive"]
    neu = polarity["neutral"]
    neg = polarity["negative"]
    
    assert round(pos + neu + neg, 1) == 100.0
    assert pos >= 85.0
    assert neg <= 5.0
    assert (pos - neg) > 80.0

def test_absa_aspect_scores():
    """Verify SemEval ABSA aspect dimensions across multiple channels."""
    metrics = ssa.get_shamse_aggregate_metrics()
    aspects = metrics["aspect_scores"]
    
    assert "food_quality" in aspects
    assert "atmosphere_events" in aspects
    assert "service_hospitality" in aspects
    assert "value_pricing" in aspects
    assert "queue_speed" in aspects
    
    # Food quality top strength
    assert aspects["food_quality"]["score_pct"] == 96.5
    # Atmosphere and event space
    assert aspects["atmosphere_events"]["score_pct"] == 94.8
    # Queue and wait time bottleneck
    assert aspects["queue_speed"]["score_pct"] == 74.5

def test_multilingual_distribution_including_russian():
    """Verify language breakdown includes Persian, English, Turkish, Russian, and Arabic."""
    metrics = ssa.get_shamse_aggregate_metrics()
    langs = metrics["languages_dist"]
    
    assert "ru" in langs
    assert langs["ru"]["share_pct"] == 4.1
    assert langs["ru"]["count"] == 207
    
    # Language detection engine
    assert ssa.detect_language("کوبیده زعفرانی با تهدیگ کره‌ای عالی بود") == "fa"
    assert ssa.detect_language("Sensational kebab and friendly hospitable staff") == "en"
    assert ssa.detect_language("Çok lezzetli kebap ve nefis safranlı pilav") == "tr"
    assert ssa.detect_language("مطعم فارسي ممتاز ولذيذ جدا في شارع الاستقلال") == "ar"
    assert ssa.detect_language("Превосходный ресторан персидской кухни и вкусный шашлык") == "ru"

def test_tripadvisor_and_yandex_review_sentiment():
    """Test algorithmic analysis on TripAdvisor and Yandex review examples."""
    # TripAdvisor review sample
    ta_rev = {
        "text": "One of the best culinary surprises in Beyoglu! Authentic Persian Chelo Kabab Koobideh. Courteous staff and hot cardamom tea. Truly deserves Travelers' Choice!",
        "rating": 5
    }
    ta_res = ssa.analyze_review_sentiment(ta_rev)
    assert ta_res["polarity"] == "positive"
    assert ta_res["score"] > 0.5
    assert "food_quality" in ta_res["detected_aspects"]
    assert "service_hospitality" in ta_res["detected_aspects"]
    
    # Yandex Russian review sample
    yx_rev = {
        "text": "Превосходный ресторан персидской кухни! Шашлык кубиде сочный, рис с шафраном невероятно вкусный. Очень вежливый персонал.",
        "rating": 5
    }
    yx_res = ssa.analyze_review_sentiment(yx_rev)
    assert yx_res["polarity"] == "positive"
    assert yx_res["score"] > 0.5
    assert "food_quality" in yx_res["detected_aspects"]
    assert "service_hospitality" in yx_res["detected_aspects"]

def test_infographic_and_report_artifacts():
    """Verify that SVG infographic and HTML reports reflect TripAdvisor and Yandex data."""
    ssa.save_artifacts()
    
    # SVG Infographic check
    svg_path = os.path.join(ssa.PROJECT_ROOT, "assets", "img", "shamse_sentiment_infographic.svg")
    assert os.path.exists(svg_path)
    with open(svg_path, "r", encoding="utf-8") as f:
        svg_content = f.read()
    assert "<svg" in svg_content
    assert "TripAdvisor" in svg_content
    assert "Yandex Maps" in svg_content
    assert "۵,۰۵۵" in svg_content
    assert "Travelers' Choice" in svg_content
    assert "★ 4.75" in svg_content or "★ ۴٫۷۵" in svg_content
    
    # HTML Report check
    report_path = os.path.join(ssa.PROJECT_ROOT, "reports", "shamse_sentiment_report.html")
    assert os.path.exists(report_path)
    with open(report_path, "r", encoding="utf-8") as f:
        report_html = f.read()
    assert "TripAdvisor" in report_html
    assert "Yandex Maps" in report_html
    assert "۵,۰۵۵" in report_html
    assert "Travelers' Choice" in report_html
    assert "Дмитрий Смирнов" in report_html
    assert "Sarah Jenkins" in report_html
