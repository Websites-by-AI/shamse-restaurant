#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
آزمون‌های خودکار سامانه ۱۰۰ مهارت هوش تجاری و گیت‌وی‌های پایش نظرات
(Tests for 100 Hospitality Intelligence Skills & Reputation Gateways)
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import reputation_skills as rep

checks = []
fails = []


def ok(cond, msg, extra=None):
    if cond:
        checks.append("PASS " + msg + ((" | %s" % str(extra)) if extra else ""))
    else:
        fails.append("FAIL " + msg + ((" | %s" % str(extra)) if extra else ""))


# 1) بررسی تعداد و ساختار ۱۰۰ مهارت
skills = rep.get_all_skills()
ok(len(skills) == 100, "exactly 100 skills registered in database", len(skills))

clusters = rep.get_clusters()
ok(len(clusters) == 10, "exactly 10 functional clusters registered", len(clusters))

# 2) بررسی توزیع یکدست مهارت‌ها (۱۰ مهارت در هر خوشه)
cluster_counts = {}
seen_ids = set()
for s in skills:
    sid = s.get("id")
    ok(sid and sid not in seen_ids, f"unique skill id {sid}")
    seen_ids.add(sid)

    cid = s.get("cluster_id")
    cluster_counts[cid] = cluster_counts.get(cid, 0) + 1

    ok(bool(s.get("name_fa")), f"{sid} has persian name")
    ok(bool(s.get("name_en")), f"{sid} has english name")
    ok(bool(s.get("description")), f"{sid} has description")
    ok(bool(s.get("engine_tool")), f"{sid} has tool/engine")
    ok(bool(s.get("trigger")), f"{sid} has trigger condition")
    ok(bool(s.get("action")), f"{sid} has action defined")

for cl in clusters:
    cid = cl["id"]
    cnt = cluster_counts.get(cid, 0)
    ok(cnt == 10, f"cluster {cid} ({cl['title_en']}) contains exactly 10 skills", cnt)

# 3) بررسی گیت‌وی‌های ورودی
gateways = rep.get_gateways_status()
ok(len(gateways) >= 7, "at least 7 omnichannel gateways configured", len(gateways))
for gid, ginfo in gateways.items():
    ok(bool(ginfo.get("name_fa")), f"gateway {gid} has persian name")
    ok(len(ginfo.get("channels", [])) >= 1, f"gateway {gid} has connected channels")
    ok(ginfo.get("status") in ["ready", "active"], f"gateway {gid} status operational", ginfo.get("status"))

# 4) جستجو و دریافت اختصاصی مهارت
sk21 = rep.get_skill_by_id("SKILL-021")
ok(sk21 and "5-Star" in sk21["name_en"], "skill-021 retrieval works", sk21.get("name_fa") if sk21 else None)

sk_lower = rep.get_skill_by_id("skill-031")
ok(sk_lower and "Food Safety" in sk_lower["name_en"], "case-insensitive lookup works", sk_lower.get("name_fa") if sk_lower else None)

search_seo = rep.search_skills("سئو")
ok(len(search_seo) >= 2, "search for 'سئو' returns relevant skills", len(search_seo))

search_crisis = rep.search_skills("بحران")
ok(len(search_crisis) >= 3, "search for 'بحران' returns crisis skills", len(search_crisis))

# 5) شبیه‌سازی پایپ‌لاین نظرات و فعال‌سازی مهارت‌ها
# سناریو ۱: نظر ۵ ستاره با نام غذا در گوگل مپ
sim_pos = rep.simulate_review_pipeline("Google Maps", 5, "کباب کوبیده زعفرانی شمسه عالی بود و پرسنل فوق‌العاده مودب بودند.", "سارا امینی")
ok(sim_pos["rating"] == 5.0, "positive review rating preserved")
ok(sim_pos["language"] == "fa", "persian language detected")
ok(sim_pos["sentiment_score"] > 0.8, "sentiment score high positive", sim_pos["sentiment_score"])
triggered_pos_ids = [s["id"] for s in sim_pos["triggered_skills"]]
ok("SKILL-001" in triggered_pos_ids, "Google GBP skill triggered")
ok("SKILL-021" in triggered_pos_ids, "5-star praise skill triggered")
ok("SKILL-016" in triggered_pos_ids, "dish sentiment extraction triggered")
ok(not sim_pos["is_crisis"], "positive review is not a crisis")

# سناریو ۲: نظر ۱ ستاره مسمومیت و هشدار بحران
sim_crisis = rep.simulate_review_pipeline("Google Maps", 1, "بعد از خوردن سالاد مسموم شدیم و دل‌درد شدید گرفتیم!", "رضا نوری")
ok(sim_crisis["is_crisis"], "crisis correctly flagged")
ok(sim_crisis["crisis_type"] == "safety", "safety crisis type identified")
triggered_crisis_ids = [s["id"] for s in sim_crisis["triggered_skills"]]
ok("SKILL-031" in triggered_crisis_ids, "food safety warning skill triggered")
ok("SKILL-035" in triggered_crisis_ids, "head chef escalation skill triggered")
ok("🚨" in sim_crisis["internal_action_note"], "emergency action note generated")

# سناریو ۳: نظر ترکی در اینستاگرام
sim_tr = rep.simulate_review_pipeline("Instagram", 5, "Harika bir lezzet, ellerinize sağlık!", "Emre Demir")
ok(sim_tr["language"] == "tr", "turkish language detected")
triggered_tr_ids = [s["id"] for s in sim_tr["triggered_skills"]]
ok("SKILL-004" in triggered_tr_ids, "instagram comments skill triggered")
ok("SKILL-012" in triggered_tr_ids, "turkish gastronomy NLP skill triggered")

# سناریو ۴: شکایت از صف و شلوغی
sim_queue = rep.simulate_review_pipeline("Google Maps", 3, "غذا خوب بود ولی نیم ساعت در صف خیابان استقلال معطل شدیم.", "مهدی")
triggered_queue_ids = [s["id"] for s in sim_queue["triggered_skills"]]
ok("SKILL-023" in triggered_queue_ids, "peak-hour queue skill triggered")
ok("SKILL-081" in triggered_queue_ids, "yield management dead-hour skill triggered")
ok("/reserve" in sim_queue["generated_ai_reply"], "reply guides user to online reservation")

print("\n".join(checks))
print("\n===== %d checks, %d failures =====" % (len(checks), len(fails)))
if fails:
    print("FAILED:", fails)
    sys.exit(1)
