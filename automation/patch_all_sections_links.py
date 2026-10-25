#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Ensure all sections in index.html (Header Nav, Branches, Reviews, Footer)
have comprehensive, working direct links to:
- restaurant_portal.html (with magic token)
- admin_panel.html (with auth bypass)
- shamse_sentiment_report.html
- All 4 deliverables (PDF, PPTX, MP3, Web)
- Google Maps reviews of both branches
- The new System Learning Infographic SVG
"""

def main():
    path = "/home/user/shamse-restaurant/index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Header Navigation Bar: Add Portal & Report links
    if 'href="restaurant_portal.html?token=SHAMSE-TAK-2026"' not in html.split('<header')[1].split('</header>')[0]:
        nav_target = '<a href="admin_panel.html" class="btn btn--ghost desk" style="font-size:.75rem;padding:6px 10px;border-color:#ffd21e;color:#ffd21e">⚙️ پنل مدیریت</a>'
        nav_replacement = """<a href="restaurant_portal.html?token=SHAMSE-TAK-2026" class="btn btn--gold desk" style="font-size:.75rem;padding:6px 10px">🍽 پرتال شمسه</a>
    <a href="shamse_sentiment_report.html" class="btn btn--ghost desk" style="font-size:.75rem;padding:6px 10px;border-color:#2ecc71;color:#2ecc71">🎙️ گزارش نقدها</a>
    <a href="admin_panel.html?auth=shamse2026" class="btn btn--ghost desk" style="font-size:.75rem;padding:6px 10px;border-color:#ffd21e;color:#ffd21e">⚙️ پنل مدیریت</a>"""
        html = html.replace(nav_target, nav_replacement)

    # 2. Branches Section: Enrich Branch 1 & Branch 2 CTA buttons
    old_b1_cta = """          <div class="branch__cta">
            <a class="btn btn--gold" href="#reserve" data-branch="taksim">رزرو در این شعبه</a>
            <a class="btn btn--line" href="https://www.google.com/maps/search/?api=1&amp;query=Shamse%20Restaurant%20Istiklal%20Caddesi%20No%3A179%20Beyoglu%20Istanbul" target="_blank" rel="noopener">مسیریابی در گوگل‌مپ</a>
          </div>"""
    new_b1_cta = """          <div class="branch__cta" style="flex-wrap:wrap;gap:8px">
            <a class="btn btn--gold" href="#reserve" data-branch="taksim">رزرو در این شعبه</a>
            <a class="btn btn--line" href="https://maps.google.com/?q=Istiklal+Caddesi+179+Beyoglu+Istanbul" target="_blank" rel="noopener">🗺️ نقدهای گوگل مپ (۴٫۸★ - ۲,۴۵۰ نقد)</a>
            <a class="btn btn--ghost" href="restaurant_portal.html?token=SHAMSE-TAK-2026" style="border-color:var(--copper);color:var(--copper)">🍽 پرتال شعبه استقلال</a>
          </div>"""
    if old_b1_cta in html:
        html = html.replace(old_b1_cta, new_b1_cta)

    old_b2_cta = """          <div class="branch__cta">
            <a class="btn btn--gold" href="#reserve" data-branch="kocatepe">رزرو در این شعبه</a>
            <a class="btn btn--line" href="https://www.google.com/maps/search/?api=1&amp;query=Abd%C3%BClhak%20Hamit%20Cd.%20No%3A17%20Kocatepe%20Beyoglu%20Istanbul" target="_blank" rel="noopener">مسیریابی در گوگل‌مپ</a>
          </div>"""
    new_b2_cta = """          <div class="branch__cta" style="flex-wrap:wrap;gap:8px">
            <a class="btn btn--gold" href="#reserve" data-branch="kocatepe">رزرو در این شعبه</a>
            <a class="btn btn--line" href="https://maps.google.com/?q=Abdulhak+Hamit+Caddesi+17+Kocatepe+Istanbul" target="_blank" rel="noopener">🗺️ نقدهای گوگل مپ (۴٫۷★ - ۱,۶۲۰ نقد)</a>
            <a class="btn btn--ghost" href="restaurant_portal.html?token=SHAMSE-TAK-2026" style="border-color:var(--copper);color:var(--copper)">🍽 پرتال شعبه کوجاتپه</a>
          </div>"""
    if old_b2_cta in html:
        html = html.replace(old_b2_cta, new_b2_cta)

    # 3. Reviews Section: Add Comprehensive Deliverables & Portal bar
    reviews_bar = """
    <!-- Reviews Section Comprehensive Links & Deliverables Bar -->
    <div class="rev" style="background:var(--ink-3);border:1.5px solid var(--line-copper);padding:20px;border-radius:6px;margin:24px 0">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:14px">
        <div>
          <span style="color:#ffd21e;font-weight:900;font-size:1.05rem">📦 دسترسی مستقیم به کلیه پرونده‌های ممیزی و پرتال شعبات شمسه:</span>
          <p style="font-size:.8rem;color:var(--muted);margin:3px 0 0">مشاهده تحلیل احساسات ۵,۰۵۵ نقد، دانلود گزارش‌ها، پرتال اختصاصی و نقدهای زنده شعبات</p>
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <a href="restaurant_portal.html?token=SHAMSE-TAK-2026" class="btn btn--gold" style="padding:6px 14px;font-size:.8rem">
            🍽 پرتال شمسه (ورود با توکن)
          </a>
          <a href="admin_panel.html?auth=shamse2026" class="btn btn--line" style="padding:6px 14px;font-size:.8rem;border-color:#ffd21e;color:#ffd21e">
            ⚙️ پنل ادمین
          </a>
        </div>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:10px">
        <a href="shamse_sentiment_report.html" target="_blank" class="btn btn--ghost" style="padding:10px 12px;font-size:.8rem;border-color:#2ecc71;color:#2ecc71;display:flex;align-items:center;justify-content:space-between">
          <span>🌐 پرونده وب و تحلیل احساسات</span> <span>↗</span>
        </a>
        <a href="reports/shamse_sentiment_podcast_report.pdf" download class="btn btn--ghost" style="padding:10px 12px;font-size:.8rem;display:flex;align-items:center;justify-content:space-between">
          <span>📄 دانلود گزارش کامل (PDF)</span> <span>⬇</span>
        </a>
        <a href="reports/mizban_restaurant_intelligence_pitch.pptx" download class="btn btn--ghost" style="padding:10px 12px;font-size:.8rem;display:flex;align-items:center;justify-content:space-between">
          <span>📊 اسلایدهای ارائه (PPTX)</span> <span>⬇</span>
        </a>
        <a href="assets/audio/shamse_intelligence_podcast.mp3" download class="btn btn--ghost" style="padding:10px 12px;font-size:.8rem;display:flex;align-items:center;justify-content:space-between">
          <span>🎙️ پادکست بریفینگ (MP3)</span> <span>⬇</span>
        </a>
        <a href="assets/img/shamse_system_learning_infographic.svg" target="_blank" class="btn btn--ghost" style="padding:10px 12px;font-size:.8rem;border-color:var(--copper);color:var(--copper);display:flex;align-items:center;justify-content:space-between">
          <span>🧠 اینفوگرافیک یادگیری سیستم</span> <span>↗</span>
        </a>
        <a href="https://maps.google.com/?q=Istiklal+Caddesi+179+Beyoglu+Istanbul" target="_blank" class="btn btn--ghost" style="padding:10px 12px;font-size:.8rem;display:flex;align-items:center;justify-content:space-between">
          <span>🗺️ نقدهای گوگل استقلال (۴٫۸★)</span> <span>↗</span>
        </a>
        <a href="https://maps.google.com/?q=Abdulhak+Hamit+Caddesi+17+Kocatepe+Istanbul" target="_blank" class="btn btn--ghost" style="padding:10px 12px;font-size:.8rem;display:flex;align-items:center;justify-content:space-between">
          <span>🗺️ نقدهای گوگل کوجاتپه (۴٫۷★)</span> <span>↗</span>
        </a>
      </div>
    </div>
"""
    if "Reviews Section Comprehensive Links & Deliverables Bar" not in html:
        rev_marker = '<!-- Multi-Platform Sentiment KPI Row -->'
        html = html.replace(rev_marker, reviews_bar + "\n\n    " + rev_marker)

    # 4. Footer: Add Management & Reports links under "دسترسی سریع"
    footer_flist_target = """      <h4>دسترسی سریع</h4>
      <ul class="flist">
        <li><a href="#home">صفحه اصلی</a></li>"""

    footer_flist_replacement = """      <h4>دسترسی سریع</h4>
      <ul class="flist">
        <li><a href="#home">صفحه اصلی</a></li>
        <li><a href="restaurant_portal.html?token=SHAMSE-TAK-2026" style="color:var(--copper);font-weight:bold">🍽 پرتال اختصاصی رستوران شمسه</a></li>
        <li><a href="admin_panel.html?auth=shamse2026" style="color:#ffd21e;font-weight:bold">⚙️ پیشخوان ادمین سیستم (WP-Admin)</a></li>
        <li><a href="shamse_sentiment_report.html" style="color:#2ecc71;font-weight:bold">🎙️ گزارش نقدها و پادکست (Web Dossier)</a></li>
        <li><a href="reports/shamse_sentiment_podcast_report.pdf" download style="color:#f8f8f8">📄 دانلود گزارش رسمی (PDF)</a></li>
        <li><a href="reports/mizban_restaurant_intelligence_pitch.pptx" download style="color:#f8f8f8">📊 پرزنتیشن هوش تجاری (PPTX)</a></li>
        <li><a href="assets/audio/shamse_intelligence_podcast.mp3" download style="color:#f8f8f8">🎙️ دانلود فایل صوتی پادکست (MP3)</a></li>
        <li><a href="assets/img/shamse_system_learning_infographic.svg" target="_blank" style="color:#2ecc71">🧠 اینفوگرافیک یادگیری سیستم (SVG)</a></li>"""

    if "🍽 پرتال اختصاصی رستوران شمسه" not in html:
        html = html.replace(footer_flist_target, footer_flist_replacement)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    print("Patched index.html with links across all sections successfully!")

if __name__ == "__main__":
    main()
