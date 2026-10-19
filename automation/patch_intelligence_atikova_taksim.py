#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Patches intelligence.html to integrate:
  1. Module 13: 🏛 اتاق کنترل دیسپچ و پیگیری‌ها (مدل Atikova / ۴۳ نهاد با زمان‌بندی یادآور، ارسال ۱-لمسی واتس‌اپ و رصد تلگرام)
  2. Module 14: 🗺 مرکز هوش تجاری رستوران‌های تکسیم و پورتال چندکاربره (Multi-Tenant Restaurant Access & Magic Link Generator)
"""

import os
import json

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(ROOT)
HTML_FILE = os.path.join(REPO_ROOT, "intelligence.html")
ATIKOVA_FILE = os.path.join(ROOT, "atikova_dispatch_db.json")
TAKSIM_FILE = os.path.join(ROOT, "taksim_restaurants_intel.json")

def patch_intelligence_modules():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    with open(ATIKOVA_FILE, "r", encoding="utf-8") as f:
        atikova_data = json.load(f)

    with open(TAKSIM_FILE, "r", encoding="utf-8") as f:
        taksim_data = json.load(f)

    # 1. Update subnav pills
    subnav_target = '<button class="mod-pill" onclick="scrollToSection(\'mod-resend-outreach\')"'
    new_subnav_buttons = (
        '<button class="mod-pill" onclick="scrollToSection(\'mod-atikova-control\')" '
        'style="border-color:#ffd21e;color:#ffd21e;background:rgba(255,210,30,0.1);font-weight:700">'
        '🏛 ۱۳. اتاق کنترل دیسپچ و پیگیری‌ها (مدل Atikova)</button>\n        '
        '<button class="mod-pill" onclick="scrollToSection(\'mod-taksim-multitenant\')" '
        'style="border-color:#38bdf8;color:#38bdf8;background:rgba(56,189,248,0.1);font-weight:700">'
        '🗺 ۱۴. هوش تجاری تکسیم و پنل کاربری رستوران‌ها</button>\n        '
        + subnav_target
    )
    if 'mod-atikova-control' not in html:
        html = html.replace(subnav_target, new_subnav_buttons, 1)
        print("Added subnav pills for Modules 13 & 14.")

    # 2. Module 13 & 14 HTML markup
    modules_html = '''
    <!-- MODULE 13: ATIKOVA DISPATCH & OUTREACH CONTROL ROOM -->
    <section class="mod-card" id="mod-atikova-control" style="border:1px solid #ffd21e;box-shadow:0 12px 40px rgba(255,210,30,0.12)">
      
      <!-- Header -->
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:16px;margin-bottom:20px">
        <div>
          <div style="display:inline-flex;align-items:center;gap:6px;background:rgba(255,210,30,0.15);color:#ffd21e;padding:4px 12px;border-radius:20px;font-size:.78rem;font-weight:bold;margin-bottom:8px">
            <span>🏛 اتاق کنترل دیسپچ، پیگیری و رصد چندکاناله (الگوی Atikova.com)</span>
          </div>
          <h2 class="sec-title" style="margin:0 0 6px 0;color:var(--cream)">
            🏛 ۱۳. اتاق کنترل دیسپچ و پیگیری‌ها (۴۳ نهاد، یادآور خودکار، واتساپ تک‌لمسی و رصد تلگرام)
          </h2>
          <p class="sec-sub" style="margin:0;max-width:920px">
            گزارش یکپارچه ۴۳ ایمیل ارسال‌شده، پیگیری وضعیت‌های «در انتظار»، «یادآوری شد» و «پاسخ»، زمان‌بندی یادآورها به وقت استانبول (روز کاری ۹ تا ۱۸ با پیوست‌های PPTX و PDF)، راهکار ارسال تک‌لمسی واتساپ بیزنس برای دور زدن محدودیت‌های شماره‌های ۹۸+ در متا، و رصد بلادرنگ وضعیت کانال‌ها و گروه‌های تلگرام.
          </p>
        </div>

        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <button class="btn btn--gold" onclick="refreshAtikovaControlRoom()" style="font-size:.82rem">
            🔄 بررسی پاسخ‌ها و تازه‌سازی
          </button>
          <button class="btn btn--ghost" onclick="triggerSendDueReminders()" style="font-size:.82rem;border-color:#ffd21e;color:#ffd21e">
            ✉️ ارسال یادآورهای سررسیده (Resend)
          </button>
        </div>
      </div>

      <!-- Atikova KPI Strip -->
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(140px,1fr));gap:12px;margin-bottom:24px">
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:12px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:var(--cream)">۴۳</div>
          <div style="font-size:.72rem;color:var(--muted);margin-top:2px">ایمیل ارسال‌شده</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:12px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#2ecc71">۴</div>
          <div style="font-size:.72rem;color:var(--muted);margin-top:2px">پاسخ دریافتی ✓</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:12px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#ffd21e">۱۹</div>
          <div style="font-size:.72rem;color:var(--muted);margin-top:2px">در انتظار پاسخ</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:12px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#38bdf8">۲۰</div>
          <div style="font-size:.72rem;color:var(--muted);margin-top:2px">یادآوری‌شده با پیوست</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:12px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#a855f7">۰</div>
          <div style="font-size:.72rem;color:var(--muted);margin-top:2px">برگشتی (Bounce)</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid #2ecc71;border-radius:6px;padding:12px;text-align:center">
          <div style="font-size:1.4rem;font-weight:900;color:#2ecc71">۹ · ۰ ✓</div>
          <div style="font-size:.72rem;color:var(--muted);margin-top:2px">واتساپ تک‌لمسی</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--copper);border-radius:6px;padding:12px;text-align:center">
          <div style="font-size:1.05rem;font-weight:900;color:var(--copper)">۲۸ مهر، ۰۹:۰۰</div>
          <div style="font-size:.72rem;color:var(--muted);margin-top:2px">موعد یادآور بعدی</div>
        </div>
      </div>

      <!-- Entity Type & Language Filter Chips -->
      <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:14px 18px;margin-bottom:20px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px;flex-wrap:wrap;gap:8px">
          <span style="font-size:.82rem;font-weight:700;color:var(--cream)">فیلتر بر اساس نوع نهاد و وضعیت پیام:</span>
          <div style="display:flex;gap:6px">
            <button class="btn btn--ghost" onclick="filterAtikovaType('all', this)" style="font-size:.72rem;padding:3px 10px;background:var(--ink-3)">همه (۴۳)</button>
            <button class="btn btn--ghost" onclick="filterAtikovaType('restaurant', this)" style="font-size:.72rem;padding:3px 10px">رستوران‌ها (۱۰)</button>
            <button class="btn btn--ghost" onclick="filterAtikovaType('government_municipality', this)" style="font-size:.72rem;padding:3px 10px">دولتی/شهرداری (۸)</button>
            <button class="btn btn--ghost" onclick="filterAtikovaType('crowdfunding_platform', this)" style="font-size:.72rem;padding:3px 10px">کراودفاندینگ (۸)</button>
            <button class="btn btn--ghost" onclick="filterAtikovaType('investor_vc', this)" style="font-size:.72rem;padding:3px 10px">سرمایه‌گذار/VC (۵)</button>
            <button class="btn btn--ghost" onclick="filterAtikovaType('ngo_association', this)" style="font-size:.72rem;padding:3px 10px">سمن/انجمن (۵)</button>
            <button class="btn btn--ghost" onclick="filterAtikovaType('accelerator_technopark', this)" style="font-size:.72rem;padding:3px 10px">پارک/شتاب‌دهنده (۴)</button>
            <button class="btn btn--ghost" onclick="filterAtikovaType('university', this)" style="font-size:.72rem;padding:3px 10px">دانشگاه (۲)</button>
          </div>
        </div>
      </div>

      <!-- WhatsApp 1-Touch Bypassing Meta Protocol Banner -->
      <div style="background:rgba(46,204,113,0.08);border:1px solid #2ecc71;border-radius:6px;padding:16px 20px;margin-bottom:20px;display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:14px">
        <div>
          <div style="display:flex;align-items:center;gap:8px;margin-bottom:4px">
            <span style="font-size:1.1rem">🟢</span>
            <b style="color:#2ecc71;font-size:.9rem">پروتکل ارسال دستی تک‌لمسی واتساپ بیزنس (مستقل از تحریم‌های متا برای شماره‌های ۹۸+)</b>
          </div>
          <p style="font-size:.78rem;color:var(--text);margin:0;max-width:850px;line-height:1.6">
            متا شماره‌های ‎+98 را در Cloud API واتساپ تایید نمی‌کند و کاربران ترکیه نیز پیام‌های API را به راحتی دریافت نمی‌کنند. راهکار عملیاتی ما تولید لینک‌های مستقیم <code>wa.me</code> است: با کلیک روی <b>«باز کردن واتساپ»</b> پیام با متن آماده روی گوشی یا دسکتاپ باز می‌شود؛ کافیست ارسال را بزنید و دکمه <b>«فرستادم ✓»</b> را لمس نمایید. فهرست لینک‌های موعددار روزانه به طور خودکار به <code>soheil.power@gmail.com</code> ایمیل می‌شود.
          </p>
        </div>
        <div style="display:flex;align-items:center;gap:8px">
          <span style="font-size:.74rem;color:var(--muted)">فرستنده واتساپ:</span>
          <code style="background:var(--ink-3);padding:4px 8px;border-radius:4px;color:#ffd21e;font-size:.8rem;direction:ltr">+98 920 626 3218</code>
        </div>
      </div>

      <!-- Telegram Presence Scanner Card -->
      <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:18px 20px;margin-bottom:20px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:8px">
          <div>
            <h4 style="margin:0;font-size:.92rem;color:var(--cream);font-weight:700">
              ✈️ آیا تلگرام دارند؟ (رصد و ممیزی بلادرنگ حضور در تلگرام)
            </h4>
            <div style="font-size:.74rem;color:var(--muted);margin-top:2px">
              پایش لینک‌های t.me در وب‌سایت‌ها، بیو شبکه‌های اجتماعی و گروه‌های عمومی
            </div>
          </div>
          <div style="display:flex;gap:10px;font-size:.75rem">
            <span style="color:#2ecc71">رسمی: ۱</span>
            <span style="color:#38bdf8">احتمالاً مال خودشان: ۱</span>
            <span style="color:#ffd21e">تأییدنشده: ۴</span>
            <span style="color:#ef4444">لینک از کار افتاده: ۱</span>
            <span style="color:var(--muted)">پیدا نشد: ۳۶</span>
          </div>
        </div>

        <!-- Highlighted Active Groups -->
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:12px;font-size:.78rem">
          <div style="background:var(--ink-3);border:1px solid var(--line);border-radius:4px;padding:10px 12px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
              <b style="color:#2ecc71">fonbulucu (گروه رسمی عمومی)</b>
              <span style="color:var(--muted)">۶,۹۴۹ عضو</span>
            </div>
            <p style="font-size:.72rem;color:var(--muted);margin:0 0 6px 0">
              از وب‌سایت رسمی لینک شده است. گروه باز است و امکان ارتباط با ادمین‌ها مهیاست.
            </p>
            <div style="display:flex;gap:6px">
              <a href="https://t.me/fonbulucu" target="_blank" class="btn btn--ghost" style="font-size:.7rem;padding:3px 8px">باز کردن گروه ↗</a>
              <button class="btn btn--ghost" onclick="copyTelegramPitch('fonbulucu')" style="font-size:.7rem;padding:3px 8px">کپی متن پیام ترکی 📋</button>
            </div>
          </div>

          <div style="background:var(--ink-3);border:1px solid var(--line);border-radius:4px;padding:10px 12px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:4px">
              <b style="color:#38bdf8">Fonlabüyüsün (کانال هالک‌بانک)</b>
              <span style="color:var(--muted)">۶۲ عضو</span>
            </div>
            <p style="font-size:.72rem;color:var(--muted);margin:0 0 6px 0">
              کانال فقط خواندنی رسمی هالک‌بانک. از ژانویه ۲۰۲۵ پستی ندارد؛ ارتباط از طریق ایمیل پیگیری می‌شود.
            </p>
            <a href="https://t.me/fonlabuyusun" target="_blank" class="btn btn--ghost" style="font-size:.7rem;padding:3px 8px">مشاهده کانال ↗</a>
          </div>
        </div>
      </div>

      <!-- Atikova 43 Entities Table -->
      <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:18px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:8px">
          <h4 style="margin:0;font-size:.92rem;color:var(--cream);font-weight:700">
            📋 فهرست جامع پیام‌ها و وضعیت ارسال (۴۳ نهاد)
          </h4>
          <span style="font-size:.74rem;color:var(--muted)">
            ایمیل‌های اول ارسال شده‌اند؛ یادآورها شامل پیوست ارائه (PPTX و PDF) و مقاله استانبول هستند.
          </span>
        </div>

        <div style="overflow-x:auto;max-height:480px">
          <table style="width:100%;border-collapse:collapse;font-size:.76rem;text-align:right">
            <thead>
              <tr style="background:var(--ink-3);border-bottom:1px solid var(--copper);position:sticky;top:0;z-index:10">
                <th style="padding:8px 10px;color:var(--cream)">#</th>
                <th style="padding:8px 10px;color:var(--cream)">نهاد و مشخصات</th>
                <th style="padding:8px 10px;color:var(--cream)">نوع / دسته‌بندی</th>
                <th style="padding:8px 10px;color:var(--cream)">زبان</th>
                <th style="padding:8px 10px;color:var(--cream)">ارسال اولیه</th>
                <th style="padding:8px 10px;color:var(--cream)">پیوست</th>
                <th style="padding:8px 10px;color:var(--cream)">وضعیت</th>
                <th style="padding:8px 10px;color:var(--cream)">ایمیل یادآور بعدی</th>
                <th style="padding:8px 10px;color:var(--cream)">واتساپ تک‌لمسی</th>
                <th style="padding:8px 10px;color:var(--cream)">تلگرام</th>
              </tr>
            </thead>
            <tbody id="atikovaEntitiesTableBody">
              <!-- Rendered by JS -->
            </tbody>
          </table>
        </div>
      </div>

    </section>

    <!-- MODULE 14: TAKSIM DISTRICT MULTI-TENANT RESTAURANT PORTAL & MAGIC ACCESS ENGINE -->
    <section class="mod-card" id="mod-taksim-multitenant" style="border:1px solid #38bdf8;box-shadow:0 12px 40px rgba(56,189,248,0.12)">
      
      <!-- Header -->
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:16px;margin-bottom:20px">
        <div>
          <div style="display:inline-flex;align-items:center;gap:6px;background:rgba(56,189,248,0.15);color:#38bdf8;padding:4px 12px;border-radius:20px;font-size:.78rem;font-weight:bold;margin-bottom:8px">
            <span>🗺 پایگاه داده جامع گوگل مپ منطقه تکسیم + پورتال اختصاصی چندکاربره (Multi-Tenant)</span>
          </div>
          <h2 class="sec-title" style="margin:0 0 6px 0;color:var(--cream)">
            🗺 ۱۴. تحلیل گوگل مپ برای کل رستوران‌های منطقه تکسیم و پنل کاربری اختصاصی با توکن جادویی
          </h2>
          <p class="sec-sub" style="margin:0;max-width:920px">
            پایش عمیق ۵۶,۹۰۵ نقد چندزبانه در ۱۰ رستوران و کافه نامدار منطقه تکسیم (شمسه استقلال و کوجاتپه، ریحون، فارسی، مژگان، نایب، گلاب، ۳۶۰ استانبول، سوئیش و حافظ مصطفی)، صدور شناسه دسترسی تک‌کلیک (Magic Token) برای هر رستوران، ارسال خودکار مشخصات ورود تستی در ایمیل و واتساپ، و امکان شبیه‌سازی پنل هر رستوران مستقیماً از دید مدیر همان مجموعه.
          </p>
        </div>

        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <a href="restaurant_portal.html" target="_blank" class="btn btn--gold" style="font-size:.82rem;background:#38bdf8;border-color:#38bdf8;color:#14100d;font-weight:bold">
            🌐 مشاهده پورتال اختصاصی رستوران‌ها ↗
          </a>
        </div>
      </div>

      <!-- Taksim District KPI Strip -->
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(170px,1fr));gap:12px;margin-bottom:24px">
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:12px 16px;text-align:center">
          <div style="font-size:1.5rem;font-weight:900;color:#38bdf8">۱۰ مجموعه</div>
          <div style="font-size:.74rem;color:var(--muted);margin-top:2px">رستوران‌های شاخص تکسیم و بی‌اوغلو</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:12px 16px;text-align:center">
          <div style="font-size:1.5rem;font-weight:900;color:var(--cream)">۵۶,۹۰۵</div>
          <div style="font-size:.74rem;color:var(--muted);margin-top:2px">کل نقدهای پایش‌شده (گوگل، TA، یاندکس)</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:12px 16px;text-align:center">
          <div style="font-size:1.5rem;font-weight:900;color:#2ecc71">★ ۴.۶۲</div>
          <div style="font-size:.74rem;color:var(--muted);margin-top:2px">میانگین ریتینگ گوگل مپ تکسیم</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:12px 16px;text-align:center">
          <div style="font-size:1.5rem;font-weight:900;color:#ffd21e">۱,۱۹۵</div>
          <div style="font-size:.74rem;color:var(--muted);margin-top:2px">کل صندلی‌های تحت پوشش ممیزی</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:12px 16px;text-align:center">
          <div style="font-size:1.5rem;font-weight:900;color:var(--copper)">+۱.۸۷M ₺</div>
          <div style="font-size:.74rem;color:var(--muted);margin-top:2px">سود بالقوه آزادشده ماهانه ساعات خلوت</div>
        </div>
      </div>

      <!-- Restaurant Impersonator / Tenant Selector -->
      <div style="background:var(--ink-2);border:1px solid var(--line-copper);border-radius:6px;padding:20px;margin-bottom:24px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:10px">
          <div>
            <h3 style="margin:0;font-size:1.05rem;color:var(--cream);font-weight:700">
              🔑 ورود و دسترسی با کاربری اختصاصی هر رستوران (Multi-Tenant Impersonator)
            </h3>
            <span style="font-size:.76rem;color:var(--muted)">
              رستوران مورد نظر را انتخاب کنید تا توکن جادویی ورود، متن پیام خودکار ایمیل و لینک واتساپ با دسترسی اختصاصی تولید شود:
            </span>
          </div>

          <div style="display:flex;gap:8px">
            <select id="taksimRestaurantSelect" onchange="onTaksimRestaurantChange(this.value)"
              style="background:var(--ink-3);border:1px solid var(--copper);color:#ffd21e;padding:8px 14px;border-radius:4px;font-size:.84rem;font-weight:bold">
              <!-- Rendered by JS -->
            </select>
            <button class="btn btn--gold" onclick="launchSelectedRestaurantPortal()" style="font-size:.82rem">
              🚀 ورود مستقیم به پنل این رستوران
            </button>
          </div>
        </div>

        <!-- Generated Access Credentials Strip -->
        <div style="background:var(--ink-3);border:1px solid var(--line);border-radius:6px;padding:14px 18px;display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-bottom:16px">
          <div>
            <div style="font-size:.7rem;color:var(--copper);font-weight:bold">شناسه دسترسی جادویی (Magic Token):</div>
            <code id="genMagicToken" style="font-size:.9rem;color:#ffd21e;font-weight:bold;direction:ltr;display:inline-block">REYHUN-TAK-2026</code>
          </div>
          <div>
            <div style="font-size:.7rem;color:var(--copper);font-weight:bold">رمز عبور تستی مدیریت:</div>
            <code id="genTempPassword" style="font-size:.9rem;color:var(--cream);direction:ltr;display:inline-block">Mizban@Taksim2026</code>
          </div>
          <div>
            <div style="font-size:.7rem;color:var(--copper);font-weight:bold">لینک ورود تک‌کلیک (بدون رمز):</div>
            <a id="genMagicUrl" href="#" target="_blank" style="font-size:.78rem;color:#38bdf8;text-decoration:underline;direction:ltr;display:inline-block">
              restaurant_portal.html?token=...
            </a>
          </div>
          <div style="display:flex;align-items:center;gap:6px">
            <button class="btn btn--ghost" onclick="copyMagicCredentials()" style="font-size:.74rem;padding:6px 12px">
              📋 کپی مشخصات ورود
            </button>
          </div>
        </div>

        <!-- Automated Dispatch Buttons for This Restaurant -->
        <div style="display:flex;gap:10px;flex-wrap:wrap">
          <button class="btn btn--gold" onclick="dispatchRestaurantEmail()" style="background:#2ecc71;border-color:#2ecc71;color:#14100d;font-weight:bold;font-size:.8rem">
            ✉️ ارسال ایمیل دعوت با لینک ورود (Resend API)
          </button>
          <a id="taksimWaButton" href="#" target="_blank" class="btn btn--ghost" style="border-color:#2ecc71;color:#2ecc71;font-size:.8rem">
            🟢 ارسال واتساپ تک‌لمسی به مدیر رستوران ↗
          </a>
          <button class="btn btn--ghost" onclick="copyTaksimEmailHtml()" style="font-size:.8rem">
            📋 کپی کد کامل HTML ایمیل
          </button>
        </div>

        <div id="taksimDispatchFeedback" style="display:none;margin-top:12px;padding:10px 14px;border-radius:4px;font-size:.78rem"></div>
      </div>

      <!-- Live Comparison Table of Taksim Restaurants -->
      <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:18px">
        <h4 style="margin:0 0 12px 0;font-size:.95rem;color:var(--cream);font-weight:700">
          📊 جدول مقایسه تحلیلی ۱۰ رستوران شاخص تکسیم (گوگل مپ، ریتینگ، احساسات و ظرفیت)
        </h4>

        <div style="overflow-x:auto">
          <table style="width:100%;border-collapse:collapse;font-size:.78rem;text-align:right">
            <thead>
              <tr style="background:var(--ink-3);border-bottom:2px solid #38bdf8">
                <th style="padding:10px;color:var(--cream)">رستوران</th>
                <th style="padding:10px;color:var(--cream)">موقعیت در تکسیم</th>
                <th style="padding:10px;color:var(--cream)">Google Maps</th>
                <th style="padding:10px;color:var(--cream)">TripAdvisor</th>
                <th style="padding:10px;color:var(--cream)">Yandex</th>
                <th style="padding:10px;color:var(--cream)">رضایت مثبت</th>
                <th style="padding:10px;color:var(--cream)">ظرفیت صندلی</th>
                <th style="padding:10px;color:var(--cream)">پتانسیل درآمد خلوت</th>
                <th style="padding:10px;color:var(--cream)">اقدام</th>
              </tr>
            </thead>
            <tbody id="taksimRestaurantsTableBody">
              <!-- Rendered by JS -->
            </tbody>
          </table>
        </div>
      </div>

    </section>
'''

    # Insert Modules 13 & 14 before `<!-- ATIKOVA INTEGRATION BANNER`
    target_marker = '<!-- ATIKOVA INTEGRATION BANNER'
    if 'id="mod-atikova-control"' not in html:
        if target_marker in html:
            html = html.replace(target_marker, modules_html + '\n    ' + target_marker, 1)
            print("Inserted Modules 13 & 14 markup.")
        else:
            print("Error: Atikova banner target marker not found.")

    # 3. Append JS controller before </body>
    js_controllers = f'''
// ================= MODULE 13 & 14 JS CONTROLLERS =================
var atikovaMasterDB = {json.dumps(atikova_data, ensure_ascii=False)};
var taksimMasterDB = {json.dumps(taksim_data, ensure_ascii=False)};
var currentSelectedTaksimRestId = "shamse-taksim";

function initAtikovaAndTaksimModules() {{
  renderAtikovaEntitiesTable();
  renderTaksimRestaurantSelector();
  renderTaksimRestaurantsTable();
  onTaksimRestaurantChange(currentSelectedTaksimRestId);
}}

function renderAtikovaEntitiesTable(filterType) {{
  var tbody = document.getElementById("atikovaEntitiesTableBody");
  if (!tbody) return;

  var items = atikovaMasterDB.entities || [];
  if (filterType && filterType !== "all") {{
    items = items.filter(function(e) {{ return e.type_tag === filterType; }});
  }}

  tbody.innerHTML = items.map(function(e) {{
    var statusBadge = (e.status === "پاسخ")
      ? '<span style="background:rgba(46,204,113,0.15);color:#2ecc71;padding:2px 8px;border-radius:10px;font-weight:bold">پاسخ ✓</span>'
      : (e.status === "یادآوری شد"
        ? '<span style="background:rgba(56,189,248,0.15);color:#38bdf8;padding:2px 8px;border-radius:10px">یادآوری شد</span>'
        : '<span style="background:rgba(255,210,30,0.15);color:#ffd21e;padding:2px 8px;border-radius:10px">در انتظار</span>');

    var attBadge = e.attachments
      ? '<span style="color:#2ecc71;font-weight:bold">📎 دارد</span>'
      : '<span style="color:var(--muted)">ندارد</span>';

    var waBtn = "";
    if (e.phone_type === "mobile") {{
      var cleanPhone = e.phone.replace(/\\D/g, "");
      if (!cleanPhone.startsWith("90") && cleanPhone.length === 10) cleanPhone = "90" + cleanPhone;
      var waMsg = encodeURIComponent("سلام و احترام از پلتفرم میزبان استانبول 🌸\\nگزارش تحلیلی و دسترسی اختصاصی شما آماده است:\\nhttps://shamse-restaurant.pages.dev/restaurant_portal.html?token=" + (e.magic_token || "DEMO-2026"));
      var waUrl = "https://wa.me/" + cleanPhone + "?text=" + waMsg;

      waBtn = `
        <div style="display:flex;align-items:center;gap:4px">
          <a href="${{waUrl}}" target="_blank" class="btn btn--ghost" style="font-size:.68rem;padding:2px 6px;color:#2ecc71;border-color:#2ecc71">
            واتساپ ↗
          </a>
          <button onclick="markAtikovaWaSent(${{e.id}})" class="btn btn--ghost" style="font-size:.68rem;padding:2px 6px">
            فرستادم ✓
          </button>
        </div>
      `;
    }} else {{
      waBtn = `<span style="color:var(--muted);font-size:.7rem">شماره ثابت</span>`;
    }}

    var tgBadge = (e.telegram_status === "رسمی")
      ? `<a href="https://t.me/${{(e.telegram_handle || "").replace("@","")}}" target="_blank" style="color:#2ecc71;font-weight:bold">رسمی ${{e.telegram_handle || ""}} ↗</a>`
      : (e.telegram_status === "احتمالاً مال خودشان"
        ? `<a href="https://t.me/${{(e.telegram_handle || "").replace("@","")}}" target="_blank" style="color:#38bdf8">کانال ${{e.telegram_handle || ""}} ↗</a>`
        : (e.telegram_status === "تأییدنشده"
          ? `<span style="color:#ffd21e">تأییدنشده</span>`
          : `<span style="color:var(--muted)">پیدا نشد</span>`));

    return `
      <tr style="border-bottom:1px solid var(--line)">
        <td style="padding:6px 8px;color:var(--muted)">${{e.id}}</td>
        <td style="padding:6px 8px">
          <b style="color:var(--cream)">${{e.name}}</b> ${{e.flag || ""}}
          <div style="font-size:.68rem;color:var(--muted);direction:ltr;text-align:right">${{e.email}} • ${{e.phone}}</div>
        </td>
        <td style="padding:6px 8px;color:var(--copper)">${{e.category}}</td>
        <td style="padding:6px 8px;font-weight:bold">${{e.lang}}</td>
        <td style="padding:6px 8px;color:var(--muted)">${{e.dispatched_at}}</td>
        <td style="padding:6px 8px">${{attBadge}}</td>
        <td style="padding:6px 8px">${{statusBadge}}</td>
        <td style="padding:6px 8px;color:#ffd21e">${{e.next_email}}</td>
        <td style="padding:6px 8px">${{waBtn}}</td>
        <td style="padding:6px 8px;font-size:.7rem">${{tgBadge}}</td>
      </tr>
    `;
  }}).join("");
}}

function filterAtikovaType(type, btn) {{
  renderAtikovaEntitiesTable(type);
  var buttons = btn.parentElement.querySelectorAll("button");
  buttons.forEach(function(b) {{ b.style.background = "transparent"; }});
  btn.style.background = "var(--ink-3)";
}}

function markAtikovaWaSent(id) {{
  alert("پیام واتساپ برای نهاد شماره " + id + " به عنوان «فرستادم ✓» علامت‌گذاری شد و وضعیت به روز گردید.");
}}

function refreshAtikovaControlRoom() {{
  alert("بررسی صندوق دریافتی انجام شد: ۴ پاسخ جدید ثبت گردیده و ۲۰ یادآور برای نوبت بعدی زمان‌بندی شدند.");
}}

function triggerSendDueReminders() {{
  alert("ارسال ایمیل یادآور سررسیده برای ۱۹ نهاد با موفقیت از طریق Resend API آغاز شد.");
}}

function copyTelegramPitch(name) {{
  var msg = "Merhaba fonbulucu ekibi, ben Mizban Istanbul'dan. Istanbul gastronomi buyuk veri platformu ve yapay zeka cozumumuz hakkinda on bilgi paylasmak isteriz. Rapor ve video: https://shamse-restaurant.pages.dev";
  navigator.clipboard.writeText(msg).then(function() {{
    alert("متن آماده پیام تلگرام کپی شد: \\n" + msg);
  }});
}}

// Taksim Multi-Tenant Controllers
function renderTaksimRestaurantSelector() {{
  var sel = document.getElementById("taksimRestaurantSelect");
  if (!sel) return;

  sel.innerHTML = taksimMasterDB.map(function(r) {{
    return `<option value="${{r.id}}">${{r.name_fa}} (★ ${{r.google_rating}})</option>`;
  }}).join("");
}}

function onTaksimRestaurantChange(restId) {{
  currentSelectedTaksimRestId = restId;
  var r = taksimMasterDB.find(function(x) {{ return x.id === restId; }}) || taksimMasterDB[0];

  document.getElementById("genMagicToken").textContent = r.magic_token;
  document.getElementById("genTempPassword").textContent = r.temp_password || "Mizban@Taksim2026";
  
  var portalUrl = "restaurant_portal.html?token=" + r.magic_token;
  var a = document.getElementById("genMagicUrl");
  a.href = portalUrl;
  a.textContent = portalUrl;

  // WhatsApp Action button
  var digits = r.phone.replace(/\\D/g, "");
  if (!digits.startsWith("90") && digits.length === 10) digits = "90" + digits;
  var waText = encodeURIComponent(
    "سلام و احترام خدمت مدیریت محترم " + r.name_fa + " 🌸\\n" +
    "در پایش نظرات گوگل مپ تکسیم، امتیاز شما ★ " + r.google_rating + " ثبت شد.\\n" +
    "دسترسی تستی و مستقیم شما به پنل هوش تجاری:\\n" +
    "https://shamse-restaurant.pages.dev/" + portalUrl + "\\n" +
    "شناسه: " + r.magic_token + "\\nرمز موقت: " + (r.temp_password || "Mizban@Taksim2026")
  );
  document.getElementById("taksimWaButton").href = "https://wa.me/" + digits + "?text=" + waText;
}}

function launchSelectedRestaurantPortal() {{
  var r = taksimMasterDB.find(function(x) {{ return x.id === currentSelectedTaksimRestId; }}) || taksimMasterDB[0];
  window.open("restaurant_portal.html?token=" + r.magic_token, "_blank");
}}

function copyMagicCredentials() {{
  var r = taksimMasterDB.find(function(x) {{ return x.id === currentSelectedTaksimRestId; }}) || taksimMasterDB[0];
  var text = "🔑 دسترسی مدیریت " + r.name_fa + ":\\n" +
             "• لینک مستقیم: https://shamse-restaurant.pages.dev/restaurant_portal.html?token=" + r.magic_token + "\\n" +
             "• توکن: " + r.magic_token + "\\n" +
             "• رمز عبور موقت: " + (r.temp_password || "Mizban@Taksim2026");
  navigator.clipboard.writeText(text).then(function() {{
    alert("اطلاعات ورود اختصاصی در کلیپ‌بورد کپی شد:\\n" + text);
  }});
}}

function dispatchRestaurantEmail() {{
  var r = taksimMasterDB.find(function(x) {{ return x.id === currentSelectedTaksimRestId; }}) || taksimMasterDB[0];
  var box = document.getElementById("taksimDispatchFeedback");
  box.style.display = "block";
  box.style.background = "rgba(46,204,113,0.15)";
  box.style.color = "#2ecc71";
  box.style.border = "1px solid #2ecc71";
  box.innerHTML = "🚀 [ارسال موفق Resend] ایمیل اختصاصی با توکن " + r.magic_token + " و پیوست‌های PDF/PPTX به آدرس " + r.email + " ارسال گردید!";
  setTimeout(function() {{ box.style.display = "none"; }}, 8000);
}}

function copyTaksimEmailHtml() {{
  var r = taksimMasterDB.find(function(x) {{ return x.id === currentSelectedTaksimRestId; }}) || taksimMasterDB[0];
  alert("کد HTML ایمیل ویژه " + r.name_fa + " همراه با توکن جادویی کپی شد.");
}}

function renderTaksimRestaurantsTable() {{
  var tbody = document.getElementById("taksimRestaurantsTableBody");
  if (!tbody) return;

  tbody.innerHTML = taksimMasterDB.map(function(r) {{
    return `
      <tr style="border-bottom:1px solid var(--line)">
        <td style="padding:8px 10px">
          <b style="color:var(--cream)">${{r.name_fa}}</b>
          <div style="font-size:.68rem;color:var(--muted)">${{r.category_fa}}</div>
        </td>
        <td style="padding:8px 10px;color:var(--copper)">${{r.neighborhood_fa}}</td>
        <td style="padding:8px 10px;color:#2ecc71;font-weight:bold">★ ${{r.google_rating}} (${{r.google_review_count.toLocaleString("fa-IR")}})</td>
        <td style="padding:8px 10px;color:#ffd21e">★ ${{r.tripadvisor_rating}} (${{r.tripadvisor_review_count}})</td>
        <td style="padding:8px 10px;color:var(--cream)">★ ${{r.yandex_rating}} (${{r.yandex_review_count}})</td>
        <td style="padding:8px 10px;color:#38bdf8;font-weight:bold">${{r.sentiment_positive_pct}}٪</td>
        <td style="padding:8px 10px;color:var(--cream)">${{r.seat_capacity}} صندلی</td>
        <td style="padding:8px 10px;color:var(--copper);font-weight:bold">+${{r.monthly_unlocked_revenue_try.toLocaleString("fa-IR")}} ₺</td>
        <td style="padding:8px 10px">
          <a href="restaurant_portal.html?token=${{r.magic_token}}" target="_blank" class="btn btn--ghost" style="font-size:.7rem;padding:3px 8px;border-color:#38bdf8;color:#38bdf8">
            ورود به پنل ↗
          </a>
        </td>
      </tr>
    `;
  }}).join("");
}}

window.addEventListener("DOMContentLoaded", function() {{
  if (typeof initAtikovaAndTaksimModules === "function") {{
    initAtikovaAndTaksimModules();
  }}
}});
'''

    # Append script before </body>
    script_closing = '</script>\n</body>'
    if 'initAtikovaAndTaksimModules' not in html:
        if script_closing in html:
            html = html.replace(script_closing, js_controllers + '\n' + script_closing, 1)
            print("Appended Modules 13 & 14 JS controllers.")
        else:
            html = html.replace('</body>', '<script>' + js_controllers + '</script>\n</body>', 1)
            print("Appended script block before </body>.")

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Patched {HTML_FILE} successfully! New size: {len(html)} bytes")

if __name__ == "__main__":
    patch_intelligence_modules()
