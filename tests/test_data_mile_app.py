#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite for Data Mile Engine, Google Maps Intel Infographics & Money Analytics.
"""

import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import data_mile_engine as dme

def test_data_mile_engine():
    # 1. Test Google Maps Summary
    gsum = dme.get_google_maps_summary()
    assert gsum["total_venues"] == 19, "Must cover all 19 venues"
    assert gsum["total_reviews"] >= 27000, f"Expected 27,000+ reviews, got {gsum['total_reviews']}"
    assert 4.4 <= gsum["average_rating"] <= 4.8, f"Average rating out of expected bounds: {gsum['average_rating']}"
    assert "positive_pct" in gsum["sentiment_dist"], "Sentiment dist must have positive_pct"
    assert "food_flavor" in gsum["aspect_scores"], "Aspect scores must include food_flavor"
    assert len(gsum["top_venues"]) == 5, "Top venues must return 5 entries"
    print("PASS Google Maps summary verified")

    # 2. Test Money Infographic Data
    msum = dme.get_money_infographic_data()
    assert msum["revpash"]["optimized_club_try"] > msum["revpash"]["traditional_try"], "Optimized RevPASH must exceed traditional"
    assert msum["monthly_offpeak_monetization"]["net_profit_try"] >= 150000, "Monthly net profit must be at least 150k TRY"
    assert msum["menu_engineering_bcg"]["star_margin_pct"] >= 70, "BCG Star margin must be >= 70%"
    assert msum["franchise_roi_payback"]["full_dining_months"] < 15, "Payback period must be under 15 months"
    print("PASS Money infographic data verified")

    # 3. Test Data Mile App Calculation
    app_calc = dme.calculate_data_mile_app("shamse-taksim", seats=60)
    assert app_calc["venue_name"] == "رستوران شمسه (شعبه استقلال)", "Selected venue matched"
    assert len(app_calc["milestones"]) == 4, "Must have exactly 4 progressive milestones"
    for m in app_calc["milestones"]:
        assert m["monthly_gain_try"] > 0, f"Milestone {m['mile']} must have positive monthly gain"
        assert len(m["checklist"]) >= 3, f"Milestone {m['mile']} must have at least 3 checklist items"
    
    assert app_calc["total_monthly_gain_try"] == 365000, "Total monthly gain should be 365,000 TRY"
    assert app_calc["total_annual_gain_try"] == 4380000, "Total annual gain should be 4,380,000 TRY"
    print("PASS Data Mile app calculation verified")

    # 4. Test Generic Fallback Calculation (without venue_id)
    generic_calc = dme.calculate_data_mile_app(None, seats=80, current_rating=4.6)
    assert generic_calc["venue_name"] == "رستوران منتخب شما"
    assert generic_calc["seats"] == 80
    assert len(generic_calc["milestones"]) == 4
    print("PASS Generic venue calculation verified")

    print("\n===== ALL DATA MILE ENGINE TESTS PASSED (0 FAILURES) =====")

if __name__ == "__main__":
    test_data_mile_engine()


def test_html_infographic_and_app_presence():
    with open("index.html", "r", encoding="utf-8") as f:
        index_html = f.read()

    assert 'id="ecosystem-infographic"' in index_html
    assert 'id="ecoTab-arch"' in index_html
    assert 'id="ecoTab-gmaps"' in index_html
    assert 'id="ecoTab-money"' in index_html
    assert 'id="ecoTab-datamile"' in index_html
    assert '۲۷,۵۱۰' in index_html
    assert '۴٫۵۷' in index_html
    assert 'RevPASH' in index_html
    assert '۴٬۳۸۰٬۰۰۰' in index_html
    assert 'switchEcoTab' in index_html

    with open("intelligence.html", "r", encoding="utf-8") as f:
        intel_html = f.read()

    assert 'id="mod-datamile"' in intel_html
    assert '۲۷,۵۱۰' in intel_html
    assert 'ABSA' in intel_html
    assert 'RevPASH' in intel_html
    assert 'BCG' in intel_html
