#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
تست‌های آفلاین موتور اخبار شمسه (بدون نیاز به شبکه یا توکن).

اجرا:  python3 tests/test_news.py
"""
import datetime as dt
import json
import os
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import content      # noqa: E402
import news         # noqa: E402
import telegram_bot as tb  # noqa: E402

checks, fails = [], []


def ok(cond, label, extra=""):
    checks.append(("PASS " if cond else "FAIL ") + label + ((" | " + str(extra)) if extra else ""))
    if not cond:
        fails.append(label)


# ---------------------------------------------------------------- 1) feed parsing
SAMPLE_RSS = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0"><channel>
  <item>
    <title>İstanbul Kültür Yolu Festivali'nde 200 lezzet durağı</title>
    <link>https://example.com/news/1</link>
    <pubDate>Mon, 13 Oct 2026 09:00:00 GMT</pubDate>
    <description><![CDATA[<p>Festival kapsamında <b>200</b> lezzet durağı tescillendi.</p>]]></description>
  </item>
  <item>
    <title>New Persian restaurant opens in Berlin</title>
    <link>https://example.com/news/2</link>
    <pubDate>Sun, 12 Oct 2026 08:00:00 GMT</pubDate>
    <description>Iranian cuisine grows in Europe.</description>
  </item>
</channel></rss>"""

items = news.parse_feed(SAMPLE_RSS)
ok(len(items) == 2, "parse_feed returns both items", len(items))
ok(items[0]["title"].startswith("İstanbul"), "title parsed", items[0]["title"][:40])
ok(items[0]["link"] == "https://example.com/news/1", "link parsed")
ok("<" not in items[0]["desc"] and "200" in items[0]["desc"], "html stripped from description", items[0]["desc"][:40])

ATOM = """<?xml version="1.0"?>
<feed xmlns="http://www.w3.org/2005/Atom">
  <entry><title>Istanbul food festival</title><link href="https://example.com/a/1"/>
  <updated>2026-10-13T10:00:00Z</updated><summary>Food festival news.</summary></entry>
</feed>"""
ok(len(news.parse_feed(ATOM)) == 1, "atom feed parsed")

# ---------------------------------------------------------------- 2) dates + ids
d1 = news.parse_date("Mon, 13 Oct 2026 09:00:00 GMT")
d2 = news.parse_date("2026-10-13T10:00:00Z")
ok(d1 and d1.year == 2026 and d1.tzinfo, "rfc822 date parsed with tz")
ok(d2 and d2.tzinfo, "iso date parsed with tz")
ok(news.parse_date("garbage") is None, "bad date -> None")
ok(news.item_id("https://a", "t") == news.item_id("https://a", "t"), "item_id stable")
ok(len(news.item_id("https://a", "t")) == 16, "item_id length 16")

# ---------------------------------------------------------------- 3) AI JSON safety
ok(news.parse_ai_json('{"score": 8, "post": true, "title_fa": "خبر", "summary_fa": "خلاصه"}')["score"] == 8,
   "plain JSON accepted")
wrapped = news.parse_ai_json('Sure! Here you go:\n```json\n{"score": 12, "post": true, "title_fa": "الف", "summary_fa": "ب"}\n```')
ok(wrapped and wrapped["score"] == 10, "score clamped to 10", wrapped and wrapped["score"])
low = news.parse_ai_json('{"score": -3, "post": false}')
ok(low and low["score"] == 0, "score clamped to 0")
ok(news.parse_ai_json("no json at all") is None, "garbage -> None")
ok(news.parse_ai_json('{"post": true}') is None, "missing score -> None")
default_post = news.parse_ai_json('{"score": 8, "title_fa": "x", "summary_fa": "y"}')
ok(default_post and default_post["post"] is True, "post defaults from score")

# ---------------------------------------------------------------- 4) collect_new (dedupe + age + limit)
conf = {"max_age_days": 14}
now = dt.datetime(2026, 10, 14, tzinfo=dt.timezone.utc)
first = news.item_id("https://example.com/news/1", items[0]["title"])
db = {"items": {first: {"id": first, "score": 8}}}          # بررسی‌شده → هرگز تکرار نشود
flat = list(items) + [{"title": "Old news", "link": "https://example.com/old", "pub": "Mon, 01 Jan 2024 00:00:00 GMT",
                       "desc": ""}]
new = news.collect_new(conf, db, flat, now, limit=10)
ok(len(new) == 1 and new[0]["link"] == "https://example.com/news/2", "dedupe + age filter", [x["link"] for x in new])
ok(len(news.collect_new(conf, db, flat, now, limit=1)) == 1, "limit respected")
# آیتم بررسی‌نشده (score=None) باید برگردد تا هوش مصنوعی دوباره امتحان کند
db2 = {"items": {first: {"id": first, "score": None}}}
retried = news.collect_new(conf, db2, items, now, limit=10)
ok(first in [x["id"] for x in retried], "unjudged items are retried", len(retried))
# نویز آشکار به هوش مصنوعی نمی‌رود
noise = [{"title": "Heavy rain and flooding in Istanbul", "link": "https://example.com/flood",
          "pub": "Mon, 13 Oct 2026 09:00:00 GMT", "desc": ""}]
ok(news.collect_new(conf, {"items": {}}, noise, now, limit=10) == [], "obvious noise filtered before AI")
# خبر مرتبط بالاتر از خبر بی‌ربط اولویت می‌گیرد
mixed = noise + [{"title": "İstanbul gastronomi festivali", "link": "https://example.com/food",
                  "pub": "Mon, 13 Oct 2026 09:00:00 GMT", "desc": "lezzet"}]
ordered = news.collect_new(conf, {"items": {}}, mixed, now, limit=10)
ok(len(ordered) == 1 and ordered[0]["link"] == "https://example.com/food", "food hint sorts higher", ordered)
# اعتبارسنجی فارسی
ok(news.fa_text_ok("این یک متن فارسی است", 0.5) != "", "persian text accepted")
ok(news.fa_text_ok("english words only here", 0.5) == "", "non-persian text rejected")

# ---------------------------------------------------------------- 5) post composition
sel = [{"link": "https://example.com/news/2", "source": "Test Feed", "title": "T",
        "title_fa": "رستوران ایرانی <b>جدید</b>", "summary_fa": "خلاصهٔ خبر فارسی.", "score": 9}]
post = news.build_post(sel, conf)
ok("رستوران ایرانی" in post and "&lt;b&gt;" in post, "title escaped in HTML post")
ok("https://example.com/news/2" in post, "link included in post")
ok(content.SITE_LABEL in post and content.TAGS in post, "post has site + tags")
ok(content.FOOTER.strip() not in post, "channel news post uses its own compact footer")

# ---------------------------------------------------------------- 6) footer + buttons + caption fitting
ok("shamse-restaurant.pages.dev" in content.FOOTER and "@shamse_restaurant_bot" in content.FOOTER
   and "@shamse_restaurant" in content.FOOTER and content.PHONE in content.FOOTER,
   "post FOOTER has site + bot + channel + phone")
rows = content.CHANNEL_BUTTONS["inline_keyboard"]
ok(all("url" in b for row in rows for b in row), "channel buttons all have urls", len(rows))
ok(any(b["url"] == content.SITE for row in rows for b in row), "channel buttons link the site")
ok(any(b["url"].endswith("shamse_restaurant_bot") for row in rows for b in row), "channel buttons link the bot")
long_text = ("خبر " * 300) + content.FOOTER
fitted = tb.fit_caption("خط اول\n" + long_text)
ok(len(fitted) <= 1024, "fit_caption keeps caption <= 1024", len(fitted))
ok("shamse_restaurant_bot" in fitted, "fit_caption preserves the signature")
ok(len(tb.fit_caption("کوتاه")) == 5, "fit_caption leaves short text untouched")

# ---------------------------------------------------------------- 7) feed config sanity
conf_file = json.load(open(os.path.join(ROOT, "automation", "news_feeds.json"), encoding="utf-8"))
ok(len(conf_file["feeds"]) >= 5, "at least 5 feeds configured", len(conf_file["feeds"]))
ok(all(f["url"].startswith("https://") and f.get("cat") for f in conf_file["feeds"]), "every feed has https url + category")
ok(0 < conf_file["min_score"] <= 10, "min_score sane", conf_file["min_score"])

print("\n".join(checks))
print("\n===== %d checks, %d failures =====" % (len(checks), len(fails)))
if fails:
    print("FAILED:", fails)
    sys.exit(1)
