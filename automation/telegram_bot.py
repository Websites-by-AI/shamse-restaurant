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
import bot_skills as sk  # noqa: E402
import franchise_lib as fl  # noqa: E402
import intelligence_lib as il  # noqa: E402
import reputation_skills as rep  # noqa: E402
import restaurants_lib as rl  # noqa: E402

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
    """pollinations بدون کلید است، پس AI همیشه در دسترس است مگر صریحاً خاموش شود."""
    return (os.environ.get("AI_PROVIDER") or "").strip().lower() not in ("none", "off", "0")


AI_ENDPOINTS = {
    # نام سرویس → (آدرس، مدل پیش‌فرض، نوع کلید: repo | user | none=بدون کلید)
    "cloudflare": ("https://api.cloudflare.com/client/v4/accounts/{account}/ai/v1",
                   "@cf/meta/llama-3.3-70b-instruct-fp8-fast", "cf"),   # Workers AI — پلن رایگان
    "github": ("https://models.github.ai/inference", "openai/gpt-4o-mini", "repo"),
    "github-legacy": ("https://models.inference.ai.azure.com", "gpt-4o-mini", "repo"),
    "pollinations": ("https://text.pollinations.ai/openai", "openai", "none"),  # رایگان و بدون کلید
    "openrouter": ("https://openrouter.ai/api/v1", "meta-llama/llama-3.3-70b-instruct:free", "user"),
    "openai": ("https://api.openai.com/v1", "gpt-4o-mini", "user"),
    "custom": ("", "gpt-4o-mini", "user"),
}


def _ai_candidates():
    """فهرست سرویس‌هایی که به‌ترتیب امتحان می‌شوند."""
    provider = (os.environ.get("AI_PROVIDER") or "").strip().lower()
    key = (os.environ.get("AI_API_KEY") or "").strip()
    out = []
    if provider in ("", "auto"):
        if key:
            provider = "openai"
        elif os.environ.get("GITHUB_TOKEN"):
            provider = "github"
        elif os.environ.get("CLOUDFLARE_API_TOKEN") and os.environ.get("CLOUDFLARE_ACCOUNT_ID"):
            provider = "cloudflare"
        else:
            provider = "pollinations"      # بدون کلید و رایگان
    account = os.environ.get("CLOUDFLARE_ACCOUNT_ID", "")
    cf_token = os.environ.get("CLOUDFLARE_API_TOKEN", "")
    names = [provider]
    if provider == "cloudflare":
        pass
    if provider == "github":                      # اگر مدل‌های گیت‌هاب جواب نداد، درگاه قدیمی
        names.append("github-legacy")
    if cf_token and account and "cloudflare" not in names:
        names.append("cloudflare")                # Workers AI روی حساب خودمان — اولویت بالا
    if "pollinations" not in names:
        names.append("pollinations")              # رایگان و بدون کلید — پشتیبان همیشگی
    if key and "openai" not in names:
        names.append("openai")
    for name in names:
        base, model, kind = AI_ENDPOINTS.get(name, ("", "openai", "user"))
        base = os.environ.get("AI_BASE_URL") or base
        model = os.environ.get("AI_MODEL") or model
        k = {"repo": os.environ.get("GITHUB_TOKEN", ""), "user": key,
             "cf": cf_token, "none": ""}[kind]
        if not base or (not k and kind != "none"):
            continue
        try:
            base = base.format(account=account)
        except (KeyError, IndexError):
            continue
        out.append((name, base, model, k))
    return out


def _ai_request(name, base, model, key, prompt, system):
    body = json.dumps({
        "model": model,
        "messages": [{"role": "system", "content": system}, {"role": "user", "content": prompt}],
        "temperature": 0.8,
        "max_tokens": 600,
    }).encode("utf-8")
    headers = {"Content-Type": "application/json", "Accept": "application/json"}
    if key:                                        # pollinations بدون کلید کار می‌کند
        headers["Authorization"] = "Bearer " + key
    if name.startswith("github"):
        headers["X-GitHub-Api-Version"] = "2022-11-28"
    req = urllib.request.Request(base.rstrip("/") + "/chat/completions", data=body, headers=headers)
    with urllib.request.urlopen(req, timeout=60) as resp:
        raw = resp.read().decode("utf-8")
    data = json.loads(raw)                        # متن غیر-JSON ⇒ خطا برای امتحان سرویس بعدی
    return ((data.get("choices") or [{}])[0].get("message", {}) or {}).get("content", "").strip()


def call_ai(prompt, system):
    """تولید متن با اولین سرویس سالم. در صورت شکست یا خروجی نامعتبر → None (قالب آماده)."""
    candidates = _ai_candidates()
    if not candidates:
        print("[ai] no provider configured — template mode")
        return None
    for name, base, model, key in candidates:
        print("[ai] trying %s (%s / %s)" % (name, base, model))
        try:
            text = _ai_request(name, base, model, key, prompt, system)
        except urllib.error.HTTPError as exc:
            print("[ai] %s HTTP %s — %s" % (name, exc.code, exc.read().decode("utf-8", "replace")[:160]))
            continue
        except Exception as exc:  # noqa: BLE001
            print("[ai] %s unavailable (%s)" % (name, exc))
            continue
        if len(text) < 120 or len(re.findall(r"[\u0600-\u06FF]", text)) < 80:
            print("[ai] %s response rejected (not usable Persian): %r" % (name, text[:60]))
            continue
        print("[ai] %s accepted (%d chars)" % (name, len(text)))
        return text
    print("[ai] all endpoints failed — template fallback")
    return None


SYSTEM = (
    "تو مدیر شبکه‌های اجتماعی «رستوران شمسه» هستی؛ رستوران ایرانی در استانبول با دو شعبه: "
    "تکسیم (خیابان استقلال پلاک ۱۷۹، دو طبقه) و کوجاتپه (عبدالحکیم حمیت ۱۷)، تلفن +90 501 325 24 52، "
    "ساعات ۱۲:۰۰ تا ۰۱:۳۰، طبقهٔ دوم شعبهٔ استقلال ظرفیت ۶۰ نفر برای میتاپ. "
    "یک پست کوتاه فارسی برای کانال تلگرام بنویس: ۳ تا ۵ خط، ۲ تا ۴ ایموجی، پایان با ۱ تا ۲ هشتگ. "
    "هزینه‌ها و ساعات را دقیقاً همان‌طور که در متن پایه آمده نگه دار و شمارهٔ تلفن +90 501 325 24 52 را یک بار ذکر کن. "
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
    # شمارهٔ تلفن با ارقام لاتین (قابل کپی/تماس) و بقیهٔ متن فارسی
    text = template.format(phone=content.PHONE, menu=content.MENU_URL,
                           reserve=content.RESERVE_URL, events=content.EVENTS_URL)
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
            if content.FOOTER.strip() not in ai_text:
                ai_text = ai_text.rstrip() + content.FOOTER
            print("[ai] using AI-generated text")
            return img, fit_caption(ai_text)
        print("[ai] falling back to curated template")
    return img, fit_caption(text + content.FOOTER)


CAPTION_MAX = 1024


def fit_caption(text):
    """کپشن عکس حداکثر ۱۰۲۴ کاراکتر است؛ متن را طوری کوتاه کن که امضا (FOOTER) حفظ شود."""
    if len(text) <= CAPTION_MAX:
        return text
    footer = content.FOOTER.strip()
    tail = ""
    if footer and footer in text:
        text, tail = text.split(footer, 1)
        tail = footer + tail
    room = CAPTION_MAX - len(tail) - 3
    return text[:max(room, 0)].rstrip() + "…" + tail


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

    payload = {"chat_id": chat, "caption": text[:1024], "parse_mode": "HTML",
               "reply_markup": content.CHANNEL_BUTTONS}
    if len(text) <= 1024:
        resp = api("sendPhoto", dict(payload, photo=photo))
        if resp.get("ok"):
            print("[telegram] photo post sent ✔ message_id=%s" % resp["result"]["message_id"])
            return True
        print("[telegram] sendPhoto failed: %s — trying text only" % resp.get("description"))
    resp = api("sendMessage", {"chat_id": chat, "text": text, "disable_web_page_preview": False,
                               "reply_markup": content.CHANNEL_BUTTONS})
    if resp.get("ok"):
        print("[telegram] text post sent ✔ message_id=%s" % resp["result"]["message_id"])
        return True
    print("[telegram] FAILED: %s" % resp.get("description"))
    return False


def typing(chat_id):
    """نمایش «در حال نوشتن…» قبل از پاسخ (تجربهٔ کاربری بهتر)."""
    return api("sendChatAction", {"chat_id": chat_id, "action": "typing"})


def reply(chat_id, text, buttons=True, keyboard=False):
    payload = {"chat_id": chat_id, "text": text, "disable_web_page_preview": True}
    if keyboard:
        payload["reply_markup"] = content.KEYBOARD
    elif buttons:
        payload["reply_markup"] = content.BUTTONS
    return api("sendMessage", payload)


def send_welcome(chat_id):
    """خوش‌آمد با عکس + کیبورد ثابت؛ اگر عکس ناموفق بود، متن ساده."""
    caption = content.REPLIES["start"]
    r = api("sendPhoto", {"chat_id": chat_id, "photo": content.SITE + "/assets/img/interior.jpg",
                          "caption": caption[:1024], "reply_markup": content.KEYBOARD})
    if r.get("ok"):
        return r
    return reply(chat_id, caption, buttons=False, keyboard=True)


def handle_callback(upd, db):
    """دکمه‌های شیشه‌ای: ثبت‌نام/لغو رویداد و فهرست ثبت‌نام‌های من."""
    cq = upd.get("callback_query") or {}
    data = (cq.get("data") or "").strip()
    msg = cq.get("message") or {}
    chat_id = ((msg.get("chat") or {}).get("id")) or ((cq.get("from") or {}).get("id"))
    msg_id = msg.get("message_id")
    user = cq.get("from") or {}
    if not chat_id or not data:
        return False

    if data == "areas":
        api("answerCallbackQuery", {"callback_query_id": cq.get("id"), "text": "📍 انتخاب محله"})
        api("sendMessage", {"chat_id": chat_id, "text": "یک محله را انتخاب کنید:",
                            "reply_markup": rl.area_keyboard()})
        return True

    if data.startswith("area:"):
        aid = data.partition(":")[2]
        items = rl.filter_restaurants(area_id=aid)
        area_title = next((fa for a, fa, _ in rl.AREAS if a == aid), aid)
        body = rl.format_list_compact(items, title="رستوران‌های منطقهٔ " + area_title)
        api("answerCallbackQuery", {"callback_query_id": cq.get("id"), "text": area_title})
        reply(chat_id, body, buttons=True)
        return True

    if data.startswith("cat:"):
        cat = data.partition(":")[2]
        items = rl.filter_restaurants(category=cat)
        cat_title = "رستوران‌های ایرانی و فارسی استانبول" if cat == "iranian" else "رستوران‌های افغانستانی استانبول"
        body = rl.format_list_compact(items, title=cat_title)
        api("answerCallbackQuery", {"callback_query_id": cq.get("id"), "text": cat_title})
        reply(chat_id, body, buttons=True)
        return True

    if data == "my":
        keys = sk.user_rsvps(db, chat_id)
        lines = ["📋 ثبت‌نام‌های شما:"]
        for key in keys:
            found = sk.find_occurrence(key)
            if found:
                day, ev, _k = found
                lines.append("• %s — %s" % (ev.get("title", ""), sk.fa_date(day)))
        if len(lines) == 1:
            lines.append("هنوز در رویدادی ثبت‌نام نکرده‌اید. /rsvp را بفرستید.")
        api("answerCallbackQuery", {"callback_query_id": cq.get("id"), "text": "📋"})
        reply(chat_id, "\n".join(lines), buttons=True)
        return True

    action, _, key = data.partition(":")
    if action not in ("rsvp", "un"):
        api("answerCallbackQuery", {"callback_query_id": cq.get("id"), "text": "دستور نامشخص"})
        return False

    found = sk.find_occurrence(key)
    if not found:
        api("answerCallbackQuery", {"callback_query_id": cq.get("id"),
                                    "text": "این رویداد به پایان رسیده است."})
        return True
    day, ev, _k = found
    join = action == "rsvp"
    res = sk.toggle_rsvp(db, chat_id, key, join)
    if res["changed"]:
        sk.touch_user(db, chat_id, user)
    toast = ("✅ ثبت شد — %s نفر" % res["count"]) if join else "❌ لغو شد"
    api("answerCallbackQuery", {"callback_query_id": cq.get("id"), "text": toast})
    if msg_id:
        trans = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
        text = ("🎫 <b>%s</b>\n🗓 %s — %s %s\n📍 %s\n💰 %s\n👥 ثبت‌نام‌شده: %s"
                % (ev.get("title", ""), sk.WEEKDAYS[day.weekday()], sk.fa_date(day), ev.get("time", ""),
                   ev.get("place", ""), ev.get("price", ""),
                   str(res["count"]).translate(trans)))
        buttons = {"inline_keyboard": [
            ([{"text": "❌ لغو ثبت‌نام", "callback_data": "un:" + key}]
             if join else [{"text": "🎫 ثبت‌نام می‌کنم", "callback_data": "rsvp:" + key}]),
            [{"text": "📋 ثبت‌نام‌های من", "callback_data": "my"}]]}
        api("editMessageText", {"chat_id": chat_id, "message_id": msg_id, "text": text,
                                "parse_mode": "HTML", "reply_markup": buttons})
    return True


def skill_reply(cmd, text, chat_id, db):
    """مهارت‌های ربات: ثبت‌نام، پروفایل، لغو اطلاع‌رسانی. None = مربوط به این‌ها نیست."""
    if cmd == "rsvp":
        body = sk.events_list_text(db)
        r = reply(chat_id, body, buttons=False)
        api("sendMessage", {"chat_id": chat_id, "text": "برای ثبت‌نام، رویداد را انتخاب کنید:",
                            "reply_markup": sk.rsvp_keyboard(db)})
        return r
    if cmd == "my":
        user = sk.touch_user(db, chat_id)
        keys = sk.user_rsvps(db, chat_id)
        lines = ["👤 <b>پروفایل شما</b>",
                 "• نام: %s" % (user.get("name") or "—"),
                 "• عضو از: %s" % sk.fa_date(__import__("datetime").date.fromisoformat(user["joined"])),
                 "• رویدادهایی که ثبت‌نام کرده‌اید: %s" % str(user.get("events", 0)).translate(
                     str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹"))]
        if keys:
            lines.append("")
            for key in keys:
                found = sk.find_occurrence(key)
                if found:
                    day, ev, _k = found
                    lines.append("• %s — %s" % (ev.get("title", ""), sk.fa_date(day)))
        lines += ["", "برای لغو اطلاع‌رسانی‌ها /stop و برای فعال‌سازی دوباره /start را بفرستید."]
        return reply(chat_id, "\n".join(lines), buttons=True)
    if cmd == "stop":
        sk.touch_user(db, chat_id, opt_in=False)
        return reply(chat_id, "🔕 اطلاع‌رسانی‌ها خاموش شد. هر وقت خواستید /start بفرستید تا دوباره روشن شود.",
                     buttons=False)
    return None



MENTION = "@shamse_restaurant_bot"
RL_SECONDS = 2.5          # ضداسپم: حداقل فاصلهٔ پاسخ به هر چت


def _norm(text):
    """نرمال‌سازی متن فارسی: حذف نیم‌فاصله، فاصله‌های اضافی و یکسان‌سازی."""
    return re.sub(r"\s+", " ", (text or "").replace("\u200c", " ").replace("ي", "ی")).strip().lower()


def should_reply(text, chat_type):
    """در چت خصوصی همیشه؛ در گروه فقط برای دستور یا منشن."""
    if chat_type == "private":
        return True
    if (text or "").lstrip().startswith("/"):
        return True
    return MENTION.lower() in (text or "").lower()


def clean_text(text):
    """حذف منشن ربات از متن گروه + اصلاح فاصله‌های باقی‌مانده."""
    return re.sub(r"\s+", " ", re.sub(r"@?shamse_restaurant_bot", " ", text or "", flags=re.I)).strip()


def kb_answer(text):
    """پاسخ آمادهٔ دقیق برای سؤالات پرتکرار (بدون هوش مصنوعی)."""
    n = _norm(text)
    for keywords, answer in content.KB:
        if any(k in n for k in keywords):
            return answer.replace("**", "")
    return None


def ai_answer(question):
    """پاسخ آزاد با هوش مصنوعی، فقط بر اساس اطلاعات رسمی رستوران."""
    system = ("تو پشتیبان رسمی رستوران شمسه در تلگرام هستی. فقط بر اساس اطلاعات زیر پاسخ بده؛ "
              "از خودت قیمت، آدرس یا وعدهٔ تازه نساز. پاسخ کوتاه (حداکثر ۳ خط)، مودب و فارسی با یک ایموجی.\n\n"
              + content.AI_FACTS)
    for name, base, model, key in _ai_candidates():
        try:
            raw = _ai_request(name, base, model, key, question, system)
        except Exception:  # noqa: BLE001 — موتور بعدی
            continue
        text = (raw or "").strip()
        if len(text) >= 30 and len(re.findall(r"[\u0600-\u06FF]", text)) >= 15:
            print("[poll] answered by %s (%d chars)" % (name, len(text)))
            return text[:700]
    return None


def handle_updates(state, minutes=0, timeout=0):
    """پاسخ به پیام‌ها. minutes>0 یعنی long-poll تا آن مدت (پاسخ آنی)."""
    if minutes:
        timeout = 25
        print("[poll] long-poll for %s min (timeout=%ss)" % (persian_numbers(str(minutes)), timeout))
    started = time.time()
    handled = 0
    db = sk.load_db()
    while True:
        resp = api("getUpdates", {"offset": int(state.get("update_offset", 0)), "limit": 50,
                                  "allowed_updates": ["message", "callback_query"], "timeout": timeout})
        if not resp.get("ok"):
            print("[poll] getUpdates failed:", resp.get("description"))
            break
        for upd in resp.get("result") or []:
            state["update_offset"] = upd["update_id"] + 1
            chan = ((upd.get("channel_post") or {}).get("chat")
                    or ((upd.get("my_chat_member") or {}).get("chat")) or {})
            if chan.get("type") == "channel" and chan.get("id"):
                state["detected_chat_id"] = chan["id"]
                state["detected_chat_title"] = chan.get("title")

            if upd.get("callback_query"):
                if handle_callback(upd, db):
                    handled += 1
                continue

            msg = upd.get("message") or {}
            chat = msg.get("chat") or {}
            chat_id, chat_type = chat.get("id"), chat.get("type", "private")
            raw_text = (msg.get("text") or "").strip()
            if not chat_id:
                continue
            if not raw_text:
                kind = next((k for k in ("voice", "photo", "sticker", "video", "document", "audio")
                             if msg.get(k)), None)
                if kind and should_reply("@", chat.get("type")) is False:
                    continue
                text_map = {"voice": "🎤 پیام صوتی", "photo": "🖼 عکس", "sticker": "🙂 استیکر",
                            "video": "🎬 ویدیو", "document": "📄 فایل", "audio": "🎵 صدا"}
                reply(chat_id, "دریافت شد: %s ✅\nمن فعلاً فقط متن را می‌فهمم — سؤالتان را تایپ کنید یا از دکمه‌های پایین استفاده کنید.\n"
                               "☎️ برای هماهنگی سریع: %s" % (text_map.get(kind, "پیام"), content.PHONE), buttons=True)
                sk.bump(db, "nontext")
                handled += 1
                continue
            if not should_reply(raw_text, chat_type):
                continue

            text = clean_text(raw_text)
            label = content.QUICK.get(raw_text) or content.QUICK.get(text)
            cmd = None
            if raw_text.startswith("/"):
                cmd = raw_text.split()[0].split("@")[0].lstrip("/").lower()
            elif label:
                cmd = label

            now = time.time()
            rl = state.setdefault("rl", {})
            if now - float(rl.get(str(chat_id), 0)) < RL_SECONDS:
                continue                       # ضداسپم
            rl[str(chat_id)] = now

            sk.touch_user(db, chat_id, msg.get("from") or {}, opt_in=(None if cmd != "start" else True))
            sk.bump(db, "messages")
            if cmd:
                sk.bump(db, "cmd:" + cmd)

            payload = raw_text.split()[1:2]
            if cmd == "start" and payload:
                cmd = payload[0].split("@")[0].lower()   # دیپ‌لینک: t.me/...?start=rsvp

            if cmd == "start":
                r = send_welcome(chat_id)
                out = "(welcome)"
            elif cmd in ("rsvp", "my", "stop"):
                r = skill_reply(cmd, text, chat_id, db)
                out = "/" + cmd
            elif cmd == "news":
                r, out = reply(chat_id, news_reply()), "news"
            elif cmd == "areas":
                r = reply(chat_id, content.REPLIES["areas"], buttons=False)
                api("sendMessage", {"chat_id": chat_id, "text": "منطقهٔ مورد نظر را انتخاب کنید:",
                                    "reply_markup": rl.area_keyboard()})
                out = "/areas"
            elif cmd == "search":
                q = " ".join(raw_text.split()[1:]) if len(raw_text.split()) > 1 else ""
                if q:
                    results = rl.filter_restaurants(query=q)
                    if results:
                        out_msg = rl.format_list_compact(results, title="نتایج جستجو برای «%s»" % q)
                    else:
                        out_msg = "رستورانی برای «%s» پیدا نشد. برای دیدن همه، /restaurants را بزنید." % q
                    r = reply(chat_id, out_msg, buttons=True)
                else:
                    r = reply(chat_id, content.REPLIES["search"], buttons=True)
                out = "/search"
            elif cmd == "campaign":
                parts = raw_text.split()
                etype = parts[1].lower() if len(parts) > 1 else "mafia"
                camp = il.generate_campaign(etype)
                ros_lines = ["\n📋 <b>برنامه زمان‌بندی:</b>"] + ["• %s: %s" % (t, d) for t, d in camp.get("run_of_show", [])]
                out_msg = camp.get("telegram", "") + "\n" + "\n".join(ros_lines)
                r = reply(chat_id, out_msg, buttons=True)
                out = "/campaign"
            elif cmd == "skills":
                parts = raw_text.split(maxsplit=1)
                if len(parts) > 1 and parts[1].strip():
                    q = parts[1].strip()
                    matched = rep.search_skills(q)[:4]
                    if matched:
                        lines = [f"⚡ <b>نتایج جستجوی مهارت برای «{q}»:</b>\n"]
                        for m in matched:
                            lines.append(f"• <b>{m['id']}: {m['name_fa']}</b>\n  <i>ابزار:</i> {m['engine_tool']}\n  <i>اقدام:</i> {m['action']}\n")
                        lines.append(f"🌐 مشاهده ۱۰۰ مهارت کامل در سایت:\n{content.SITE}/intelligence.html#mod-gateways")
                        out_msg = "\n".join(lines)
                    else:
                        out_msg = f"مهارتی با عبارت «{q}» یافت نشد.\n\n" + content.REPLIES.get("skills", "")
                else:
                    out_msg = content.REPLIES.get("skills", "")
                r = reply(chat_id, out_msg, buttons=True)
                out = "/skills"
            elif cmd == "franchise":
                r = reply(chat_id, content.REPLIES["franchise"], buttons=True)
                out = "/franchise"
            elif cmd in content.REPLIES:
                r = reply(chat_id, content.REPLIES[cmd], buttons=True)
                out = "/" + cmd
            else:
                out_text = kb_answer(text)
                source = "kb"
                if out_text:
                    sk.bump(db, "kb_answers")
                else:
                    typing(chat_id)
                    out_text = ai_answer(text)
                    source = "ai"
                if source == "ai" and out_text:
                    sk.bump(db, "ai_answers")
                if not out_text:
                    out_text = content.FALLBACK
                    source = "fallback"
                r = reply(chat_id, out_text, buttons=True)
                out = source
            print("[poll] %s [%s] %s -> %s" % (chat_type, out, text[:36].replace("\n", " ") or "?",
                                               "ok" if r.get("ok") else r.get("description")))
            handled += 1
        if not minutes or (time.time() - started) >= minutes * 60:
            break
    try:
        sk.save_db(db)
    except OSError as exc:
        print("[poll] could not save bot db:", exc)
    return handled


CHANNEL_DESCRIPTION = (
    "🍽 رستوران ایرانی شمسه در استانبول — دو شعبه: تکسیم و کوجاتپه.\n"
    "طبقهٔ دوم شعبهٔ استقلال میزبان میتاپ و گردهمایی (ظرفیت ۶۰ نفر).\n"
    "🎫 ثبت‌نام رویدادها با ربات: @shamse_restaurant_bot\n"
    "🌐 وب‌سایت: shamse-restaurant.pages.dev"
)

BOT_DESCRIPTION = (
    "راهنمای رستوران‌های ایرانی، فارسی و افغانستانی در استانبول.\n\n"
    "فهرست ۱۹ رستوران معتبر با آدرس دقیق، موقعیت نقشه، شماره تماس، وب‌سایت و منو "
    "(تکسیم، زیتین‌بورنو، اسنیورت، بیلیک‌دوزو، شیشلی، فاتیح و بخش آسیایی):\n"
    "• ۱۲ رستوران ایرانی و فارسی (فارسی، ریحون، سفیر، شمسه، سودی، آسمان، مژگان، شاندیز، نایب، کیوان)\n"
    "• ۷ رستوران افغانستانی (بهار افغان، افغان کباب، آریا، سفره افغان، افغان ترک، منان کابل، افغان بیک)\n\n"
    "🌐 سایت: shamse-restaurant.pages.dev/restaurants.html\n"
    "📣 کانال: @shamse_restaurant"
)

BOT_SHORT = "راهنمای رستوران‌های ایرانی و افغانستانی استانبول با آدرس، منو، نقشه و لینک"

COMMANDS = [
    {"command": "restaurants", "description": "فهرست ۱۹ رستوران ایرانی و افغان"},
    {"command": "iranian", "description": "۱۲ رستوران ایرانی و فارسی با آدرس و منو"},
    {"command": "afghan", "description": "۷ رستوران افغانستانی با آدرس و منو"},
    {"command": "areas", "description": "جستجو بر اساس محله‌های استانبول"},
    {"command": "search", "description": "جستجوی رستوران یا غذا"},
    {"command": "campaign", "description": "تولید تبلیغ دورهمی و کلاب با AI"},
    {"command": "skills", "description": "⚡ ۱۰۰ مهارت هوش تجاری و گیت‌وی‌ها"},
    {"command": "franchise", "description": "🏢 هوش فرانچایز و تحلیل شعب"},
    {"command": "intel", "description": "تحلیل رقبا و حاشیه سود منو"},
    {"command": "space", "description": "تحلیل درآمد فضای خالی رستوران"},
    {"command": "rsvp", "description": "ثبت‌نام رویدادها و میتاپ‌ها"},
    {"command": "events", "description": "تقویم رویدادها"},
    {"command": "my", "description": "پروفایل من"},
    {"command": "news", "description": "اخبار و فراخوان‌ها"},
    {"command": "start", "description": "شروع و منوی اصلی"},
    {"command": "contact", "description": "تماس و ثبت رستوران"},
    {"command": "help", "description": "راهنمای کامل"},
    {"command": "stop", "description": "خاموش‌کردن اطلاع‌رسانی"},
]

GUIDE_MARKER = "راهنمای رستوران شمسه"


def mode_brand():
    """یک‌بار اجرا: پروفایل ربات + عنوان و توضیح کانال + پست راهنما (سنجاق‌شده)."""
    me = api("getMe")
    if not me.get("ok"):
        print("token problem:", me.get("description"))
        return 2
    name_res = api("setMyName", {"name": "رستوران‌های ایرانی و افغان استانبول"})
    print("bot name     :", name_res.get("ok"))
    print("bot profile  :", api("setMyDescription", {"description": BOT_DESCRIPTION, "language_code": ""}).get("ok"),
          "|", api("setMyShortDescription", {"short_description": BOT_SHORT, "language_code": ""}).get("ok"),
          "| commands:", api("setMyCommands", {"commands": COMMANDS}).get("ok"))
    menu = api("setChatMenuButton", {"menu_button": {"type": "web_app", "text": "رستوران‌های استانبول",
                                                     "web_app": {"url": content.SITE + "/restaurants.html"}}})
    print("menu button  :", menu.get("ok"), menu.get("description", ""))

    chat, src = resolve_chat()
    if not chat:
        print(NEED_SETUP + ": هیچ کانالی پیدا نشد — ربات را ادمین کانال کنید.")
        return 2
    info = api("getChat", {"chat_id": chat})
    cur_title = (info.get("result") or {}).get("title") or ""
    print("channel      :", cur_title, "| source:", src)

    if cur_title != "رستوران شمسه | Shamse Restaurant":
        r = api("setChatTitle", {"chat_id": chat, "title": "رستوران شمسه | Shamse Restaurant"})
        print("setChatTitle :", r.get("ok"), r.get("description", ""))

    r = api("setChatDescription", {"chat_id": chat, "description": CHANNEL_DESCRIPTION})
    print("setChatDescription:", r.get("ok"), r.get("description", ""), "| len:", len(CHANNEL_DESCRIPTION))
    if not r.get("ok"):
        print("   ↳ اگر باز هم نشد، ربات باید اجازهٔ «تغییر اطلاعات کانال» (can_change_info) داشته باشد.")

    pinned = ((info.get("result") or {}).get("pinned_message") or {})
    pinned_text = pinned.get("text") or pinned.get("caption") or ""
    if GUIDE_MARKER in pinned_text:
        print("pinned guide : already pinned ✔ (message_id=%s)" % pinned.get("message_id"))
        return 0

    sent = api("sendMessage", {"chat_id": chat, "text": content.GUIDE_POST,
                               "disable_web_page_preview": False, "reply_markup": content.BUTTONS})
    if not sent.get("ok"):
        print("send guide   : FAILED —", sent.get("description"))
        return 2
    mid = sent["result"]["message_id"]
    pin = api("pinChatMessage", {"chat_id": chat, "message_id": mid, "disable_notification": False})
    print("guide post   : sent ✔ message_id=%s | pinned:" % mid, pin.get("ok"), pin.get("description", ""))
    return 0 if pin.get("ok") else 0


def news_reply():
    """آخرین خبرهای منتشرشده از دیتابیس اخبار (news_db.json)."""
    path = os.path.join(os.path.dirname(os.path.abspath(__file__)), "news_db.json")
    try:
        with open(path, encoding="utf-8") as fh:
            db = json.load(fh)
    except (OSError, ValueError):
        db = {}
    items = [x for x in (db.get("items") or {}).values() if x.get("posted")]
    items.sort(key=lambda x: x.get("posted_at") or "", reverse=True)
    if not items:
        return ("📰 هنوز خبری منتشر نشده است.\nکانال ما را دنبال کنید: " + content.CHANNEL_URL +
                "\n🌐 " + content.SITE_LABEL)
    lines = ["📰 آخرین اخبار و فراخوان‌های مرتبط", ""]
    for x in items[:5]:
        lines.append("• %s\n  🔗 %s" % ((x.get("title_fa") or x.get("title") or "")[:90], x.get("link", "")))
    lines += ["", "🌐 %s · 📣 %s" % (content.SITE_LABEL, content.CHANNEL_URL)]
    return "\n".join(lines)



def mode_remind():
    """یادآور شب رویداد برای کسانی که فردا در رویدادی ثبت‌نام کرده‌اند."""
    db = sk.load_db()
    due = sk.reminders_due(db)
    if not due:
        print("[remind] یادآوری لازم نیست")
        return 0
    sent = 0
    for item in due:
        ev, day = item["event"], item["day"]
        text = ("⏰ <b>یادآور رویداد</b>\nفردا %s: <b>%s</b> ساعت %s\n📍 %s\n💰 %s\n\n"
                "منتظرتان هستیم! اگر نمی‌توانید بیایید، با دکمهٔ زیر لغو کنید."
                % (sk.fa_date(day), ev.get("title", ""), ev.get("time", ""), ev.get("place", ""),
                   ev.get("price", "")))
        for uid in item["users"]:
            r = api("sendMessage", {"chat_id": uid, "text": text, "parse_mode": "HTML",
                                    "reply_markup": {"inline_keyboard": [
                                        [{"text": "❌ لغو ثبت‌نام", "callback_data": "un:" + item["id"].rsplit("@", 1)[0]}]]}})
            if r.get("ok"):
                sent += 1
        db["reminders"][item["id"]] = dt.date.today().isoformat()
    sk.save_db(db)
    print("[remind] %s یادآور ارسال شد" % persian_numbers(str(sent)))
    return 0


def mode_broadcast(args):
    """ارسال پیام گروهی به کاربران (برای اطلاعیه‌های رستوران)."""
    if not args.text:
        print("متن پیام را با --text بدهید.")
        return 2
    db = sk.load_db()

    def send(uid, text):
        return api("sendMessage", {"chat_id": uid, "text": text, "parse_mode": "HTML",
                                   "reply_markup": content.BUTTONS}).get("ok")

    res = sk.broadcast(db, send, args.text, dry_run=args.dry_run)
    sk.bump(db, "broadcasts")
    if not args.dry_run:
        sk.save_db(db)
    print("[broadcast] %s=%s | ناموفق=%s | لغو‌شده=%s" % (
        "گیرندگان" if args.dry_run else "ارسال‌شده",
        persian_numbers(str(res["sent"])), persian_numbers(str(res["failed"])), persian_numbers(str(res["skipped"]))))
    return 0


def mode_report():
    """گزارش وضعیت ربات: کاربران، ثبت‌نام‌ها، پرمصرف‌ترین دستورها."""
    db = sk.load_db()
    st = sk.stats(db)
    trans = str.maketrans("0123456789", "۰۱۲۳۴۵۶۷۸۹")
    print("👥 کاربران: %s (فعال: %s)" % (str(st["users"]).translate(trans), str(st["opted_in"]).translate(trans)))
    print("🎫 ثبت‌نام‌های فعال: %s" % str(st["rsvps"]).translate(trans))
    print("📊 پرمصرف‌ترین‌ها:", ", ".join("%s=%s" % (k, v) for k, v in st["top_counters"]) or "—")
    for key, entries in sorted(db["rsvps"].items()):
        found = sk.find_occurrence(key)
        title = found[1]["title"] if found else key
        print("   • %s → %s نفر" % (title, str(len(entries)).translate(trans)))
    return 0


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
    chain = _ai_candidates() if ai_enabled() else []
    print("ai           :", ("enabled — chain: " + " → ".join(n for n, *_ in chain)) if chain
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


def mode_poll(minutes=0):
    state = load_state()
    handled = handle_updates(state, minutes=minutes)
    save_state(state)                      # rl/offset هم ذخیره می‌شود
    if handled:
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
                        choices=["post", "poll", "selftest", "discover", "brand", "remind", "broadcast", "report"])
    parser.add_argument("--dry-run", action="store_true", help="فقط نمایش، بدون ارسال")
    parser.add_argument("--force", action="store_true", help="نادیده گرفتن قاعدهٔ «یک پست در روز»")
    parser.add_argument("--topic", type=int, default=None, help="شمارهٔ موضوع برای تست")
    parser.add_argument("--loop", type=int, default=0, help="دقیقهٔ long-poll برای حالت poll (پاسخ آنی)")
    parser.add_argument("--text", default="", help="متن پیام برای حالت broadcast")
    args = parser.parse_args()

    if args.mode != "selftest" and not TOKEN:
        print("ERROR: TELEGRAM_BOT_TOKEN is not set", file=sys.stderr)
        return 2
    return {"selftest": mode_selftest, "discover": mode_discover, "brand": mode_brand,
            "remind": mode_remind, "report": mode_report, "broadcast": lambda: mode_broadcast(args),
            "poll": lambda: mode_poll(args.loop), "post": lambda: mode_post(args)}[args.mode]()


if __name__ == "__main__":
    sys.exit(main())
