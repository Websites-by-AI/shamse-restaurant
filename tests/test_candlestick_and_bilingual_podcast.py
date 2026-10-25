#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
آزمون‌های جامع چارت کندل‌استیک فارکس احساسات، تقویم دوگانه، مقایسه های‌تک در برابر فیکس سریع، و پادکست دوزبانه
Tests for Candlestick Sentiment Chart, Dual Calendars, High-Tech vs. Easy Fix, and Bilingual Podcasts
"""

import os
import sys
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "automation"))

import candlestick_sentiment_engine as cse


def test_candlestick_sessions_data():
    """بررسی داده‌های ۶ جلسه کندل‌استیک، شاخص‌های OHLC، تقویم‌های شمسی و میلادی و نگاشت مهارت‌ها"""
    sessions = cse.get_candlestick_sessions()
    assert len(sessions) == 6, f"Expected 6 candlestick sessions, got {len(sessions)}"

    for s in sessions:
        assert s["id"].startswith("CANDLE-")
        assert 4.0 <= s["low"] <= s["high"] <= 5.0
        assert s["low"] <= s["open"] <= s["high"]
        assert s["low"] <= s["close"] <= s["high"]
        assert s["volume_guests"] > 100

        # تقویم دوگانه
        assert "۱۴۰۵" in s["date_shamsi"], "Shamsi date must have 1405"
        assert "2026" in s["date_miladi"], "Miladi date must have 2026"

        # مقایسه های‌تک در برابر فیکس سریع
        assert "High-Tech" in s["high_tech_tag"]
        assert "Easy" in s["easy_fix_tag"]
        assert "$" in s["high_tech_cost"]
        assert "لیر" in s["easy_fix_cost"] or "رایگان" in s["easy_fix_cost"]
        assert s["skill_code"].startswith("SKILL-")


def test_candlestick_svg_generation():
    """بررسی تولید نمودار SVG و فایل برداری کندل‌استیک"""
    svg = cse.generate_candlestick_svg()
    assert "<svg" in svg and "</svg>" in svg
    assert "CANDLE-01" in svg
    assert "CANDLE-06" in svg
    assert "Bullish" in svg

    svg_file = os.path.join(REPO_ROOT, "assets", "img", "sentiment_candlestick_chart.svg")
    assert os.path.exists(svg_file), "SVG chart file must exist"
    assert os.path.getsize(svg_file) > 2000, "SVG chart size must be >2KB"


def test_bilingual_podcast_audio_files():
    """بررسی وجود فایل‌های صوتی پادکست فارسی و ترکی استانبولی"""
    audio_fa = os.path.join(REPO_ROOT, "assets", "audio", "shamse_intelligence_podcast.mp3")
    audio_tr = os.path.join(REPO_ROOT, "assets", "audio", "shamse_intelligence_podcast_tr.mp3")
    root_fa = os.path.join(REPO_ROOT, "shamse_intelligence_podcast.mp3")
    root_tr = os.path.join(REPO_ROOT, "shamse_intelligence_podcast_tr.mp3")

    assert os.path.exists(audio_fa), "Farsi podcast asset must exist"
    assert os.path.exists(audio_tr), "Turkish podcast asset must exist"
    assert os.path.exists(root_fa), "Root Farsi podcast must exist"
    assert os.path.exists(root_tr), "Root Turkish podcast must exist"

    assert os.path.getsize(audio_fa) > 500000, "Farsi audio should be >500KB"
    assert os.path.getsize(audio_tr) > 200000, "Turkish audio should be >200KB"


def test_admin_panel_has_candlestick_and_bilingual_podcast():
    """بررسی وجود بخش چارت کندل‌استیک، جدول مقایسه های‌تک، تقویم دوگانه و پلیر دوزبانه در ادمین پنل"""
    admin_path = os.path.join(REPO_ROOT, "admin_panel.html")
    with open(admin_path, "r", encoding="utf-8") as f:
        admin_html = f.read()

    assert "Forex-Style Candlestick Sentiment v2.4" in admin_html
    assert "CANDLE-01" in admin_html
    assert "CANDLE-06" in admin_html
    assert "۲۴ مهر ۱۴۰۵" in admin_html
    assert "16 October 2026" in admin_html
    assert "High-Tech AI Frontier" in admin_html
    assert "Easy Quick Fix" in admin_html
    assert "SKILL-01" in admin_html and "SKILL-25" in admin_html
    assert "adminAudioPlayerFa" in admin_html
    assert "adminAudioPlayerTr" in admin_html
    assert "Türkçe Podcast" in admin_html
    assert "Mizban İstanbul ve Şemse Restoran" in admin_html


def test_shamse_sentiment_report_and_pdf_have_turkish_podcast():
    """بررسی وجود پادکست ترکی و چارت در پرونده وب و PDF"""
    web_path = os.path.join(REPO_ROOT, "shamse_sentiment_report.html")
    with open(web_path, "r", encoding="utf-8") as f:
        web_html = f.read()

    assert "shamse_intelligence_podcast_tr.mp3" in web_html
    assert "تحلیل تکنیکال فارکس احساسات" in web_html

    pdf_path = os.path.join(REPO_ROOT, "reports", "shamse_sentiment_podcast_report.pdf")
    import fitz
    doc = fitz.open(pdf_path)
    pdf_text = "".join(page.get_text() for page in doc)
    assert "shamse_intelligence_podcast_tr.mp3" in pdf_text or "ترکی استانبولی" in pdf_text
