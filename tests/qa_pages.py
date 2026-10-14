#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
مجموعهٔ تست QA سایت شمسه (Playwright).

اجرا:
    python3 -m http.server 8080 --bind 0.0.0.0 --directory /home/user/shamse-restaurant &
    python3 tests/qa_pages.py            # یا: python3 tests/qa_pages.py https://shamse-restaurant.pages.dev/

پوشش: سرریز افقی ۳۲۰→۱۴۴۰، فونت Vazirmatn واقعی، صفر خطای کنسول، ناوبری و لینک‌های متقابل،
فیلتر/جست‌وجو/مرتب‌سازی و RSVP رویدادها، اعتبارسنجی فرم میزبانی، جداول صفحهٔ مارکتینگ،
فوتر همهٔ صفحات، لینک تلگرام، و خودکفایی preview.html.
"""
import sys
from playwright.sync_api import sync_playwright

BASE = (sys.argv[1] if len(sys.argv) > 1 else "http://127.0.0.1:8080/").rstrip("/") + "/"
WIDTHS = [1440, 1280, 1024, 901, 768, 390, 320]
PAGES = ["index.html", "marketing.html", "events.html"]
TG = "https://t.me/shamse_restaurant_bot"
CH = "https://t.me/shamse_restaurant"
report, fails = [], []


def ok(cond, label, extra=""):
    report.append(("PASS " if cond else "FAIL ") + label + ((" | " + str(extra)) if extra else ""))
    if not cond:
        fails.append(label)


with sync_playwright() as pw:
    browser = pw.chromium.launch()

    # ---------- A. layout / fonts / console ----------
    for page_name in PAGES:
        for w in WIDTHS:
            ctx = browser.new_context(viewport={"width": w, "height": 900}, device_scale_factor=1)
            page = ctx.new_page()
            errs = []
            page.on("pageerror", lambda e: errs.append("pageerror: %s" % e))
            page.on("console", lambda m: errs.append("console: %s" % m.text) if m.type == "error" else None)
            page.goto(BASE + page_name, wait_until="load")
            page.wait_for_timeout(450)
            sw, iw = page.evaluate("[document.documentElement.scrollWidth, window.innerWidth]")
            ok(sw <= iw + 1, "%s @%d no horizontal overflow" % (page_name, w), "scrollW=%d innerW=%d" % (sw, iw))
            fam = page.evaluate("getComputedStyle(document.querySelector('h1')).fontFamily")
            ok("Vazirmatn" in fam, "%s @%d h1 uses Vazirmatn" % (page_name, w), fam[:40])
            if w == 1440:
                ok(bool(page.evaluate("document.fonts.check('700 32px Vazirmatn')")),
                   "%s font loaded" % page_name)
                widths = page.evaluate("""() => {
                  const c=document.createElement('canvas').getContext('2d');
                  const t='رستوران شمسه استانبول';
                  c.font='700 40px Vazirmatn'; const a=c.measureText(t).width;
                  c.font='700 40px Tahoma';    const b=c.measureText(t).width;
                  return [Math.round(a), Math.round(b)];
                }""")
                ok(widths[0] != widths[1], "%s webfont != fallback" % page_name,
                   "vazir=%s tahoma=%s" % tuple(widths))
            ok(not errs, "%s @%d 0 console errors" % (page_name, w), errs[:2])
            ctx.close()

    # ---------- B. nav wiring + cross links ----------
    page = browser.new_page(viewport={"width": 1440, "height": 900})
    page.goto(BASE + "index.html", wait_until="load")
    links = page.eval_on_selector_all("#nav a", "els => els.map(e => e.getAttribute('href'))")
    ok("events.html" in links and "marketing.html" in links, "index nav -> both new pages", links)
    vis = page.evaluate("""() => { const o={}; document.querySelectorAll('#nav .na-opt')
        .forEach(e => o[e.getAttribute('href')] = getComputedStyle(e).display); return o; }""")
    ok(all(v != "none" for v in vis.values()), "index @1440 shows optional nav items", vis)
    page.set_viewport_size({"width": 1200, "height": 900})
    page.wait_for_timeout(300)
    vis2 = page.evaluate("""() => { const o={}; document.querySelectorAll('#nav .na-opt')
        .forEach(e => o[e.getAttribute('href')] = getComputedStyle(e).display); return o; }""")
    ok(all(v == "none" for v in vis2.values()), "index @1200 hides optional nav items", vis2)
    page.set_viewport_size({"width": 1440, "height": 900})
    page.click('#nav a[href="events.html"]')
    page.wait_for_load_state("load")
    ok(page.url.endswith("events.html"), "nav click -> events.html")
    page.goto(BASE + "index.html", wait_until="load")
    top = page.eval_on_selector_all(".topbar a", "els => els.map(e=>e.getAttribute('href'))")
    foot = page.eval_on_selector_all(".footer a", "els => els.map(e=>e.getAttribute('href'))")
    ok("events.html" in top, "index topbar -> events.html")
    ok("events.html" in foot and "marketing.html" in foot, "index footer -> both new pages")
    page.close()

    # ---------- C. every page: footer + telegram ----------
    for pn in PAGES:
        pg = browser.new_page(viewport={"width": 1440, "height": 900})
        pg.goto(BASE + pn, wait_until="load")
        ok(pg.locator("footer.footer").count() == 1, "%s has footer" % pn)
        tg = pg.evaluate("(u) => document.querySelectorAll('a[href=\"' + u + '\"]').length", TG)
        ok(tg >= 2, "%s has >=2 telegram links" % pn, tg)
        ch = pg.evaluate("(u) => document.querySelectorAll('a[href=\"' + u + '\"]').length", CH)
        ok(ch >= 1, "%s links the public channel" % pn, ch)
        pg.close()

    for pn, want in (("events.html", ["index.html", "marketing.html"]),
                     ("marketing.html", ["index.html", "events.html"])):
        page = browser.new_page(viewport={"width": 1440, "height": 900})
        page.goto(BASE + pn, wait_until="load")
        hrefs = page.eval_on_selector_all("a", "els => els.map(e=>e.getAttribute('href'))")
        for w_ in want:
            ok(w_ in hrefs, "%s links back to %s" % (pn, w_))
        page.close()

    # ---------- D. events interactions ----------
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    errs = []
    page.on("pageerror", lambda e: errs.append(str(e)))
    page.goto(BASE + "events.html", wait_until="load")
    page.wait_for_timeout(400)
    ok(page.eval_on_selector_all("#eventsGrid .ev", "e => e.length") == 10, "events: 10 cards")
    ok(page.inner_text("#evCount") == "۱۰", "events: counter ۱۰", page.inner_text("#evCount"))
    page.click('.fchip[data-cat="book"]')
    page.wait_for_timeout(250)
    ok(page.eval_on_selector_all("#eventsGrid .ev:not(.hide)", "e => e.length") == 1, "events: book filter -> 1")
    page.click('.fchip[data-cat="all"]')
    page.wait_for_timeout(200)
    page.fill("#evSearch", "موسیقی")
    page.wait_for_timeout(300)
    ok(page.eval_on_selector_all("#eventsGrid .ev:not(.hide)", "e => e.length") == 1, "events: search -> 1")
    page.fill("#evSearch", "")
    page.wait_for_timeout(250)
    page.select_option("#evSort", "popular")
    page.wait_for_timeout(350)
    ok(page.eval_on_selector("#eventsGrid .ev .cnum", "e => e.dataset.base") == "48", "events: sort popular")
    page.select_option("#evSort", "date")
    page.wait_for_timeout(250)
    card = page.locator("#eventsGrid .ev").first
    title = card.locator("h3").inner_text()
    before = card.locator(".cnum").inner_text()
    card.locator(".rsvp").click()
    page.wait_for_timeout(200)
    after = card.locator(".cnum").inner_text()
    ok(before != after and "ثبت شد" in card.locator(".rsvp").inner_text(), "events: RSVP increments",
       "%s %s->%s" % (title, before, after))
    order = page.eval_on_selector_all("#eventsGrid .ev h3", "e => e.map(x => x.textContent)")
    page.reload(wait_until="load")
    page.wait_for_timeout(600)
    ok(page.eval_on_selector_all("#eventsGrid .ev h3", "e => e.map(x => x.textContent)") == order,
       "events: date order restored")
    same = page.locator("#eventsGrid .ev", has_text=title).first
    ok(same.locator(".cnum").inner_text() == after and "ثبت شد" in same.locator(".rsvp").inner_text(),
       "events: RSVP persists after reload")
    page.click('#hostForm button[type="submit"]')
    page.wait_for_timeout(200)
    ok(page.eval_on_selector_all("#hostForm .field.bad", "e => e.length") == 4,
       "host form: 4 invalid fields flagged")
    page.fill("#hName", "شب شعر معاصر فارسی")
    page.fill("#hGroup", "باشگاه ادبی استانبول")
    page.fill("#hDate", "2026-11-20")
    page.select_option("#hTime", "۱۹:۰۰")
    page.click('#hostForm button[type="submit"]')
    page.wait_for_timeout(700)
    ok(page.locator("#hostForm .field.bad").count() == 0, "host form: valid after fill")
    ok(page.is_visible("#hostOk") and page.locator("#eventsGrid .ev.ev-created").count() == 1,
       "host form: card injected + success shown")
    ok(not errs, "events: 0 page errors", errs[:2])
    page.close()

    # ---------- E. marketing content ----------
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    page.goto(BASE + "marketing.html", wait_until="load")
    page.wait_for_timeout(400)
    ok(page.locator(".model").count() == 12, "marketing: 12 model cards")
    ok(page.locator(".ptable tbody tr").count() == 18, "marketing: 18 platform rows (incl. Telegram)",
       page.locator(".ptable tbody tr").count())
    ok(page.locator(".road .phase").count() == 3, "marketing: 3 roadmap phases")
    ok(page.locator(".cal tbody tr").count() == 7, "marketing: 7 calendar rows")
    ext = page.eval_on_selector_all(".ptable a, .src a", "els => els.map(e=>e.href)")
    ok(all(h.startswith("http") for h in ext) and len(ext) >= 18, "marketing: source links absolute", len(ext))
    page.close()

    # ---------- F. preview.html self-contained ----------
    page = browser.new_page(viewport={"width": 1440, "height": 1000})
    errs = []
    page.on("pageerror", lambda e: errs.append(str(e)))
    page.on("console", lambda m: errs.append(m.text) if m.type == "error" else None)
    page.goto(BASE + "preview.html", wait_until="load")
    page.wait_for_timeout(800)
    ok(bool(page.evaluate("document.fonts.check('700 32px Vazirmatn')")), "preview: font from data URI")
    ext = page.evaluate("""() => performance.getEntriesByType('resource').map(r => r.name)
        .filter(n => n.startsWith('http') && !n.startsWith('data:') && n !== location.href)""")
    ok(len(ext) == 0, "preview: zero external requests", ext[:3])
    ok(not errs, "preview: 0 console errors", errs[:2])
    page.close()
    browser.close()

print("\n".join(report))
print("\n===== %d checks, %d failures =====" % (len(report), len(fails)))
if fails:
    print("FAILED:", fails)
    sys.exit(1)
