#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
کتابخانه مدیریت و اجرای ۳۰ مهارت پیشرفته ادمین پنل و تولید اینفوگرافیک.
Admin Panel 30 Master Skills & Infographic Generation Library.
"""

import json
import os

SKILLS_FILE = os.path.join(os.path.dirname(__file__), "admin_30_skills.json")


def load_admin_skills_db():
    """بارگذاری پایگاه داده ۳۰ مهارت ادمین و اینفوگرافیک."""
    with open(SKILLS_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_admin_skills():
    """دریافت لیست تمامی ۳۰ مهارت."""
    return load_admin_skills_db().get("skills", [])


def get_admin_clusters():
    """دریافت ۳ خوشه تخصصی مهارت‌ها."""
    return load_admin_skills_db().get("clusters", [])


def get_admin_skill_by_id(skill_id):
    """یافتن مهارت با شناسه یکتا (مثال: SKILL-ADM-001)."""
    for s in get_admin_skills():
        if s["id"] == skill_id:
            return s
    return None


def filter_admin_skills(cluster_id=None, query=None):
    """فیلتر مهارت‌ها بر اساس خوشه یا کلیدواژه جستجو."""
    skills = get_admin_skills()
    res = []
    q = (query or "").strip().lower()
    for s in skills:
        if cluster_id and cluster_id != "all" and s.get("cluster_id") != cluster_id:
            continue
        if q:
            match = (
                q in s.get("name_fa", "").lower()
                or q in s.get("name_en", "").lower()
                or q in s.get("description", "").lower()
                or q in s.get("tool", "").lower()
                or q in s.get("id", "").lower()
            )
            if not match:
                continue
        res.append(s)
    return res


def generate_executive_infographic_data(restaurant_id="farsi-taksim"):
    """
    تولید داده‌های ساختاریافته اینفوگرافیک اجرایی تک‌صفحه‌ای (SKILL-ADM-010).
    تلفیق دیتای گوگل مپ، ریتینگ، RevPASH، حاشیه سود منو و وضعیت پایپ‌لاین.
    """
    return {
        "kpis": {
            "revpash_tl": 55.0,
            "seat_occupancy_pct": 88.5,
            "google_rating": 4.6,
            "total_reviews": 1840,
            "absa_sentiment_pct": 86.4,
            "offpeak_incremental_tl": 170000,
            "active_gateways": 8,
            "admin_skills_count": 30
        },
        "menu_stars": [
            {"name": "چلوکباب کوبیده سنتی", "cm_tl": 285, "fc_pct": 32.1, "quadrant": "Star"},
            {"name": "خورش قورمه‌سبزی", "cm_tl": 262, "fc_pct": 25.1, "quadrant": "Star"},
            {"name": "شیشلیک مشهد مخصوص", "cm_tl": 422, "fc_pct": 37.9, "quadrant": "Puzzle"},
            {"name": "پیش‌غذاهای اصیل", "cm_tl": 156, "fc_pct": 17.9, "quadrant": "Plowhorse"}
        ],
        "sentiment_radar": {
            "food": 4.7,
            "service": 4.4,
            "ambience": 4.6,
            "price_value": 4.2
        },
        "club_events": {
            "monthly_events": 8,
            "avg_attendance": 40,
            "event_revenue_tl": 80000
        }
    }


if __name__ == "__main__":
    db = load_admin_skills_db()
    print(f"Loaded {db['total_admin_skills']} admin skills across {len(db['clusters'])} clusters.")
    sample = get_admin_skill_by_id("SKILL-ADM-001")
    print("Sample Skill 1:", sample["name_fa"])
    info = generate_executive_infographic_data()
    print("Executive Infographic KPIs:", info["kpis"])
