#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
آزمون‌های خودکار سامانه هوش فرانچایز، داده‌های نمایشگاه ینی‌کاپی و ممیزی شعب
(Tests for Smart Franchise AI Suite & Yenikapı Expo Intelligence)
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import franchise_lib as fl

checks = []
fails = []


def ok(cond, msg, extra=None):
    if cond:
        checks.append("PASS " + msg + ((" | %s" % str(extra)) if extra else ""))
    else:
        fails.append("FAIL " + msg + ((" | %s" % str(extra)) if extra else ""))


# 1) اطلاعات نمایشگاه ینی‌کاپی
expo = fl.get_expo_intelligence()
ok("Yenikapı" in expo.get("venue", ""), "venue is Yenikapı Avrasya Fuar Merkezi")
ok("15-18" in expo.get("dates", ""), "dates include 15-18 October 2026")
ok("Medyafors" in expo.get("organizer", ""), "organizer Medyafors verified")

# 2) بررسی شایعات و حقایق نمایشگاه
rumors = fl.get_exhibition_rumors()
ok(len(rumors) == 5, "exactly 5 key rumors analyzed from the expo", len(rumors))
for r in rumors:
    ok(bool(r.get("id")), f"{r.get('id')} has id")
    ok(bool(r.get("title")), f"{r.get('id')} has title")
    ok(bool(r.get("rumor")), f"{r.get('id')} has rumor text")
    ok(bool(r.get("reality")), f"{r.get('id')} has reality fact-check")

# 3) مدل‌های سه‌گانه فرانچایز
models = fl.get_franchise_models()
ok(len(models) == 3, "3 franchise tiers defined", list(models.keys()))
for mid, mdata in models.items():
    ok(mdata.get("initial_investment_try", 0) > 1000000, f"{mid} initial investment > 1M TRY")
    ok(mdata.get("franchise_fee_try", 0) > 200000, f"{mid} franchise fee defined")
    ok(mdata.get("royalty_monthly_pct", 0) in [4.0, 4.5, 5.0], f"{mid} royalty percentage sane (4-5%)")

# 4) محاسبات مالی و آزمون ضد فریب (Anti-Phantom ROI)
for mid in ["express", "full_dining", "lounge_cafe"]:
    roi = fl.calculate_franchise_roi(mid)
    ok(roi["monthly_net_profit_try"] > 0, f"{mid} monthly net profit positive", roi["monthly_net_profit_try"])
    ok(roi["cost_breakdown"]["food_cost_pct"] == 30.0, f"{mid} food cost benchmark 30%")
    ok(roi["cost_breakdown"]["labor_pct"] == 22.0, f"{mid} labor cost benchmark 22%")
    ok(roi["payback_months_nominal"] < 24.0, f"{mid} nominal payback period < 24 months", roi["payback_months_nominal"])
    ok(roi["payback_months_inflation_adjusted"] >= roi["payback_months_nominal"],
       f"{mid} inflation adjusted payback accounts for Turkish Lira inflation", roi["payback_months_inflation_adjusted"])
    ok("A+" in roi["transparency_rating"], f"{mid} transparency rating A+")

# 5) ممیزی تطبیق و یکدستی شبکه چندشعبه‌ای
audit = fl.audit_branch_consistency()
ok(audit["total_branches_audited"] == 3, "3 branches audited")
ok(audit["network_average_google_rating"] >= 4.5, "network google rating >= 4.5", audit["network_average_google_rating"])
ok(audit["network_food_cost_compliance_pct"] > 90.0, "food cost compliance > 90%", audit["network_food_cost_compliance_pct"])
ok(len(audit["branch_rankings"]) == 3, "branches ranked by mystery shopper score")

print("\n".join(checks))
print("\n===== %d checks, %d failures =====" % (len(checks), len(fails)))
if fails:
    print("FAILED:", fails)
    sys.exit(1)
