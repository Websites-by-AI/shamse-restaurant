#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست‌های آفلاین ربات تلگرام شمسه (بدون شبکه و بدون توکن).

اجرا:  python3 tests/test_bot.py
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import content        # noqa: E402
import telegram_bot as tb  # noqa: E402

checks, fails = [], []


def ok(cond, label, extra=""):
    checks.append(("PASS " if cond else "FAIL ") + label + ((" | " + str(extra)) if extra else ""))
    if not cond:
        fails.append(label)


# ---------------------------------------------------------------- 1) keyboard & quick replies
rows = content.KEYBOARD["keyboard"]
ok(len(rows) >= 2 and all(len(r) >= 1 for r in rows), "keyboard has rows", len(rows))
ok(content.KEYBOARD["resize_keyboard"] is True, "keyboard resizes")
ok(content.KEYBOARD["is_persistent"] is True, "keyboard is persistent")
labels = [b["text"] for row in rows for b in row]
ok(all(l in content.QUICK for l in labels), "every keyboard label maps to a command", labels)
SKILLS = {"news", "rsvp", "my", "stop"}
ok(all(v in content.REPLIES or v in SKILLS for v in content.QUICK.values()),
   "every quick command is handled (REPLIES or skills)", list(content.QUICK.values()))

# ---------------------------------------------------------------- 2) normalisation / matching
ok(tb._norm("ساعت‌کاری  شما") == "ساعت کاری شما", "ZWNJ + double spaces normalised", tb._norm("ساعت‌کاری  شما"))
ok(tb._norm("چي") == "چی", "arabic yeh normalised")
ok(tb.kb_answer("ساعت کاریتون چنده؟") and "۱۲:۰۰" in tb.kb_answer("ساعت کاریتون چنده؟"), "hours question answered")
ok(tb.kb_answer("پارکینگ دارید؟") is not None, "parking answered")
ok(tb.kb_answer("آدرس کجاست؟") is not None, "address answered")
ok(tb.kb_answer("halal?") is not None, "english halal answered")
ok(tb.kb_answer("گیاهی چی دارید؟") is not None, "vegetarian answered")
ok(tb.kb_answer("برای میتاپ باید چیکار کنم؟") is not None, "meetup answered")
ok(tb.kb_answer("سؤال کاملاً نامربوط qwerty") is None, "unrelated text goes to AI", )
ok(all("**" not in ans for _kw, ans in content.KB), "no markdown leftovers in KB answers")

# ---------------------------------------------------------------- 3) group etiquette
ok(tb.should_reply("سلام", "private") is True, "private: always reply")
ok(tb.should_reply("/menu", "group") is True, "group: commands answered")
ok(tb.should_reply("سلام @shamse_restaurant_bot ساعت چند؟", "supergroup") is True, "group: mentions answered")
ok(tb.should_reply("سلام بچه‌ها", "supergroup") is False, "group: chatter ignored")
ok(tb.clean_text("سلام @shamse_restaurant_bot ساعت چند؟") == "سلام ساعت چند؟", "mention stripped", tb.clean_text("سلام @shamse_restaurant_bot ساعت چند؟"))
ok(tb.clean_text("shamse_restaurant_bot hello") == "hello", "mention without @ stripped")

# ---------------------------------------------------------------- 4) AI answer guard (offline)
real_candidates = tb._ai_candidates
real_request = tb._ai_request
try:
    tb._ai_candidates = lambda: []
    ok(tb.ai_answer("سلام") is None, "no engines -> None (fallback used)")

    tb._ai_candidates = lambda: [("fake", "http://x", "m", "k")]

    def boom(*a, **k):
        raise RuntimeError("network down")

    tb._ai_request = boom
    ok(tb.ai_answer("سلام") is None, "engine failure -> None")

    tb._ai_request = lambda *a, **k: "کوتاه"
    ok(tb.ai_answer("سلام") is None, "too-short answer rejected")

    tb._ai_request = lambda *a, **k: "english only answer here"
    ok(tb.ai_answer("سلام") is None, "non-persian answer rejected")

    good = "🕐 هر دو شعبه همه‌روزه از ۱۲:۰۰ تا ۰۱:۳۰ باز است؛ خوش آمدید!"
    tb._ai_request = lambda *a, **k: good * 20
    ans = tb.ai_answer("ساعت کاری؟")
    ok(ans == (good * 20)[:700], "valid answer accepted and capped at 700", len(ans or ""))
finally:
    tb._ai_candidates = real_candidates
    tb._ai_request = real_request

# ---------------------------------------------------------------- 5) misc UX
ok("ساعت کاریتون" in content.FALLBACK and "/menu" in content.FALLBACK, "fallback guides the user")
ok("@shamse_restaurant" in content.REPLIES["start"] and content.SITE_LABEL in content.REPLIES["start"],
   "welcome shows site + channel")
ok("halal" in content.AI_FACTS.lower() or "حلال" in content.AI_FACTS, "AI facts cover halal")
ok(content.PHONE in content.AI_FACTS and "۶۰" in content.AI_FACTS, "AI facts include phone + capacity")
ok(all(k in content.REPLIES for k in ("start", "menu", "events", "reserve", "branches", "contact", "help")),
   "all documented commands exist")
ok(content.CHANNEL_BUTTONS["inline_keyboard"] and all(
    "url" in b for row in content.CHANNEL_BUTTONS["inline_keyboard"] for b in row), "channel buttons valid")

# ---------------------------------------------------------------- 6) CLI contract
import inspect  # noqa: E402
src = inspect.getsource(tb.main)
ok("--loop" in src, "poll supports --loop for instant replies")
ok("mode_poll(args.loop)" in src, "poll passes loop minutes through")
ok("send_welcome" in inspect.getsource(tb.handle_updates), "welcome uses the photo + keyboard path")

print("\n".join(checks))
print("\n===== %d checks, %d failures =====" % (len(checks), len(fails)))
if fails:
    print("FAILED:", fails)
    sys.exit(1)
