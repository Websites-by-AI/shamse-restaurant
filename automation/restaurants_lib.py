#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
کتابخانهٔ راهنمای رستوران‌های ایرانی، فارسی و افغانستانی در استانبول.
"""
import json
import os
import re

DATA_PATH = os.path.join(os.path.dirname(os.path.abspath(__file__)), "restaurants.json")

_CACHE = None

AREAS = [
    ("taksim", "تکسیم و بی‌اوغلو", "Taksim / Beyoğlu"),
    ("zeytinburnu", "زیتین‌بورنو", "Zeytinburnu"),
    ("esenyurt", "اسنیورت", "Esenyurt"),
    ("beylikduzu", "بیلیک‌دوزو", "Beylikdüzü"),
    ("sisli", "شیشلی", "Şişli"),
    ("fatih", "فاتیح و آکسارای", "Fatih / Aksaray"),
    ("asian", "بخش آسیایی (آتاشهیر/مال‌تپه)", "Asian Side"),
]


def load_restaurants():
    """بارگذاری لیست رستوران‌ها از JSON."""
    global _CACHE
    if _CACHE is None:
        if os.path.exists(DATA_PATH):
            with open(DATA_PATH, "r", encoding="utf-8") as f:
                _CACHE = json.load(f)
        else:
            _CACHE = []
    return _CACHE


def filter_restaurants(category=None, area_id=None, query=None):
    """فیلتر بر اساس دسته‌بندی (iranian/afghan)، محله یا جستجوی متنی."""
    items = load_restaurants()
    if category:
        items = [r for r in items if r.get("category") == category]
    if area_id:
        items = [r for r in items if r.get("area_id") == area_id]
    if query:
        q = re.sub(r"\s+", " ", query.replace("\u200c", " ").strip().lower())
        tokens = [t for t in q.split() if len(t) > 1]

        def match(r):
            blob = " ".join([
                r.get("name_fa", ""),
                r.get("name_en", ""),
                r.get("neighborhood_fa", ""),
                r.get("neighborhood_en", ""),
                r.get("address_fa", ""),
                r.get("notes_fa", ""),
                " ".join(r.get("specialties", [])),
            ]).replace("\u200c", " ").lower()
            return any(t in blob for t in tokens)

        items = [r for r in items if match(r)]
    return items


def format_card(r):
    """قالب‌بندی کارت کامل یک رستوران برای پیام تلگرام."""
    badge = "🍽 ایرانی و فارسی" if r.get("category") == "iranian" else "🇦🇫 افغانستانی"
    specs = " · ".join(r.get("specialties", []))
    lines = [
        "🔹 <b>%s</b> (%s)" % (r.get("name_fa", ""), r.get("name_en", "")),
        "🏷 دسته: %s | 📍 %s" % (badge, r.get("neighborhood_fa", "")),
        "🏠 <b>آدرس:</b> %s" % r.get("address_fa", ""),
        "🇹🇷 <i>%s</i>" % r.get("address_tr", ""),
        "☎️ <b>تلفن:</b> %s" % r.get("phone", "—"),
    ]
    if r.get("website"):
        lines.append("🌐 <b>وب‌سایت / منو:</b> %s" % r.get("website"))
    if r.get("maps_url"):
        lines.append("🗺 <b>مسیریابی گوگل مپ:</b> %s" % r.get("maps_url"))
    if specs:
        lines.append("🍲 <b>غذاهای شاخص:</b> %s" % specs)
    if r.get("notes_fa"):
        lines.append("ℹ️ %s" % r.get("notes_fa"))
    return "\n".join(lines)


def format_list_compact(restaurants, title=None, limit=10):
    """فهرست خلاصهٔ رستوران‌ها با لینک‌ها و مشخصات کلیدی."""
    count = len(restaurants)
    if not count:
        return "هیچ رستورانی با این مشخصات یافت نشد."
    lines = []
    if title:
        lines.append("📌 <b>%s</b> (%d رستوران)\n" % (title, count))
    for i, r in enumerate(restaurants[:limit], 1):
        icon = "🍽" if r.get("category") == "iranian" else "🇦🇫"
        name = r.get("name_fa", "")
        area = r.get("neighborhood_fa", "")
        phone = r.get("phone", "")
        web = r.get("website", "")
        maps = r.get("maps_url", "")
        lines.append("%d. %s <b>%s</b> — %s" % (i, icon, name, area))
        lines.append("   📍 %s" % r.get("address_fa", ""))
        contact_parts = []
        if phone:
            contact_parts.append("☎️ " + phone)
        if web:
            contact_parts.append("🌐 <a href='%s'>سایت/منو</a>" % web)
        if maps:
            contact_parts.append("🗺 <a href='%s'>نقشه</a>" % maps)
        if contact_parts:
            lines.append("   " + " | ".join(contact_parts))
        lines.append("")
    if count > limit:
        lines.append("<i>... و %d رستوران دیگر</i>" % (count - limit))
    return "\n".join(lines).strip()


def inline_buttons_for_restaurant(r):
    """دکمه‌های شیشه‌ای برای یک رستوران (وب‌سایت + گوگل مپ)."""
    row = []
    if r.get("website"):
        row.append({"text": "🌐 وب‌سایت / منو", "url": r.get("website")})
    if r.get("maps_url"):
        row.append({"text": "🗺 مسیریابی روی نقشه", "url": r.get("maps_url")})
    rows = [row] if row else []
    return {"inline_keyboard": rows}


def area_keyboard():
    """کیبورد شیشه‌ای انتخاب محله."""
    buttons = []
    row = []
    for aid, name_fa, _ in AREAS:
        row.append({"text": name_fa, "callback_data": "area:" + aid})
        if len(row) == 2:
            buttons.append(row)
            row = []
    if row:
        buttons.append(row)
    buttons.append([{"text": "🍽 همه ایرانی‌ها", "callback_data": "cat:iranian"},
                    {"text": "🇦🇫 همه افغانستانی‌ها", "callback_data": "cat:afghan"}])
    return {"inline_keyboard": buttons}
