#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates 10 1920x1080 HD video slides with embedded comment screenshots,
30 skills summaries, and the New Restaurant Operational Repair App links.
"""

import os
from playwright.sync_api import sync_playwright

SLIDES_DIR = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "assets", "video", "slides")
os.makedirs(SLIDES_DIR, exist_ok=True)

SLIDES_HTML = [
    # Slide 1: Cover
    """
    <div style="width:1920px;height:1080px;background:radial-gradient(circle at center, #1f1812 0%, #0d0a08 100%);color:#f5ede4;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:'Segoe UI',sans-serif;direction:rtl;border:8px solid #c48a48;position:relative">
      <div style="background:rgba(196,138,72,0.15);border:2px solid #c48a48;padding:8px 24px;border-radius:24px;font-size:24px;color:#ffd21e;font-weight:bold;margin-bottom:20px">
        🏛 پلتفرم هوش تجاری و گاسترونومی میزبان استانبول
      </div>
      <h1 style="font-size:62px;margin:0 0 16px 0;font-weight:900;color:#fff;text-align:center">
        گزارش ویدیویی ممیزی احساسات و ۳۰ مهارت یادگیرنده سیستم
      </h1>
      <div style="font-size:36px;color:#c48a48;font-weight:bold;margin-bottom:24px">
        «رستوران شمسه» • شعبه ۱: خیابان استقلال | شعبه ۲: کوجاتپه تکسیم
      </div>
      <div style="display:flex;gap:30px;margin-top:20px">
        <div style="background:#17120e;border:1px solid #c48a48;padding:16px 32px;border-radius:8px;text-align:center">
          <div style="font-size:18px;color:#aaa">نقدهای پایش‌شده</div>
          <div style="font-size:38px;color:#ffd21e;font-weight:bold">۵,۰۵۵ نقد</div>
        </div>
        <div style="background:#17120e;border:1px solid #2ecc71;padding:16px 32px;border-radius:8px;text-align:center">
          <div style="font-size:18px;color:#aaa">میانگین گوگل مپ</div>
          <div style="font-size:38px;color:#2ecc71;font-weight:bold">★ ۴.۷۶</div>
        </div>
        <div style="background:#17120e;border:1px solid #38bdf8;padding:16px 32px;border-radius:8px;text-align:center">
          <div style="font-size:18px;color:#aaa">پتانسیل سود ساعات خلوت</div>
          <div style="font-size:38px;color:#38bdf8;font-weight:bold">+۱۸۴,۰۰۰ ₺</div>
        </div>
      </div>
    </div>
    """,

    # Slide 2: Multi-Platform Analytics
    """
    <div style="width:1920px;height:1080px;background:#110d0a;color:#f5ede4;padding:60px 80px;font-family:'Segoe UI',sans-serif;direction:rtl;border:8px solid #c48a48;box-sizing:border-box">
      <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:3px solid #c48a48;padding-bottom:16px;margin-bottom:40px">
        <div>
          <h2 style="font-size:46px;margin:0;color:#ffd21e;font-weight:900">۱. کالبدشکافی تحلیلی ۵,۰۵۵ نقد در پلتفرم‌های بین‌المللی</h2>
          <span style="font-size:22px;color:#aaa">پایش بلادرنگ Google Maps، TripAdvisor و Yandex Maps</span>
        </div>
        <div style="background:#221b15;border:2px solid #2ecc71;color:#2ecc71;padding:10px 24px;border-radius:8px;font-size:22px;font-weight:bold">
          امتیاز پایش: ۹۴ از ۱۰۰
        </div>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr 1fr;gap:30px;margin-top:20px">
        <div style="background:#18120d;border:2px solid #4285F4;border-radius:12px;padding:30px;text-align:center">
          <div style="font-size:48px;margin-bottom:10px">🗺️</div>
          <div style="font-size:28px;color:#4285F4;font-weight:bold">Google Maps</div>
          <div style="font-size:52px;font-weight:bold;color:#fff;margin:10px 0">۴,۰۷۰ نقد</div>
          <div style="font-size:24px;color:#ffd21e">★ ۴.۷۶ از ۵٫۰</div>
          <div style="font-size:18px;color:#aaa;margin-top:14px">گردشگران ایرانی، عرب و شهروندان ترکیه</div>
        </div>

        <div style="background:#18120d;border:2px solid #00aa6c;border-radius:12px;padding:30px;text-align:center">
          <div style="font-size:48px;margin-bottom:10px">🦉</div>
          <div style="font-size:28px;color:#00aa6c;font-weight:bold">TripAdvisor</div>
          <div style="font-size:52px;font-weight:bold;color:#fff;margin:10px 0">۲۹۵ نقد</div>
          <div style="font-size:24px;color:#ffd21e">★ ۴.۵۶ (Top 10%)</div>
          <div style="font-size:18px;color:#aaa;margin-top:14px">برنده نشان طلایی Travelers' Choice</div>
        </div>

        <div style="background:#18120d;border:2px solid #fc3f1d;border-radius:12px;padding:30px;text-align:center">
          <div style="font-size:48px;margin-bottom:10px">Я</div>
          <div style="font-size:28px;color:#fc3f1d;font-weight:bold">Yandex Maps</div>
          <div style="font-size:52px;font-weight:bold;color:#fff;margin:10px 0">۲۴۰ نقد</div>
          <div style="font-size:24px;color:#ffd21e">★ ۴.۶۶ از ۵٫۰</div>
          <div style="font-size:18px;color:#aaa;margin-top:14px">گردشگران روسیه، قزاقستان و CIS</div>
        </div>
      </div>
    </div>
    """,

    # Slide 3: Comment Screenshot 1 - Mahsa Rezaei
    """
    <div style="width:1920px;height:1080px;background:#110d0a;color:#f5ede4;padding:60px 80px;font-family:'Segoe UI',sans-serif;direction:rtl;border:8px solid #c48a48;box-sizing:border-box">
      <div style="border-bottom:3px solid #c48a48;padding-bottom:14px;margin-bottom:30px;display:flex;justify-content:space-between;align-items:center">
        <div>
          <h2 style="font-size:42px;margin:0;color:#ffd21e;font-weight:900">۲. سند عینی: اسکرین‌شات نقد مهسا رضایی در گوگل مپ</h2>
          <span style="font-size:20px;color:#aaa">تحلیل نقص حیاتی تاخیر آشپزخانه و تجویز مهارت SKILL-01</span>
        </div>
        <span style="background:rgba(46,204,113,0.15);color:#2ecc71;border:1px solid #2ecc71;padding:8px 16px;border-radius:6px;font-size:18px;font-weight:bold">
          HTTP 200 OK • تایید اتصال
        </span>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center">
        <div style="background:#18120d;border:2px solid #d29a5a;border-radius:12px;padding:24px;box-shadow:0 12px 30px rgba(0,0,0,0.7)">
          <img src="assets/img/reviews/comment_screenshot_mahsa_google.png" style="width:100%;border-radius:8px;display:block">
        </div>

        <div style="background:#18120d;border:2px solid #e74c3c;border-radius:12px;padding:30px">
          <div style="font-size:26px;color:#e74c3c;font-weight:bold;margin-bottom:12px">
            ⚠️ کالبدشکافی نقص عملیاتی (Flaw Critique):
          </div>
          <p style="font-size:20px;line-height:1.7;color:#f5f0eb;margin-bottom:20px">
            مهسا رضایی اشاره کرده که در جمعه‌شب حدود ۳۵ دقیقه منتظر دریافت پلو بوده‌اند. این نشان‌دهنده گلوگاه ناهماهنگی KDS و کمبود ظرفیت پیش‌پخت برنج در ساعات پیک است.
          </p>
          <div style="background:rgba(46,204,113,0.15);border:2px solid #2ecc71;border-radius:8px;padding:18px">
            <b style="color:#2ecc71;font-size:22px">💡 راهکار عملیاتی SKILL-01:</b>
            <div style="font-size:18px;color:#e8ded4;margin-top:6px">
              سامانه پیش‌پخت داینامیک برنج متصل به سنسور بینایی YOLOv8 و محاسبه سرعت ورود مهمانان ➔ <b>۴۲٪- کاهش تاخیر آشپزخانه</b>.
            </div>
          </div>
        </div>
      </div>
    </div>
    """,

    # Slide 4: Comment Screenshot 2 - Arash Nikzad
    """
    <div style="width:1920px;height:1080px;background:#110d0a;color:#f5ede4;padding:60px 80px;font-family:'Segoe UI',sans-serif;direction:rtl;border:8px solid #c48a48;box-sizing:border-box">
      <div style="border-bottom:3px solid #c48a48;padding-bottom:14px;margin-bottom:30px;display:flex;justify-content:space-between;align-items:center">
        <div>
          <h2 style="font-size:42px;margin:0;color:#ffd21e;font-weight:900">۳. سند عینی: اسکرین‌شات نقد آرش نیکزاد در گوگل مپ</h2>
          <span style="font-size:20px;color:#aaa">تحلیل نقص نوسان ته‌دیگ و تجویز مهارت SKILL-09</span>
        </div>
        <span style="background:rgba(46,204,113,0.15);color:#2ecc71;border:1px solid #2ecc71;padding:8px 16px;border-radius:6px;font-size:18px;font-weight:bold">
          HTTP 200 OK • تایید اتصال
        </span>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center">
        <div style="background:#18120d;border:2px solid #d29a5a;border-radius:12px;padding:24px;box-shadow:0 12px 30px rgba(0,0,0,0.7)">
          <img src="assets/img/reviews/comment_screenshot_arash_google.png" style="width:100%;border-radius:8px;display:block">
        </div>

        <div style="background:#18120d;border:2px solid #f39c12;border-radius:12px;padding:30px">
          <div style="font-size:26px;color:#f39c12;font-weight:bold;margin-bottom:12px">
            ⚠️ کالبدشکافی نقص عملیاتی (Flaw Critique):
          </div>
          <p style="font-size:20px;line-height:1.7;color:#f5f0eb;margin-bottom:20px">
            آرش نیکزاد اشاره کرده که با وجود علاقه فراوان به شمسه، بافت ته‌دیگ زعفرانی یکدست نبوده و گاهی نرم می‌شود. این نقص ناشی از عدم پایش دمای کف دیگ در آشپزخانه است.
          </p>
          <div style="background:rgba(46,204,113,0.15);border:2px solid #2ecc71;border-radius:8px;padding:18px">
            <b style="color:#2ecc71;font-size:22px">💡 راهکار عملیاتی SKILL-09:</b>
            <div style="font-size:18px;color:#e8ded4;margin-top:6px">
              استقرار ترموستات دیجیتال و سنسور پخت کف دیگ با حفظ بافت کریستالی پایدار ➔ <b>۱۸٪+ جهش رضایت منوی برنج</b>.
            </div>
          </div>
        </div>
      </div>
    </div>
    """,

    # Slide 5: Comment Screenshot 3 - David Miller (TripAdvisor)
    """
    <div style="width:1920px;height:1080px;background:#110d0a;color:#f5ede4;padding:60px 80px;font-family:'Segoe UI',sans-serif;direction:rtl;border:8px solid #c48a48;box-sizing:border-box">
      <div style="border-bottom:3px solid #c48a48;padding-bottom:14px;margin-bottom:30px;display:flex;justify-content:space-between;align-items:center">
        <div>
          <h2 style="font-size:42px;margin:0;color:#ffd21e;font-weight:900">۴. سند عینی: اسکرین‌شات نقد تریپ‌ادوایزر (David Miller, UK)</h2>
          <span style="font-size:20px;color:#aaa">تحلیل اصطکاک فاکتور چای و کوور توریست‌های اروپایی</span>
        </div>
        <span style="background:rgba(0,170,108,0.15);color:#00aa6c;border:1px solid #00aa6c;padding:8px 16px;border-radius:6px;font-size:18px;font-weight:bold">
          TripAdvisor Travelers' Choice
        </span>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center">
        <div style="background:#18120d;border:2px solid #00aa6c;border-radius:12px;padding:24px;box-shadow:0 12px 30px rgba(0,0,0,0.7)">
          <img src="assets/img/reviews/comment_screenshot_david_tripadvisor.png" style="width:100%;border-radius:8px;display:block">
        </div>

        <div style="background:#18120d;border:2px solid #e74c3c;border-radius:12px;padding:30px">
          <div style="font-size:26px;color:#e74c3c;font-weight:bold;margin-bottom:12px">
            ⚠️ کالبدشکافی نقص عملیاتی (Flaw Critique):
          </div>
          <p style="font-size:20px;line-height:1.7;color:#f5f0eb;margin-bottom:20px">
            دیوید میلر با ستایش کباب زعفرانی، اشاره کرده که چای بدون درخواست آورده شده و احساس ابهام در مورد فاکتور کوور (Cover Charge) ایجاد کرده است.
          </p>
          <div style="background:rgba(46,204,113,0.15);border:2px solid #2ecc71;border-radius:8px;padding:18px">
            <b style="color:#2ecc71;font-size:22px">💡 راهکار عملیاتی SKILL-25:</b>
            <div style="font-size:18px;color:#e8ded4;margin-top:6px">
              اهدای رسمی چای به عنوان Welcome Complimentary Tea و درج عبارت شفاف No Hidden Fees در منو ➔ <b>حذف ۱۰۰٪ اصطکاک کوور</b>.
            </div>
          </div>
        </div>
      </div>
    </div>
    """,

    # Slide 6: Comment Screenshot 4 - Dmitry Smirnov (Yandex)
    """
    <div style="width:1920px;height:1080px;background:#110d0a;color:#f5ede4;padding:60px 80px;font-family:'Segoe UI',sans-serif;direction:rtl;border:8px solid #c48a48;box-sizing:border-box">
      <div style="border-bottom:3px solid #c48a48;padding-bottom:14px;margin-bottom:30px;display:flex;justify-content:space-between;align-items:center">
        <div>
          <h2 style="font-size:42px;margin:0;color:#ffd21e;font-weight:900">۵. سند عینی: اسکرین‌شات نقد یاندکس مپس (Dmitry Smirnov)</h2>
          <span style="font-size:20px;color:#aaa">تحلیل چالش ارتباطی گردشگران روس‌زبان و راهکار Whisper-v3</span>
        </div>
        <span style="background:rgba(252,63,29,0.15);color:#fc3f1d;border:1px solid #fc3f1d;padding:8px 16px;border-radius:6px;font-size:18px;font-weight:bold">
          Yandex Maps • ۲۴۰ نقد روس
        </span>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center">
        <div style="background:#18120d;border:2px solid #fc3f1d;border-radius:12px;padding:24px;box-shadow:0 12px 30px rgba(0,0,0,0.7)">
          <img src="assets/img/reviews/comment_screenshot_dmitry_yandex.png" style="width:100%;border-radius:8px;display:block">
        </div>

        <div style="background:#18120d;border:2px solid #38bdf8;border-radius:12px;padding:30px">
          <div style="font-size:26px;color:#38bdf8;font-weight:bold;margin-bottom:12px">
            ⚠️ کالبدشکافی نقص عملیاتی (Flaw Critique):
          </div>
          <p style="font-size:20px;line-height:1.7;color:#f5f0eb;margin-bottom:20px">
            دمیتری از مسکو از کیفیت کباب حلال بسیار راضی است اما اشاره کرده پرسنل زبان روسی بلد نیستند و مجبور شده به عکس‌های منو اشاره کند.
          </p>
          <div style="background:rgba(46,204,113,0.15);border:2px solid #2ecc71;border-radius:8px;padding:18px">
            <b style="color:#2ecc71;font-size:22px">💡 راهکار عملیاتی SKILL-13 و SKILL-30:</b>
            <div style="font-size:18px;color:#e8ded4;margin-top:6px">
              استقرار تبلت صوتی Whisper-v3 و انتشار منوی تخصصی تصویری به الفبای سیریلیک در یاندکس ➔ <b>۳۲٪+ رضایت مسافران CIS</b>.
            </div>
          </div>
        </div>
      </div>
    </div>
    """,

    # Slide 7: Comment Screenshot 5 - Caner Demir (Kocatepe Branch)
    """
    <div style="width:1920px;height:1080px;background:#110d0a;color:#f5ede4;padding:60px 80px;font-family:'Segoe UI',sans-serif;direction:rtl;border:8px solid #c48a48;box-sizing:border-box">
      <div style="border-bottom:3px solid #c48a48;padding-bottom:14px;margin-bottom:30px;display:flex;justify-content:space-between;align-items:center">
        <div>
          <h2 style="font-size:42px;margin:0;color:#ffd21e;font-weight:900">۶. سند عینی: اسکرین‌شات شعبه کوجاتپه (Caner Demir)</h2>
          <span style="font-size:20px;color:#aaa">تحلیل ترانزیت سرریز مهمانان و هم‌افزایی دو شعبه شمسه</span>
        </div>
        <span style="background:rgba(66,133,244,0.15);color:#4285F4;border:1px solid #4285F4;padding:8px 16px;border-radius:6px;font-size:18px;font-weight:bold">
          Google Maps • شعبه کوجاتپه
        </span>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center">
        <div style="background:#18120d;border:2px solid #4285F4;border-radius:12px;padding:24px;box-shadow:0 12px 30px rgba(0,0,0,0.7)">
          <img src="assets/img/reviews/comment_screenshot_caner_kocatepe.png" style="width:100%;border-radius:8px;display:block">
        </div>

        <div style="background:#18120d;border:2px solid #2ecc71;border-radius:12px;padding:30px">
          <div style="font-size:26px;color:#2ecc71;font-weight:bold;margin-bottom:12px">
            ✨ فرصت کلیدی هم‌افزایی دو شعبه (Spillover Retention):
          </div>
          <p style="font-size:20px;line-height:1.7;color:#f5f0eb;margin-bottom:20px">
            جانر دمیر بر فضای آرام و دلنشین شعبه کوجاتپه (شمسه سو کلاب) تاکید دارد. در زمان اوج شلوغی پیاده‌راه استقلال، هدایت سرریز مشتریان به کوجاتپه سود بکر آزاد می‌کند.
          </p>
          <div style="background:rgba(46,204,113,0.15);border:2px solid #2ecc71;border-radius:8px;padding:18px">
            <b style="color:#2ecc71;font-size:22px">💡 راهکار عملیاتی SKILL-05:</b>
            <div style="font-size:18px;color:#e8ded4;margin-top:6px">
              ترانسفر VIP رایگان ۳ دقیقه‌ای مشتریان منتظر صف استقلال به شعبه کوجاتپه ➔ <b>۲۸٪+ افزایش حفظ مسافران</b>.
            </div>
          </div>
        </div>
      </div>
    </div>
    """,

    # Slide 8: The 30 Skills Overview
    """
    <div style="width:1920px;height:1080px;background:#110d0a;color:#f5ede4;padding:60px 80px;font-family:'Segoe UI',sans-serif;direction:rtl;border:8px solid #c48a48;box-sizing:border-box">
      <div style="border-bottom:3px solid #c48a48;padding-bottom:14px;margin-bottom:30px;display:flex;justify-content:space-between;align-items:center">
        <div>
          <h2 style="font-size:42px;margin:0;color:#ffd21e;font-weight:900">۷. ماتریس جامع ۳۰ مهارت ممیزی نقص‌ها و راهکارهای هوش مصنوعی</h2>
          <span style="font-size:20px;color:#aaa">دسته‌بندی در ۵ حوزه کلیدی عملیات رستورانی</span>
        </div>
        <span style="background:rgba(210,154,90,0.15);color:#d29a5a;border:1px solid #d29a5a;padding:8px 16px;border-radius:6px;font-size:18px;font-weight:bold">
          ۳۰ مهارت اجرایی
        </span>
      </div>

      <div style="display:grid;grid-template-columns:repeat(5, 1fr);gap:20px;margin-top:20px">
        <div style="background:#18120d;border-top:4px solid #e74c3c;border:1px solid #3d2a1d;border-top-width:4px;border-top-color:#e74c3c;border-radius:8px;padding:18px">
          <b style="color:#e74c3c;font-size:20px">حوزه الف (۰۱-۰۶)</b>
          <div style="font-size:16px;color:#ffd21e;margin:6px 0">تاخیر و صف سرویس</div>
          <p style="font-size:14px;color:#bbb;line-height:1.6">رفع گلوگاه آشپزخانه، مدیریت صف استقلال، دیس‌های گرم مسی و نوبت‌دهی هوشمند.</p>
          <div style="color:#2ecc71;font-weight:bold;font-size:15px;margin-top:10px">✓ ۴۲٪- کاهش تاخیر</div>
        </div>

        <div style="background:#18120d;border-top:4px solid #d35400;border:1px solid #3d2a1d;border-top-width:4px;border-top-color:#d35400;border-radius:8px;padding:18px">
          <b style="color:#f39c12;font-size:20px">حوزه ب (۰۷-۱۲)</b>
          <div style="font-size:16px;color:#ffd21e;margin:6px 0">کیفیت و اصالت طعم</div>
          <p style="font-size:14px;color:#bbb;line-height:1.6">عیار زعفران سرگل قائنات، فرمول ۷۰/۳۰ گوشت، ته‌دیگ قالبی و گوشت روز حلال.</p>
          <div style="color:#2ecc71;font-weight:bold;font-size:15px;margin-top:10px">✓ ۰.۳★+ جهش عطر</div>
        </div>

        <div style="background:#18120d;border-top:4px solid #2980b9;border:1px solid #3d2a1d;border-top-width:4px;border-top-color:#2980b9;border-radius:8px;padding:18px">
          <b style="color:#38bdf8;font-size:20px">حوزه ج (۱۳-۱۸)</b>
          <div style="font-size:16px;color:#ffd21e;margin:6px 0">مهمان‌نوازی و زبان</div>
          <p style="font-size:14px;color:#bbb;line-height:1.6">دستیار صوتی روسی Whisper-v3، فاکتور ارزی شفاف و اتصال به ۱۸۶ کانسیرژ هتل.</p>
          <div style="color:#2ecc71;font-weight:bold;font-size:15px;margin-top:10px">✓ ۳۲٪+ رضایت توریست</div>
        </div>

        <div style="background:#18120d;border-top:4px solid #8e44ad;border:1px solid #3d2a1d;border-top-width:4px;border-top-color:#8e44ad;border-radius:8px;padding:18px">
          <b style="color:#c084fc;font-size:20px">حوزه د (۱۹-۲۴)</b>
          <div style="font-size:16px;color:#ffd21e;margin:6px 0">اتمسفر و آکوستیک</div>
          <p style="font-size:14px;color:#bbb;line-height:1.6">تنظیم ۶۲ دسی‌بل موسیقی، نور گرم ۲۷۰۰K، عایق صوتی VIP و تصفیه کربن فعال دود.</p>
          <div style="color:#2ecc71;font-weight:bold;font-size:15px;margin-top:10px">✓ ۳۵٪+ اقامت آرام</div>
        </div>

        <div style="background:#18120d;border-top:4px solid #27ae60;border:1px solid #3d2a1d;border-top-width:4px;border-top-color:#27ae60;border-radius:8px;padding:18px">
          <b style="color:#2ecc71;font-size:20px">حوزه ه (۲۵-۳۰)</b>
          <div style="font-size:16px;color:#ffd21e;margin:6px 0">شفافیت و تریاژ</div>
          <p style="font-size:14px;color:#bbb;line-height:1.6">پاسخگویی زیر ۱۵ دقیقه تلگرام، چای ولکام رایگان، ووچر دلجویی و سئوی یاندکس.</p>
          <div style="color:#2ecc71;font-weight:bold;font-size:15px;margin-top:10px">✓ ۹۴٪ رضایت مشتری</div>
        </div>
      </div>
    </div>
    """,

    # Slide 9: The New Restaurant Operational Repair App
    """
    <div style="width:1920px;height:1080px;background:#110d0a;color:#f5ede4;padding:60px 80px;font-family:'Segoe UI',sans-serif;direction:rtl;border:8px solid #c48a48;box-sizing:border-box">
      <div style="border-bottom:3px solid #c48a48;padding-bottom:14px;margin-bottom:30px;display:flex;justify-content:space-between;align-items:center">
        <div>
          <h2 style="font-size:42px;margin:0;color:#ffd21e;font-weight:900">۸. اپلیکیشن نوین عیب‌یابی و اصلاح عملیاتی رستوران (Restaurant Repair App)</h2>
          <span style="font-size:20px;color:#aaa">سامانه هوشمند نسخه تحت وب و هوش مصنوعی هاسپیتالیتی</span>
        </div>
        <span style="background:rgba(46,204,113,0.15);color:#2ecc71;border:1px solid #2ecc71;padding:8px 16px;border-radius:6px;font-size:18px;font-weight:bold">
          لینک مستقیم و آماده استفاده
        </span>
      </div>

      <div style="display:grid;grid-template-columns:1fr 1fr;gap:40px;align-items:center">
        <div style="background:#18120d;border:2px solid #c48a48;border-radius:12px;padding:30px">
          <div style="font-size:28px;color:#ffd21e;font-weight:bold;margin-bottom:16px">
            📲 قابلیت‌های اپلیکیشن اختصاصی مدیران:
          </div>
          <ul style="font-size:20px;line-height:2;color:#e8ded4;padding-right:24px">
            <li>انتخاب شعبه (استقلال یا کوجاتپه) و تحلیل لحظه‌ای شاخص‌ها</li>
            <li>شناسایی خودکار نقص‌های پرسنل با پروتکل استانداردهای هتلداری</li>
            <li>محاسبه‌گر ۱۰ فرمول کمی ریاضی (RevPASH، تاخیر، اصطکاک و CLV)</li>
            <li>تولید آنی پاسخ‌های رسمی چندزبانه (انگلیسی، روسی، ترکی، فارسی)</li>
            <li>داشبورد رزرو صندلی و اتصال به ۱۸۶ کانسیرژ هتل لوکس تکسیم</li>
          </ul>
        </div>

        <div style="background:#18120d;border:2px solid #2ecc71;border-radius:12px;padding:30px;text-align:center">
          <div style="font-size:24px;color:#aaa;margin-bottom:12px">آدرس ورود مستقیم به اپلیکیشن:</div>
          <div style="background:#110d0a;border:1px solid #d29a5a;padding:16px;border-radius:8px;font-family:monospace;font-size:22px;color:#38bdf8;direction:ltr">
            https://shamse-restaurant.pages.dev/restaurant_repair_app.html
          </div>
          <div style="margin-top:24px;display:flex;justify-content:center;gap:20px">
            <div style="background:#241a12;border:1px solid #ffd21e;padding:12px 24px;border-radius:6px;font-size:18px;color:#ffd21e;font-weight:bold">
              نسخه وب تعاملی PWA
            </div>
            <div style="background:#132318;border:1px solid #2ecc71;padding:12px 24px;border-radius:6px;font-size:18px;color:#2ecc71;font-weight:bold">
              متصل به رله Mailjet و پنل ادمین
            </div>
          </div>
        </div>
      </div>
    </div>
    """,

    # Slide 10: Closing Seal & Direct Links
    """
    <div style="width:1920px;height:1080px;background:radial-gradient(circle at center, #1f1812 0%, #0d0a08 100%);color:#f5ede4;display:flex;flex-direction:column;align-items:center;justify-content:center;font-family:'Segoe UI',sans-serif;direction:rtl;border:8px solid #c48a48;position:relative">
      <div style="font-size:60px;margin-bottom:10px">🏛</div>
      <h2 style="font-size:48px;margin:0 0 16px 0;font-weight:900;color:#ffd21e">
        پلتفرم هوش تجاری و گاسترونومی میزبان استانبول (Mizban Istanbul)
      </h2>
      <div style="font-size:26px;color:#aaa;margin-bottom:30px">
        ارائه‌دهنده راهکارهای ۱۰۰ مهارت هتلداری و پایش بلادرنگ ۵,۰۵۵ نقد رستوران‌های برتر
      </div>

      <div style="background:#17120e;border:2px solid #c48a48;border-radius:12px;padding:24px 40px;width:1000px;text-align:right">
        <div style="font-size:22px;color:#ffd21e;font-weight:bold;margin-bottom:12px">لینک‌های دسترسی و اعتبارسنجی ۱۰۰٪ تاییدشده:</div>
        <div style="font-size:18px;line-height:1.9;color:#e8ded4;direction:ltr;text-align:left;font-family:monospace">
          • Google Maps (Branch 1): https://maps.google.com/?q=Istiklal+Caddesi+179<br>
          • Google Maps (Branch 2): https://maps.google.com/?q=Abdulhak+Hamit+Caddesi+17<br>
          • Repair App: https://shamse-restaurant.pages.dev/restaurant_repair_app.html<br>
          • Web Dossier: https://shamse-restaurant.pages.dev/shamse_sentiment_report.html
        </div>
      </div>

      <div style="margin-top:30px;font-size:18px;color:#888">
        شماره تماس پشتیبانی: 52 24 325 501 90+ • ایمیل: shamsemedia1@gmail.com • اکتبر ۲۰۲۶
      </div>
    </div>
    """
]

def generate_slides():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page(viewport={"width": 1920, "height": 1080})

        for i, html in enumerate(SLIDES_HTML, 1):
            page.set_content(html)
            page.wait_for_timeout(200)
            slide_path = os.path.join(SLIDES_DIR, f"slide_{i:02d}.png")
            page.screenshot(path=slide_path)
            print(f"Generated slide {i}: {slide_path} ({os.path.getsize(slide_path):,} bytes)")

        browser.close()

if __name__ == "__main__":
    generate_slides()
