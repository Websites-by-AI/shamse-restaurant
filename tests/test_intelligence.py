#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست‌های آفلاین ماژول هوش تجاری، تحلیل رقبا، بهینه‌سازی فضا و داده‌های آتیکووا.
"""
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import intelligence_lib as il  # noqa: E402

checks, fails = [], []


def ok(cond, label, extra=""):
    checks.append(("PASS " if cond else "FAIL ") + label + ((" | " + str(extra)) if extra else ""))
    if not cond:
        fails.append(label)


# 1) تولید کمپین و تبلیغات با هوش مصنوعی
for etype in ["mafia", "tech", "poetry"]:
    c = il.generate_campaign(etype)
    ok(bool(c.get("title")), f"campaign {etype} has title")
    ok(len(c.get("telegram", "")) > 100, f"campaign {etype} telegram text length", len(c.get("telegram", "")))
    ok(len(c.get("instagram", "")) > 80, f"campaign {etype} instagram text length", len(c.get("instagram", "")))
    ok(len(c.get("run_of_show", [])) >= 3, f"campaign {etype} run of show items", len(c.get("run_of_show", [])))

custom_c = il.generate_campaign("mafia", venue_note="پروژکتور 4K و اینترنت اختصاصی فعال است")
ok("پروژکتور 4K" in custom_c["telegram"], "custom venue note embedded into campaign")

# 2) ماتریس تحلیل رقبا
matrix = il.COMPETITOR_MATRIX
ok(len(matrix) >= 6, "competitor matrix has at least 6 venues", len(matrix))
for comp in matrix:
    name = comp.get("name")
    ok(comp.get("avg_spend_try", 0) > 200, f"{name} spend > 200 TRY", comp.get("avg_spend_try"))
    ok(comp.get("google_rating", 0) >= 4.0, f"{name} rating >= 4.0", comp.get("google_rating"))
    ok(comp.get("reviews_count", 0) > 100, f"{name} reviews > 100", comp.get("reviews_count"))
    ok(bool(comp.get("strengths")), f"{name} has strengths", name)

# 3) مهندسی منو و هزینه‌ها
menu_data = il.MENU_ENGINEERING
ok(len(menu_data) >= 5, "menu engineering covers at least 5 dishes", len(menu_data))
for dish in menu_data:
    item = dish.get("item")
    price = dish.get("selling_price_try", 0)
    cost = dish.get("food_cost_try", 0)
    margin = dish.get("margin_try", 0)
    pct = dish.get("food_cost_pct", 0)
    ok(price > cost, f"{item} selling price > food cost", (price, cost))
    ok(margin == price - cost, f"{item} margin matches price - cost", margin)
    ok(10 <= pct <= 45, f"{item} food cost percentage sane (10-45%)", pct)

# 4) تحلیل احساسات گوگل مپ
sentiment = il.GOOGLE_MAPS_SENTIMENT
ok(sentiment["total_analyzed_reviews"] >= 2000, "over 2000 reviews analyzed", sentiment["total_analyzed_reviews"])
ok(sentiment["positive_pct"] > 75, "positive sentiment > 75%", sentiment["positive_pct"])
ok(len(sentiment["top_positive_themes"]) >= 3, "positive themes identified", len(sentiment["top_positive_themes"]))
ok(len(sentiment["top_negative_themes"]) >= 2, "negative themes identified", len(sentiment["top_negative_themes"]))
auto_replies = sentiment["ai_auto_reply_templates"]["positive"]
ok("fa" in auto_replies and "tr" in auto_replies and "en" in auto_replies, "auto-replies in 3 languages")

# 5) فرمول بهینه‌سازی و درآمدزایی از فضای خالی
yld = il.calculate_space_yield(total_seats=140)
ok(yld["empty_seats_off_peak"] > 50, "empty seats detected in off-peak hours", yld["empty_seats_off_peak"])
ok(yld["incremental_monthly_try"] > 100000, "incremental monthly revenue > 100k TRY", yld["incremental_monthly_try"])
ok(yld["incremental_monthly_usd"] > 3000, "incremental monthly revenue > $3k USD", yld["incremental_monthly_usd"])
ok(yld["annual_projected_try"] == yld["incremental_monthly_try"] * 12, "annual projection accurate")

# 6) بنچ‌مارک پلتفرم‌های بین‌المللی
benchmarks = il.GLOBAL_BENCHMARKS
names = [b["platform"] for b in benchmarks]
ok("RestauRent" in names, "RestauRent benchmarked")
ok("Tagvenue" in names, "Tagvenue benchmarked")
ok("OpenTable Private Dining" in names, "OpenTable benchmarked")
ok("Tripleseat" in names, "Tripleseat benchmarked")
ok("Yabangee" in names, "Yabangee benchmarked")

# 7) دیتابیس جامع استانبول و شبکه آتیکووا
istanbul_db_path = os.path.join(ROOT, "automation", "istanbul_directory.json")
ok(os.path.exists(istanbul_db_path), "istanbul_directory.json exists")
with open(istanbul_db_path, "r", encoding="utf-8") as f:
    dir_data = json.load(f)
ok(len(dir_data.get("persian_and_afghan", [])) == 19, "19 core restaurants included")
ok(len(dir_data.get("atikova_hospitality_network", [])) >= 10, "Atikova hospitality network included")
ok(len(dir_data.get("istanbul_landmarks", [])) >= 4, "Istanbul landmarks included")

print("\n".join(checks))
print("\n===== %d checks, %d failures =====" % (len(checks), len(fails)))
if fails:
    print("FAILED:", fails)
    sys.exit(1)
