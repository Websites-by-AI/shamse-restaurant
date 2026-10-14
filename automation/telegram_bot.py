#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
اتوماسیون تلگرام رستوران شمسه  —  @shamse_restaurant_bot

حالت‌های اجرا:
    post      ساخت و ارسال پست به کانال (هوش مصنوعی + قالب جایگزین)
    poll      خواندن پیام‌های مستقیم و پاسخ به دستورها (/menu /events /reserve ...)
    selftest  بررسی سلامت توکن، دسترسی کانال و وضعیت هوش مصنوعی
    discover  پیدا کردن شناسهٔ کانال از آپدیت‌ها (بعد از افزودن ربات به کانال)

نمونه:
    TELEGRAM_BOT_TOKEN=... python3 automation/telegram_bot.py post --dry-run
    TELEGRAM_BOT_TOKEN=... python3 automation/telegram_bot.py selftest

متغیرهای محیطی:
    TELEGRAM_BOT_TOKEN  (اجباری) توکن ربات — در گیت‌هاب به‌صورت Secret
    TELEGRAM_CHAT_ID    شناسه یا @نام‌کاربری کانال (اختیاری؛ در نبودش خودکار کشف می‌شود)
    AI_PROVIDER         github | openai | none  (پیش‌فرض: github اگر GITHUB_TOKEN باشد)
    AI_API_KEY          کلید سرویس هوش مصنوعی (اختیاری — مثل OpenRouter/OpenAI)
    AI_BASE_URL         آدرس سازگار با OpenAI (اختیاری)
    AI_MODEL            نام مدل (پیش‌فرض: openai/gpt-4o-mini)
    SITE_BASE           آدرس سایت (پیش‌فرض: GitHub Pages)
"""

import argparse
import datetime as dt
import json
import os
import re
import sys
import time
import urllib.error
import urllib.request

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import content  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
STATE_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "state.json")

TOKEN = (os.environ.get("TELEGRAM_BOT_TOKEN") or "").strip()
CHAT = (os.environ.get("TELEGRAM_CHAT_ID") or os.environ.get("TELEGRAM_CHANNEL") or "").strip()
SITE = (os.environ.get("SITE_BASE") or content.SITE).rstrip("/")
API = "https://api.telegram.org/bot%s/%s"

FA_DIGITS = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
NEED_SETUP = "🟡 ACTION NEEDED"


# ---------------------------------------------------------------- utilities
def api(method, payload=None, retries=3):
    """فراخوانی Bot API با مدیریت 429 و خطاهای شبکه."""
    if not TOKEN:
        return {"ok": False, "description": "TELEGRAM_BOT_TOKEN is not set"}
    url = API % (TOKEN, method)
    data = json.dumps(payload).encode("utf-8") if payload is not None else None
    last = {"ok": False, "description": "request failed"}
    for attempt in range(retries):
        req = urllib.request.Request(url, data=data, headers={"Content-Type": "application/json"})
        try:
            with urllib.request.urlopen(req, timeout=45) as resp:
                return json.loads(resp.read().decode("utf-8"))
        except urllib.error.HTTPError as exc:
            body = exc.read().decode("utf-8", "replace")
            try:
                parsed = json.loads(body)
            except ValueError:
                parsed = {"ok": False, "description": body[:200], "error_code": exc.code}
            if parsed.get("error_code") == 429:
                wait = int((parsed.get("parameters") or {}).get("retry_after", 5))
                print("[api] 429 — retry in %ss" % wait)
                time.sleep(wait + 1)
                last = parsed
                continue
            return parsed
        except Exception as exc:  # noqa: BLE001 — network flake: retry
            last = {"ok": False, "description": str(exc)}
            time.sleep(2)
    return last


def load_state():
    try:
        with open(STATE_FILE, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return {}


def save_state(state):
    tmp = STATE_FILE + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(state, fh, ensure_ascii=False, indent=2, sort_keys=True)
        fh.write("\n")
    os.replace(tmp, STATE_FILE)


def persian_numbers(text):
    return text.translate(FA_DIGITS)


# ---------------------------------------------------------------- AI writing (با جایگزین خودکار)
def ai_enabled():
    provider = (os.environ.get("AI_PROVIDER") or "").strip().lower()
    if provider in ("none", "off", "0"):
        return False
    if provider in ("github", "openai", "custom"):
        return True
    return bool(os.environ.get("AI_API_KEY") or os.environ.get("GITHUB_TOKEN"))


def call_ai(prompt, system):
    """تولید متن با سرویس سازگار OpenAI. در صورت شکست یا خروجی نامعتبر → None."""
    provider = (os.environ.get("AI_PROVIDER") or "").strip().lower()
    key = (os.environ.get("AI_API_KEY") or "").strip()
    if provider == "github" or (not provider and not key and os.environ.get("GITHUB_TOKEN")):
        base = os.environ.get("AI_BASE_URL") or "https://models.github.ai/inference"
        key = key or os.environ.get("GITHUB_TOKEN", "")
        model = os.environ.get("AI_MODEL") or "openai/gpt-4o-mini"
    else:
        base = os.environ.get("AI_BASE_URL") or "https://api.openai.com/v1"
        model = os.environ.get("AI_MODEL") or "openai/gpt-4o-mini"
    if not key:
        print("[ai] no key — template mode")
        return None

    body = json.dumps({
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
        "temperature": 0.8,
        "max_tokens": 600,
    }).encode("utf-8")
    req = urllib.request.Request(base.rstrip("/") + "/chat/completions", data=body, headers={
        "Authorization": "Bearer " + key,
        "Content-Type": "application/json",
        "Accept": "application/json",
        "X-GitHub-Api-Version": "2022-11-28",
    })
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            raw = resp.read().decode("utf-8")
            data = json.loads(raw)
            text = (data.get("choices") or [{}])[0].get("message", {}).get("content", "").strip()
    except urllib.error.HTTPError as exc:
        print("[ai] HTTP %s — %s" % (exc.code, exc.read().decode("utf-8", "replace")[:180]))
        return None
    except Exception as exc:  # noqa: BLE001
        print("[ai] unavailable (%s) — template fallback" % exc)
        return None

    # اعتبارسنجی خروجی: حداقل ۱۲۰ کاراکتر، اکثراً فارسی، بدون توکن‌های عجیب
    if len(text) < 120 or len(re.findall(r"[\u0600-\u06FF]", text)) < 80:
        print("[ai] response rejected (not usable Persian text): %r" % text[:60])
        return None
    return text


SYSTEM = (
    "تو مدیر شبکه‌های اجتماعی «رستوران شمسه» هستی؛ رستوران ایرانی در استانبول با دو شعبه: "
    "تکسیم (خیابان استقلال پلاک ۱۷۹، دو طبقه) و کوجاتپه (عبدالحکیم حمیت ۱۷)، تلفن +90 501 325 24 52، "
    "ساعات ۱۲:۰۰ تا ۰۱:۳۰، طبقهٔ دوم شعبهٔ استقلال ظرفیت ۶۰ نفر برای میتاپ. "
    "یک پست کوتاه فارسی برای کانال تلگرام بنویس: ۳ تا ۵ خط، ۲ تا ۴ ایموجی، پایان با ۱ تا ۲ هشتگ. "
    "فقط متن پست را بنویس؛ هیچ قیمت، تخفیف یا وعدهٔ جدیدی که به تو گفته نشده از خودت نساز."
)


def compose(force_topic=None):
    """متن پست + کلید عکس. اول هوش مصنوعی، بعد قالب آماده."""
    today = dt.date.today()
    topics = content.TOPICS
    if force_topic is not None:
        idx = force_topic % len(topics)
    elif today.weekday() == 3 and len(topics) > 14:      # پنجشنبه: یادآور رویدادها
        idx = 14 % len(topics)
    else:
        idx = today.toordinal() % min(14, len(topics))
    img, template = topics[idx]
    text = template.format(phone=persian_numbers(content.PHONE), menu=content.MENU_URL,
                           reserve=content.RESERVE_URL, events=content.EVENTS_URL)
    text = persian_numbers(text) if False else text
    text = text.rstrip() + "\n\n" + content.TAGS

    if ai_enabled():
        print("[ai] provider=%s model=%s" % (
            (os.environ.get("AI_PROVIDER") or ("github" if os.environ.get("GITHUB_TOKEN") else "openai")),
            os.environ.get("AI_MODEL") or "openai/gpt-4o-mini"))
        ai_text = call_ai(
            "موضوع امروز: «%s».\nمتن پایه (می‌توانی بازنویسی کنی ولی اطلاعاتش را تغییر نده):\n%s\n\n"
            "در پایان یک دعوت به اقدام (CTA) با یکی از این لینک‌ها بگذار: %s یا %s"
            % (template.strip().splitlines()[0][:80], text, content.MENU_URL, content.EVENTS_URL),
            SYSTEM,
        )
        if ai_text:
            if content.TAGS.split()[0] not in ai_text:
                ai_text = ai_text.rstrip() + "\n\n" + content.TAGS
            print("[ai] using AI-generated text")
            return img, ai_text
        print("[ai] falling back to curated template")
    return img, text


# ---------------------------------------------------------------- Telegram actions
def resolve_chat(state=None):
    """شناسهٔ کانال: متغیر محیطی → شناسهٔ کشف‌شدهٔ ذخیره‌شده → کشف زنده از آپدیت‌ها."""
    if CHAT:
        return CHAT, "env"
    state = state if state is not None else load_state()
    if state.get("detected_chat_id"):
        return state["detected_chat_id"], "state"
    found = discover_channel()
    if found:
        state["detected_chat_id"] = found["id"]
        state["detected_chat_title"] = found.get("title")
        try:
            save_state(state)
        except OSError:
            pass
        return found["id"], "auto-discovered"
    return None, None


def discover_channel():
    """کانال‌هایی که ربات در آن‌ها عضو/ادمین شده را از آپدیت‌ها پیدا می‌کند."""
    resp = api("getUpdates", {"limit": 100, "allowed_updates": ["channel_post", "my_chat_member", "message"]})
    if not resp.get("ok"):
        return None
    for upd in reversed(resp.get("result") or []):
        for key in ("channel_post", "my_chat_member", "message"):
            chat = ((upd.get(key) or {}).get("chat") or {})
            if chat.get("type") == "channel":
                return {"id": chat.get("id"), "title": chat.get("title"),
                        "username": chat.get("username")}
    return None


def send_post(img, text, dry_run=False, chat=None):
    photo = "%s/assets/img/%s.jpg" % (SITE, img)
    if dry_run:
        print("\n----- DRY RUN (nothing sent) -----")
        print("chat :", chat or "<unresolved>")
        print("photo:", photo)
        print("text :\n" + text)
        print("----------------------------------\n")
        return True
    if not chat:
        print(NEED_SETUP + ": کانالی پیدا نشد. ربات را در کانال ادمین کنید و یک پیام در کانال بگذارید،")
        print("             یا متغیر TELEGRAM_CHAT_ID را در تنظیمات مخزن ثبت کنید.")
        return False

    payload = {"chat_id": chat, "caption": text[:1024], "parse_mode": "HTML"}
    if len(text) <= 1024:
        resp = api("sendPhoto", dict(payload, photo=photo))
        if resp.get("ok"):
            print("[telegram] photo post sent ✔ message_id=%s" % resp["result"]["message_id"])
            return True
        print("[telegram] sendPhoto failed: %s — trying text only" % resp.get("description"))
    resp = api("sendMessage", {"chat_id": chat, "text": text, "disable_web_page_preview": False})
    if resp.get("ok"):
        print("[telegram] text post sent ✔ message_id=%s" % resp["result"]["message_id"])
        return True
    print("[telegram] FAILED: %s" % resp.get("description"))
    return False


def reply(chat_id, text, buttons=True):
    payload = {"chat_id": chat_id, "text": text, "disable_web_page_preview": True}
    if buttons:
        payload["reply_markup"] = content.BUTTONS
    return api("sendMessage", payload)


def handle_updates(state):
    """پاسخ به پیام‌های مستقیم و دستورها (بدون هوش مصنوعی — پاسخ‌های آمادهٔ دقیق)."""
    offset = int(state.get("update_offset", 0))
    resp = api("getUpdates", {"offset": offset, "limit": 50, "allowed_updates": ["message"],
                              "timeout": 0})
    if not resp.get("ok"):
        print("[poll] getUpdates failed:", resp.get("description"))
        return 0
    handled = 0
    for upd in resp.get("result") or []:
        state["update_offset"] = upd["update_id"] + 1
        chan = ((upd.get("channel_post") or {}).get("chat")
                or ((upd.get("my_chat_member") or {}).get("chat")) or {})
        if chan.get("type") == "channel" and chan.get("id"):
            state["detected_chat_id"] = chan["id"]
            state["detected_chat_title"] = chan.get("title")
        msg = upd.get("message") or {}
        chat_id = (msg.get("chat") or {}).get("id")
        text = (msg.get("text") or "").strip()
        if not chat_id or not text:
            continue
        cmd = text.split()[0].split("@")[0].lstrip("/").lower()
        if cmd in content.REPLIES:
            out = content.REPLIES[cmd]
            buttons = cmd in ("start", "menu", "events", "reserve")
        else:
            out, buttons = content.FALLBACK, True
        r = reply(chat_id, out, buttons)
        print("[poll] %s from %s -> %s" % (text[:24] or "?", chat_id, "ok" if r.get("ok") else r.get("description")))
        handled += 1
    return handled


# ---------------------------------------------------------------- modes
def mode_selftest():
    me = api("getMe")
    print("token        :", "OK — @%s (id %s)" % (me["result"]["username"], me["result"]["id"])
          if me.get("ok") else "FAILED — " + str(me.get("description")))
    state = load_state()
    chat, src = resolve_chat(state)
    if chat:
        info = api("getChat", {"chat_id": chat})
        if info.get("ok"):
            print("channel      :", "%s (%s) — source: %s" % (info["result"].get("title"), chat, src))
            member = api("getChatMember", {"chat_id": chat, "user_id": me["result"]["id"]})
            status = (member.get("result") or {}).get("status") if member.get("ok") else member.get("description")
            print("bot in channel:", status)
        else:
            print("channel      :", "cannot access %s — %s" % (chat, info.get("description")))
    else:
        print("channel      :", NEED_SETUP + " — ربات هنوز در هیچ کانالی ادمین نیست.")
    print("ai           :", "enabled (provider=%s)" % (os.environ.get("AI_PROVIDER") or "auto") if ai_enabled()
          else "disabled — قالب‌های آماده استفاده می‌شود")
    print("state        : update_offset=%s last_post=%s" % (state.get("update_offset", 0),
                                                            state.get("last_post_date", "—")))
    return 0


def mode_discover():
    found = discover_channel()
    if not found:
        print("کانالی پیدا نشد. ۱) ربات را در کانال ادمین کنید ۲) یک پیام در کانال بفرستید ۳) دوباره اجرا کنید.")
        return 1
    print(json.dumps(found, ensure_ascii=False))
    print("\nبرای ثبت دائمی:  TELEGRAM_CHAT_ID=%s   (یا در گیت‌هاب → Settings → Variables)" % found["id"])
    return 0


def mode_poll():
    state = load_state()
    handled = handle_updates(state)
    if handled:
        save_state(state)
        print("[poll] %s پیام پاسخ داده شد" % persian_numbers(str(handled)))
    else:
        print("[poll] پیام جدیدی نبود")
    return 0


def mode_post(args):
    state = load_state()
    today = dt.date.today().isoformat()
    if state.get("last_post_date") == today and not args.force and not args.dry_run:
        print("[post] امروز قبلاً پست شده (%s) — برای ارسال دوباره --force بدهید" % today)
        return 0

    img, text = compose(args.topic)
    chat, src = resolve_chat(state)
    if chat:
        print("[post] target: %s (source: %s)" % (chat, src))
    sent = send_post(img, text, dry_run=args.dry_run, chat=chat)

    if sent and not args.dry_run:
        state["last_post_date"] = today
        state["last_post_topic"] = img
        save_state(state)
    return 0 if sent else 2


def main():
    parser = argparse.ArgumentParser(description="اتوماسیون تلگرام رستوران شمسه")
    parser.add_argument("mode", nargs="?", default="selftest",
                        choices=["post", "poll", "selftest", "discover"])
    parser.add_argument("--dry-run", action="store_true", help="فقط نمایش، بدون ارسال")
    parser.add_argument("--force", action="store_true", help="نادیده گرفتن قاعدهٔ «یک پست در روز»")
    parser.add_argument("--topic", type=int, default=None, help="شمارهٔ موضوع برای تست")
    args = parser.parse_args()

    if args.mode != "selftest" and not TOKEN:
        print("ERROR: TELEGRAM_BOT_TOKEN is not set", file=sys.stderr)
        return 2
    return {"selftest": mode_selftest, "discover": mode_discover,
            "poll": mode_poll, "post": lambda: mode_post(args)}[args.mode]()


if __name__ == "__main__":
    sys.exit(main())
