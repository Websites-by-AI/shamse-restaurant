#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست‌های آفلاین دیتابیس و کتابخانهٔ رستوران‌های ایرانی و افغانستانی در استانبول.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import restaurants_lib as rl  # noqa: E402

checks, fails = [], []


def ok(cond, label, extra=""):
    checks.append(("PASS " if cond else "FAIL ") + label + ((" | " + str(extra)) if extra else ""))
    if not cond:
        fails.append(label)


all_r = rl.load_restaurants()
ok(len(all_r) >= 15, "at least 15 restaurants loaded", len(all_r))

# ---------------------------------------------------------------- 1) صحت فیلدها و لینک‌ها
for r in all_r:
    rid = r.get("id")
    ok(bool(rid), "has id", rid)
    ok(bool(r.get("name_fa")), "has name_fa", rid)
    ok(bool(r.get("name_en")), "has name_en", rid)
    ok(r.get("category") in ("iranian", "afghan"), "category valid", (rid, r.get("category")))
    ok(bool(r.get("neighborhood_fa")), "has neighborhood_fa", rid)
    ok(bool(r.get("address_fa")), "has address_fa", rid)
    ok(bool(r.get("address_tr")), "has address_tr", rid)
    ok(bool(r.get("phone")), "has phone", rid)
    ok("maps.google.com" in r.get("maps_url", "") or "yandex" in r.get("maps_url", ""), "maps url valid", (rid, r.get("maps_url")))
    ok(len(r.get("specialties", [])) >= 2, "specialties listed", (rid, len(r.get("specialties", []))))

# ---------------------------------------------------------------- 2) تفکیک ایرانی و افغانستانی
ir = rl.filter_restaurants(category="iranian")
af = rl.filter_restaurants(category="afghan")
ok(len(ir) >= 10, "at least 10 Iranian/Farsi restaurants", len(ir))
ok(len(af) >= 5, "at least 5 Afghan restaurants", len(af))
ok(len(ir) + len(af) == len(all_r), "all restaurants categorized")

# ---------------------------------------------------------------- 3) فیلتر بر اساس محله
taksim = rl.filter_restaurants(area_id="taksim")
ok(len(taksim) >= 4, "taksim restaurants count", len(taksim))
zeytin = rl.filter_restaurants(area_id="zeytinburnu")
ok(len(zeytin) >= 3, "zeytinburnu restaurants count", len(zeytin))
esenyurt = rl.filter_restaurants(area_id="esenyurt")
ok(len(esenyurt) >= 2, "esenyurt restaurants count", len(esenyurt))
sisli = rl.filter_restaurants(area_id="sisli")
ok(len(sisli) >= 1, "sisli restaurants count", len(sisli))
fatih = rl.filter_restaurants(area_id="fatih")
ok(len(fatih) >= 2, "fatih restaurants count", len(fatih))
asian = rl.filter_restaurants(area_id="asian")
ok(len(asian) >= 2, "asian side restaurants count", len(asian))

# ---------------------------------------------------------------- 4) جستجو بر اساس کلمات کلیدی
mantu_matches = rl.filter_restaurants(query="منتو")
ok(len(mantu_matches) >= 2 and all(m["category"] == "afghan" for m in mantu_matches),
   "mantu search finds Afghan restaurants", len(mantu_matches))
qaboli_matches = rl.filter_restaurants(query="قابلی پلو")
ok(len(qaboli_matches) >= 3, "qaboli search matches", len(qaboli_matches))
farsi_matches = rl.filter_restaurants(query="فارسی")
ok(any(m["id"] == "farsi-taksim" for m in farsi_matches), "farsi search finds Farsi restaurant")
koobideh = rl.filter_restaurants(query="کوبیده")
ok(len(koobideh) >= 3, "koobideh search matches", len(koobideh))

# ---------------------------------------------------------------- 5) قالب‌بندی و دکمه‌ها
card = rl.format_card(all_r[0])
ok("آدرس:" in card and "تلفن:" in card and "گوگل مپ" in card, "card contains key sections")
compact = rl.format_list_compact(ir[:3], title="رستوران‌های منتخب")
ok("رستوران‌های منتخب" in compact and "1." in compact and "2." in compact, "compact list formatted")
kb = rl.area_keyboard()
ok(len(kb["inline_keyboard"]) >= 4, "area keyboard has rows", len(kb["inline_keyboard"]))
btns = rl.inline_buttons_for_restaurant(all_r[0])
ok(len(btns["inline_keyboard"]) >= 1, "restaurant buttons valid")

print("\n".join(checks))
print("\n===== %d checks, %d failures =====" % (len(checks), len(fails)))
if fails:
    print("FAILED:", fails)
    sys.exit(1)
