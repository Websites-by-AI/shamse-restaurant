#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
آزمون‌های خودکار ماژول مقالات علمی ISI و مدل‌های هاگینگ‌فیس.
Tests for Academic Papers and Hugging Face AI Engine.
"""

import os
import sys

_cur = os.path.dirname(os.path.abspath(__file__))
_root = os.path.dirname(_cur)
if _root not in sys.path:
    sys.path.insert(0, _root)
_auto = os.path.join(_root, "automation")
if _auto not in sys.path:
    sys.path.insert(0, _auto)

import academic_ai_engine as aae

passed = 0
failed = 0

def check(condition, desc, val=None):
    global passed, failed
    if condition:
        passed += 1
        print(f"PASS {desc}" + (f" | {val}" if val is not None else ""))
    else:
        failed += 1
        print(f"FAIL {desc}" + (f" | {val}" if val is not None else ""))

# 1. Academic papers database checks
papers = aae.load_academic_papers()
check(len(papers) == 10, "exactly 10 ISI academic papers registered", len(papers))

for p in papers:
    pid = p.get("id")
    check(bool(pid), f"{pid} has valid id")
    check(bool(p.get("title")), f"{pid} has English title")
    check(len(p.get("authors", [])) >= 1, f"{pid} has at least 1 author")
    check(bool(p.get("journal")), f"{pid} has journal/conference")
    check(p.get("year", 0) >= 1980, f"{pid} year >= 1980", p.get("year"))
    check(bool(p.get("doi_or_url")), f"{pid} has DOI or URL")
    check(bool(p.get("breakthrough_fa")), f"{pid} has Persian breakthrough")
    check(bool(p.get("math_formula")), f"{pid} has math formula")
    check(bool(p.get("github_repo")), f"{pid} has GitHub code repo")
    check(bool(p.get("huggingface_model")), f"{pid} has Hugging Face model")

# 2. RevPASH mathematical formula test (Kimes 1999)
# If revenue is 77,000 TRY, 140 seats, 10 hours => 77000 / 1400 = 55.0 TRY/seat-hour
revpash = aae.calculate_kimes_revpash(77000, 140, 10)
check(revpash == 55.0, "Kimes RevPASH calculates accurately", revpash)
check(aae.calculate_kimes_revpash(0, 100, 10) == 0.0, "RevPASH 0 revenue is 0.0")
check(aae.calculate_kimes_revpash(50000, 0, 10) == 0.0, "RevPASH 0 seats handled gracefully")

# 3. Kasavana & Smith (1982) Menu Engineering BCG Matrix test
sample_dishes = [
    {"name": "کوبیده", "price": 420, "food_cost": 135, "sold_quantity": 150},
    {"name": "قورمه‌سبزی", "price": 350, "food_cost": 88, "sold_quantity": 180},
    {"name": "کشک بادمجان", "price": 190, "food_cost": 34, "sold_quantity": 210},
    {"name": "شیشلیک", "price": 680, "food_cost": 258, "sold_quantity": 60}
]
bcg_res = aae.classify_kasavana_smith_menu(sample_dishes)
check(len(bcg_res) == 4, "BCG classified all 4 dishes", len(bcg_res))
quadrants = [b["quadrant"] for b in bcg_res]
check("Star" in quadrants, "at least one Star quadrant identified", quadrants)
check("Plowhorse" in quadrants or "Puzzle" in quadrants or "Star" in quadrants, "quadrant distribution sane")

for b in bcg_res:
    check(b["contribution_margin"] == b["price"] - b["food_cost"], f"{b['name']} CM matches price - cost")
    check(b["food_cost_pct"] > 0, f"{b['name']} food cost % positive", b["food_cost_pct"])

# 4. SemEval-2014 ABSA framework test (Pontiki et al. 2014)
aspect_mentions = {
    "food": [1, 1, 1, 0, 1], # mostly positive
    "service": [-1, -1, 0], # slow service
    "price": [1, 1, 0],
    "ambience": [1, 1, 1, 1]
}
absa_res = aae.calculate_absa_score(aspect_mentions)
check(absa_res["food"]["rating_out_of_5"] > 4.0, "Food aspect rating high", absa_res["food"]["rating_out_of_5"])
check(absa_res["service"]["rating_out_of_5"] < 3.0, "Service aspect rating low", absa_res["service"]["rating_out_of_5"])
check(2.0 <= absa_res["composite_score"] <= 5.0, "Composite score in 2-5 range", absa_res["composite_score"])

# 5. Anti-Phantom Franchise Payback test (Bradach 1997)
roi = aae.calculate_anti_phantom_franchise_roi(1450000, 151900, 0.35)
check(roi["nominal_payback_months"] < roi["inflation_adjusted_payback_months"], 
      "inflation adjusted payback is longer than nominal", 
      (roi["nominal_payback_months"], roi["inflation_adjusted_payback_months"]))
check(roi["transparency_rating"] == "A+", "Transparency rating is A+")

# 6. Hugging Face registry check
hf_models = aae.get_huggingface_model_registry()
check(len(hf_models) >= 5, "at least 5 Hugging Face models in registry", len(hf_models))
for hfm in hf_models:
    check("huggingface.co" in hfm["url"], f"valid HF url for {hfm['model_id']}")

print(f"\n===== {passed} checks, {failed} failures =====")
if failed > 0:
    sys.exit(1)
