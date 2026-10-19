#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite for Shamse Restaurant Reviews, Aspect-Based Sentiment Analysis (ABSA),
Infographic Generation, and Report Integrity.
"""

import os
import sys
import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "automation"))
import shamse_sentiment_analyzer as ssa

def test_branch_metrics_and_rating_accuracy():
    """Verify metrics for both Shamse branches and aggregate weighted calculation."""
    metrics = ssa.get_shamse_aggregate_metrics()
    branches = metrics["branches"]
    
    # Branch 1: Taksim İstiklal
    assert "shamse-taksim" in branches
    taksim = branches["shamse-taksim"]
    assert taksim["google_rating"] == 4.8
    assert taksim["google_review_count"] == 2450
    assert "خیابان استقلال" in taksim["address"]
    assert any("میتاپ" in f for f in taksim["features"])
    
    # Branch 2: Kocatepe
    assert "shamse-kocatepe" in branches
    kocatepe = branches["shamse-kocatepe"]
    assert kocatepe["google_rating"] == 4.7
    assert kocatepe["google_review_count"] == 1620
    assert "کوجاتپه" in kocatepe["address"]

    # Aggregates
    assert metrics["total_google_reviews"] == 2450 + 1620
    assert metrics["total_google_reviews"] == 4070
    assert metrics["weighted_google_rating"] == 4.76
    assert metrics["grand_total_feedback"] > 4500

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
    assert (pos - neg) > 80.0  # Net sentiment score > 80

def test_absa_aspect_scores():
    """Verify SemEval ABSA aspect dimensions and identification of strengths vs bottlenecks."""
    metrics = ssa.get_shamse_aggregate_metrics()
    aspects = metrics["aspect_scores"]
    
    assert "food_quality" in aspects
    assert "atmosphere_events" in aspects
    assert "service_hospitality" in aspects
    assert "value_pricing" in aspects
    assert "queue_speed" in aspects
    
    # Food quality is top strength
    assert aspects["food_quality"]["score_pct"] == 96.2
    assert "کوبیده" in aspects["food_quality"]["sample_keywords"]
    
    # Atmosphere and event space is competitive differentiator
    assert aspects["atmosphere_events"]["score_pct"] == 94.5
    assert "مافیا" in aspects["atmosphere_events"]["sample_keywords"]
    
    # Service and hospitality
    assert aspects["service_hospitality"]["score_pct"] == 91.8
    assert "چای" in aspects["service_hospitality"]["sample_keywords"]
    
    # Queue and wait time identified as bottleneck
    assert aspects["queue_speed"]["score_pct"] == 74.3
    assert "گلوگاه" in aspects["queue_speed"]["status"]

def test_multilingual_distribution_and_detection():
    """Verify language breakdown and automatic language classification."""
    metrics = ssa.get_shamse_aggregate_metrics()
    langs = metrics["languages_dist"]
    
    assert langs["fa"]["share_pct"] == 71.5
    assert langs["en"]["share_pct"] == 18.2
    assert langs["tr"]["share_pct"] == 8.1
    assert langs["ar"]["share_pct"] == 2.2
    
    # Language detection engine
    assert ssa.detect_language("کوبیده زعفرانی با تهدیگ کره‌ای عالی بود") == "fa"
    assert ssa.detect_language("Sensational kebab and friendly hospitable staff") == "en"
    assert ssa.detect_language("Çok lezzetli kebap ve nefis safranlı pilav") == "tr"
    assert ssa.detect_language("مطعم فارسي ممتاز ولذيذ جدا في شارع الاستقلال") == "ar"

def test_review_sentiment_scoring_and_aspect_extraction():
    """Test algorithmic analysis on positive, mixed, and complaint reviews."""
    # Positive Persian Review
    pos_rev = {
        "text": "کوبیده‌شان واقعاً همان طعم بازاری نوستالژیک ایران را دارد؛ تهدیگ زعفرانی کره‌ای و چای باقلوای عالی بود. برخورد پرسنل هم بسیار صمیمی و محترمانه است.",
        "rating": 5
    }
    pos_res = ssa.analyze_review_sentiment(pos_rev)
    assert pos_res["polarity"] == "positive"
    assert pos_res["score"] > 0.5
    assert "food_quality" in pos_res["detected_aspects"]
    assert "service_hospitality" in pos_res["detected_aspects"]
    
    # Complaint regarding weekend queue
    complaint_rev = {
        "text": "جمعه شب بیش از ۳۰ دقیقه در ورودی خیابان استقلال در صف منتظر میز موندیم. شلوغی سالن زیاد بود و سرویس‌دهی کند شد.",
        "rating": 2
    }
    complaint_res = ssa.analyze_review_sentiment(complaint_rev)
    assert complaint_res["polarity"] == "negative"
    assert complaint_res["score"] < 0.0
    assert "queue_speed" in complaint_res["detected_aspects"]

def test_infographic_and_report_artifacts():
    """Verify that SVG infographic and HTML reports are generated and properly structured."""
    ssa.save_artifacts()
    
    # SVG Infographic check
    svg_path = os.path.join(ssa.PROJECT_ROOT, "assets", "img", "shamse_sentiment_infographic.svg")
    assert os.path.exists(svg_path)
    with open(svg_path, "r", encoding="utf-8") as f:
        svg_content = f.read()
    assert "<svg" in svg_content
    assert "۴,۰۷۰" in svg_content
    assert "۸۸٫۲٪" in svg_content
    assert "۹۶٫۲٪" in svg_content
    assert "شعبه استقلال" in svg_content
    assert "شعبه کوجاتپه" in svg_content
    
    # HTML Report check
    report_path = os.path.join(ssa.PROJECT_ROOT, "reports", "shamse_sentiment_report.html")
    root_report_path = os.path.join(ssa.PROJECT_ROOT, "shamse_sentiment_report.html")
    assert os.path.exists(report_path)
    assert os.path.exists(root_report_path)
    
    with open(report_path, "r", encoding="utf-8") as f:
        report_html = f.read()
    assert "<!DOCTYPE html>" in report_html
    assert "dir=\"rtl\"" in report_html
    assert "تحلیل عمیق نظرات و شاخص احساسات رستوران شمسه" in report_html
    assert "مهسا رضایی" in report_html
    assert "David Miller" in report_html
    assert "Caner Demir" in report_html
