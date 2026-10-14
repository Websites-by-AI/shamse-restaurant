#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
دیتابیس اخبار و فراخوان‌های مرتبط + بررسی با هوش مصنوعی + انتشار خودکار در کانال شمسه.

اجرا:
    python3 automation/news.py --dry-run          # فقط بررسی و پیش‌نمایش (بدون ارسال)
    python3 automation/news.py                    # بررسی + انتشار در کانال
    python3 automation/news.py --limit 6          # حداکثر ۶ خبر برای بررسی در این اجرا
    python3 automation/news.py --report           # فقط وضعیت دیتابیس

ساختار:
    news_feeds.json  → منابع (فیدها) و آستانه‌ها
    news_db.json     → دیتابیس محلی: هر آیتم با امتیاز، خلاصهٔ فارسی و وضعیت انتشار
"""
import argparse
import datetime as dt
import hashlib
import html
import json
import os
import re
import sys
import urllib.error
import urllib.request
import xml.etree.ElementTree as ET

HERE = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, HERE)
import telegram_bot as tb  # noqa: E402  (api / _ai_candidates / _ai_request / resolve_chat)
import content  # noqa: E402

CONF_FILE = os.path.join(HERE, "news_feeds.json")
DB_FILE = os.path.join(HERE, "news_db.json")
UA = "Mozilla/5.0 (compatible; ShamseNews/1.0; +https://shamse-restaurant.pages.dev)"
KEEP_ITEMS = 400

AI_SYSTEM = (
    "تو ویراستار هوش مصنوعی «رستوران شمسه» هستی؛ رستوران ایرانی در استانبول با دو شعبه (تکسیم و کوجاتپه) "
    "و طبقهٔ میتاپ ۶۰ نفره در شعبهٔ استقلال. کارت: از میان خبرهای دریافتی، فقط موارد «مرتبط» را برای کانال "
    "تلگرام رستوران انتخاب کنی. معیار ارتباط: رویدادها/جشنواره‌های غذا و گاسترونومی استانبول، اخبار صنعت رستوران، "
    "فرهنگ و غذای ایرانی، رویدادهای جامعهٔ ایرانی و بین‌المللی‌ها در استانبول، فراخوان‌های فرهنگی/هنری که می‌تواند "
    "مخاطب رستوران باشد. اخبار نامرتبط سیاسی/ورزشی/دور از غذا و فرهنگ را رد کن."
)

AI_TEMPLATE = """خبر زیر را بررسی کن و فقط یک JSON برگردان (بدون هیچ متن اضافه):

{{"score": <0 تا 10 عدد صحیح>, "post": <true یا false>, "title_fa": "<عنوان فارسی کوتاه، حداکثر ۹۰ کاراکتر>", "summary_fa": "<خلاصهٔ فارسی ۱ تا ۲ جمله‌ای، حداکثر ۲۲۰ کاراکتر>"}}

قواعد: اگر «post» را false بگذاری، یعنی خبر برای کانال مناسب نیست. از بزرگ‌نمایی یا اضافه‌کردن اطلاعات از خودت پرهیز کن.

منبع: {feed}
دسته: {cat}
عنوان اصلی: {title}
خلاصهٔ اصلی: {desc}"""


# ---------------------------------------------------------------- io helpers
def load_json(path, default):
    try:
        with open(path, encoding="utf-8") as fh:
            return json.load(fh)
    except (OSError, ValueError):
        return default


def save_json(path, obj):
    tmp = path + ".tmp"
    with open(tmp, "w", encoding="utf-8") as fh:
        json.dump(obj, fh, ensure_ascii=False, indent=2, sort_keys=True)
        fh.write("\n")
    os.replace(tmp, path)


# ---------------------------------------------------------------- feed parsing
def fetch(url, timeout=30):
    req = urllib.request.Request(url, headers={
        "User-Agent": UA,
        "Accept": "application/rss+xml, application/atom+xml, application/xml, text/xml, */*",
    })
    with urllib.request.urlopen(req, timeout=timeout) as resp:
        return resp.read()


def strip_html(text):
    return re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html.unescape(text or ""))).strip()


ATOM_NS = "{http://www.w3.org/2005/Atom}"


def _node_text(node, *names):
    """متن اولین تگ موجود، با پشتیبانی از فضای‌نام Atom."""
    for name in names:
        for candidate in (name, ATOM_NS + name):
            value = node.findtext(candidate)
            if value and value.strip():
                return value.strip()
    return ""


def parse_feed(raw):
    """RSS/Atom → فهرست آیتم‌ها (برای تست آفلاین هم استفاده می‌شود)."""
    root = ET.fromstring(raw)
    out = []
    for it in root.findall(".//item") + root.findall(".//" + ATOM_NS + "entry"):
        title = html.unescape(_node_text(it, "title"))
        link = _node_text(it, "link")
        if not link:  # atom: <link href="..."/>
            el = it.find(ATOM_NS + "link")
            link = (el.get("href") if el is not None else "") or ""
        pub = _node_text(it, "pubDate", "updated", "published", "date")
        desc = strip_html(_node_text(it, "description", "summary", "content"))[:400]
        if title and link:
            out.append({"title": title, "link": link.strip(), "pub": pub, "desc": desc})
    return out


def parse_date(value):
    """pubDate → datetime(UTC) یا None."""
    if not value:
        return None
    try:
        from email.utils import parsedate_to_datetime
        d = parsedate_to_datetime(value)
        return d if d.tzinfo else d.replace(tzinfo=dt.timezone.utc)
    except Exception:  # noqa: BLE001
        try:
            return dt.datetime.fromisoformat(value.replace("Z", "+00:00"))
        except ValueError:
            return None


def item_id(link, title):
    return hashlib.sha1((link + "|" + title).encode("utf-8")).hexdigest()[:16]


# ---------------------------------------------------------------- ai judging
def parse_ai_json(text):
    """استخراج JSON از پاسخ مدل، حتی اگر متن اضافه داشته باشد."""
    if not text:
        return None
    for candidate in re.findall(r"\{.*?\}", text, re.S) + re.findall(r"\{.*\}", text, re.S):
        try:
            data = json.loads(candidate)
        except ValueError:
            continue
        if not isinstance(data, dict) or "score" not in data:
            continue
        try:
            score = int(round(float(data.get("score"))))
        except (TypeError, ValueError):
            continue
        data["score"] = max(0, min(10, score))
        data["post"] = bool(data.get("post", data["score"] >= 7))
        data["title_fa"] = fa_text_ok(strip_html(str(data.get("title_fa", ""))), 0.5)[:120]
        data["summary_fa"] = fa_text_ok(strip_html(str(data.get("summary_fa", ""))), 0.4)[:260]
        return data
    return None


def fa_text_ok(text, min_ratio):
    """اگر متن به‌قدر کافی فارسی نیست، خالی برگردان تا از متن اصلی استفاده شود."""
    if not text:
        return ""
    persian = len(re.findall(r"[\u0600-\u06FF]", text))
    letters = len(re.findall(r"[A-Za-z\u0600-\u06FF]", text)) or 1
    return text if (persian / letters) >= min_ratio else ""


def ai_judge(item, feed_name, cat):
    """نظر هوش مصنوعی دربارهٔ یک خبر. None = هیچ موتوری پاسخ معتبر نداد."""
    prompt = AI_TEMPLATE.format(feed=feed_name, cat=cat, title=item["title"], desc=item["desc"] or "—")
    for name, base, model, key in tb._ai_candidates():
        try:
            raw = tb._ai_request(name, base, model, key, prompt, AI_SYSTEM)
        except Exception as exc:  # noqa: BLE001
            print("  [ai] %s failed (%s)" % (name, exc))
            continue
        verdict = parse_ai_json(raw)
        if verdict:
            verdict["engine"] = name
            return verdict
        print("  [ai] %s returned unusable JSON" % name)
    return None


# ---------------------------------------------------------------- db + selection
NOISE = ("flood", "rain ", "weather", "storm", "earthquake", "hurricane", "election", "court",
         "police", "military", "war ", "killed", "accident", "زلزله", "سیل", "انتخابات", "دادگاه",
         "پلیس", "جنگ", "تصادف", "هواشناسی")
FOOD_HINTS = ("restoran", "restaurant", "gastronom", "yemek", "lezzet", "mutfak", "kafe", "cafe",
              "chef", "şef", "menu", "menü", "food", "festival", "tat", "sofra", "şarap", "çay",
              "رستوران", "غذا", "کافه", "آشپز", "شیرینی", "خورش", "کباب", "نان", "چای", "سفره",
              "میزبان", "پذیرایی", "جشنواره")


def relevance_hint(item):
    """امتیاز سرانگشتی (۰ تا ۲) برای اولویت‌بندی پیش از هوش مصنوعی — نه جایگزین آن."""
    text = (item.get("title", "") + " " + item.get("desc", "")).lower()
    if any(word in text for word in NOISE) and not any(word in text for word in FOOD_HINTS):
        return -1                      # نویز آشکار: به هوش مصنوعی هم فرستاده نمی‌شود
    return 1 if any(word in text for word in FOOD_HINTS) else 0


def collect_new(conf, db, feeds_items, now, limit):
    """آیتم‌های تازه (یا بررسی‌نشده) که باید به هوش مصنوعی بروند."""
    fresh = []
    for item in feeds_items:
        iid = item_id(item["link"], item["title"])
        known = db["items"].get(iid)
        if known and known.get("score") is not None:
            continue                    # قبلاً بررسی و ثبت شده
        published = parse_date(item["pub"])
        if published and (now - published) > dt.timedelta(days=conf["max_age_days"]):
            continue
        hint = relevance_hint(item)
        if hint < 0:
            continue
        item["id"] = iid
        item["published"] = published.isoformat() if published else None
        item["hint"] = hint
        fresh.append(item)
    # اولویت: مرتبط‌ترها، بعد تازه‌ترها
    fresh.sort(key=lambda x: (-x.get("hint", 0), x.get("published") or ""), reverse=False)
    fresh.sort(key=lambda x: x.get("published") or "", reverse=True)
    fresh.sort(key=lambda x: -x.get("hint", 0))
    return fresh[:limit]


def build_post(selected, conf):
    """متن پست کانال برای خبرهای انتخاب‌شده."""
    lines = ["📰 اخبار و فراخوان‌های مرتبط", ""]
    for i, it in enumerate(selected, 1):
        title = html.escape(it.get("title_fa") or it["title"])
        summary = html.escape(it.get("summary_fa") or "")
        if summary and not re.search(r"[\u0600-\u06FF]{8,}", summary):
            summary = ""
        src = html.escape(it.get("source") or "")
        lines.append('<b>%d) %s</b>' % (i, title))
        if summary:
            lines.append(summary)
        lines.append('🔗 <a href="%s">%s</a>' % (html.escape(it["link"], quote=True),
                                                "متن کامل" + (" — " + src if src else "")))
        lines.append("")
    lines.append("🌐 سایت: %s | 🤖 ربات: @shamse_restaurant_bot" % content.SITE_LABEL)
    lines.append(content.TAGS)
    return "\n".join(lines).strip()


def prune(db):
    items = db.get("items", {})
    if len(items) <= KEEP_ITEMS:
        return
    order = sorted(items.values(), key=lambda x: x.get("first_seen") or "", reverse=True)
    db["items"] = {it["id"]: it for it in order[:KEEP_ITEMS]}


def report(db):
    items = list(db.get("items", {}).values())
    posted = [i for i in items if i.get("posted")]
    pending = [i for i in items if i.get("score") is None]
    print("دیتابیس اخبار: %d آیتم | منتشرشده: %d | در انتظار بررسی: %d" %
          (len(items), len(posted), len(pending)))
    for it in sorted(posted, key=lambda x: x.get("posted_at") or "", reverse=True)[:8]:
        print("  ✔ [%s] %s" % (it.get("score"), (it.get("title_fa") or it["title"])[:74]))


# ---------------------------------------------------------------- main run
def run(args):
    conf = load_json(CONF_FILE, None)
    if not conf:
        print("news_feeds.json پیدا نشد/نامعتبر است")
        return 2
    db = load_json(DB_FILE, {"items": {}, "runs": []})
    db.setdefault("items", {})
    db.setdefault("runs", [])
    if args.report:
        report(db)
        return 0

    now = dt.datetime.now(dt.timezone.utc)
    limit = args.limit or conf.get("max_candidates_per_run", 12)

    # 1) دریافت فیدها
    feeds_items = []
    for feed in conf["feeds"]:
        try:
            items = parse_feed(fetch(feed["url"]))
            for it in items:
                it["source"] = feed["name"]
                it["cat"] = feed["cat"]
            feeds_items.append((feed, items))
            print("فید «%s»: %d آیتم" % (feed["name"], len(items)))
        except Exception as exc:  # noqa: BLE001 — یک فید خراب کل اجرا را متوقف نمی‌کند
            print("فید «%s» خطا داد: %s" % (feed["name"], exc))

    flat = [it for _f, items in feeds_items for it in items]
    new_items = collect_new(conf, db, flat, now, limit)
    print("آیتم تازه برای بررسی: %d" % len(new_items))

    # 2) بررسی با هوش مصنوعی
    for it in new_items:
        verdict = ai_judge(it, it["source"], it["cat"])
        entry = {
            "id": it["id"], "title": it["title"], "link": it["link"], "source": it["source"],
            "cat": it["cat"], "published": it.get("published"), "first_seen": now.isoformat(),
            "score": None, "post": None, "title_fa": "", "summary_fa": "",
            "engine": None, "posted": False, "posted_at": None, "message_id": None,
        }
        if verdict:
            entry.update(score=verdict["score"], post=verdict["post"],
                         title_fa=verdict.get("title_fa", ""), summary_fa=verdict.get("summary_fa", ""),
                         engine=verdict.get("engine"))
            print("  • [%2d%s] %s" % (verdict["score"], " ✓" if verdict["post"] else " ✗", it["title"][:70]))
        else:
            print("  • [??] بدو‌ن نظر AI: %s" % it["title"][:70])
        db["items"][it["id"]] = entry

    # 3) انتخاب و انتشار
    ready = [x for x in db["items"].values()
             if not x.get("posted") and x.get("post") and (x.get("score") or 0) >= conf.get("min_score", 7)]
    ready.sort(key=lambda x: (-(x.get("score") or 0), x.get("published") or ""))
    selected = ready[:conf.get("max_posts_per_run", 3)]

    if not selected:
        print("خبر واجد شرایطی برای انتشار نیست (آستانه: %s)." % conf.get("min_score", 7))
    elif args.dry_run:
        print("\n----- پیش‌نمایش پست اخبار (ارسال نشد) -----")
        print(build_post(selected, conf))
        print("-------------------------------------------\n")
    else:
        chat, _src = tb.resolve_chat()
        if not chat:
            print(tb.NEED_SETUP + ": کانالی برای انتشار پیدا نشد.")
        else:
            text = build_post(selected, conf)
            photo = "%s/%s" % (content.SITE.rstrip("/"), conf.get("cover_image", "").lstrip("/"))
            if len(text) <= 1024 and conf.get("cover_image"):
                r = tb.api("sendPhoto", {"chat_id": chat, "photo": photo, "caption": text,
                                         "parse_mode": "HTML", "reply_markup": content.CHANNEL_BUTTONS})
            else:
                r = tb.api("sendMessage", {"chat_id": chat, "text": text,
                                           "parse_mode": "HTML", "reply_markup": content.CHANNEL_BUTTONS,
                                           "disable_web_page_preview": True})
            if r.get("ok"):
                mid = r["result"]["message_id"]
                for it in selected:
                    it["posted"] = True
                    it["posted_at"] = now.isoformat()
                    it["message_id"] = mid
                print("[news] %d خبر در کانال منتشر شد ✔ message_id=%s" % (len(selected), mid))
            else:
                print("[news] ارسال ناموفق:", r.get("description"))

    db["runs"].append({"at": now.isoformat(), "feeds": len(conf["feeds"]), "new": len(new_items),
                       "posted": (0 if (args.dry_run or not selected) else len(selected))})
    db["runs"] = db["runs"][-60:]
    prune(db)
    save_json(DB_FILE, db)
    print("دیتابیس ذخیره شد: %s (%d آیتم)" % (os.path.relpath(DB_FILE), len(db["items"])))
    return 0


def main(argv=None):
    parser = argparse.ArgumentParser(description="اخبار و فراخوان‌های شمسه — بررسی با هوش مصنوعی")
    parser.add_argument("--dry-run", action="store_true", help="بدون ارسال؛ فقط پیش‌نمایش")
    parser.add_argument("--limit", type=int, default=0, help="حداکثر خبر برای بررسی در این اجرا")
    parser.add_argument("--report", action="store_true", help="فقط وضعیت دیتابیس")
    return run(parser.parse_args(argv))


if __name__ == "__main__":
    sys.exit(main())
