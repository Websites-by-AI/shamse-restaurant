#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مهارت‌های ربات شمسه: تقویم رویدادها، ثبت‌نام (RSVP)، پروفایل کاربر، یادآور و پیام گروهی.

این ماژول بدون سرور کار می‌کند؛ همهٔ داده‌ها در `bot_db.json` کنار همین فایل ذخیره می‌شود.
"""
import datetime as dt
import json
import os
import re

HERE = os.path.dirname(os.path.abspath(__file__))
EVENTS_FILE = os.path.join(HERE, "events.json")
DB_FILE = os.path.join(HERE, "bot_db.json")

WEEKDAYS = ["دوشنبه", "سه‌شنبه", "چهارشنبه", "پنجشنبه", "جمعه", "شنبه", "یکشنبه"]
JMONTHS = ["فروردین", "اردیبهشت", "خرداد", "تیر", "مرداد", "شهریور",
           "مهر", "آبان", "آذر", "دی", "بهمن", "اسفند"]


# ---------------------------------------------------------------- تاریخ شمسی
def gregorian_to_jalali(gy, gm, gd):
    """تبدیل تاریخ میلادی به شمسی (الگوریتم استاندارد، بدون وابستگی خارجی)."""
    g_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    j_days = [31, 31, 31, 31, 31, 31, 30, 30, 30, 30, 30, 29]
    gy -= 1600
    gm -= 1
    gd -= 1
    g_day_no = 365 * gy + (gy + 3) // 4 - (gy + 99) // 100 + (gy + 399) // 400
    for i in range(gm):
        g_day_no += g_days[i]
    if gm > 1 and ((gy + 1600) % 4 == 0 and ((gy + 1600) % 100 != 0 or (gy + 1600) % 400 == 0)):
        g_day_no += 1
    g_day_no += gd
    j_day_no = g_day_no - 79
    j_np = j_day_no // 12053
    j_day_no %= 12053
    jy = 979 + 33 * j_np + 4 * (j_day_no // 1461)
    j_day_no %= 1461
    if j_day_no >= 366:
        jy += (j_day_no - 1) // 365
        j_day_no = (j_day_no - 1) % 365
    i = 0
    while i < 11 and j_day_no >= j_days[i]:
        j_day_no -= j_days[i]
        i += 1
    return jy, i + 1, j_day_no + 1


def fa_date(d):
    """«۲۳ مهر ۱۴۰۵» برای یک date/datetime."""
    jy, jm, jd = gregorian_to_jalali(d.year, d.month, d.day)
    trans = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
    return "%s %s %s" % (str(jd).translate(trans), JMONTHS[jm - 1], str(jy).translate(trans))


# ---------------------------------------------------------------- رویدادها
def load_events():
    try:
        with open(EVENTS_FILE, encoding="utf-8") as fh:
            data = json.load(fh)
    except (OSError, ValueError):
        return {"weekly": [], "special": []}
    data.setdefault("weekly", [])
    data.setdefault("special", [])
    return data


def next_occurrence(event, today, weekday=None, include_today=True):
    """نزدیک‌ترین تاریخ وقوع یک رویداد هفتگی."""
    delta = (weekday - today.weekday()) % 7
    if delta == 0 and not include_today:
        delta = 7
    return today + dt.timedelta(days=delta)


def upcoming(limit=6, today=None, weeks=1):
    """فهرست وقوع‌های پیش‌رو (هفتگی + ویژه) با کلید یکتا."""
    today = today or dt.date.today()
    out = []
    for ev in load_events()["weekly"]:
        for w in range(weeks):
            day = next_occurrence(ev, today + dt.timedelta(days=7 * w), ev["day"])
            if day < today:
                day += dt.timedelta(days=7)
            out.append((day, ev, "%s@%s" % (ev["id"], day.isoformat())))
    for ev in load_events()["special"]:
        try:
            day = dt.date.fromisoformat(ev["date"])
        except (KeyError, ValueError):
            continue
        if day >= today:
            out.append((day, ev, "%s@%s" % (ev["id"], day.isoformat())))
    out.sort(key=lambda x: (x[0], x[1].get("time", "")))
    # حذف تکرارها (یک رویداد در یک تاریخ فقط یک بار)
    seen, uniq = set(), []
    for item in out:
        if item[2] in seen:
            continue
        seen.add(item[2])
        uniq.append(item)
    return uniq[:limit]


def rsvp_key_parts(key):
    ev_id, _, day = (key or "").partition("@")
    return ev_id, day


def find_occurrence(key, today=None):
    for day, ev, k in upcoming(limit=40, today=today, weeks=3):
        if k == key:
            return day, ev, k
    return None


def label(ev, day, cap=None):
    line = "🗓 %s — %s %s" % (WEEKDAYS[day.weekday()], fa_date(day), ev.get("time", ""))
    return line


# ---------------------------------------------------------------- دیتابیس
def load_db():
    try:
        with open(DB_FILE, encoding="utf-8") as fh:
            db = json.load(fh)
    except (OSError, ValueError):
        db = {}
    db.setdefault("users", {})
    db.setdefault("rsvps", {})
    db.setdefault("counters", {})
    db.setdefault("reminders", {})
    return db


def save_db(db):
    tmp = DB_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(db, fh, ensure_ascii=False, indent=2, sort_keys=True)
        fh.write("\n")
    os.replace(tmp, DB_FILE)


def touch_user(db, chat_id, from_user=None, opt_in=None):
    """ثبت/به‌روزرسانی کاربر (اکثراً به‌صورت خودکار هنگام اولین پیام)."""
    uid = str(chat_id)
    user = db["users"].setdefault(uid, {
        "joined": dt.date.today().isoformat(), "opt_in": True, "events": 0, "name": ""})
    if from_user:
        name = " ".join(x for x in [from_user.get("first_name"), from_user.get("last_name")] if x)
        if name:
            user["name"] = name
        if from_user.get("username"):
            user["username"] = from_user["username"]
    if opt_in is not None:
        user["opt_in"] = bool(opt_in)
    return user


def toggle_rsvp(db, chat_id, key, join=True):
    """ثبت‌نام/لغو ثبت‌نام یک کاربر در یک رویداد (بدون دست‌زدن به ثبت‌نام دیگران)."""
    uid = str(chat_id)
    user = touch_user(db, chat_id)
    entries = db["rsvps"].get(key, {}) if not join else db["rsvps"].setdefault(key, {})
    was = uid in entries
    if join:
        entries[uid] = dt.datetime.utcnow().isoformat(timespec="seconds")
        if not was:
            user["events"] = int(user.get("events", 0)) + 1
    elif was:
        entries.pop(uid, None)
        user["events"] = max(0, int(user.get("events", 0)) - 1)
        if not entries:                      # فقط وقتی هیچ‌کس دیگری ثبت‌نام نکرده باشد
            db["rsvps"].pop(key, None)
    return {"joined": join and bool(db["rsvps"].get(key)), "count": len(db["rsvps"].get(key, {})),
            "changed": was != join}


def user_rsvps(db, chat_id):
    uid = str(chat_id)
    out = []
    for key, entries in db["rsvps"].items():
        if uid in entries:
            out.append(key)
    return sorted(out)


def count_rsvp(db, key):
    return len(db["rsvps"].get(key, {}))


def bump(db, name):
    c = db.setdefault("counters", {})
    c[name] = int(c.get(name, 0)) + 1


# ---------------------------------------------------------------- زمان‌بندی و ارسال
def should_finalize(event, weekday=None):
    """قاعدهٔ تأیید رویداد: چند روز قبل نهایی شود (برای نمایش ظرفیت)."""
    return True


def reminders_due(db, now=None, tomorrows=None):
    """کاربرانی که رویدادشان فردا است و باید یادآور بگیرند."""
    now = now or dt.datetime.utcnow()
    today = now.date()
    tomorrow = today + dt.timedelta(days=1)
    out = []
    for key, entries in db["rsvps"].items():
        found = find_occurrence(key, today=today)
        if not found:
            continue
        day, ev, k = found
        if day != tomorrow:
            continue
        rid = key + "@" + now.strftime("%Y-%m-%d")
        if db["reminders"].get(rid):
            continue
        users = [uid for uid in entries]
        if users:
            out.append({"id": rid, "users": users, "event": ev, "day": day})
    return out


def rsvp_summary(ev, day, count, capacity=None):
    trans = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
    cap = capacity or ev.get("capacity")
    cap_txt = (" از %s" % str(cap).translate(trans)) if cap else ""
    return ("🎫 <b>%s</b>\n%s · %s\n💺 ظرفیت: %s%s · 👥 ثبت‌نام‌شده: %s\n💰 %s"
            % (ev.get("title", ""), fa_date(day), ev.get("time", ""), day.weekday() and "" or "",
               cap_txt, str(count).translate(trans), ev.get("price", "")))


def events_list_text(db, today=None, limit=5):
    """متن فهرست رویدادهای پیش‌رو همراه با تعداد ثبت‌نام."""
    from content import SITE_LABEL, EVENTS_URL  # noqa: E402 — جلوگیری از چرخهٔ import
    lines = ["🎫 رویدادهای پیش‌رو (طبقهٔ دوم شعبهٔ استقلال)", ""]
    for day, ev, key in upcoming(limit=limit, today=today):
        lines.append("• <b>%s</b> — %s %s\n  💺 %s · 👥 %s نفر ثبت‌نام کرده"
                     % (ev.get("title", ""), WEEKDAYS[day.weekday()], fa_date(day), ev.get("time", ""),
                        str(count_rsvp(db, key)).translate(str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹"))))
    lines += ["", "برای ثبت‌نام دکمهٔ زیر را بزنید یا /rsvp را بفرستید.",
              "🌐 %s/events.html · 📣 @shamse_restaurant" % SITE_LABEL]
    return "\n".join(lines)


def rsvp_keyboard(db, today=None, limit=5):
    """دکمه‌های شیشه‌ای ثبت‌نام برای نزدیک‌ترین رویدادها."""
    uid_rows = []
    for day, ev, key in upcoming(limit=limit, today=today):
        mark = "✅ " if False else ""
        uid_rows.append([{"text": "%s%s — %s" % (mark, ev.get("title", "")[:32], fa_date(day)),
                          "callback_data": "rsvp:" + key}])
    uid_rows.append([{"text": "📋 ثبت‌نام‌های من", "callback_data": "my"}])
    return {"inline_keyboard": uid_rows}


def broadcast(db, send, text, dry_run=False, limit=200):
    """ارسال پیام به همهٔ کاربرانی که اعلام‌کرده‌اند (opt-in). send(chat_id, text) → bool"""
    sent, failed, skipped = 0, 0, 0
    for uid, user in sorted(db["users"].items()):
        if not user.get("opt_in", True):
            skipped += 1
            continue
        if sent >= limit:
            break
        if dry_run:
            sent += 1
            continue
        try:
            if send(uid, text):
                sent += 1
            else:
                failed += 1
        except Exception:  # noqa: BLE001
            failed += 1
    return {"sent": sent, "failed": failed, "skipped": skipped}


def stats(db):
    users = db.get("users", {})
    opted = [u for u in users.values() if u.get("opt_in", True)]
    return {
        "users": len(users),
        "opted_in": len(opted),
        "rsvps": sum(len(v) for v in db.get("rsvps", {}).values()),
        "top_counters": sorted((db.get("counters") or {}).items(), key=lambda x: -x[1])[:6],
    }
