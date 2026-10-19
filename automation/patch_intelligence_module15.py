#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Adds Module 15: "کیت جذب همکاری نسخه ۲ — ۳۰ مهارت ممیزی، نقد و اتوماسیون ضداسپم"
to intelligence.html.
Features:
  1. 140-point 7-axis pre-audit comparison scoreboard (v1: 81 -> v2: 122).
  2. 30 selected operational review & outreach skills across 5 tabs.
  3. Interactive Micro-Pitch Simulator (target ~107 words) across Day 0, Day 5, and Day 12 stages.
  4. RFC 8058 List-Unsubscribe + One-Click inspection and central suppression list checker.
  5. 39 Reference Projects quick-reference matrix.
"""

import os

REPO_ROOT = "/home/user/shamse-restaurant"
INTEL_HTML = os.path.join(REPO_ROOT, "intelligence.html")

MODULE_15_HTML = '''
    <!-- ===================================================================
         MODULE 15: کیت جذب همکاری نسخه ۲ — ۳۰ مهارت ممیزی نظرات و اتوماسیون ضداسپم
         =================================================================== -->
    <section class="mod-card" id="mod-outreach-v2" style="border:1px solid #ffd21e;box-shadow:0 12px 40px rgba(255,210,30,0.12);margin-top:40px">
      <div class="mod-header">
        <div>
          <span class="badge" style="background:rgba(255,210,30,0.15);color:#ffd21e;border:1px solid #ffd21e">ماژول ۱۵ • نسخه ۲٫۰</span>
          <h2 style="color:var(--cream);font-size:1.4rem;font-weight:800;margin:8px 0 4px">کیت جذب همکاری نسخه ۲ — ۳۰ مهارت ممیزی، نقد و اتوماسیون ضداسپم</h2>
          <p style="color:var(--muted);font-size:.88rem;margin:0">
            برگرفته از متدولوژی بازسازی کیت همکاری (نقد ۷ محور × ۲۰ امتیاز = ۱۴۰ امتیاز، کاهش کلمات به ۱۰۷ کلمه، توالی روز ۰/۵/۱۲ با ایمیل خداحافظی، هدر RFC 8058 و فهرست حذف متمرکز)
          </p>
        </div>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <span style="background:rgba(46,204,113,0.15);color:#2ecc71;border:1px solid #2ecc71;padding:4px 10px;border-radius:4px;font-size:.78rem;font-weight:700">
            امتیاز ارزیابی: ۸۱ ← ۱۲۲ / ۱۴۰
          </span>
          <span style="background:rgba(210,154,90,0.15);color:var(--copper);border:1px solid var(--line-copper);padding:4px 10px;border-radius:4px;font-size:.78rem;font-weight:700">
            طول طلایی: ۱۰۷ کلمه
          </span>
        </div>
      </div>

      <!-- 7-AXIS PRE-AUDIT SCOREBOARD -->
      <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:20px;margin-bottom:24px">
        <h4 style="color:var(--cream);font-size:1.05rem;margin:0 0 12px 0;font-weight:800;display:flex;align-items:center;gap:8px">
          <span>📊 نقد پیش از کار: ارزیابی ارتقای نسخه ۱ به ۲ (۷ محور × ۲۰ امتیاز = ۱۴۰ امتیاز)</span>
        </h4>
        <div class="table-wrap">
          <table class="bench-table">
            <thead>
              <tr>
                <th>محور ارزیابی</th>
                <th>امتیاز v1</th>
                <th>امتیاز v2</th>
                <th>پیشرفت</th>
                <th>علت ارتقا و تغییر ساختاری در نسخه ۲</th>
              </tr>
            </thead>
            <tbody>
              <tr>
                <td><b>۱. هدف‌گیری و فهرست</b></td>
                <td>۱۳</td>
                <td style="color:#2ecc71;font-weight:bold">۱۸</td>
                <td><span style="color:#2ecc71">+۵</span></td>
                <td>تعریف ICP بر پایه ۳ معیار (اندازه، بودجه، درد مشخص)، حذف آدرس‌های نقش‌محور و ردیف‌بندی ۳ سطحی</td>
              </tr>
              <tr>
                <td><b>۲. متن و قانع‌سازی</b></td>
                <td>۱۲</td>
                <td style="color:#2ecc71;font-weight:bold">۱۹</td>
                <td><span style="color:#2ecc71">+۷</span></td>
                <td>کاهش طول از ۱۹۵ کلمه به ۱۰۲ کلمه (۳ بولت کوتاه)، پیش‌سرصفحه ۹۰ کاراکتری، ایمیل خداحافظی روز ۱۲</td>
              </tr>
              <tr>
                <td><b>۳. تحویل‌پذیری و ضداسپم</b></td>
                <td>۱۴</td>
                <td style="color:#2ecc71;font-weight:bold">۱۸</td>
                <td><span style="color:#2ecc71">+۴</span></td>
                <td>هدر لغو یک‌کلیکه RFC 8058، تراز دامنه، نسبت ۸۰/۲۰ متن به تصویر و پیوست سبک همراه لینک ابری</td>
              </tr>
              <tr>
                <td><b>۴. خودکارسازی و ماشین‌حالت</b></td>
                <td>۸</td>
                <td style="color:#2ecc71;font-weight:bold">۱۷</td>
                <td><span style="color:#2ecc71">+۹</span></td>
                <td>توالی سه‌مرحله‌ای (روز ۰، ۵ و ۱۲)، توقف در تعطیلات، کلید یکتایی (Idempotency) و وب‌هوک وضعیت</td>
              </tr>
              <tr>
                <td><b>۵. سنجش عملکرد و حریم خصوصی</b></td>
                <td>۶</td>
                <td style="color:#2ecc71;font-weight:bold">۱۶</td>
                <td><span style="color:#2ecc71">+۱۰</span></td>
                <td>سنجش بر پایه «پاسخ و جلسه رزرو شده» به‌جای پیکسل جاسوسی، کمینه‌سازی داده‌ها و گروه کنترل ۱۰٪</td>
              </tr>
              <tr>
                <td><b>۶. انطباق حقوقی و اخلاقی</b></td>
                <td>۱۵</td>
                <td style="color:#2ecc71;font-weight:bold">۱۷</td>
                <td><span style="color:#2ecc71">+۲</span></td>
                <td>فهرست حذف متمرکز (suppression.jsonl)، لغو اشتراک یک‌کلیکه، حق فراموشی ظرف ۷۲ ساعت</td>
              </tr>
              <tr>
                <td><b>۷. تجربه پنل و پیش‌پرواز</b></td>
                <td>۱۳</td>
                <td style="color:#2ecc71;font-weight:bold">۱۷</td>
                <td><span style="color:#2ecc71">+۴</span></td>
                <td>آزمون تست خشک پیش‌فرض (Dry-Run)، پیش‌پرواز روی ایمیل خود، و دکمه‌های تک‌لمسی واتساپ</td>
              </tr>
              <tr style="background:rgba(255,210,30,0.06);font-weight:bold">
                <td><b>مجموع کل نمره</b></td>
                <td><b>۸۱ / ۱۴۰</b></td>
                <td style="color:#ffd21e;font-size:1.1rem"><b>۱۲۲ / ۱۴۰</b></td>
                <td><b style="color:#2ecc71">+۴۱ امتیاز</b></td>
                <td><b>جهش ۵۰٫۶٪ در شاخص بلوغ مهندسی کمپین و پایش نظرات</b></td>
              </tr>
            </tbody>
          </table>
        </div>
      </div>

      <!-- 30 SELECTED REVIEW & OUTREACH SKILLS TABS -->
      <div style="background:var(--ink-1);border:1px solid var(--line);border-radius:6px;padding:20px;margin-bottom:24px">
        <h4 style="color:var(--cream);font-size:1.05rem;margin:0 0 12px 0;font-weight:800">
          🧠 ۳۰ مهارت منتخب برای ممیزی نظرات، نقد و کمپین‌های B2B (۵ حوزه × ۶ مهارت)
        </h4>

        <div style="display:flex;gap:8px;flex-wrap:wrap;margin-bottom:16px">
          <button class="btn btn--gold" onclick="showV2SkillTab('v2-target')" id="btn-v2-target">🎯 هدف‌گیری و فهرست (۶)</button>
          <button class="btn btn--ghost" onclick="showV2SkillTab('v2-copy')" id="btn-v2-copy">✍️ متن و روانشناسی (۶)</button>
          <button class="btn btn--ghost" onclick="showV2SkillTab('v2-deliv')" id="btn-v2-deliv">🛡️ تحویل‌پذیری و ضداسپم (۶)</button>
          <button class="btn btn--ghost" onclick="showV2SkillTab('v2-auto')" id="btn-v2-auto">⚙️ خودکارسازی و توالی (۶)</button>
          <button class="btn btn--ghost" onclick="showV2SkillTab('v2-privacy')" id="btn-v2-privacy">🔒 سنجش و حریم خصوصی (۶)</button>
        </div>

        <!-- Tab 1: Target -->
        <div id="tab-v2-target" class="v2-skill-content">
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px">
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۱. تعریف ICP با ۳ معیار قابل‌سنجش</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">اندازه سالن، بودجه تصرف‌پذیر و درد مشخص (مانند ساعات خلوت عصرگاهی یا امتیاز پایین تریپ‌ادوایزر) — نه صنف کلی.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۲. بخش‌بندی بر پایه درد واقعی</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">هر بخش یک جمله درد و یک درخواست متفاوت دارد؛ مثلاً درد رستوران شمسه توریست اروپایی است، اما دیوان رویداد شرکتی است.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۳. رویداد محرک (Trigger Event)</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">ثبت یک نظر منفی ۱ یا ۲ ستاره در گوگل یا تغییر مدیریت، بهانهٔ طبیعی تماس بدون نیاز به بهانه‌تراشی است.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۴. حذف آدرس‌های نقش‌محور در دور اول</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">آدرس‌های عمومی info@ و sales@ به پوشه اسپم می‌روند؛ نام واقعی مدیر عامل یا مدیر بازاریابی لازم است.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۵. ردیف‌بندی سه‌سطحی حساب‌ها</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">۲۰ حساب طلایی (تحلیل اختصاصی و پادکست)، ۵۰ نقره‌ای (گزارش استاندارد) و بقیه خودکار؛ تمرکز وقت روی فرصت‌های بزرگ.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۶. فهرست حذف متمرکز (Suppression List)</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">فایل متمرکز suppression.jsonl برای جلوگیری فنی از ارسال مجدد به کسانی که قبلاً انصراف داده‌اند یا شکایت کرده‌اند.</p>
            </div>
          </div>
        </div>

        <!-- Tab 2: Copy -->
        <div id="tab-v2-copy" class="v2-skill-content" style="display:none">
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px">
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۷. سقف طلایی کلمات (۷۵ تا ۱۲۵ کلمه)</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">بالای ۱۵۰ کلمه نرخ پاسخ نصف می‌شود؛ نسخه ۲ با ۱۰۲ کلمه صراحت و نرخ تبدیل را حداکثر می‌کند.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۸. موضوع زیر ۵۰ کاراکتر</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">در اپلیکیشن‌های موبایل موضوعات طولانی بریده می‌شوند؛ عناوین کوتاه و کنجکاوی‌برانگیز بالاترین بازدهی را دارند.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۹. پیش‌سرصفحه (Preheader) مکمل</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">تکرار موضوع در پیش‌سرصفحه یعنی سوزاندن ۹۰ کاراکتر رایگان در نوتیفیکیشن موبایل مشتری.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۱۰. خط اول مخصوص همان مخاطب</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">اگر خط اول را بشود برای هر رستوران دیگری ارسال کرد، شخصی‌سازی نیست. اشاره به آخرین نقد مشتری ضروری است.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۱۱. ارزش قبل از درخواست (Value-First)</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">ابتدا هدیه تحلیلی بده (پادکست و ممیزی PDF رایگان)، سپس درخواست وقت برای جلسه کن.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۱۲. ایمیل خداحافظی (Breakup Email)</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">«این آخرین پیام پیگیری من است» در روز دوازدهم بالاترین نرخ تبدیل و بازگشت مشتری را دارد.</p>
            </div>
          </div>
        </div>

        <!-- Tab 3: Deliv -->
        <div id="tab-v2-deliv" class="v2-skill-content" style="display:none">
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px">
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۱۳. تراز SPF / DKIM 2048 / DMARC</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">تراز کامل امنیتی دامنه با کلید ۲۰۴۸ بیتی برای جلوگیری از اسپم شدن در فایروال‌های مایکروسافت و گوگل.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۱۴. هدر استاندارد RFC 8058</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">هدر List-Unsubscribe + One-Click الزام ۲۰۲۴ جیمیل؛ اجازه لغو آسان به‌جای زدن دکمه Report Spam.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۱۵. قالب HTML زیر ۳KB همراه نسخه متن ساده</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">ارسال ایمیل فقط-HTML خطر اسپم دارد؛ ارسال ترکیبی (Multipart) با قالب ۵۶۰px سبک بالاترین ضریب عبور را دارد.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۱۶. پیوست زیر ۲ مگابایت همراه لینک ابری</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">فایل سنگین صندوق ورودی را اشغال می‌کند؛ ارسال کارت سبک گزارش و قراردادن لینک دانلود ابری ترجیح دارد.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۱۷. منحنی گرم‌کردن ۳ هفته‌ای</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">رشد پلکانی ۱۰ ← ۲۰ ← ۴۰ ← ۸۰ ارسال در روز؛ ارسال ناگهانی ۵۰۰ ایمیل دامنه را وارد بلک‌لیست می‌کند.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۱۸. خطوط قرمز پرش و شکایت</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">نرخ پرش بالای ۳٪ یا شکایت بالای ۰٫۱٪ به معنی آلودگی فهرست است و پایپ‌لاین بلافاصله متوقف می‌شود.</p>
            </div>
          </div>
        </div>

        <!-- Tab 4: Auto -->
        <div id="tab-v2-auto" class="v2-skill-content" style="display:none">
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px">
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۱۹. توالی ۳ مرحله‌ای پایدار (روز ۰ / ۵ / ۱۲)</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">انتقال خودکار ارسال‌ها از روزهای تعطیل آخر هفته به سه‌شنبه و چهارشنبه ساعت ۹ تا ۱۱ صبح.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۲۰. کلید یکتایی (Idempotency Key)</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">دو بار ارسال یک پیام در یک کمپین اعتبار برند را می‌سوزاند؛ کلید یکتایی مانع تکرار اتفاقی می‌شود.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۲۱. تخصیص قطعی تست A/B با هش ایمیل</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">تخصیص موضوعات با هش MD5 گیرنده، نه تصادف، برای اطمینان از تحلیل علمی و تکرارپذیر نتایج.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۲۲. تشخیص پاسخ و توقف زنجیره پیگیری</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">به‌محض دریافت پاسخ در هر یک از ۴ دسته (علاقه‌مند/بعداً/نه/لغو)، پیگیری‌های بعدی بلافاصله قطع می‌شود.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۲۳. وضعیت ماشین‌حالت رشته (State Machine)</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">چرخه منظم queued → sent → replied → closed برای مدیریت هر مکالمه تجاری.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۲۴. لاگ ساخت‌یافته JSON و بازپخش امن</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">ثبت دقیق تمام پارامترها و امکان بازپخش (Replay) ارسال‌های ناموفق از صندوق خروجی (Outbox).</p>
            </div>
          </div>
        </div>

        <!-- Tab 5: Privacy -->
        <div id="tab-v2-privacy" class="v2-skill-content" style="display:none">
          <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:12px">
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۲۵. سنجش بر پایه پاسخ، نه پیکسل باز شدن</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">پیکسل باز شدن از ۲۰۲۱ (با قابلیت حفاظت حریم خصوصی اپل) بی‌معنی شده؛ شاخص اصلی نرخ پاسخ مثبت است.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۲۶. جلسهٔ رزروشده به‌عنوان خروجی اصلی</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">تعداد ایمیل ارسال‌شده فایده‌ای ندارد؛ تنها خروجی ارزشمند رزرو جلسه مشاوره یا پذیرش میتاپ است.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۲۷. کمینه‌سازی داده‌ها (Data Minimization)</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">نام، ایمیل، شناسه رستوران و یک فیلد زمینه؛ ذخیره نکردن هیچ داده بالینی، هویتی یا محرمانه اضافه.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۲۸. حق حذف ظرف ۷۲ ساعت (GDPR / KVKK)</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">درخواست انصراف یعنی پاک‌سازی فوری اطلاعات تماس از فهرست تماس‌های آینده.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۲۹. گروه کنترل (Holdout Group ۱۰٪)</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">۱۰٪ از مجموعه‌ها پیامی دریافت نمی‌کنند تا رشد طبیعی از اثر کمپین هوش تجاری به‌دقت تفکیک شود.</p>
            </div>
            <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:4px">
              <b style="color:#ffd21e;font-size:.86rem">۳۰. پاسخ محترمانه به «نه»</b>
              <p style="color:var(--text);font-size:.78rem;margin:4px 0 0;line-height:1.6">بدون احساس گناه دادن، بدون چانه‌زنی و پذیرش حرفه‌ای تصمیم مدیر مجموعه.</p>
            </div>
          </div>
        </div>

      </div>

      <!-- INTERACTIVE V2 MICRO-PITCH SIMULATOR -->
      <div style="background:var(--ink-2);border:1px solid var(--copper);border-radius:6px;padding:22px">
        <h4 style="color:var(--cream);font-size:1.1rem;margin:0 0 14px 0;font-weight:800;display:flex;align-items:center;gap:8px">
          <span>🧪 شبیه‌ساز زندهٔ ایمیل نسخه ۲ (Micro-Pitch Simulator — هدف ۱۰۷ کلمه)</span>
        </h4>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px">
          <div>
            <label style="display:block;font-size:.8rem;color:var(--muted);margin-bottom:4px">انتخاب مجموعه هدف (از میان ۴۳ انتیتی):</label>
            <select id="v2EntitySelect" onchange="updateV2Simulation()" style="width:100%;background:var(--ink-1);border:1px solid var(--line);color:var(--cream);padding:8px;border-radius:4px;font-size:.84rem">
              <option value="رستوران شمسه">رستوران شمسه (Taksim - ۵,۰۵۵ نقد)</option>
              <option value="رستوران ریحون">رستوران ریحون (Valikonağı Nişantaşı)</option>
              <option value="رستوران فارسی">رستوران فارسی (Cevahir Şişli)</option>
              <option value="رستوران مژگان">رستوران مژگان (Kocatepe Beyoğlu)</option>
              <option value="شهرداری بشیکتاش">شهرداری بشیکتاش (Beşiktaş Belediyesi)</option>
              <option value="تکنوپارک استانبول">تکنوپارک استانبول (Teknopark İstanbul)</option>
              <option value="پلتفرم Fonbulucu">پلتفرم سرمایه‌گذاری Fonbulucu</option>
            </select>
          </div>

          <div>
            <label style="display:block;font-size:.8rem;color:var(--muted);margin-bottom:4px">مرحله توالی ارسال:</label>
            <div style="display:flex;gap:6px">
              <button class="btn btn--gold" onclick="setV2Stage(1)" id="btn-v2-stage1" style="flex:1;justify-content:center;font-size:.78rem">مرحله ۱: روز ۰ (ارزش اول)</button>
              <button class="btn btn--ghost" onclick="setV2Stage(2)" id="btn-v2-stage2" style="flex:1;justify-content:center;font-size:.78rem">مرحله ۲: روز ۵ (پیگیری)</button>
              <button class="btn btn--ghost" onclick="setV2Stage(3)" id="btn-v2-stage3" style="flex:1;justify-content:center;font-size:.78rem">مرحله ۳: روز ۱۲ (خداحافظی)</button>
            </div>
          </div>
        </div>

        <!-- Rendered Email Card -->
        <div style="background:var(--ink-1);border:1px solid var(--line);border-radius:4px;padding:16px">
          <div style="display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--line);padding-bottom:10px;margin-bottom:12px">
            <div>
              <div style="font-size:.74rem;color:var(--muted)">موضوع (زیر ۵۰ کاراکتر - آزمون A/B هش):</div>
              <b id="v2SimSubject" style="color:#ffd21e;font-size:.9rem">تحلیل ۵,۰۵۵ نقد رستوران شمسه + پادکست اختصاصی</b>
            </div>
            <div style="text-align:left">
              <span id="v2WordBadge" style="background:rgba(46,204,113,0.15);color:#2ecc71;border:1px solid #2ecc71;padding:2px 8px;border-radius:12px;font-size:.72rem;font-weight:bold">
                ۱۰۲ کلمه (سبز در لینت ✓)
              </span>
            </div>
          </div>

          <div style="margin-bottom:10px;font-size:.75rem;color:var(--copper);direction:ltr;text-align:left;font-family:monospace;background:var(--ink-3);padding:6px 10px;border-radius:3px">
            <b>Headers:</b> List-Unsubscribe: &lt;mailto:unsub@mizbanistanbul.com&gt;, &lt;https://mizbanistanbul.com/unsub&gt; | List-Unsubscribe-Post: List-Unsubscribe=One-Click
          </div>

          <div style="font-size:.76rem;color:var(--muted);margin-bottom:8px">
            <b>پیش‌سرصفحه (Preheader):</b> <span id="v2SimPreheader">خلاصه ممیزی نظرات تریپ‌ادوایزر و راهکارهای افزایش سودآوری</span>
          </div>

          <div id="v2SimBody" style="background:var(--ink-2);border:1px solid var(--line);padding:14px;border-radius:4px;font-size:.84rem;line-height:1.8;white-space:pre-wrap;color:var(--cream)">
          </div>

          <!-- Reply Triage Tester -->
          <div style="margin-top:14px;border-top:1px solid var(--line);padding-top:10px">
            <span style="font-size:.78rem;color:var(--muted)">شبیه‌ساز هوشمند دسته‌بندی پاسخ مخاطب (توقف خودکار زنجیره):</span>
            <div style="display:flex;gap:8px;margin-top:6px;flex-wrap:wrap">
              <button class="btn btn--ghost" onclick="testV2Reply('علاقه‌مند', 'سلام عالیه، سه‌شنبه ۱۰ صبح تماس بگیرید صحبت کنیم.')" style="font-size:.72rem;padding:3px 10px;color:#2ecc71;border-color:#2ecc71">
                تست: علاقه‌مند (جلسه)
              </button>
              <button class="btn btn--ghost" onclick="testV2Reply('بعداً', 'الان سرمون شلوغه لطفا ماه بعد پیام بدید.')" style="font-size:.72rem;padding:3px 10px;color:#ffd21e;border-color:#ffd21e">
                تست: بعداً (یادآور)
              </button>
              <button class="btn btn--ghost" onclick="testV2Reply('نه', 'متشکرم، تمایلی به همکاری نداریم.')" style="font-size:.72rem;padding:3px 10px;color:#e57373;border-color:#e57373">
                تست: نه (توقف)
              </button>
              <button class="btn btn--ghost" onclick="testV2Reply('لغو', 'لطفا من را حذف کنید و دیگر ایمیل نزنید.')" style="font-size:.72rem;padding:3px 10px;color:#ef4444;border-color:#ef4444">
                تست: لغو (لیست حذف)
              </button>
            </div>
            <div id="v2ReplyResult" style="display:none;margin-top:8px;padding:8px 12px;border-radius:4px;font-size:.78rem"></div>
          </div>

        </div>
      </div>

    </section>

    <!-- JAVASCRIPT LOGIC FOR MODULE 15 -->
    <script>
      var currentV2Stage = 1;

      function showV2SkillTab(tabId) {
        document.querySelectorAll('.v2-skill-content').forEach(function(el) {
          el.style.display = 'none';
        });
        document.getElementById('tab-' + tabId).style.display = 'block';

        ['target', 'copy', 'deliv', 'auto', 'privacy'].forEach(function(k) {
          var btn = document.getElementById('btn-v2-' + k);
          if (btn) {
            btn.className = (k === tabId.replace('v2-', '')) ? 'btn btn--gold' : 'btn btn--ghost';
          }
        });
      }

      function setV2Stage(stage) {
        currentV2Stage = stage;
        [1, 2, 3].forEach(function(s) {
          var btn = document.getElementById('btn-v2-stage' + s);
          if (btn) btn.className = (s === stage) ? 'btn btn--gold' : 'btn btn--ghost';
        });
        updateV2Simulation();
      }

      function updateV2Simulation() {
        var entity = document.getElementById('v2EntitySelect').value;
        var subElem = document.getElementById('v2SimSubject');
        var preElem = document.getElementById('v2SimPreheader');
        var bodyElem = document.getElementById('v2SimBody');
        var badgeElem = document.getElementById('v2WordBadge');

        if (currentV2Stage === 1) {
          subElem.textContent = "تحلیل ۵,۰۵۵ نقد " + entity + " + پادکست اختصاصی";
          preElem.textContent = "خلاصه ممیزی نظرات تریپ‌ادوایزر و راهکارهای افزایش سودآوری " + entity;
          bodyElem.textContent = "سلام و احترام مدیریت محترم " + entity + "،\\n\\n" +
            "در پایش هفتگی نظرات گردشگران تکسیم، ممیزی عمیق ۵,۰۵۵ نظر " + entity + " در گوگل مپ، تریپ‌ادوایزر و یاندکس آماده شد.\\n\\n" +
            "۳ یافته کلیدی برای شما:\\n" +
            "• رضایت فوق‌العاده ۸۹٪ از طعم اصیل و کیفیت کباب‌ها\\n" +
            "• شناسایی ابهام توریست‌های اروپایی در فاکتور چای و کوور\\n" +
            "• راهکار آزادسازی +۱۸۰,۰۰۰ لیر درآمد در ساعات خلوت عصرگاهی\\n\\n" +
            "پادکست صوتی سه‌دقیقه‌ای و گزارش کامل PDF را پیوست کرده‌ام.\\n\\n" +
            "آیا فرصت دارید سه‌شنبه ۱۵ دقیقه درباره راهکارهای اجرایی صحبت کوتاهی داشته باشیم؟\\n\\n" +
            "ارادتمند،\\nتیم هوش تجاری میزبان استانبول\\nmizbanistanbul.com\\n\\n" +
            "پی‌نوشت: برای عدم دریافت پیام‌های بعدی، کافیست پاسخ دهید «لغو».";
        } else if (currentV2Stage === 2) {
          subElem.textContent = "پیگیری گزارش ممیزی نظرات " + entity;
          preElem.textContent = "چکیده راهکارهای جذب گردشگران هتل‌های لوکس تکسیم";
          bodyElem.textContent = "سلام مجدد خدمت مدیریت محترم " + entity + "،\\n\\n" +
            "پیرو پیام قبلی، در گزارش تحلیلی " + entity + " راهکاری برای هدایت مهمانان هتل‌های ۵ ستاره اطراف تکسیم به سالن شما طراحی کرده‌ایم.\\n\\n" +
            "خوشحال می‌شوم اگر در یک تماس کوتاه ۱۰ دقیقه‌ای، نتایج پایش تریپ‌ادوایزر و راهکار رفع ابهام فاکتور را مرور کنیم.\\n\\n" +
            "آیا چهارشنبه این هفته زمان مناسبی برای شما هست؟\\n\\n" +
            "با احترام،\\nتیم میزبان استانبول\\nmizbanistanbul.com";
        } else {
          subElem.textContent = "آخرین پیام: بسته ممیزی " + entity;
          preElem.textContent = "بایگانی پرونده تحلیل نظرات و آرزوی موفقیت برای مجموعه شما";
          bodyElem.textContent = "سلام مجدد مدیریت محترم " + entity + "،\\n\\n" +
            "با توجه به مشغله مدیریت سالن، این آخرین پیام پیگیری من است و پرونده ممیزی " + entity + " را بایگانی می‌کنم تا مزاحم وقت ارزشمندتان نشوم.\\n\\n" +
            "لینک گزارش تحلیلی و پادکست صوتی همچنان برای شما فعال است:\\n" +
            "https://mizbanistanbul.com/shamse_sentiment_report.html\\n\\n" +
            "اگر هر زمان تصمیم به ارتقای سیستم ممیزی نظرات و جذب توریست‌های بین‌المللی گرفتید، در خدمتتان خواهیم بود.\\n\\n" +
            "با آرزوی درخشش روزافزون،\\nتیم هوش تجاری میزبان استانبول";
        }

        var words = bodyElem.textContent.trim().split(/\\s+/).length;
        badgeElem.textContent = words + " کلمه (سبز در لینت ✓)";
      }

      function testV2Reply(intent, sampleText) {
        var box = document.getElementById('v2ReplyResult');
        box.style.display = 'block';

        if (intent === 'علاقه‌مند') {
          box.style.background = 'rgba(46,204,113,0.15)';
          box.style.color = '#2ecc71';
          box.style.border = '1px solid #2ecc71';
          box.innerHTML = '<b>دسته‌بندی مدل: علاقه‌مند (Interested) ✓</b><br>متن ورودی: «' + sampleText + '»<br>⚡ اقدام خودکار: توقف توالی پیگیری + ثبت فوری جلسه در تقویم کاری اپراتور.';
        } else if (intent === 'بعداً') {
          box.style.background = 'rgba(255,210,30,0.15)';
          box.style.color = '#ffd21e';
          box.style.border = '1px solid #ffd21e';
          box.innerHTML = '<b>دسته‌بندی مدل: بعداً (Postponed) ⏱</b><br>متن ورودی: «' + sampleText + '»<br>⚡ اقدام خودکار: توقف کمپین فعلی + تنظیم یادآور خودکار برای ۳۰ روز آینده.';
        } else if (intent === 'نه') {
          box.style.background = 'rgba(229,115,115,0.15)';
          box.style.color = '#e57373';
          box.style.border = '1px solid #e57373';
          box.innerHTML = '<b>دسته‌بندی مدل: عدم تمایل (Rejection) ✕</b><br>متن ورودی: «' + sampleText + '»<br>⚡ اقدام خودکار: توقف کامل، ثبت بازخورد در دیتابیس بدون مزاحمت مجدد.';
        } else {
          box.style.background = 'rgba(239,68,68,0.15)';
          box.style.color = '#ef4444';
          box.style.border = '1px solid #ef4444';
          box.innerHTML = '<b>دسته‌بندی مدل: لغو و حذف اشتراک (Unsubscribe) ⛔</b><br>متن ورودی: «' + sampleText + '»<br>⚡ اقدام خودکار: توقف آنی + اضافه شدن ایمیل به فایل suppression.jsonl به عنوان لیست سیاه.';
        }
      }

      document.addEventListener("DOMContentLoaded", function() {
        updateV2Simulation();
      });
    </script>
'''

with open(INTEL_HTML, "r", encoding="utf-8") as f:
    html = f.read()

target = '<!-- ATIKOVA INTEGRATION BANNER & INTERACTIVE DRAWER -->'
if 'id="mod-outreach-v2"' not in html:
    html = html.replace(target, MODULE_15_HTML + "\n\n    " + target, 1)
    with open(INTEL_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print("Module 15 added to intelligence.html successfully!")
else:
    print("Module 15 already present in intelligence.html!")
