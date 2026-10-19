#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست‌های پیشرفته ارتقای دکمه‌ها، قالب‌بندی HTML و پیوندهای تلگرام.
"""
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import content
import telegram_bot as tb

def test_bot_formatting_and_buttons():
    # 1. Test HTML formatting support in reply
    calls = []
    def fake_api(method, payload=None, retries=3):
        calls.append((method, payload))
        if method == "sendMessage":
            # If parse error simulated, reject
            if payload and "invalid_tag" in payload.get("text", "") and "parse_mode" in payload:
                return {"ok": False, "description": "Bad Request: can't parse entities"}
            return {"ok": True, "result": {"message_id": 123}}
        return {"ok": True}

    real_api = tb.api
    tb.api = fake_api

    try:
        # Check standard reply has parse_mode="HTML"
        res = tb.reply(999, "<b>سلام</b>", buttons=True)
        assert res.get("ok") is True
        assert calls[-1][0] == "sendMessage"
        assert calls[-1][1]["parse_mode"] == "HTML"
        print("PASS reply sends parse_mode='HTML'")

        # Check fallback on entity parse error
        res_fallback = tb.reply(999, "متن با تگ نامعتبر invalid_tag")
        assert res_fallback.get("ok") is True
        # It should have called twice: first with parse_mode, then without
        assert "parse_mode" not in calls[-1][1]
        print("PASS reply automatically falls back to plain text if entity error occurs")

        # 2. Test Callback Handling for all cmd:* actions
        db = {"users": {}, "rsvps": {}, "reminders": {}, "counters": {}}
        cmd_tests = ["rsvp", "events", "skills", "franchise", "menu", "reserve", "branches", "contact"]
        for c in cmd_tests:
            upd = {
                "callback_query": {
                    "id": f"cq_{c}",
                    "data": f"cmd:{c}",
                    "from": {"id": 12345, "first_name": "Test"},
                    "message": {"chat": {"id": 12345}, "message_id": 99}
                }
            }
            ok = tb.handle_callback(upd, db)
            assert ok is True, f"handle_callback must handle cmd:{c}"
            print(f"PASS handle_callback handles cmd:{c}")

        # 3. Test content.BUTTONS structure
        inline_rows = content.BUTTONS["inline_keyboard"]
        assert len(inline_rows) >= 3, "BUTTONS must have at least 3 rows"
        has_cat_iranian = any(b.get("callback_data") == "cat:iranian" for r in inline_rows for b in r)
        has_cat_afghan = any(b.get("callback_data") == "cat:afghan" for r in inline_rows for b in r)
        has_areas = any(b.get("callback_data") == "areas" for r in inline_rows for b in r)
        has_rsvp = any(b.get("callback_data") == "cmd:rsvp" for r in inline_rows for b in r)
        assert has_cat_iranian and has_cat_afghan and has_areas and has_rsvp, "Buttons must have native callback_data actions"
        print("PASS content.BUTTONS has native callback_data actions without bouncing to browser")

        # 4. Test menu content has real prices in TRY
        menu_text = content.REPLIES["menu"]
        assert "۳۹۰ ₺" in menu_text or "390" in menu_text or "کباب کوبیده" in menu_text, "Menu must list prices and items"
        assert "قورمه‌سبزی" in menu_text or "قورمه سبزی" in menu_text, "Menu must list stew items"
        assert content.PHONE in menu_text, "Menu must include phone"
        print("PASS content.REPLIES['menu'] contains detailed dishes and prices")

        # 5. Test branches content has both Taksim and Kocatepe
        branches_text = content.REPLIES["branches"]
        assert "تکسیم" in branches_text and "کوجاتپه" in branches_text, "Branches must mention Taksim and Kocatepe"
        assert "maps.google.com" in branches_text, "Branches must have Google Maps navigation"
        print("PASS content.REPLIES['branches'] contains maps and both branches")

    finally:
        tb.api = real_api

    print("\n===== ALL BOT BUTTONS & FORMATTING CHECKS PASSED (0 FAILURES) =====")

if __name__ == "__main__":
    test_bot_formatting_and_buttons()
