#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Make the social presence general for Istanbul restaurant needs (Mizban Istanbul),
and ensure Shamse Restaurant has only ONE verified official account in it (@shamse.resturan).
"""

def update_index_html():
    path = "index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Topbar Socials: General for Istanbul restaurants (Mizban Istanbul)
    old_topbar_socials = """      <span class="socials">
        <a href="https://www.instagram.com/shamse.resturan" target="_blank" rel="noopener" aria-label="اینستاگرام">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.4A6.4 6.4 0 1018.4 12 6.4 6.4 0 0012 5.6zm0 10.6A4.2 4.2 0 1116.2 12 4.2 4.2 0 0112 16.2zm6.6-10.9a1.5 1.5 0 11-1.5-1.5 1.5 1.5 0 011.5 1.5z"/></svg>
        </a>
          <a href="https://t.me/shamse_restaurant_bot" target="_blank" rel="noopener" aria-label="تلگرام"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3l-3 14.1c-.2 1-.8 1.3-1.7.8l-4.6-3.4-2.2 2.1c-.2.2-.5.4-.9.4l.3-4.7 8.5-7.7c.4-.3-.1-.5-.6-.2L7.3 12.4 2.7 11c-1-.3-1-1 .2-1.5l17.5-6.8c.8-.3 1.6.2 1.5 1.6z"/></svg></a>
          <a href="https://t.me/shamse_restaurant" target="_blank" rel="noopener" aria-label="کانال تلگرام"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M3 10v4h3l5 4V6l-5 4H3zm13.5 2a4.5 4.5 0 00-2-3.7v7.4a4.5 4.5 0 002-3.7zM14 3v2.2a7 7 0 010 13.6V21a9 9 0 000-18z"/></svg></a>
        <a href="https://wa.me/905013252452" target="_blank" rel="noopener" aria-label="واتساپ">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1.1.1-1.8-.1-.4-.1-1-.3-1.7-.6-2.6-1.2-4.3-4-4.4-4.2-.1-.2-1-1.4-1-2.6s.6-1.8.9-2.1c.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.8c.1.2.1.4 0 .6l-.4.6c-.1.2-.3.3-.1.6.2.3.7 1.1 1.4 1.7.9.8 1.6 1 1.9 1.2.2.1.4.1.6-.1l.8-.9c.2-.2.4-.2.6-.1l1.7.9c.5.2.5.4.5.6s-.2.6-.2.6z"/></svg>
        </a>
      </span>"""

    new_topbar_socials = """      <span class="socials" title="رسانه‌های عمومی میزبان استانبول">
        <a href="https://www.instagram.com/mizbanistanbul" target="_blank" rel="noopener" aria-label="اینستاگرام میزبان استانبول" title="اینستاگرام میزبان استانبول (@mizbanistanbul)">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.4A6.4 6.4 0 1018.4 12 6.4 6.4 0 0012 5.6zm0 10.6A4.2 4.2 0 1116.2 12 4.2 4.2 0 0112 16.2zm6.6-10.9a1.5 1.5 0 11-1.5-1.5 1.5 1.5 0 011.5 1.5z"/></svg>
        </a>
        <a href="https://t.me/mizbanistanbul" target="_blank" rel="noopener" aria-label="کانال تلگرام میزبان استانبول" title="کانال تلگرام میزبان استانبول (@mizbanistanbul)">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3l-3 14.1c-.2 1-.8 1.3-1.7.8l-4.6-3.4-2.2 2.1c-.2.2-.5.4-.9.4l.3-4.7 8.5-7.7c.4-.3-.1-.5-.6-.2L7.3 12.4 2.7 11c-1-.3-1-1 .2-1.5l17.5-6.8c.8-.3 1.6.2 1.5 1.6z"/></svg>
        </a>
        <a href="https://wa.me/905013252452" target="_blank" rel="noopener" aria-label="واتساپ پشتیبانی و رزرواسیون" title="واتساپ رزرواسیون">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1.1.1-1.8-.1-.4-.1-1-.3-1.7-.6-2.6-1.2-4.3-4-4.4-4.2-.1-.2-1-1.4-1-2.6s.6-1.8.9-2.1c.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.8c.1.2.1.4 0 .6l-.4.6c-.1.2-.3.3-.1.6.2.3.7 1.1 1.4 1.7.9.8 1.6 1 1.9 1.2.2.1.4.1.6-.1l.8-.9c.2-.2.4-.2.6-.1l1.7.9c.5.2.5.4.5.6s-.2.6-.2.6z"/></svg>
        </a>
        <a href="https://youtube.com/@mizbanistanbul" target="_blank" rel="noopener" aria-label="یوتیوب میزبان استانبول" title="یوتیوب میزبان استانبول">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.6 7.2s-.2-1.4-.8-2c-.8-.8-1.7-.8-2.1-.9C16.2 4.1 12 4.1 12 4.1h0s-4.2 0-6.7.2c-.4.1-1.3.1-2.1.9-.6.6-.8 2-.8 2S2.2 8.8 2.2 10.5v1.6c0 1.6.2 3.3.2 3.3s.2 1.4.8 2c.8.8 1.8.8 2.2.9 1.6.1 6.6.2 6.6.2s4.2 0 6.7-.2c.4-.1 1.3-.1 2.1-.9.6-.6.8-2 .8-2s.2-1.6.2-3.3v-1.6c0-1.6-.2-3.3-.2-3.3zM10 14.6V8.9l5.3 2.9z"/></svg>
        </a>
      </span>"""

    if old_topbar_socials in html:
        html = html.replace(old_topbar_socials, new_topbar_socials)

    # 2. Branches: Add Shamse's ONLY single verified account
    old_b1_info = """            <li><span>🚶</span><span>۷ دقیقه با ماشین از میدان تکسیم؛ دسترسی پیاده از ایستگاه مترو استقلال</span></li>"""
    new_b1_info = """            <li><span>🚶</span><span>۷ دقیقه با ماشین از میدان تکسیم؛ دسترسی پیاده از ایستگاه مترو استقلال</span></li>
            <li><span>📸</span><span>تنها پیج رسمی اینستاگرام شمسه: <a href="https://www.instagram.com/shamse.resturan" target="_blank" rel="noopener" style="color:var(--copper);font-weight:bold" dir="ltr">@shamse.resturan</a></span></li>"""

    if old_b1_info in html and "تنها پیج رسمی اینستاگرام شمسه" not in html:
        html = html.replace(old_b1_info, new_b1_info)

    # 3. Contact Section: Platform socials + Shamse's ONLY verified account
    old_contact_socials = """          <li>
            <span class="ic"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3l-3 14.1c-.2 1-.8 1.3-1.7.8l-4.6-3.4-2.2 2.1c-.2.2-.5.4-.9.4l.3-4.7 8.5-7.7c.4-.3-.1-.5-.6-.2L7.3 12.4 2.7 11c-1-.3-1-1 .2-1.5l17.5-6.8c.8-.3 1.6.2 1.5 1.6z"/></svg></span>
            <span><b>تلگرام</b><a href="https://t.me/shamse_restaurant" target="_blank" rel="noopener" dir="ltr">کانال: @shamse_restaurant</a> · <a href="https://t.me/shamse_restaurant_bot" target="_blank" rel="noopener" dir="ltr">ربات: @shamse_restaurant_bot</a><br><small>منو، رویدادها و رزرو — پاسخ خودکار ۲۴ ساعته</small></span>
          </li>
        </ul>
        <div class="socials">
          <a href="https://www.instagram.com/shamse.resturan" target="_blank" rel="noopener" aria-label="اینستاگرام">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.4A6.4 6.4 0 1018.4 12 6.4 6.4 0 0012 5.6zm0 10.6A4.2 4.2 0 1116.2 12 4.2 4.2 0 0112 16.2zm6.6-10.9a1.5 1.5 0 11-1.5-1.5 1.5 1.5 0 011.5 1.5z"/></svg>
          </a>
          <a href="https://t.me/shamse_restaurant_bot" target="_blank" rel="noopener" aria-label="تلگرام"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3l-3 14.1c-.2 1-.8 1.3-1.7.8l-4.6-3.4-2.2 2.1c-.2.2-.5.4-.9.4l.3-4.7 8.5-7.7c.4-.3-.1-.5-.6-.2L7.3 12.4 2.7 11c-1-.3-1-1 .2-1.5l17.5-6.8c.8-.3 1.6.2 1.5 1.6z"/></svg></a>
          <a href="https://wa.me/905013252452" target="_blank" rel="noopener" aria-label="واتساپ">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1.1.1-1.8-.1-.4-.1-1-.3-1.7-.6-2.6-1.2-4.3-4-4.4-4.2-.1-.2-1-1.4-1-2.6s.6-1.8.9-2.1c.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.8c.1.2.1.4 0 .6l-.4.6c-.1.2-.3.3-.1.6.2.3.7 1.1 1.4 1.7.9.8 1.6 1 1.9 1.2.2.1.4.1.6-.1l.8-.9c.2-.2.4-.2.6-.1l1.7.9c.5.2.5.4.5.6s-.2.6-.2.6z"/></svg>
          </a>
          <a href="tel:+905013252452" aria-label="تماس تلفنی">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8c1.2 2.4 3.2 4.4 5.6 5.6l1.9-1.9c.3-.3.7-.4 1.1-.2 1.1.4 2.3.6 3.5.6.6 0 1 .4 1 1V19c0 .6-.4 1-1 1-8.3 0-15-6.7-15-15 0-.6.4-1 1-1h3.2c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.5.1.4 0 .8-.2 1.1L6.6 10.8z"/></svg>
          </a>
        </div>"""

    new_contact_socials = """          <li>
            <span class="ic"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3l-3 14.1c-.2 1-.8 1.3-1.7.8l-4.6-3.4-2.2 2.1c-.2.2-.5.4-.9.4l.3-4.7 8.5-7.7c.4-.3-.1-.5-.6-.2L7.3 12.4 2.7 11c-1-.3-1-1 .2-1.5l17.5-6.8c.8-.3 1.6.2 1.5 1.6z"/></svg></span>
            <span><b>تلگرام پلتفرم میزبان استانبول</b><a href="https://t.me/mizbanistanbul" target="_blank" rel="noopener" dir="ltr">کانال: @mizbanistanbul</a> · <a href="https://t.me/mizbanistanbul_bot" target="_blank" rel="noopener" dir="ltr">ربات: @mizbanistanbul_bot</a><br><small>پایش رویدادها، تخفیف‌ها و رزرواسیون رستوران‌های استانبول</small></span>
          </li>
          <li>
            <span class="ic"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.4A6.4 6.4 0 1018.4 12 6.4 6.4 0 0012 5.6zm0 10.6A4.2 4.2 0 1116.2 12 4.2 4.2 0 0112 16.2zm6.6-10.9a1.5 1.5 0 11-1.5-1.5 1.5 1.5 0 011.5 1.5z"/></svg></span>
            <span><b>تنها حساب رسمی رستوران شمسه</b><a href="https://www.instagram.com/shamse.resturan" target="_blank" rel="noopener" dir="ltr" style="color:var(--copper);font-weight:bold">اینستاگرام: @shamse.resturan</a><br><small>تنها حساب تاییدشده مجموعه شمسه در شبکه‌های اجتماعی</small></span>
          </li>
        </ul>
        <div class="socials" title="رسانه‌های عمومی میزبان استانبول">
          <a href="https://www.instagram.com/mizbanistanbul" target="_blank" rel="noopener" aria-label="اینستاگرام میزبان استانبول" title="اینستاگرام میزبان استانبول (@mizbanistanbul)">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.4A6.4 6.4 0 1018.4 12 6.4 6.4 0 0012 5.6zm0 10.6A4.2 4.2 0 1116.2 12 4.2 4.2 0 0112 16.2zm6.6-10.9a1.5 1.5 0 11-1.5-1.5 1.5 1.5 0 011.5 1.5z"/></svg>
          </a>
          <a href="https://t.me/mizbanistanbul" target="_blank" rel="noopener" aria-label="کانال تلگرام میزبان استانبول" title="کانال تلگرام میزبان استانبول (@mizbanistanbul)"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3l-3 14.1c-.2 1-.8 1.3-1.7.8l-4.6-3.4-2.2 2.1c-.2.2-.5.4-.9.4l.3-4.7 8.5-7.7c.4-.3-.1-.5-.6-.2L7.3 12.4 2.7 11c-1-.3-1-1 .2-1.5l17.5-6.8c.8-.3 1.6.2 1.5 1.6z"/></svg></a>
          <a href="https://wa.me/905013252452" target="_blank" rel="noopener" aria-label="واتساپ سراسری"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1.1.1-1.8-.1-.4-.1-1-.3-1.7-.6-2.6-1.2-4.3-4-4.4-4.2-.1-.2-1-1.4-1-2.6s.6-1.8.9-2.1c.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.8c.1.2.1.4 0 .6l-.4.6c-.1.2-.3.3-.1.6.2.3.7 1.1 1.4 1.7.9.8 1.6 1 1.9 1.2.2.1.4.1.6-.1l.8-.9c.2-.2.4-.2.6-.1l1.7.9c.5.2.5.4.5.6s-.2.6-.2.6z"/></svg></a>
          <a href="tel:+905013252452" aria-label="تماس تلفنی"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M6.6 10.8c1.2 2.4 3.2 4.4 5.6 5.6l1.9-1.9c.3-.3.7-.4 1.1-.2 1.1.4 2.3.6 3.5.6.6 0 1 .4 1 1V19c0 .6-.4 1-1 1-8.3 0-15-6.7-15-15 0-.6.4-1 1-1h3.2c.6 0 1 .4 1 1 0 1.2.2 2.4.6 3.5.1.4 0 .8-.2 1.1L6.6 10.8z"/></svg></a>
        </div>"""

    if old_contact_socials in html:
        html = html.replace(old_contact_socials, new_contact_socials)

    # 4. Footer Socials: General platform + Single Shamse account card
    old_footer_socials = """      <p><b>میزبان استانبول (Mizban Istanbul)؛</b> پلتفرم جامع معرفی رستوران‌های ایرانی، فارسی و افغانستانی، هوش تجاری گاسترونومی، مدیریت رویدادهای کلاب و فرانچایز در استانبول.</p>
      <div class="socials">
        <a href="https://www.instagram.com/shamse.resturan" target="_blank" rel="noopener" aria-label="اینستاگرام">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.4A6.4 6.4 0 1018.4 12 6.4 6.4 0 0012 5.6zm0 10.6A4.2 4.2 0 1116.2 12 4.2 4.2 0 0112 16.2zm6.6-10.9a1.5 1.5 0 11-1.5-1.5 1.5 1.5 0 011.5 1.5z"/></svg>
        </a>
          <a href="https://t.me/shamse_restaurant_bot" target="_blank" rel="noopener" aria-label="تلگرام"><svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3l-3 14.1c-.2 1-.8 1.3-1.7.8l-4.6-3.4-2.2 2.1c-.2.2-.5.4-.9.4l.3-4.7 8.5-7.7c.4-.3-.1-.5-.6-.2L7.3 12.4 2.7 11c-1-.3-1-1 .2-1.5l17.5-6.8c.8-.3 1.6.2 1.5 1.6z"/></svg></a>
        <a href="https://wa.me/905013252452" target="_blank" rel="noopener" aria-label="واتساپ">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1.1.1-1.8-.1-.4-.1-1-.3-1.7-.6-2.6-1.2-4.3-4-4.4-4.2-.1-.2-1-1.4-1-2.6s.6-1.8.9-2.1c.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.8c.1.2.1.4 0 .6l-.4.6c-.1.2-.3.3-.1.6.2.3.7 1.1 1.4 1.7.9.8 1.6 1 1.9 1.2.2.1.4.1.6-.1l.8-.9c.2-.2.4-.2.6-.1l1.7.9c.5.2.5.4.5.6s-.2.6-.2.6z"/></svg>
        </a>
        <a href="https://youtube.com/@shamse.resturan" target="_blank" rel="noopener" aria-label="یوتیوب">
          <svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.6 7.2s-.2-1.4-.8-2c-.8-.8-1.7-.8-2.1-.9C16.2 4.1 12 4.1 12 4.1h0s-4.2 0-6.7.2c-.4.1-1.3.1-2.1.9-.6.6-.8 2-.8 2S2.2 8.8 2.2 10.5v1.6c0 1.6.2 3.3.2 3.3s.2 1.4.8 2c.8.8 1.8.8 2.2.9 1.6.1 6.6.2 6.6.2s4.2 0 6.7-.2c.4-.1 1.3-.1 2.1-.9.6-.6.8-2 .8-2s.2-1.6.2-3.3v-1.6c0-1.6-.2-3.3-.2-3.3zM10 14.6V8.9l5.3 2.9z"/></svg>
        </a>
      </div>"""

    new_footer_socials = """      <p><b>میزبان استانبول (Mizban Istanbul)؛</b> پلتفرم جامع معرفی رستوران‌های ایرانی و شرقی، هوش تجاری گاسترونومی، مدیریت رویدادهای کلاب و فرانچایز در استانبول.</p>
      
      <!-- General Platform Socials for Istanbul Restaurants -->
      <div style="margin-top:14px">
        <span style="font-size:.78rem;color:var(--copper);display:block;margin-bottom:6px">رسانه‌های رسمی پلتفرم میزبان استانبول:</span>
        <div class="socials" style="margin-top:2px">
          <a href="https://www.instagram.com/mizbanistanbul" target="_blank" rel="noopener" aria-label="اینستاگرام میزبان استانبول" title="اینستاگرام @mizbanistanbul">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2.2c3.2 0 3.6 0 4.9.1 1.2.1 1.8.2 2.2.4.6.2 1 .5 1.4.9.4.4.7.8.9 1.4.2.4.4 1 .4 2.2.1 1.3.1 1.7.1 4.9s0 3.6-.1 4.9c-.1 1.2-.2 1.8-.4 2.2-.2.6-.5 1-.9 1.4-.4.4-.8.7-1.4.9-.4.2-1 .4-2.2.4-1.3.1-1.7.1-4.9.1s-3.6 0-4.9-.1c-1.2-.1-1.8-.2-2.2-.4-.6-.2-1-.5-1.4-.9-.4-.4-.7-.8-.9-1.4-.2-.4-.4-1-.4-2.2C2.2 15.6 2.2 15.2 2.2 12s0-3.6.1-4.9c.1-1.2.2-1.8.4-2.2.2-.6.5-1 .9-1.4.4-.4.8-.7 1.4-.9.4-.2 1-.4 2.2-.4C8.4 2.2 8.8 2.2 12 2.2zm0 3.4A6.4 6.4 0 1018.4 12 6.4 6.4 0 0012 5.6zm0 10.6A4.2 4.2 0 1116.2 12 4.2 4.2 0 0112 16.2zm6.6-10.9a1.5 1.5 0 11-1.5-1.5 1.5 1.5 0 011.5 1.5z"/></svg>
          </a>
          <a href="https://t.me/mizbanistanbul" target="_blank" rel="noopener" aria-label="کانال تلگرام میزبان استانبول" title="کانال @mizbanistanbul">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.9 4.3l-3 14.1c-.2 1-.8 1.3-1.7.8l-4.6-3.4-2.2 2.1c-.2.2-.5.4-.9.4l.3-4.7 8.5-7.7c.4-.3-.1-.5-.6-.2L7.3 12.4 2.7 11c-1-.3-1-1 .2-1.5l17.5-6.8c.8-.3 1.6.2 1.5 1.6z"/></svg>
          </a>
          <a href="https://wa.me/905013252452" target="_blank" rel="noopener" aria-label="واتساپ سراسری رزرواسیون" title="واتساپ رزرواسیون">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M12 2a10 10 0 00-8.6 15.1L2 22l5-1.3A10 10 0 1012 2zm5.3 14.1c-.2.6-1.3 1.2-1.8 1.2-.5.1-1.1.1-1.8-.1-.4-.1-1-.3-1.7-.6-2.6-1.2-4.3-4-4.4-4.2-.1-.2-1-1.4-1-2.6s.6-1.8.9-2.1c.2-.2.5-.3.7-.3h.5c.2 0 .4 0 .6.5l.8 1.8c.1.2.1.4 0 .6l-.4.6c-.1.2-.3.3-.1.6.2.3.7 1.1 1.4 1.7.9.8 1.6 1 1.9 1.2.2.1.4.1.6-.1l.8-.9c.2-.2.4-.2.6-.1l1.7.9c.5.2.5.4.5.6s-.2.6-.2.6z"/></svg>
          </a>
          <a href="https://youtube.com/@mizbanistanbul" target="_blank" rel="noopener" aria-label="یوتیوب میزبان استانبول" title="یوتیوب میزبان استانبول">
            <svg viewBox="0 0 24 24" fill="currentColor"><path d="M21.6 7.2s-.2-1.4-.8-2c-.8-.8-1.7-.8-2.1-.9C16.2 4.1 12 4.1 12 4.1h0s-4.2 0-6.7.2c-.4.1-1.3.1-2.1.9-.6.6-.8 2-.8 2S2.2 8.8 2.2 10.5v1.6c0 1.6.2 3.3.2 3.3s.2 1.4.8 2c.8.8 1.8.8 2.2.9 1.6.1 6.6.2 6.6.2s4.2 0 6.7-.2c.4-.1 1.3-.1 2.1-.9.6-.6.8-2 .8-2s.2-1.6.2-3.3v-1.6c0-1.6-.2-3.3-.2-3.3zM10 14.6V8.9l5.3 2.9z"/></svg>
          </a>
        </div>
      </div>

      <!-- Single Official Account for Shamse Restaurant -->
      <div style="margin-top:14px;background:rgba(210,154,90,0.08);border:1px solid rgba(210,154,90,0.25);padding:10px 14px;border-radius:4px">
        <span style="font-size:.76rem;color:var(--muted);display:block">تنها حساب رسمی رستوران شمسه در شبکه‌های اجتماعی:</span>
        <a href="https://www.instagram.com/shamse.resturan" target="_blank" rel="noopener" style="display:inline-flex;align-items:center;gap:6px;color:var(--copper);font-weight:bold;font-size:.82rem;margin-top:4px;text-decoration:none">
          <span>📷 اینستاگرام شمسه: @shamse.resturan</span> ↗
        </a>
      </div>"""

    if old_footer_socials in html:
        html = html.replace(old_footer_socials, new_footer_socials)

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated index.html socials successfully!")

def update_restaurants_html():
    path = "restaurants.html"
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # Replace top/footer general socials
    html = html.replace('https://www.instagram.com/shamse.resturan" target="_blank" rel="noopener" aria-label="اینستاگرام"', 'https://www.instagram.com/mizbanistanbul" target="_blank" rel="noopener" aria-label="اینستاگرام میزبان استانبول"')
    html = html.replace('https://t.me/shamse_restaurant_bot" target="_blank" rel="noopener" aria-label="تلگرام"', 'https://t.me/mizbanistanbul" target="_blank" rel="noopener" aria-label="تلگرام میزبان استانبول"')
    html = html.replace('<li><a href="https://t.me/shamse_restaurant_bot" target="_blank" rel="noopener" dir="ltr">@shamse_restaurant_bot</a> (تلگرام)</li>', '<li><a href="https://t.me/mizbanistanbul" target="_blank" rel="noopener" dir="ltr">@mizbanistanbul</a> (کانال تلگرام)</li>')
    html = html.replace('https://t.me/shamse_restaurant_bot" class="btn desk"', 'https://t.me/mizbanistanbul_bot" class="btn desk"')

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated restaurants.html socials successfully!")

def update_events_html():
    path = "events.html"
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace('https://www.instagram.com/shamse.resturan" target="_blank" rel="noopener" aria-label="اینستاگرام"', 'https://www.instagram.com/mizbanistanbul" target="_blank" rel="noopener" aria-label="اینستاگرام میزبان استانبول"')
    html = html.replace('https://t.me/shamse_restaurant" target="_blank" rel="noopener" aria-label="کانال تلگرام"', 'https://t.me/mizbanistanbul" target="_blank" rel="noopener" aria-label="کانال تلگرام میزبان استانبول"')
    html = html.replace('https://t.me/shamse_restaurant_bot" target="_blank" rel="noopener" aria-label="تلگرام"', 'https://t.me/mizbanistanbul_bot" target="_blank" rel="noopener" aria-label="ربات تلگرام"')
    html = html.replace('<li><a href="https://t.me/shamse_restaurant_bot" target="_blank" rel="noopener" dir="ltr">@shamse_restaurant_bot</a> (تلگرام)</li>', '<li><a href="https://t.me/mizbanistanbul" target="_blank" rel="noopener" dir="ltr">@mizbanistanbul</a> (تلگرام)</li>')

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated events.html socials successfully!")

def update_marketing_html():
    path = "marketing.html"
    if not os.path.exists(path):
        return
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    html = html.replace('https://www.instagram.com/shamse.resturan" target="_blank" rel="noopener" aria-label="اینستاگرام"', 'https://www.instagram.com/mizbanistanbul" target="_blank" rel="noopener" aria-label="اینستاگرام میزبان استانبول"')
    html = html.replace('https://t.me/shamse_restaurant" target="_blank" rel="noopener" aria-label="کانال تلگرام"', 'https://t.me/mizbanistanbul" target="_blank" rel="noopener" aria-label="کانال تلگرام میزبان استانبول"')
    html = html.replace('https://t.me/shamse_restaurant_bot" target="_blank" rel="noopener" aria-label="تلگرام"', 'https://t.me/mizbanistanbul_bot" target="_blank" rel="noopener" aria-label="ربات تلگرام"')
    html = html.replace('<li><a href="https://t.me/shamse_restaurant_bot" target="_blank" rel="noopener" dir="ltr">@shamse_restaurant_bot</a> (تلگرام)</li>', '<li><a href="https://t.me/mizbanistanbul" target="_blank" rel="noopener" dir="ltr">@mizbanistanbul</a> (تلگرام)</li>')

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Updated marketing.html socials successfully!")

import os

if __name__ == "__main__":
    update_index_html()
    update_restaurants_html()
    update_events_html()
    update_marketing_html()
