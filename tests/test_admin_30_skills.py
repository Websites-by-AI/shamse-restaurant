#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
آزمون‌های خودکار ۳۰ مهارت ادمین پنل و تولید اینفوگرافیک.
Tests for Admin Panel 30 Skills and Infographic Generation Library.
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

import admin_skills_lib as asl

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

# 1. Database structure checks
db = asl.load_admin_skills_db()
check(db.get("total_admin_skills") == 30, "total_admin_skills count is 30", db.get("total_admin_skills"))

skills = asl.get_admin_skills()
check(len(skills) == 30, "exactly 30 skills returned by get_admin_skills()", len(skills))

clusters = asl.get_admin_clusters()
check(len(clusters) == 3, "exactly 3 clusters defined", len(clusters))

# 2. Individual skill validations
seen_ids = set()
for s in skills:
    sid = s.get("id")
    check(bool(sid), f"{sid} has id")
    check(sid not in seen_ids, f"{sid} is unique")
    seen_ids.add(sid)
    
    check(bool(s.get("cluster_id")), f"{sid} has cluster_id")
    check(bool(s.get("name_fa")), f"{sid} has name_fa")
    check(bool(s.get("name_en")), f"{sid} has name_en")
    check(bool(s.get("description")), f"{sid} has description")
    check(bool(s.get("tool")), f"{sid} has tool")
    check(bool(s.get("trigger")), f"{sid} has trigger")
    check(bool(s.get("action")), f"{sid} has action")

# 3. Cluster checks
cluster_ids = {c["id"] for c in clusters}
for s in skills:
    check(s["cluster_id"] in cluster_ids, f"{s['id']} belongs to valid cluster", s["cluster_id"])

# 4. Search and filtering checks
visual_skills = asl.filter_admin_skills(cluster_id="visual-intel")
check(len(visual_skills) == 10, "visual-intel cluster has 10 skills", len(visual_skills))

crm_skills = asl.filter_admin_skills(cluster_id="admin-crm")
check(len(crm_skills) == 10, "admin-crm cluster has 10 skills", len(crm_skills))

hf_skills = asl.filter_admin_skills(cluster_id="hf-orchestration")
check(len(hf_skills) == 10, "hf-orchestration cluster has 10 skills", len(hf_skills))

revpash_search = asl.filter_admin_skills(query="RevPASH")
check(len(revpash_search) >= 1, "search for RevPASH found skill", len(revpash_search))

llama_search = asl.filter_admin_skills(query="Llama-3")
check(len(llama_search) >= 1, "search for Llama-3 found skill", len(llama_search))

# 5. Executive Infographic Generator check (SKILL-ADM-010)
infographic_data = asl.generate_executive_infographic_data()
check("kpis" in infographic_data, "infographic has kpis")
check(infographic_data["kpis"]["revpash_tl"] == 55.0, "kpis revpash matches", infographic_data["kpis"]["revpash_tl"])
check(len(infographic_data["menu_stars"]) >= 3, "infographic has menu stars", len(infographic_data["menu_stars"]))
check("food" in infographic_data["sentiment_radar"], "infographic has sentiment radar")

print(f"\n===== {passed} checks, {failed} failures =====")
if failed > 0:
    sys.exit(1)
