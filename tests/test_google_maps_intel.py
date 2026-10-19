#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
آزمون‌های خودکار ماژول هوش گوگل مپ و ژنراتور همکاری B2B.
Tests for Google Maps Intelligence and B2B Outreach module.
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

import google_maps_intel as gmi

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

# 1. Dataset checks
data = gmi.load_gmaps_intel()
check(len(data) == 19, "exactly 19 restaurants in Google Maps intel dataset", len(data))

# 2. Key validations per restaurant
for r in data:
    rid = r.get("id")
    check(bool(rid), f"{rid} has valid id")
    check(bool(r.get("name_fa")), f"{rid} has name_fa")
    check(bool(r.get("google_place_id")), f"{rid} has google_place_id")
    check(r.get("google_place_id", "").startswith("ChIJ"), f"{rid} place_id starts with ChIJ")
    check(bool(r.get("google_cid")), f"{rid} has google_cid")
    
    rating = r.get("google_rating", 0)
    check(4.0 <= rating <= 5.0, f"{rid} rating in valid range 4.0-5.0", rating)
    
    rev_count = r.get("google_review_count", 0)
    check(rev_count >= 500, f"{rid} review count >= 500", rev_count)
    
    coords = r.get("coordinates", {})
    lat = coords.get("lat", 0)
    lng = coords.get("lng", 0)
    check(40.8 <= lat <= 41.3, f"{rid} latitude in Istanbul bounds", lat)
    check(28.5 <= lng <= 29.3, f"{rid} longitude in Istanbul bounds", lng)
    
    pos = r.get("positive_themes", [])
    check(len(pos) >= 2, f"{rid} has at least 2 positive review themes", len(pos))
    
    pains = r.get("review_pain_points", [])
    check(len(pains) >= 2, f"{rid} has at least 2 review pain points", len(pains))
    
    msg = r.get("outreach_message_fa", "")
    check(len(msg) > 150, f"{rid} has detailed outreach proposal", len(msg))
    check("میزبان استانبول" in msg, f"{rid} proposal cites Mizban Istanbul brand")

# 3. GitHub Scrapers Benchmark checks
scrapers = gmi.get_github_scrapers()
check(len(scrapers) >= 5, "at least 5 top GitHub scrapers benchmarked", len(scrapers))
for sc in scrapers:
    check(bool(sc.get("repo")), f"scraper repo exists | {sc.get('repo')}")
    check(sc.get("stars_num", 0) >= 100, f"scraper has >= 100 stars | {sc.get('stars')}")
    check(bool(sc.get("url")), f"scraper has valid url | {sc.get('url')}")
    check(len(sc.get("extracted_fields", [])) >= 3, f"scraper lists extracted fields | {sc.get('repo')}")

# 4. Outreach Generator checks
pkg = gmi.generate_b2b_outreach("farsi-taksim")
check(pkg is not None, "generate_b2b_outreach for farsi-taksim returned package")
check(pkg["google_rating"] == 4.6, "pkg has correct rating", pkg["google_rating"])
check("wa.me" in pkg["whatsapp_url"], "pkg has working WhatsApp link", pkg["whatsapp_url"][:40])
check("رستوران فارسی" in pkg["message_text"], "pkg message contains restaurant name")

print(f"\n===== {passed} checks, {failed} failures =====")
if failed > 0:
    sys.exit(1)
