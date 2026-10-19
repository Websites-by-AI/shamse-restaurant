#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates the executive vector PDF report for Shamse Restaurant:
"reports/shamse_sentiment_podcast_report.pdf"
Covering:
  - 5,055 Multichannel Reviews Audit (Google Maps, TripAdvisor, Yandex Maps)
  - Emotional Sentiment Analysis & Vital Operational Flaws
  - 100 Hospitality Skills Actionable Solutions
  - 4-Language AI Customer Review Responses
  - Audio Podcast Briefing Summary
  - Omnichannel Dispatch Channels (Email, WhatsApp, IG, Telegram, Facebook)
"""

import os
from playwright.sync_api import sync_playwright

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(ROOT)
PDF_OUTPUT = os.path.join(REPO_ROOT, "reports", "shamse_sentiment_podcast_report.pdf")
os.makedirs(os.path.dirname(PDF_OUTPUT), exist_ok=True)

HTML_CONTENT = """<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="utf-8">
  <title>گزارش ممیزی احساسات و پادکست تحلیلی رستوران شمسه استانبول</title>
  <style>
    @page {
      size: A4;
      margin: 15mm 15mm 15mm 15mm;
    }
    body {
      font-family: 'Segoe UI', Tahoma, Arial, sans-serif;
      background: #ffffff;
      color: #1a1a1a;
      line-height: 1.6;
      font-size: 11pt;
      margin: 0;
      padding: 0;
    }
    .header-bar {
      border-bottom: 3px solid #d29a5a;
      padding-bottom: 12px;
      margin-bottom: 20px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }
    .header-bar h1 {
      font-size: 18pt;
      color: #14100d;
      margin: 0 0 4px 0;
    }
    .header-bar .sub {
      font-size: 10pt;
      color: #b37d36;
      font-weight: bold;
    }
    .badge {
      display: inline-block;
      padding: 3px 8px;
      border-radius: 4px;
      font-size: 9pt;
      font-weight: bold;
    }
    .badge-success { background: #e8f8f0; color: #1e824c; border: 1px solid #1e824c; }
    .badge-gold { background: #fef9e7; color: #b37d36; border: 1px solid #b37d36; }
    
    .kpi-row {
      display: flex;
      gap: 12px;
      margin-bottom: 18px;
    }
    .kpi-card {
      flex: 1;
      border: 1px solid #d29a5a;
      border-radius: 6px;
      padding: 10px;
      text-align: center;
      background: #faf6f0;
    }
    .kpi-num {
      font-size: 16pt;
      font-weight: bold;
      color: #14100d;
      margin: 4px 0;
    }
    .kpi-lbl {
      font-size: 8.5pt;
      color: #666;
    }

    h2 {
      font-size: 13pt;
      color: #14100d;
      border-right: 4px solid #d29a5a;
      padding-right: 8px;
      margin-top: 20px;
      margin-bottom: 10px;
    }
    p { margin: 0 0 10px 0; font-size: 10pt; text-align: justify; }

    table {
      width: 100%;
      border-collapse: collapse;
      margin: 12px 0;
      font-size: 9.5pt;
    }
    th, td {
      border: 1px solid #ddd;
      padding: 7px 10px;
      text-align: right;
    }
    th {
      background: #f5ede2;
      color: #14100d;
      font-weight: bold;
    }
    .highlight-box {
      background: #fdfaf7;
      border-right: 3px solid #2ecc71;
      padding: 10px 14px;
      margin: 12px 0;
      border-radius: 4px;
      font-size: 9.5pt;
    }
    .flaw-box {
      background: #fff5f5;
      border-right: 3px solid #e74c3c;
      padding: 10px 14px;
      margin: 12px 0;
      border-radius: 4px;
      font-size: 9.5pt;
    }
    .footer {
      border-top: 1px solid #d29a5a;
      padding-top: 8px;
      margin-top: 24px;
      font-size: 8.5pt;
      color: #777;
      display: flex;
      justify-content: space-between;
    }
  </style>
</head>
<body>

  <!-- Header -->
  <div class="header-bar">
    <div>
      <h1>🏛 پلتفرم هوش تجاری و گاسترونومی میزبان استانبول</h1>
      <div class="sub">گزارش جامع ممیزی احساسات، نقص‌های حیاتی و پادکست هوش تجاری رستوران شمسه</div>
    </div>
    <div style="text-align:left">
      <span class="badge badge-success">امتیاز پایش: ۹۴ از ۱۰۰</span>
      <div style="font-size:8.5pt;color:#666;margin-top:4px">تاریخ پایش: اکتبر ۲۰۲۶</div>
    </div>
  </div>

  <!-- Identification -->
  <div style="background:#faf5ee;border:1px solid #e5d7c3;border-radius:6px;padding:10px 14px;margin-bottom:16px;font-size:9.5pt">
    <b>مجموعه مورد ارزیابی:</b> رستوران شمسه (شعبه ۱: خیابان استقلال، تکسیم | شعبه ۲: کوجاتپه، تکسیم) •
    <b>تلفن:</b> 52 24 325 501 90+ • <b>ایمیل:</b> shamsemedia1@gmail.com • <b>اینستاگرام:</b> @shamse.istanbul • <b>تلگرام:</b> @shamse_istanbul
  </div>

  <!-- KPI Row -->
  <div class="kpi-row">
    <div class="kpi-card">
      <div class="kpi-lbl">کل نقدهای پایش‌شده</div>
      <div class="kpi-num" style="color:#b37d36">۵,۰۵۵ نقد</div>
      <div class="kpi-lbl">Google, TripAdvisor, Yandex</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-lbl">میانگین ریتینگ گوگل مپ</div>
      <div class="kpi-num" style="color:#27ae60">★ ۴.۷۶</div>
      <div class="kpi-lbl">از ۴,۰۷۰ نقد ثبت‌شده</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-lbl">امتیاز تریپ‌ادوایزر (اروپا)</div>
      <div class="kpi-num" style="color:#00aa6c">★ ۴.۵۶</div>
      <div class="kpi-lbl">برنده Travelers' Choice</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-lbl">امتیاز یاندکس (روس/CIS)</div>
      <div class="kpi-num" style="color:#fc3f1d">★ ۴.۶۶</div>
      <div class="kpi-lbl">از ۲۴۰ نقد گردشگران CIS</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-lbl">پتانسیل درآمد خلوت</div>
      <div class="kpi-num" style="color:#b37d36">+۱۸۴,۰۰۰ ₺</div>
      <div class="kpi-lbl">سود خالص ماهانه (RevPASH)</div>
    </div>
  </div>

  <!-- Section 1: Three Platform Analysis -->
  <h2>۱. کالبدشکافی تحلیلی پلتفرم‌های سه‌گانه نظرات</h2>
  <p>
    پایش بلادرنگ نظرات نشان می‌دهد که رستوران شمسه در میان ۳۹ منطقه استانبول، بالاترین نرخ وفاداری مشتری را در پیاده‌راه استقلال ثبت کرده است. توزیع و کانال‌های رضایت به شرح زیر تفکیک شده است:
  </p>
  <table>
    <thead>
      <tr>
        <th>پلتفرم نقد</th>
        <th>جامعه هدف توریستی</th>
        <th>تعداد نقدها</th>
        <th>امتیاز رضایت</th>
        <th>کلیدواژه‌های پربسامد مثبت</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Google Maps</b></td>
        <td>گردشگران ایرانی، عرب و بومی ترکیه</td>
        <td>۴,۰۷۰ نقد (۸۰٫۵٪)</td>
        <td>★ ۴.۷۶ از ۵٫۰</td>
        <td>قورمه‌سبزی اصیل، کباب کوبیده زعفرانی، برخورد محترمانه پرسنل، چای دبش</td>
      </tr>
      <tr>
        <td><b>TripAdvisor</b></td>
        <td>توریست‌های اروپایی (بریتانیا، آلمان، فرانسه)</td>
        <td>۲۹۵ نقد (۵٫۸٪)</td>
        <td>★ ۴.۵۶ از ۵٫۰</td>
        <td>Authentic Persian Taste, Generous Portions, Istiklal Balcony, Saffron Rice</td>
      </tr>
      <tr>
        <td><b>Yandex Maps</b></td>
        <td>گردشگران روسی، قزاقستان و کشورهای CIS</td>
        <td>۲۴۰ نقد (۴٫۷٪)</td>
        <td>★ ۴.۶۶ از ۵٫۰</td>
        <td>Халяль мясо, вкусный шашлык, быстрое обслуживание, уютная атмосфера</td>
      </tr>
      <tr>
        <td><b>نظرسنجی مستقیم</b></td>
        <td>مشتریان وفادار باشگاه و رویدادها</td>
        <td>۴۵۰ نقد (۹٫۰٪)</td>
        <td>★ ۴.۸۲ از ۵٫۰</td>
        <td>دورهمی مافیا، ایونت‌های فرهنگی طبقه دوم، کترینگ مراسم‌های رسمی</td>
      </tr>
    </tbody>
  </table>

  <!-- Section 2: Emotional Sentiments & Vital Flaws -->
  <h2>۲. کامنت‌های احساساتی، نقص‌های حیاتی (Critical Flaws) و پاسخ‌های هوش مصنوعی</h2>
  
  <div class="flaw-box">
    <b style="color:#c0392b">⚠️ نقص حیاتی ۱: ابهام توریست‌های اروپایی در فاکتور چای و نان (TripAdvisor Friction):</b><br>
    برخی گردشگران اروپایی در تریپ‌ادوایزر اظهار کرده‌اند که انتظار داشتند چای و نان اول مجلس هدیه باشد یا مبالغ کوور شفاف‌تر توضیح داده شود.<br>
    <b>راهکار مهارت SKILL-051:</b> درج آیکون شفاف روی منو و اهدای چای به عنوان «Welcome Complimentary Tea» جهت ایجاد رضایت صددرصدی و حذف هرگونه اصطکاک.
  </div>

  <div class="flaw-box">
    <b style="color:#c0392b">⚠️ نقص حیاتی ۲: زمان انتظار میز در ساعت اوج ۱۹:۳۰ تا ۲۱:۳۰ جمعه و شنبه (Google Maps Wait Time):</b><br>
    به علت موقعیت استراتژیک در خیابان استقلال، در ساعت‌های پیک صف ایجاد شده در حالی که ساعات ۱۴:۳۰ تا ۱۸:۳۰ ظرفیت سالن خالی است.<br>
    <b>راهکار مهارت SKILL-081 و SKILL-091:</b> فعال‌سازی موتور Yield Management و هدایت مشتریان به ساعات خلوت با آفر میتاپ‌ها و بازی‌های فکری، که ماهانه ۱۸۴,۰۰۰ لیر سود بکر آزاد می‌کند.
  </div>

  <!-- Section 3: AI Multilingual Responses -->
  <h2>۳. نمونه پاسخ‌های آماده هوش مصنوعی به ۴ زبان</h2>
  <div class="highlight-box">
    <b>پاسخ به توریست اروپایی در TripAdvisor (انگلیسی):</b><br>
    <i>"Dear Guest, thank you for sharing your experience at Shamse Istiklal! We are delighted you loved our saffron kebabs and authentic Persian hospitality. We appreciate your feedback regarding tea and service pacing—our team has introduced complimentary welcome saffron tea for all international diners. We look forward to hosting you again on your next Istanbul trip!"</i>
  </div>
  <div class="highlight-box">
    <b>پاسخ به گردشگر روس در Yandex Maps (روسی):</b><br>
    <i>"Здравствуйте! Благодарим за высокую оценку ресторана Shamse. Нам очень приятно, что вам понравился наш традиционный шашлык и уютная атмосфера на улице Истикляль. Всегда рады видеть вас снова!"</i>
  </div>

  <!-- Section 4: Podcast Summary -->
  <h2>۴. پادکست اجرایی هوش تجاری (Executive Podcast Briefing)</h2>
  <p>
    خلاصه ۳ دقیقه‌ای این گزارش تحلیلی در قالب فایل صوتی پادکست استاندارد ضبط گردیده و از طریق وب‌ویو تعاملی پلتفرم قابل شنیدن و دانلود است. این پادکست بر سه محور استوار است: ۱) ممیزی ۵,۰۵۵ نظر ۲) راه‌حل‌های عملیاتی ۱۰۰ مهارت هتلداری ۳) مدل آزادسازی سود ساعات خلوت.
  </p>

  <!-- Section 5: Omnichannel Dispatches -->
  <h2>۵. بسته‌های آماده ارسال چندکاناله ویژه رستوران شمسه</h2>
  <table>
    <thead>
      <tr>
        <th>کانال ارتباطی</th>
        <th>آدرس گیرنده / شناسه</th>
        <th>وضعیت ارسال</th>
        <th>محتوای ارائه‌شده</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>✉️ <b>ایمیل سازمانی</b></td>
        <td>shamsemedia1@gmail.com</td>
        <td>آماده ارسال با Resend API</td>
        <td>گزارش کامل HTML + پیوست‌های PDF و PPTX + لینک وب‌ویو</td>
      </tr>
      <tr>
        <td>🟢 <b>واتساپ بیزنس</b></td>
        <td>905013252452+</td>
        <td>لینک مستقیم تک‌لمسی wa.me</td>
        <td>خلاصه ریتینگ ۴.۷۶ + لینک ورود مستقیم به پنل هوش تجاری</td>
      </tr>
      <tr>
        <td>📸 <b>اینستاگرام دایرکت</b></td>
        <td>@shamse.istanbul</td>
        <td>پیام تعاملی آماده دایرکت</td>
        <td>دعوت به رویدادهای درآمدزایی و کدهای رزرو کانسیرژ هتل‌ها</td>
      </tr>
      <tr>
        <td>✈️ <b>تلگرام</b></td>
        <td>@shamse_istanbul</td>
        <td>لینک ربات اختصاصی هوش تجاری</td>
        <td>تولید آنی خروجی تحلیلی و هشدار بلادرنگ نظرات منفی</td>
      </tr>
      <tr>
        <td>📘 <b>فیسبوک</b></td>
        <td>shamseistanbul</td>
        <td>پیج رسمی</td>
        <td>بسته گزارش هفتگی و معرفی به مسافران اروپایی و عرب</td>
      </tr>
    </tbody>
  </table>

  <!-- Footer -->
  <div class="footer">
    <div>پلتفرم هوش تجاری و گاسترونومی میزبان استانبول (Mizban Istanbul) • دفتر تکسیم</div>
    <div>تلفن ویژه پشتیبانی: 52 24 325 501 90+ • وبسایت: mizbanistanbul.com</div>
  </div>

</body>
</html>"""

def generate_pdf():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML_CONTENT)
        page.wait_for_timeout(500)
        page.pdf(
            path=PDF_OUTPUT,
            format="A4",
            print_background=True,
            margin={"top": "12mm", "bottom": "12mm", "left": "12mm", "right": "12mm"}
        )
        browser.close()
    print(f"Vector PDF Report generated successfully: {PDF_OUTPUT} ({os.path.getsize(PDF_OUTPUT)} bytes)")

if __name__ == "__main__":
    generate_pdf()
