#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست‌های آفلاین مهارت‌های ربات شمسه (تقویم شمسی، ثبت‌نام، یادآور، پیام گروهی).

اجرا:  python3 tests/test_skills.py
"""
import datetime as dt
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import bot_skills as sk  # noqa: E402

checks, fails = [], []


def ok(cond, label, extra=""):
    checks.append(("PASS " if cond else "FAIL ") + label + ((" | " + str(extra)) if extra else ""))
    if not cond:
        fails.append(label)


# ---------------------------------------------------------------- 1) تاریخ شمسی
pairs = [((2026, 3, 21), (1405, 1, 1)), ((2026, 10, 15), (1405, 7, 23)), ((2024, 2, 20), (1402, 12, 1))]
for g, j in pairs:
    got = sk.gregorian_to_jalali(*g)
    ok(got == j, "jalali %s -> %s" % (g, j), got)
ok(sk.fa_date(dt.date(2026, 10, 15)) == "۲۳ مهر ۱۴۰۵", "fa_date persian digits", sk.fa_date(dt.date(2026, 10, 15)))
ok(sk.WEEKDAYS[dt.date(2026, 10, 15).weekday()] == "پنجشنبه", "weekday mapping")

# ---------------------------------------------------------------- 2) رویدادهای پیش‌رو
today = dt.date(2026, 10, 15)          # پنجشنبه
up = sk.upcoming(limit=4, today=today, weeks=1)
ok(len(up) == 4, "upcoming returns events", len(up))
ok(all(day >= today for day, _e, _k in up), "all occurrences are in the future")
ok(up == sorted(up, key=lambda x: (x[0], x[1].get("time", ""))), "occurrences sorted by date")
first_day, first_ev, first_key = up[0]
ok(first_day == today and "موسیقی" in first_ev["title"],
   "today's Thursday music night is still upcoming", (first_day, first_ev["title"]))
ok(first_key == "music-poetry@2026-10-15", "occurrence key format", first_key)
ok(sk.WEEKDAYS[first_day.weekday()] == "پنجشنبه", "Thursday maps to پنجشنبه")
ok(up[1][2] == "cooking-class@2026-10-17", "next is Saturday cooking class", up[1][2])
# رویدادهای یکشنبه (بازی) و دوشنبه (متخصصان) هم در فهرست باشند
ids = [ev["id"] for _d, ev, _k in sk.upcoming(limit=20, today=today, weeks=1)]
ok("game-night" in ids and "pro-night" in ids and "music-poetry" in ids,
   "weekly ids present in upcoming", ids)
found = sk.find_occurrence(first_key, today=today)
ok(found and found[2] == first_key, "find_occurrence round-trips")
ok(sk.find_occurrence("nope@2020-01-01", today=today) is None, "unknown occurrence -> None")

# weekly rollover: today is the event day -> next week
roll = [x for x in sk.upcoming(limit=20, today=dt.date(2026, 10, 17), weeks=1) if x[1]["id"] == "game-night"]
ok(roll and all(x[0] > dt.date(2026, 10, 17) for x in roll), "same-day event rolls to next week")

# special one-off event included
ok(any(ev["id"] == "chef-table" for _d, ev, _k in sk.upcoming(limit=30, today=today, weeks=3)),
   "special event appears in upcoming")

# ---------------------------------------------------------------- 3) ثبت‌نام (RSVP)
db = {"users": {}, "rsvps": {}, "counters": {}, "reminders": {}}
res = sk.toggle_rsvp(db, 111, first_key, True)
ok(res["joined"] and res["count"] == 1 and res["changed"], "first RSVP joins", res)
res2 = sk.toggle_rsvp(db, 111, first_key, True)
ok(res2["changed"] is False and res2["count"] == 1, "double tap does not double count", res2)
sk.toggle_rsvp(db, 222, first_key, True)
ok(sk.count_rsvp(db, first_key) == 2, "second user counted", sk.count_rsvp(db, first_key))
ok(sk.user_rsvps(db, 111) == [first_key] and sk.user_rsvps(db, 999) == [], "user_rsvps correct")
res3 = sk.toggle_rsvp(db, 111, first_key, False)
ok(not res3["joined"] and res3["count"] == 1 and res3["changed"], "cancel removes user", res3)
ok(sk.touch_user(db, 111)["events"] == 0, "cancel decrements the user's event counter",
   sk.touch_user(db, 111)["events"])
empty = sk.toggle_rsvp(db, 222, first_key, False)
ok(first_key not in db["rsvps"], "empty event entry is cleaned up", empty)

# ---------------------------------------------------------------- 4) یادآور
db = {"users": {}, "rsvps": {}, "counters": {}, "reminders": {}}
ev = dict(sk.load_events()["weekly"][0])             # game-night (Saturday)
ev2 = {k: v for k, v in ev.items() if k != "day"}
ev2["id"] = "special-x"
ev2["title"] = "رویداد ویژه تستی"
db["rsvps"]["special-x@2026-10-16"] = {"111": "now", "222": "now"}   # فردا = جمعه ۱۶ اکتبر
_db_events = sk.load_events
try:
    sk.load_events = lambda: {"weekly": [_db_events()["weekly"][0]],
                              "special": [{"id": "special-x", "date": "2026-10-16",
                                           "title": "رویداد ویژه تستی", "time": "19:00",
                                           "place": "تست", "price": "رایگان", "capacity": 10}]}
    due = sk.reminders_due(db, now=dt.datetime(2026, 10, 15, 9, 0))
    ok(len(due) == 1 and sorted(due[0]["users"]) == ["111", "222"], "reminder due for tomorrow", due)
    db["reminders"][due[0]["id"]] = "2026-10-15"
    ok(sk.reminders_due(db, now=dt.datetime(2026, 10, 15, 9, 0)) == [],
       "reminder is not sent twice")
    ok("special-x" in str(db["rsvps"]), "rsvp data intact after reminder pass")
finally:
    sk.load_events = _db_events

# ---------------------------------------------------------------- 5) پیام گروهی (broadcast)
db = {"users": {"1": {"opt_in": True}, "2": {"opt_in": False}, "3": {"opt_in": True}},
      "rsvps": {}, "counters": {}, "reminders": {}}
sent_to = []
res = sk.broadcast(db, lambda uid, text: sent_to.append(uid) or True, "سلام", dry_run=False)
ok(res["sent"] == 2 and res["skipped"] == 1, "broadcast respects opt-in", res)
ok(sorted(sent_to) == ["1", "3"], "only opted-in users received", sent_to)
res = sk.broadcast({"users": {"1": {}, "2": {}}, "rsvps": {}, "counters": {}, "reminders": {}},
                   lambda uid, text: True, "x", dry_run=True)
ok(res["sent"] == 2, "dry-run counts without sending", res)
res = sk.broadcast({"users": {str(i): {} for i in range(300)}, "rsvps": {}, "counters": {}, "reminders": {}},
                   lambda uid, text: True, "x", dry_run=True, limit=5)
ok(res["sent"] == 5, "broadcast honours the per-run limit", res)
ok(sk.broadcast({"users": {"1": {}}, "rsvps": {}, "counters": {}, "reminders": {}},
                lambda uid, text: (_ for _ in ()).throw(RuntimeError("net")), "x")["failed"] == 1,
   "send failures are counted, not raised")

# ---------------------------------------------------------------- 6) آمار
db = {"users": {"1": {"opt_in": True}, "2": {"opt_in": False}}, "rsvps": {first_key: {"1": "x"}},
      "counters": {"messages": 9, "ai_answers": 2}, "reminders": {}}
st = sk.stats(db)
ok(st["users"] == 2 and st["opted_in"] == 1 and st["rsvps"] == 1, "stats counts", st)
ok(st["top_counters"][0] == ("messages", 9), "top counters sorted", st["top_counters"])
sk.bump(db, "messages")
ok(db["counters"]["messages"] == 10, "bump increments")

# ---------------------------------------------------------------- 7) ذخیره/بازخوانی دیتابیس
import tempfile  # noqa: E402
tmp = tempfile.mkdtemp()
sk.DB_FILE = os.path.join(tmp, "bot_db.json")
db = sk.load_db()
sk.toggle_rsvp(db, 777, first_key, True)
sk.save_db(db)
again = sk.load_db()
ok(sk.count_rsvp(again, first_key) == 1, "db round-trip keeps rsvps")
ok("777" in again["users"], "db round-trip keeps users")
ok(all(k in again for k in ("users", "rsvps", "counters", "reminders")), "db has all sections")

print("\n".join(checks))
print("\n===== %d checks, %d failures =====" % (len(checks), len(fails)))
if fails:
    print("FAILED:", fails)
    sys.exit(1)
