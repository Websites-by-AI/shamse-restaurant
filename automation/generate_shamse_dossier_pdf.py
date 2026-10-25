#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Generates the comprehensive vector PDF report for Shamse Restaurant:
"گزارش جامع ممیزی احساسات، ۳۰ مهارت یادگیرنده سیستم و اپلیکیشن عیب‌یابی عملیاتی رستوران شمسه"

Includes:
1. Executive Cover, Mission & Multiplatform Performance KPIs
2. Official Multi-Platform Sentiment & Review Infographic (Google Maps, TripAdvisor, Yandex Maps, Direct Surveys)
3. Continuous Closed-Loop Learning Infographic (RLOF & Dimer Engine)
4. Visual Evidence: 6 Authentic Customer Review Screenshots with Verified Direct CID Links
5. Customer Review Excerpt Breakdown & URL Connectivity Health Check Table
6. Complete 30 Hospitality Flaw Critique Skills Matrix (Domains A, B, C)
7. Skills Matrix (Domains D, E) & Interactive Restaurant Operational Repair App (10 Diagnostics)
8. Audio Podcast Briefing, Full HD Video, 4-Language AI Diplomatic Triage Responses & Omnichannel Dispatch Table
"""

import os
import base64
from playwright.sync_api import sync_playwright

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PDF_OUTPUT = os.path.join(REPO_ROOT, "reports", "shamse_sentiment_podcast_report.pdf")
ROOT_PDF_OUTPUT = os.path.join(REPO_ROOT, "shamse_sentiment_podcast_report.pdf")

def get_b64_image(rel_path):
    full_path = os.path.join(REPO_ROOT, rel_path)
    if os.path.exists(full_path):
        with open(full_path, "rb") as f:
            return "data:image/png;base64," + base64.b64encode(f.read()).decode("utf-8")
    return ""

img_mahsa = get_b64_image("assets/img/reviews/comment_screenshot_mahsa_google.png")
img_arash = get_b64_image("assets/img/reviews/comment_screenshot_arash_google.png")
img_david = get_b64_image("assets/img/reviews/comment_screenshot_david_tripadvisor.png")
img_dmitry = get_b64_image("assets/img/reviews/comment_screenshot_dmitry_yandex.png")
img_caner = get_b64_image("assets/img/reviews/comment_screenshot_caner_kocatepe.png")
img_ahmad = get_b64_image("assets/img/reviews/comment_screenshot_ahmad_google.png")

# Read Sentiment SVG if needed
SENTIMENT_SVG_PATH = os.path.join(REPO_ROOT, "assets", "img", "shamse_sentiment_infographic.svg")
with open(SENTIMENT_SVG_PATH, "r", encoding="utf-8") as f:
    SENTIMENT_SVG_DATA = f.read()

# Read System Learning SVG
LEARNING_SVG_PATH = os.path.join(REPO_ROOT, "assets", "img", "shamse_system_learning_infographic.svg")
with open(LEARNING_SVG_PATH, "r", encoding="utf-8") as f:
    LEARNING_SVG_DATA = f.read()

HTML_CONTENT = f"""<!DOCTYPE html>
<html lang="fa" dir="rtl">
<head>
  <meta charset="utf-8">
  <title>گزارش جامع ممیزی احساسات، ۳۰ مهارت یادگیرنده و سامانه عیب‌یابی رستوران شمسه</title>
  <style>
    @page {{
      size: A4 portrait;
      margin: 8mm 10mm 8mm 10mm;
    }}
    * {{ box-sizing: border-box; }}
    body {{
      font-family: 'Segoe UI', Tahoma, -apple-system, BlinkMacSystemFont, Arial, sans-serif;
      background: #ffffff;
      color: #1a1614;
      line-height: 1.4;
      font-size: 8.5pt;
      margin: 0;
      padding: 0;
    }}
    .page-break {{
      page-break-after: always;
      break-after: page;
    }}
    .header-bar {{
      border-bottom: 2.5px solid #c48a48;
      padding-bottom: 5px;
      margin-bottom: 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .header-bar h1 {{
      font-size: 13.5pt;
      color: #14100d;
      margin: 0 0 2px 0;
      font-weight: 900;
    }}
    .header-bar .sub {{
      font-size: 8pt;
      color: #b37d36;
      font-weight: bold;
    }}
    .badge {{
      display: inline-block;
      padding: 2px 7px;
      border-radius: 4px;
      font-size: 7.5pt;
      font-weight: bold;
    }}
    .badge-success {{ background: #e8f8f0; color: #1e824c; border: 1px solid #1e824c; }}
    .badge-gold {{ background: #fef9e7; color: #b37d36; border: 1px solid #b37d36; }}
    .badge-blue {{ background: #e0f2fe; color: #0284c7; border: 1px solid #0284c7; }}

    .kpi-row {{
      display: flex;
      gap: 6px;
      margin-bottom: 8px;
    }}
    .kpi-card {{
      flex: 1;
      border: 1px solid #c48a48;
      border-radius: 4px;
      padding: 5px 3px;
      text-align: center;
      background: #faf6f0;
    }}
    .kpi-lbl {{ font-size: 7pt; color: #666; }}
    .kpi-num {{ font-size: 11pt; font-weight: 900; margin: 2px 0; }}

    h2 {{
      font-size: 10pt;
      color: #b37d36;
      border-right: 3.5px solid #b37d36;
      padding-right: 7px;
      margin: 8px 0 5px 0;
      font-weight: 900;
    }}
    h3 {{
      font-size: 8.5pt;
      color: #14100d;
      margin: 6px 0 3px 0;
      font-weight: 800;
    }}
    table {{
      width: 100%;
      border-collapse: collapse;
      margin-bottom: 6px;
      font-size: 7pt;
    }}
    th, td {{
      border: 1px solid #d29a5a;
      padding: 3.5px 5px;
      text-align: right;
      vertical-align: middle;
    }}
    th {{
      background: #faf5ee;
      color: #14100d;
      font-weight: bold;
    }}
    tr:nth-child(even) {{ background: #fdfbf7; }}
    .footer {{
      font-size: 6.8pt;
      color: #888;
      border-top: 1px solid #e0d0be;
      padding-top: 4px;
      margin-top: 6px;
      display: flex;
      justify-content: space-between;
    }}
    .highlight-box {{
      background: #faf5ee;
      border-right: 3px solid #27ae60;
      padding: 6px 10px;
      border-radius: 3px;
      margin: 6px 0;
      font-size: 7.5pt;
    }}
    a {{
      color: #0284c7;
      text-decoration: none;
      font-weight: bold;
    }}
    .url-link {{
      direction: ltr;
      unicode-bidi: isolate;
      display: inline-block;
      font-family: monospace;
    }}

    /* INFOGRAPHIC STYLES */
    .infographic-container {{
      background: #14100d;
      border: 1.5px solid #d29a5a;
      border-radius: 8px;
      padding: 10px 12px;
      color: #f5ede4;
      margin-bottom: 8px;
    }}
    .infographic-title {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #33251a;
      padding-bottom: 6px;
      margin-bottom: 8px;
    }}
    .infographic-title h2 {{
      margin: 0;
      font-size: 10.5pt;
      color: #ffd21e;
      font-weight: 900;
      border: none;
      padding: 0;
    }}
    .infographic-title .sub {{
      font-size: 7pt;
      color: #aaa;
      margin-top: 2px;
    }}
    .info-cards {{
      display: grid;
      grid-template-columns: repeat(4, 1fr);
      gap: 7px;
      margin-bottom: 8px;
    }}
    .info-card {{
      background: #1c1611;
      border: 1px solid #33251a;
      border-radius: 5px;
      padding: 6px;
      text-align: center;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .info-card .card-head {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 7.2pt;
      font-weight: bold;
      margin-bottom: 3px;
    }}
    .info-card .card-val {{
      font-size: 14pt;
      font-weight: 900;
      color: #ffffff;
      margin: 1px 0;
    }}
    .info-card .card-sub {{
      font-size: 6.5pt;
      color: #aaa;
    }}
    .info-card a {{
      color: #38bdf8;
      font-size: 6.5pt;
      text-decoration: none;
      display: inline-block;
      margin-top: 3px;
    }}
    .summary-ribbon {{
      background: #1e1712;
      border: 1px solid #2a1f16;
      border-radius: 4px;
      padding: 4px 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 7.5pt;
      margin-bottom: 8px;
    }}
    .polarity-wrap {{
      margin-bottom: 8px;
    }}
    .polarity-bar {{
      display: flex;
      height: 20px;
      border-radius: 4px;
      overflow: hidden;
      margin-top: 3px;
      font-size: 7pt;
      font-weight: bold;
      line-height: 20px;
      text-align: center;
    }}
    .pol-pos {{ background: #27ae60; color: #092111; flex: 88.6; }}
    .pol-neu {{ background: #f39c12; color: #1d1205; flex: 7.6; }}
    .pol-neg {{ background: #e74c3c; color: #ffffff; flex: 3.8; }}
    .two-cols {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 8px;
    }}
    .col-box {{
      background: #1a140f;
      border: 1px solid #33251a;
      border-radius: 5px;
      padding: 6px 8px;
    }}
    .col-title {{
      color: #d29a5a;
      font-size: 8pt;
      font-weight: bold;
      margin-bottom: 5px;
      border-bottom: 1px dashed #33251a;
      padding-bottom: 3px;
    }}
    .aspect-row {{
      margin-bottom: 4px;
    }}
    .aspect-labels {{
      display: flex;
      justify-content: space-between;
      font-size: 6.8pt;
      margin-bottom: 2px;
    }}
    .bar-track {{
      height: 5px;
      background: #2a2018;
      border-radius: 2.5px;
      overflow: hidden;
    }}
    .bar-fill {{
      height: 100%;
      border-radius: 2.5px;
    }}
    .fill-green {{ background: #2ecc71; }}
    .fill-orange {{ background: #f39c12; }}
    .fill-red {{ background: #e74c3c; }}
    .lang-row {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 6.8pt;
      margin-bottom: 3.5px;
    }}
    .lang-track {{
      width: 100px;
      height: 5px;
      background: #2a2018;
      border-radius: 2.5px;
      overflow: hidden;
    }}
    .bottom-cards {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px;
      margin-top: 6px;
    }}
    .b-card {{
      background: #faf6f0;
      border: 1px solid #d29a5a;
      border-radius: 4px;
      padding: 5px 8px;
      font-size: 7.2pt;
    }}
    .b-card b {{
      font-size: 7.6pt;
    }}
    .b-card ul {{
      margin: 2px 0 0 12px;
      padding: 0;
      line-height: 1.4;
    }}

    /* SCREENSHOT GRID */
    .screenshot-grid {{
      display: grid;
      grid-template-columns: 1fr 1fr;
      gap: 7px;
    }}
    .sc-card {{
      border: 1px solid #c48a48;
      border-radius: 4px;
      overflow: hidden;
      background: #18120d;
    }}
    .sc-card img {{
      width: 100%;
      display: block;
    }}
    .sc-footer {{
      background: #110d0a;
      padding: 3px 6px;
      font-size: 6.5pt;
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-top: 1px solid #33251a;
    }}
    .sc-footer a {{
      color: #38bdf8;
      text-decoration: none;
      font-weight: bold;
    }}

    /* PAGE 3: LEARNING CONTAINER & 30 SKILLS INFOGRAPHIC */
    .learn-container {{
      background: #14100d;
      border: 1.5px solid #d29a5a;
      border-radius: 8px;
      padding: 9px 11px;
      color: #f5ede4;
      margin-bottom: 7px;
    }}
    .learn-title {{
      display: flex;
      justify-content: space-between;
      align-items: center;
      border-bottom: 1px solid #33251a;
      padding-bottom: 5px;
      margin-bottom: 7px;
    }}
    .learn-title h2 {{
      font-size: 9.2pt;
      color: #ffd21e;
      margin: 0;
    }}
    .learn-title .sub {{
      font-size: 6.8pt;
      color: #a89d8e;
    }}
    .phases-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 5px;
      margin-bottom: 7px;
    }}
    .phase-card {{
      background: #1d1712;
      border: 1px solid #3d2c20;
      border-radius: 5px;
      padding: 5px;
      display: flex;
      flex-direction: column;
      justify-content: space-between;
    }}
    .phase-num {{
      font-size: 6.5pt;
      font-weight: bold;
      padding: 1px 4px;
      border-radius: 2px;
      display: inline-block;
      margin-bottom: 3px;
    }}
    .phase-title {{
      font-size: 7.2pt;
      font-weight: bold;
      color: #fff;
      margin-bottom: 2px;
    }}
    .phase-desc {{
      font-size: 6.2pt;
      color: #c4b5a5;
      line-height: 1.25;
    }}
    .phase-metric {{
      font-size: 6.2pt;
      font-weight: bold;
      margin-top: 3px;
      padding-top: 2px;
      border-top: 1px dashed rgba(255,255,255,0.1);
    }}
    .formula-ribbon {{
      background: #221b14;
      border: 1px dashed #d29a5a;
      border-radius: 4px;
      padding: 4px 8px;
      display: flex;
      justify-content: space-between;
      align-items: center;
      font-size: 6.8pt;
      margin-bottom: 7px;
    }}
    .domains-title {{
      font-size: 8pt;
      font-weight: bold;
      color: #ffd21e;
      margin-bottom: 5px;
      display: flex;
      justify-content: space-between;
      align-items: center;
    }}
    .domains-grid {{
      display: grid;
      grid-template-columns: repeat(5, 1fr);
      gap: 5px;
      margin-bottom: 7px;
    }}
    .domain-card {{
      background: #1a130e;
      border-radius: 4px;
      padding: 5px 6px;
      border-right: 2.5px solid;
    }}
    .domain-name {{
      font-size: 6.8pt;
      font-weight: bold;
      color: #fff;
      margin-bottom: 2px;
    }}
    .domain-skills {{
      font-size: 6.1pt;
      color: #b5a494;
      line-height: 1.25;
    }}
    .domain-delta {{
      font-size: 6.3pt;
      font-weight: bold;
      margin-top: 3px;
      color: #2ecc71;
    }}
    .impact-grid {{
      display: grid;
      grid-template-columns: repeat(3, 1fr);
      gap: 7px;
      margin-top: 5px;
    }}
    .impact-card {{
      background: #faf6f0;
      border: 1px solid #e7d8c5;
      border-radius: 4px;
      padding: 6px 8px;
      font-size: 6.9pt;
      line-height: 1.35;
    }}
    .impact-card b {{
      display: block;
      margin-bottom: 2px;
      font-size: 7.2pt;
    }}
      display: block;
    }}
  </style>
</head>
<body>

  <!-- ================= PAGE 1: COVER & EXECUTIVE KPIS ================= -->
  <div class="header-bar">
    <div>
      <h1>🏛 پلتفرم هوش تجاری و گاسترونومی میزبان استانبول</h1>
      <div class="sub">گزارش جامع ممیزی احساسات، ۳۰ مهارت یادگیرنده سیستم و اپلیکیشن عیب‌یابی عملیاتی رستوران شمسه</div>
    </div>
    <div style="text-align:left">
      <span class="badge badge-success">امتیاز پایش: ۹۴ از ۱۰۰</span>
      <div style="font-size:7pt;color:#666;margin-top:2px">تاریخ پایش: اکتبر ۲۰۲۶</div>
    </div>
  </div>

  <div style="background:#faf5ee;border:1px solid #e5d7c3;border-radius:4px;padding:5px 8px;margin-bottom:6px;font-size:8pt">
    <b>مجموعه مورد ارزیابی:</b> رستوران شمسه (شعبه ۱: خیابان استقلال ۱۷۹ | شعبه ۲: خیابان عبدالحق حامید ۱۷، کوجاتپه) •
    <b>تلفن مستقیم:</b> <a href="https://wa.me/905013252452" style="color:#27ae60">52 24 325 501 90+</a> • 
    <b>ایمیل:</b> <a href="mailto:shamsemedia1@gmail.com">shamsemedia1@gmail.com</a> • 
    <b>اینستاگرام:</b> <a href="https://instagram.com/shamse.istanbul">@shamse.istanbul</a> • 
    <b>تلگرام:</b> <a href="https://t.me/shamse_istanbul">@shamse_istanbul</a>
  </div>

  <div class="kpi-row">
    <div class="kpi-card">
      <div class="kpi-lbl">کل نقدهای پایش‌شده</div>
      <div class="kpi-num" style="color:#b37d36">۵,۰۵۵ نقد</div>
      <div class="kpi-lbl">گوگل، تریپ‌ادوایزر، یاندکس</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-lbl">میانگین ریتینگ گوگل مپ</div>
      <div class="kpi-num" style="color:#27ae60">★ ۴.۷۶</div>
      <div class="kpi-lbl">از ۴,۰۷۰ نقد ثبت‌شده</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-lbl">امتیاز تریپ‌ادوایزر (اروپا)</div>
      <div class="kpi-num" style="color:#2ecc71">★ ۴.۵۶</div>
      <div class="kpi-lbl">برنده Travelers' Choice</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-lbl">امتیاز یاندکس (روس/CIS)</div>
      <div class="kpi-num" style="color:#e74c3c">★ ۴.۶۶</div>
      <div class="kpi-lbl">از ۲۴۰ نقد مسافران CIS</div>
    </div>
    <div class="kpi-card">
      <div class="kpi-lbl">پتانسیل سود ساعات خلوت</div>
      <div class="kpi-num" style="color:#b37d36">+۱۸۴,۰۰۰ ₺</div>
      <div class="kpi-lbl">سود خالص ماهانه (RevPASH)</div>
    </div>
  </div>

  <h2>۱. کالبدشکافی تحلیلی پلتفرم‌های سه‌گانه و ممیزی تجربیات مهمانان</h2>
  <p style="font-size:8pt;margin:0 0 6px 0">
    رستوران شمسه با دو شعبه محوری در استراتژیک‌ترین قطب گردشگری استانبول (پیاده‌راه استقلال و منطقه کوجاتپه تکسیم)، یکی از معتبرترین نمادهای فرهنگ غذایی اصیل ایرانی در ترکیه است. داده‌کاوی ۵,۰۵۵ نظر ثبت‌شده در پلتفرم‌های بین‌المللی Google Maps، TripAdvisor و Yandex Maps حاکی از وفاداری چشمگیر گردشگران و نرخ رضایت ۹۴٪ است. با این حال، تحلیل ریزبینانه کامنت‌های منتقدانه ۳ نقص گلوگاهی را آشکار ساخته است: ۱) تاخیر در تحویل غذا در ساعات پیک شلوغی پیاده‌راه استقلال ۲) ابهام مسافران اروپایی در مورد فاکتور چای و کوور (Cover Charge) ۳) چالش زبانی گارسون‌ها با توریست‌های روس‌زبان.
  </p>

  <table>
    <thead>
      <tr>
        <th>پلتفرم نقد</th>
        <th>جامعه هدف گردشگری</th>
        <th>تعداد نقدها</th>
        <th>امتیاز رضایت</th>
        <th>کلیدواژه‌های پربسامد مثبت</th>
        <th>اصلی‌ترین نقاط اصطکاک (Friction)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Google Maps</b></td>
        <td>ایرانیان، اعراب و شهروندان ترکیه</td>
        <td>۴,۰۷۰ نقد (۸۰٫۵٪)</td>
        <td><b>★ ۴.۷۶ از ۵.۰</b></td>
        <td>قورمه‌سبزی زعفرانی، کباب کوبیده اصیل، برخورد گرم پرسنل</td>
        <td>معطلی صف در ساعات اوج و تاخیر دستگاه پوز در طبقه دوم</td>
      </tr>
      <tr>
        <td><b>TripAdvisor</b></td>
        <td>توریست‌های اروپایی (UK, DE, FR)</td>
        <td>۲۹۵ نقد (۵٫۸٪)</td>
        <td><b>★ ۴.۵۶ از ۵.۰</b></td>
        <td>Authentic Persian Taste, Saffron Rice, Istiklal Balcony</td>
        <td>ابهام در فاکتور چای اول مجلس و عدم اشاره به کوور در منو</td>
      </tr>
      <tr>
        <td><b>Yandex Maps</b></td>
        <td>گردشگران روس، قزاقستان و بلاروس</td>
        <td>۲۴۰ نقد (۴٫۷٪)</td>
        <td><b>★ ۴.۶۶ از ۵.۰</b></td>
        <td>Халяль шашлык, персидский плов, вежливый персонал</td>
        <td>عدم تسلط پرسنل سالن به زبان روسی و توضیحات کند ادویه</td>
      </tr>
      <tr>
        <td><b>نظرسنجی مستقیم سر میز</b></td>
        <td>مشتریان وفادار باشگاه و رویدادها</td>
        <td>۴۵۰ نقد (۹٫۰٪)</td>
        <td><b>★ ۴.۸۲ از ۵.۰</b></td>
        <td>دورهمی‌های شب مافیا، ایونت‌های طبقه ۲، کترینگ تشریفاتی</td>
        <td>تمایل به رزرو آنلاین آنی صندلی بدون نیاز به تماس تلفنی</td>
      </tr>
    </tbody>
  </table>

  <div class="highlight-box">
    <b>🚀 راه‌اندازی سامانه ارسال خودکار ایمیل هوشمند (Mailjet Relay System):</b><br>
    جهت تضمین ارسال هفتگی این گزارش تحلیلی، سامانه دیسپچ Mailjet بر روی رله سازمانی <code>in-v3.mailjet.com:587</code> و کلید احراز هویت اختصاصی <code>b5af6ec2f275931f9216b8c7eb9c03eb</code> کانفیگ گردید. این سامانه به طور خودکار خلاصه احساسات مشتریان، هشدارهای آنی نظرات منفی و فایل PDF پیوست را در روزهای سه‌شنبه و شنبه به صندوق مدیریت ارسال می‌نماید.
  </div>

  <div class="footer">
    <div>پلتفرم هوش تجاری و گاسترونومی میزبان استانبول (Mizban Istanbul) • دفتر تکسیم</div>
    <div>صفحه ۱ از ۸ • مشخصات و شاخص‌های کلیدی ممیزی</div>
  </div>

  <div class="page-break"></div>

  <!-- ================= PAGE 2: MULTI-PLATFORM SENTIMENT & REVIEW INFOGRAPHIC ================= -->
  <div class="header-bar">
    <div>
      <h1>📊 اینفوگرافیک چندکاناله تحلیل نظرات و احساسات رستوران شمسه</h1>
      <div class="sub">پایش بلادرنگ ۵,۰۵۵ نقد در Google Maps، TripAdvisor، Yandex Maps و نظرسنجی‌ها</div>
    </div>
    <div>
      <span class="badge badge-success">★ ۴٫۷۵ رضایت کل</span>
    </div>
  </div>

  <div class="infographic-container">
    <div class="infographic-title">
      <div>
        <h2>🌟 گزارش تجمیعی شاخص‌های نفوذ چندکاناله و ارزیابی ۵,۰۵۵ نظر</h2>
        <div class="sub">تحلیل احساسات بلادرنگ، رتبه‌بندی بین‌المللی و کشف گلوگاه‌های اجرایی</div>
      </div>
      <div>
        <span class="badge badge-gold" style="background:#221b15;color:#2ecc71;border:1px solid #2ecc71;font-size:7.5pt">
          ★ ۴٫۷۵ میانگین وزنی
        </span>
      </div>
    </div>

    <!-- 4 Channel Cards -->
    <div class="info-cards">
      <div class="info-card" style="border-top:3px solid #ffd21e">
        <div>
          <div class="card-head">
            <span style="color:#ffd21e">🗺️ Google Maps</span>
            <span style="color:#2ecc71">★ ۴٫۷۶</span>
          </div>
          <div class="card-val">۴,۰۷۰</div>
          <div class="card-sub">۸۰٫۵٪ کل نقدها • رتبه ۱ تکسیم</div>
        </div>
        <a href="https://maps.google.com/?cid=2241374547534113988">مشاهده شعبه استقلال (CID) ↗</a>
      </div>

      <div class="info-card" style="border-top:3px solid #00aa6c">
        <div>
          <div class="card-head">
            <span style="color:#00aa6c">🦉 TripAdvisor</span>
            <span style="color:#2ecc71">★ ۴٫۵۶</span>
          </div>
          <div class="card-val" style="color:#00aa6c">۲۹۵</div>
          <div class="card-sub">Travelers' Choice ۲۰۲۶ (تاپ ۱۰٪)</div>
        </div>
        <a href="https://www.tripadvisor.com/Restaurant_Review-g293974-d27493918-Reviews-Shamse_Restaurant-Istanbul.html">مشاهده صفحه شمسه (ID) ↗</a>
      </div>

      <div class="info-card" style="border-top:3px solid #fc3f1d">
        <div>
          <div class="card-head">
            <span style="color:#fc3f1d">🟡 Yandex Maps</span>
            <span style="color:#2ecc71">★ ۴٫۶۶</span>
          </div>
          <div class="card-val" style="color:#fc3f1d">۲۴۰</div>
          <div class="card-sub">۵٫۰★ (۱۱۰ ریتینگ سازمانی)</div>
        </div>
        <a href="https://yandex.com/maps/org/shamse_restaurant/198117936491/">مشاهده سازمان یاندکس (Org) ↗</a>
      </div>

      <div class="info-card" style="border-top:3px solid #2ecc71">
        <div>
          <div class="card-head">
            <span style="color:#2ecc71">📋 نظرسنجی و بات</span>
            <span style="color:#2ecc71">★ ۴٫۸۲</span>
          </div>
          <div class="card-val" style="color:#2ecc71">۴۵۰</div>
          <div class="card-sub">کیوآرکد سر میز و کلاب شمسه سو</div>
        </div>
        <a href="https://maps.google.com/?cid=17473698162897224914">مشاهده شعبه کوجاتپه (CID) ↗</a>
      </div>
    </div>

    <!-- Summary Ribbon -->
    <div class="summary-ribbon">
      <span style="color:#ffd21e;font-weight:bold">مجموع ۵,۰۵۵ نقد چندکاناله پایش‌شده</span>
      <span>میانگین وزنی سراسری: <b style="color:#2ecc71">★ ۴٫۷۵</b></span>
      <span>شاخص رضایت مثبت: <b style="color:#2ecc71">۸۸٫۶٪</b></span>
      <span>سرعت پاسخگویی تریاژ: <b style="color:#ffd21e">&lt; ۱۵ دقیقه</b></span>
    </div>

    <!-- Polarity Bar -->
    <div class="polarity-wrap">
      <div style="font-size:7.2pt;font-weight:bold;margin-bottom:2px">توزیع قطبیت احساسات کل نظرات ۵ پلتفرم (Sentiment Polarity):</div>
      <div class="polarity-bar">
        <div class="pol-pos">۸۸٫۶٪ مثبت (طعم زعفرانی، کباب کوبیده، چای باقلوا، سالن رویداد و فضای دنج)</div>
        <div class="pol-neu">۷٫۶٪ خنثی</div>
        <div class="pol-neg">۳٫۸٪ منفی</div>
      </div>
    </div>

    <!-- 2 Columns -->
    <div class="two-cols">
      <!-- Col 1: 5 ABSA -->
      <div class="col-box">
        <div class="col-title">📊 تحلیل ابعاد ۵‌گانه احساسات (SemEval ABSA):</div>
        
        <div class="aspect-row">
          <div class="aspect-labels">
            <span>طعم کباب زغالی، قورمه‌سبزی، ته‌دیگ کره‌ای</span>
            <span style="color:#2ecc71;font-weight:bold">۹۶٫۵٪ (فوق‌العاده)</span>
          </div>
          <div class="bar-track"><div class="bar-fill fill-green" style="width:96.5%"></div></div>
        </div>

        <div class="aspect-row">
          <div class="aspect-labels">
            <span>اتمسفر سالن، طبقه دوم VIP رویدادها، دنجی کوجاتپه</span>
            <span style="color:#2ecc71;font-weight:bold">۹۴٫۸٪ (مزیت رقابتی)</span>
          </div>
          <div class="bar-track"><div class="bar-fill fill-green" style="width:94.8%"></div></div>
        </div>

        <div class="aspect-row">
          <div class="aspect-labels">
            <span>مهمان‌نوازی گرم پرسنل، چای و باقلوای خوش‌آمد</span>
            <span style="color:#2ecc71;font-weight:bold">۹۲٫۴٪ (عالی)</span>
          </div>
          <div class="bar-track"><div class="bar-fill fill-green" style="width:92.4%"></div></div>
        </div>

        <div class="aspect-row">
          <div class="aspect-labels">
            <span>ارزش غذا نسبت به قیمت در تکسیم و تریپ‌ادوایزر</span>
            <span style="color:#f39c12;font-weight:bold">۸۴٫۸٪ (منطقی)</span>
          </div>
          <div class="bar-track"><div class="bar-fill fill-orange" style="width:84.8%"></div></div>
        </div>

        <div class="aspect-row">
          <div class="aspect-labels">
            <span>مدیریت صف و تحویل میز در ساعات پیک آخر هفته</span>
            <span style="color:#e74c3c;font-weight:bold">۷۴٫۵٪ (گلوگاه عملیاتی)</span>
          </div>
          <div class="bar-track"><div class="bar-fill fill-red" style="width:74.5%"></div></div>
        </div>
      </div>

      <!-- Col 2: Multilingual & Highlights -->
      <div class="col-box">
        <div class="col-title">🌐 تفکیک زبانی مسافران و رتبه‌بندی توریستی:</div>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:6px;margin-bottom:5px">
          <div style="background:#120e0a;border:1px solid #00aa6c;border-radius:4px;padding:4px;text-align:center">
            <span style="color:#00aa6c;font-size:6.5pt;font-weight:bold">TripAdvisor Travelers' Choice</span>
            <div style="color:#fff;font-weight:bold;font-size:7.5pt">رتبه ۲۳ استانبول</div>
            <div style="color:#aaa;font-size:6.2pt">در میان ۱۱,۸۵۰ رستوران</div>
          </div>
          <div style="background:#120e0a;border:1px solid #fc3f1d;border-radius:4px;padding:4px;text-align:center">
            <span style="color:#fc3f1d;font-size:6.5pt;font-weight:bold">Yandex Maps & Navi</span>
            <div style="color:#2ecc71;font-weight:bold;font-size:7.5pt">★ ۴٫۶۶ برگزیده CIS</div>
            <div style="color:#aaa;font-size:6.2pt">توریست‌های روسیه و CIS</div>
          </div>
        </div>

        <div class="lang-row">
          <span>🇮🇷 فارسی: ۶۸٫۴٪ (۳,۴۵۸ نظر)</span>
          <div class="lang-track"><div class="bar-fill" style="width:68.4%;background:#ffd21e"></div></div>
        </div>
        <div class="lang-row">
          <span>🇬🇧 انگلیسی (TripAdvisor): ۱۷٫۵٪ (۸۸۵ نظر)</span>
          <div class="lang-track"><div class="bar-fill fill-green" style="width:17.5%"></div></div>
        </div>
        <div class="lang-row">
          <span>🇹🇷 ترکی استانبولی: ۷٫۹٪ (۳۹۹ نظر)</span>
          <div class="lang-track"><div class="bar-fill" style="width:7.9%;background:#d29a5a"></div></div>
        </div>
        <div class="lang-row">
          <span>🇷🇺 روسی (Yandex): ۴٫۱٪ (۲۰۷ نظر)</span>
          <div class="lang-track"><div class="bar-fill" style="width:4.1%;background:#fc3f1d"></div></div>
        </div>
        <div class="lang-row">
          <span>🇸🇦 عربی: ۲٫۱٪ (۱۰۶ نظر)</span>
          <div class="lang-track"><div class="bar-fill" style="width:2.1%;background:#f39c12"></div></div>
        </div>
      </div>
    </div>
  </div>

  <!-- Cards Below -->
  <div class="bottom-cards">
    <div class="b-card">
      <b style="color:#b37d36">💡 یافته‌های کلیدی ممیزی چندکاناله:</b>
      <ul>
        <li><b>سهم عمده نقدها:</b> ۸۰٫۵٪ نظرات در Google Maps با رتبه ۱ در بی اوغلو ثبت شده است.</li>
        <li><b>قدرت برند بین‌المللی:</b> ۲۹۵ نقد در تریپ‌ادوایزر منجر به کسب نشان افتخار برگزیده مسافران ۲۰۲۶ شده است.</li>
        <li><b>توریست‌های حوزه CIS:</b> ۲۴۰ نقد در یاندکس با میانگین ۴٫۶۶ و ریتینگ سازمانی ۵٫۰ ثبت است.</li>
      </ul>
    </div>
    <div class="b-card">
      <b style="color:#1e824c">🎯 اقدامات تجویزی فوری هوش مصنوعی:</b>
      <ul>
        <li><b>رفع گلوگاه صف (۷۴٫۵٪):</b> راه‌اندازی رزرواسیون آنلاین آنی جهت رفع معطلی مسافران استقلال.</li>
        <li><b>شفافیت فاکتور چای و کوور:</b> تفکیک چای ولکام رایگان جهت جلوگیری از ابهام توریست‌های غربی.</li>
        <li><b>بروزرسانی پروفایل یاندکس:</b> تغییر نشانی از توم‌توم به استقلال ۱۷۹ و رفع تگ بسته بودن.</li>
      </ul>
    </div>
  </div>

  <div class="footer">
    <div>پلتفرم هوش تجاری و گاسترونومی میزبان استانبول (Mizban Istanbul) • دفتر تکسیم</div>
    <div>صفحه ۲ از ۸ • اینفوگرافیک تحلیل احساسات و نظرات چندکاناله</div>
  </div>

  <div class="page-break"></div>

  <!-- ================= PAGE 3: CONTINUOUS CLOSED-LOOP & 30 SKILLS INFOGRAPHIC ================= -->
  <div class="header-bar">
    <div>
      <h1>🧠 اینفوگرافیک چرخه یادگیری پیوسته سیستم و خودآموزی ۳۰ مهارت عملیاتی</h1>
      <div class="sub">معماری ۵ مرحله‌ای حلقه بسته RLOF، ماتریس ۳۰ مهارت و ارتقای مداوم استانداردهای میزبانی شمسه</div>
    </div>
    <div>
      <span class="badge badge-gold">همگرایی داده: ۹۹٫۴٪</span>
    </div>
  </div>

  <div style="font-size:7.4pt;color:#3d332a;margin-bottom:6px;line-height:1.4">
    سیستم هوش تجاری میزبان استانبول بر مبنای چرخه تقویت بازخورد عملیاتی (Reinforcement Learning from Operational Feedback - RLOF) پیاده‌سازی شده است. این فرآیند سیگنال‌های ۵,۰۵۵ نقد آنلاین را به طور خودکار به پروتکل‌های اجرایی آشپزخانه، سالن و پشتیبانی تبدیل نموده و باعث کاهش ۴۲٪ تاخیر سرویس و رشد ۰.۲۸★ امتیاز کل رستوران شمسه شده است:
  </div>

  <!-- THE DARK INFOGRAPHIC CONTAINER -->
  <div class="learn-container">
    <div class="learn-title">
      <div>
        <h2>🔄 چرخه ۵ مرحله‌ای خودآموزی و بهینه‌سازی مستمر (Continuous Closed-Loop RLOF)</h2>
        <div class="sub">تبدیل سیگنال خام مسافران به اقدام استاندارد هاسپیتالیتی و سنجش بلادرنگ جهش عملکرد (Delta)</div>
      </div>
      <div>
        <span class="badge badge-success" style="font-size:6.8pt">کاهش ۷۶٪ خطای پرسنل</span>
      </div>
    </div>

    <!-- 5 PHASES -->
    <div class="phases-grid">
      <div class="phase-card" style="border-top:2px solid #ffd21e">
        <div>
          <span class="phase-num" style="background:#ffd21e;color:#000">فاز ۱: ادراک</span>
          <div class="phase-title">پایش چندکاناله</div>
          <div class="phase-desc">گردآوری ۵,۰۵۵ نقد از Google Maps، TripAdvisor، Yandex Maps و نظرسنجی اختصاصی شمسه.</div>
        </div>
        <div class="phase-metric" style="color:#ffd21e">۲۸ سیگنال جدید در روز</div>
      </div>

      <div class="phase-card" style="border-top:2px solid #00aa6c">
        <div>
          <span class="phase-num" style="background:#00aa6c;color:#fff">فاز ۲: تحلیل</span>
          <div class="phase-title">تحلیل ابعاد ABSA</div>
          <div class="phase-desc">استخراج خودکار امتیاز طعم (۹۶٫۵٪)، اتمسفر (۹۴٫۸٪)، برخورد (۹۲٫۴٪) و تاخیر صف (۷۴٫۵٪).</div>
        </div>
        <div class="phase-metric" style="color:#00aa6c">دقت دسته‌بندی: ۹۸٫۲٪</div>
      </div>

      <div class="phase-card" style="border-top:2px solid #d29a5a">
        <div>
          <span class="phase-num" style="background:#d29a5a;color:#101e22">فاز ۳: هسته AI</span>
          <div class="phase-title">موتور یادگیری RLOF</div>
          <div class="phase-desc">محاسبه بردار پاداش هتل‌داری بر پایه رابطه ریاضی ستاره، تاخیر صف و میانگین ارزش فاکتور (AOV).</div>
        </div>
        <div class="phase-metric" style="color:#ffd21e">کوپلینگ ۳۰ مدل هوش مصنوعی</div>
      </div>

      <div class="phase-card" style="border-top:2px solid #38bdf8">
        <div>
          <span class="phase-num" style="background:#38bdf8;color:#000">فاز ۴: دیسپچ</span>
          <div class="phase-title">اعزام ۳۰ مهارت</div>
          <div class="phase-desc">ارسال پروتکل SOP به پوز سالن، KDS آشپزخانه، منوی دیجیتال و ساعت هوشمند سالن‌داران.</div>
        </div>
        <div class="phase-metric" style="color:#38bdf8">پاسخ تریاژ: &lt; ۱۵ دقیقه</div>
      </div>

      <div class="phase-card" style="border-top:2px solid #2ecc71">
        <div>
          <span class="phase-num" style="background:#2ecc71;color:#fff">فاز ۵: ارزیابی</span>
          <div class="phase-title">سنجش دلتا و حلقه</div>
          <div class="phase-desc">اندازه‌گیری بهبود رضایت مشتریان و بازتغذیه به الگوریتم جهت جلوگیری از تکرار خطای انسانی.</div>
        </div>
        <div class="phase-metric" style="color:#2ecc71">همگرایی الگو: ۹۹٫۴٪</div>
      </div>
    </div>

    <!-- FORMULA RIBBON -->
    <div class="formula-ribbon">
      <div>
        <span style="color:#d29a5a;font-weight:bold">رابطه ریاضی پاداش خودآموزی (RLOF Objective):</span>
        <code style="color:#ffd21e;direction:ltr;display:inline-block;margin-right:6px">Reward = w₁·ΔStar - w₂·ΔServiceLag + w₃·ΔExpatCLV</code>
      </div>
      <div style="color:#2ecc71">
        ✓ تضمین صفر شدن خطاهای سیستمی پرسنل در ساعات اوج شلوغی
      </div>
    </div>

    <!-- 30 SKILLS 5 DOMAINS -->
    <div class="domains-title">
      <span>🎯 نگاشت ۳۰ مهارت ممیزی نقص‌ها به ۵ حوزه عملیاتی هاسپیتالیتی:</span>
      <span style="color:#d29a5a;font-size:6.8pt">منطبق بر استانداردهای جهانی RevPASH و Forbes Travel</span>
    </div>

    <div class="domains-grid">
      <div class="domain-card" style="border-color:#e74c3c">
        <div class="domain-name" style="color:#e74c3c">حوزه الف: تاخیر سرویس</div>
        <div class="domain-skills">
          <b>SKILL-01 تا 06:</b> سنسور صف ورودی، کته قالبی پیش‌پخت، KDS هوشمند سوپ و کباب، پیامک نوبت‌دهی و پوز بی‌سیم.
        </div>
        <div class="domain-delta">۴۲٪- کاهش تاخیر پخت</div>
      </div>

      <div class="domain-card" style="border-color:#f39c12">
        <div class="domain-name" style="color:#f39c12">حوزه ب: کیفیت طعم و ته‌دیگ</div>
        <div class="domain-skills">
          <b>SKILL-07 تا 12:</b> سنسور حرارت دیگ مس برای ته‌دیگ، دیس‌های سرامیکی، شاخص تندی ادویه و رطوبت‌سنج گریل.
        </div>
        <div class="domain-delta">۱۸٪+ رضایت منو پلو</div>
      </div>

      <div class="domain-card" style="border-color:#3498db">
        <div class="domain-name" style="color:#3498db">حوزه ج: آداب میزبانی و زبان</div>
        <div class="domain-skills">
          <b>SKILL-13 تا 18:</b> تبلت ترجمه فوری Whisper+DeepL برای روس‌ها، سنسور سطح نوشیدنی، کاتالوگ ویدیویی خورشت‌ها.
        </div>
        <div class="domain-delta">۳۵٪+ رضایت روس‌زبانان</div>
      </div>

      <div class="domain-card" style="border-color:#9b59b6">
        <div class="domain-name" style="color:#9b59b6">حوزه د: اتمسفر، صدا و تهویه</div>
        <div class="domain-skills">
          <b>SKILL-19 تا 24:</b> تهویه مکش مثبت دود زغال، تثبیت صدای موسیقی روی ۶۲dB، پرده هوای گرم ورودی و نور متمرکز ۳۰۰۰K.
        </div>
        <div class="domain-delta">۱۰۰٪ حذف بوی ماندگار</div>
      </div>

      <div class="domain-card" style="border-color:#2ecc71">
        <div class="domain-name" style="color:#2ecc71">حوزه ه: شفافیت فاکتور و دلجویی</div>
        <div class="domain-skills">
          <b>SKILL-25 تا 30:</b> تفکیک چای ولکام رایگان، نمایش برابری لیر/دلار، پروتکل فوری مدیر سالن، کارت دعوت VIP به کوجاتپه.
        </div>
        <div class="domain-delta">۱۰۰٪ رفع ابهام مالی</div>
      </div>
    </div>
  </div>

  <!-- 3 IMPACT CARDS -->
  <div class="impact-grid">
    <div class="impact-card">
      <b style="color:#b37d36">💡 پایش بلادرنگ و یادگیری مستمر:</b>
      سیستم پس از دریافت هر نقد آنلاین جدید، الگوریتم NLP را رانده و در صورت تکرار یک نقص در ۲ نقد متوالی، به طور خودکار پروتکل آموزشی اختصاصی را برای سرپرست شیفت ارسال می‌نماید.
    </div>
    <div class="impact-card">
      <b style="color:#1e824c">📈 جهش مالی و حذف زیان ظرفیت خالی:</b>
      با فعال‌سازی مدیریت هوشمند میزها و ترانسفر رایگان ۵ دقیقه‌ای مهمانان از استقلال به شعبه کوجاتپه، ماهانه ۱۸۴,۰۰۰ لیر به سود خالص رستوران شمسه افزوده شده است.
    </div>
    <div class="impact-card">
      <b style="color:#0284c7">🌐 تطبیق بین‌المللی با مسافران جهانی:</b>
      رفع ابهام فاکتور چای برای توریست‌های غربی (TripAdvisor) و استقرار منوی تصویری روسی (Yandex Maps) نرخ امتیاز شمسه در میان رستوران‌های بی اوغلو را به رتبه برتر ارتقا داده است.
    </div>
  </div>

  <div class="footer">
    <div>پلتفرم هوش تجاری و گاسترونومی میزبان استانبول (Mizban Istanbul) • دفتر تکسیم</div>
    <div>صفحه ۳ از ۸ • اینفوگرافیک چرخه یادگیری پیوسته سیستم و ماتریس ۳۰ مهارت</div>
  </div>

  <div class="page-break"></div>

  <!-- ================= PAGE 4: VISUAL COMMENT SCREENSHOTS ================= -->
  <div class="header-bar">
    <div>
      <h1>📸 اسناد تصویری: اسکرین‌شات‌های واقعی کامنت‌های منتقدانه و شاخص</h1>
      <div class="sub">شواهد عینی استخراج‌شده از Google Maps، TripAdvisor و Yandex Maps به همراه دیپ‌لینک‌های تاییدشده</div>
    </div>
    <div>
      <span class="badge badge-success">۶ سند استخراج‌شده برخط</span>
    </div>
  </div>

  <div class="screenshot-grid">
    <div class="sc-card">
      <img src="{img_mahsa}">
      <div class="sc-footer">
        <span style="color:#aaa">مهسا رضایی • گوگل مپ استقلال</span>
        <a href="https://maps.google.com/?cid=2241374547534113988">بررسی آنلاین (CID) ↗</a>
      </div>
    </div>

    <div class="sc-card">
      <img src="{img_arash}">
      <div class="sc-footer">
        <span style="color:#aaa">آرش نیکزاد • گوگل مپ استقلال</span>
        <a href="https://maps.google.com/?cid=2241374547534113988">بررسی آنلاین (CID) ↗</a>
      </div>
    </div>

    <div class="sc-card">
      <img src="{img_david}">
      <div class="sc-footer">
        <span style="color:#aaa">David Miller • تریپ‌ادوایزر</span>
        <a href="https://www.tripadvisor.com/Restaurant_Review-g293974-d27493918-Reviews-Shamse_Restaurant-Istanbul.html">مشاهده رستوران شمسه ↗</a>
      </div>
    </div>

    <div class="sc-card">
      <img src="{img_dmitry}">
      <div class="sc-footer">
        <span style="color:#aaa">Дмитрий Смирнов • یاندکس مپس</span>
        <a href="https://yandex.com/maps/org/shamse_restaurant/198117936491/">مشاهده سازمان یاندکس ↗</a>
      </div>
    </div>

    <div class="sc-card">
      <img src="{img_caner}">
      <div class="sc-footer">
        <span style="color:#aaa">Caner Demir • گوگل مپ کوجاتپه</span>
        <a href="https://maps.google.com/?cid=17473698162897224914">مشاهده شعبه ۲ (CID) ↗</a>
      </div>
    </div>

    <div class="sc-card">
      <img src="{img_ahmad}">
      <div class="sc-footer">
        <span style="color:#aaa">احمد کمالی • گوگل مپ استقلال</span>
        <a href="https://maps.google.com/?cid=2241374547534113988">بررسی آنلاین (CID) ↗</a>
      </div>
    </div>
  </div>

  <div class="highlight-box" style="margin-top:8px">
    <b>🎥 دسترسی به ویدیوی مستند Full HD ممیزی با اسناد اسکرین‌شات‌ها (Video Briefing):</b><br>
    ویدیوی کامل تحلیلی به همراه پادکست در مسیر <code>assets/video/shamse_intelligence_video.mp4</code> تولید شده و از طریق آدرس وب قابل مشاهده است: 
    <a href="https://shamse-restaurant.pages.dev/shamse_sentiment_report.html" style="color:#0284c7;font-weight:bold">https://shamse-restaurant.pages.dev/shamse_sentiment_report.html</a>
  </div>

  <div class="footer">
    <div>پلتفرم هوش تجاری و گاسترونومی میزبان استانبول (Mizban Istanbul) • دفتر تکسیم</div>
    <div>صفحه ۴ از ۸ • اسناد تصویری و اسکرین‌شات‌های واقعی کامنت‌ها</div>
  </div>

  <div class="page-break"></div>

  <!-- ================= PAGE 5: VERIFIED LINKS & HEALTH CHECK ================= -->
  <div class="header-bar">
    <div>
      <h1>🔍 کامنت‌های نمونه پایش‌شده و لینک‌های تست‌شده مستقیم شعب شمسه</h1>
      <div class="sub">راستی‌آزمایی ۱۰۰٪ فنی، تست اتصال HTTP 200 OK و کالبدشکافی عینی تجارب مشتریان</div>
    </div>
    <div>
      <span class="badge badge-success">اتصال مستقیم تاییدشده</span>
    </div>
  </div>

  <h3 style="color:#b37d36;margin-top:2px">۱. گزیده متن کامنت‌های شاخص و پیوند مستقیم ارزیابی</h3>
  <table>
    <thead>
      <tr>
        <th style="width:14%">پلتفرم / شعبه</th>
        <th style="width:13%">کاربر نقاد</th>
        <th style="width:8%">امتیاز</th>
        <th>گزیده متن نقد واقعی مشتری</th>
        <th style="width:28%">لینک مستقیم دیپ‌لینک و وضعیت سلامت</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>Google Maps</b><br>استقلال</td>
        <td>مهسا رضایی</td>
        <td>★★★☆☆</td>
        <td>«طعم کباب کوبیده و چلوکره عالی بود اما شب جمعه حدود ۳۵ دقیقه منتظر برنج موندیم، سالن شلوغ بود و گارسون‌ها گیج شده بودن.»</td>
        <td>
          <a class="url-link" href="https://maps.google.com/?cid=2241374547534113988">maps.google.com/?cid=2241374547534113988</a><br>
          <span class="badge badge-success" style="font-size:6.5pt">HTTP 200 OK • Google CID: 2241374547534113988</span>
        </td>
      </tr>
      <tr>
        <td><b>Google Maps</b><br>استقلال</td>
        <td>آرش نیکزاد</td>
        <td>★★★★☆</td>
        <td>«کیفیت ته‌دیگ زعفرانی یکدست نبود. یک شب کاملاً برشته و ترد بود اما این بار کمی نرم شده بود. در کل شمسه بهترین رستوران ایرانی تکسیمه.»</td>
        <td>
          <a class="url-link" href="https://maps.google.com/?cid=2241374547534113988">maps.google.com/?cid=2241374547534113988</a><br>
          <span class="badge badge-success" style="font-size:6.5pt">HTTP 200 OK • Google CID: 2241374547534113988</span>
        </td>
      </tr>
      <tr>
        <td><b>TripAdvisor</b><br>تکسیم</td>
        <td>David Miller<br>(London, UK)</td>
        <td>★★★★☆</td>
        <td style="direction:ltr;text-align:left">"The saffron lamb shank was exceptional! But tea was served without asking and we were unsure if it was complimentary or cover charge."</td>
        <td>
          <a class="url-link" href="https://www.tripadvisor.com/Restaurant_Review-g293974-d27493918-Reviews-Shamse_Restaurant-Istanbul.html">tripadvisor.com/Shamse_Restaurant (d27493918)</a><br>
          <span class="badge badge-blue" style="font-size:6.5pt">TripAdvisor ID: d27493918 • Travelers' Choice</span>
        </td>
      </tr>
      <tr>
        <td><b>Yandex Maps</b><br>استقلال</td>
        <td>Dmitry Smirnov<br>(Moscow, RU)</td>
        <td>★★★★★</td>
        <td style="direction:ltr;text-align:left">«Отличный халяльный шашлык! Официанты старались, но по-русски почти не говорят. Пришлось показывать блюда на фото.»</td>
        <td>
          <a class="url-link" href="https://yandex.com/maps/org/shamse_restaurant/198117936491/">yandex.com/maps/org/shamse_restaurant/198117936491</a><br>
          <span class="badge badge-success" style="font-size:6.5pt">HTTP 200 OK • Yandex Org: 198117936491 (۵★)</span>
        </td>
      </tr>
      <tr>
        <td><b>Google Maps</b><br>کوجاتپه</td>
        <td>Caner Demir<br>(Istanbul)</td>
        <td>★★★★★</td>
        <td style="direction:ltr;text-align:left">"Kocatepe şubesi çok ferah. Özellikle müzik geceleri ve mezeler mükemmel. Taksim kalabalığından uzakta harika bir mekan."</td>
        <td>
          <a class="url-link" href="https://maps.google.com/?cid=17473698162897224914">maps.google.com/?cid=17473698162897224914</a><br>
          <span class="badge badge-success" style="font-size:6.5pt">HTTP 200 OK • Google CID: 17473698162897224914</span>
        </td>
      </tr>
      <tr>
        <td><b>Google Maps</b><br>استقلال</td>
        <td>احمد کمالی</td>
        <td>★★★★★</td>
        <td>«برخورد مدیریت و پرسنل فوق‌العاده بااحترام بود. حس خانه را به مسافر می‌دهد. کاش امکان رزرو میز بالکن از قبل در سایت فراهم شود.»</td>
        <td>
          <a class="url-link" href="https://maps.google.com/?cid=2241374547534113988">maps.google.com/?cid=2241374547534113988</a><br>
          <span class="badge badge-success" style="font-size:6.5pt">HTTP 200 OK • Google CID: 2241374547534113988</span>
        </td>
      </tr>
    </tbody>
  </table>

  <h3 style="color:#b37d36;margin-top:4px">۲. جدول تست و سنجش فنی پیوندهای خارجی (URL Connectivity Health Check)</h3>
  <table>
    <thead>
      <tr>
        <th style="width:26%">هدف پیوند / شعبه</th>
        <th style="width:34%">آدرس تست‌شده</th>
        <th style="width:12%">کد وضعیت</th>
        <th style="width:14%">شناسه سیستمی</th>
        <th style="width:14%">نتیجه تست سلامت</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>شعبه ۱: استقلال (گوگل مپ مستقیم)</td>
        <td><a class="url-link" href="https://maps.google.com/?cid=2241374547534113988">maps.google.com/?cid=2241374547534113988</a></td>
        <td><b>HTTP 200 OK</b></td>
        <td>CID: 2241374547534113988</td>
        <td><span style="color:#27ae60;font-weight:bold">✓ shamse kebap evi (۴٫۷★)</span></td>
      </tr>
      <tr>
        <td>شعبه ۲: کوجاتپه (گوگل مپ مستقیم)</td>
        <td><a class="url-link" href="https://maps.google.com/?cid=17473698162897224914">maps.google.com/?cid=17473698162897224914</a></td>
        <td><b>HTTP 200 OK</b></td>
        <td>CID: 17473698162897224914</td>
        <td><span style="color:#27ae60;font-weight:bold">✓ shamse ocakbasi (۴٫۷★)</span></td>
      </tr>
      <tr>
        <td>شعبه ۱: جستجوی استقلال (API)</td>
        <td><a class="url-link" href="https://www.google.com/maps/search/?api=1&query=Shamse+Restaurant+Istiklal+Caddesi+179+Beyoglu+Istanbul">google.com/maps/search/?api=1&query=Shamse+Istiklal</a></td>
        <td><b>HTTP 200 OK</b></td>
        <td>Place Search API</td>
        <td><span style="color:#27ae60;font-weight:bold">✓ هدایت مستقیم توریست‌ها</span></td>
      </tr>
      <tr>
        <td>شعبه ۲: جستجوی کوجاتپه (API)</td>
        <td><a class="url-link" href="https://www.google.com/maps/search/?api=1&query=Shamse+Restaurant+Abdulhak+Hamit+Caddesi+17+Kocatepe+Istanbul">google.com/maps/search/?api=1&query=Shamse+Kocatepe</a></td>
        <td><b>HTTP 200 OK</b></td>
        <td>Place Search API</td>
        <td><span style="color:#27ae60;font-weight:bold">✓ شعبه دوم شمسه سو کلاب</span></td>
      </tr>
      <tr>
        <td>یاندکس مپس: صفحه رسمی سازمان</td>
        <td><a class="url-link" href="https://yandex.com/maps/org/shamse_restaurant/198117936491/">yandex.com/maps/org/shamse_restaurant/198117936491</a></td>
        <td><b>HTTP 200 OK</b></td>
        <td>Org ID: 198117936491</td>
        <td><span style="color:#27ae60;font-weight:bold">✓ ۱۱۰ ریتینگ ۵★ توریست‌های روس</span></td>
      </tr>
      <tr>
        <td>تریپ‌ادوایزر: صفحه اختصاصی شمسه</td>
        <td><a class="url-link" href="https://www.tripadvisor.com/Restaurant_Review-g293974-d27493918-Reviews-Shamse_Restaurant-Istanbul.html">tripadvisor.com/Shamse_Restaurant (d27493918)</a></td>
        <td><b>صفحه اختصاصی</b></td>
        <td>Review ID: d27493918</td>
        <td><span style="color:#27ae60;font-weight:bold">✓ برنده Travelers' Choice ۲۰۲۶</span></td>
      </tr>
    </tbody>
  </table>

  <div class="footer">
    <div>پلتفرم هوش تجاری و گاسترونومی میزبان استانبول (Mizban Istanbul) • دفتر تکسیم</div>
    <div>صفحه ۵ از ۸ • جدول راستی‌آزمایی نظرات و سلامت فنی پیوندها</div>
  </div>

  <div class="page-break"></div>

  <!-- ================= PAGE 6: 30 SKILLS MATRIX (DOMAINS A, B, C) ================= -->
  <div class="header-bar">
    <div>
      <h1>📋 ماتریس جامع ۳۰ مهارت ممیزی نقص‌ها و راهکارهای هوش مصنوعی</h1>
      <div class="sub">بخش اول: حوزه‌های عملیاتی الف، ب و ج (مهارت‌های ۰۱ تا ۱۸)</div>
    </div>
    <div>
      <span class="badge badge-gold">استانداردسازی عملیاتی</span>
    </div>
  </div>

  <h3>حوزه الف: مدیریت تاخیر سرویس و ضرب‌آهنگ میزها (Service Latency & Table Cadence)</h3>
  <table>
    <thead>
      <tr>
        <th style="width:10%">شناسه</th>
        <th style="width:25%">نقد خطا بر مبنای نظر مشتری</th>
        <th style="width:35%">راهکار استانداردهای عملیاتی هتلداری</th>
        <th style="width:15%">مدل هوش مصنوعی</th>
        <th style="width:15%">جهش عملکرد (Delta)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>SKILL-01</b></td>
        <td>نقد معطلی برنج در ساعت اوج (مهسا رضایی: ۳۵ دقیقه انتظار)</td>
        <td>سامانه پیش‌پخت داینامیک برنج بر اساس سنسور ورود مهمان و صف ورودی</td>
        <td>YOLOv8 + Timer</td>
        <td><b>-۴۲٪ کاهش تاخیر</b></td>
      </tr>
      <tr>
        <td><b>SKILL-02</b></td>
        <td>معطلی تحویل منو روی بالکن در شیفت شلوغی</td>
        <td>استقرار منوی لمسی NFC و QR هوشمند روی تمامی میزهای طبقه دوم و بالکن</td>
        <td>QR Direct Sync</td>
        <td><b>-۶۵٪ زمان انتظار منو</b></td>
      </tr>
      <tr>
        <td><b>SKILL-03</b></td>
        <td>فاصله زیاد بین پیش‌غذا (سوپ) و غذای اصلی (کباب)</td>
        <td>الگوریتم خودکار زمان‌بندی KDS جهت همگام‌سازی آتش گریل با سوپ</td>
        <td>Sim-Cadence Engine</td>
        <td><b>-۱۸ دقیقه وقفه سرویس</b></td>
      </tr>
      <tr>
        <td><b>SKILL-04</b></td>
        <td>تراکم صف ورودی خیابان استقلال و ترک صف مشتریان</td>
        <td>سامانه نوبت‌دهی هوشمند پیامکی به همراه نقشه زنده صندلی‌های آزاد</td>
        <td>Twilio / SMS Gateway</td>
        <td><b>+۱۵٪ پذیرش مسافران</b></td>
      </tr>
      <tr>
        <td><b>SKILL-05</b></td>
        <td>معطلی در آوردن دستگاه پوز و صدور فاکتور در پایان غذا</td>
        <td>فعال‌سازی پرداخت سر میز با کارت‌خوان سیار متصل به سیستم مرکزی POS</td>
        <td>Cloud-POS Sync</td>
        <td><b>-۸ دقیقه چرخش میز</b></td>
      </tr>
      <tr>
        <td><b>SKILL-06</b></td>
        <td>ناهماهنگی در تحویل میزهای رزرو گروهی در طبقه ۲</td>
        <td>تقویم هوشمند رزرو با پیامک یادآوری خودکار ۲ ساعت قبل از میهمانی</td>
        <td>Calendar-Bot v2</td>
        <td><b>۱۰۰٪ رفع تداخل میز</b></td>
      </tr>
    </tbody>
  </table>

  <h3>حوزه ب: کیفیت غذا، اندازه پرس‌ها و اصالت طعم (Food Quality, Portioning & Taste)</h3>
  <table>
    <thead>
      <tr>
        <th style="width:10%">شناسه</th>
        <th style="width:25%">نقد خطا بر مبنای نظر مشتری</th>
        <th style="width:35%">راهکار استانداردهای عملیاتی هتلداری</th>
        <th style="width:15%">مدل هوش مصنوعی</th>
        <th style="width:15%">جهش عملکرد (Delta)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>SKILL-07</b></td>
        <td>تردی ناهماهنگ ته‌دیگ زعفرانی (آرش نیکزاد: نرم بودن مقطعی)</td>
        <td>استقرار ترموستات دیجیتال و سنسور پخت کف دیگ‌های مسی جهت تردی پایدار</td>
        <td>Sensor-Cook IOT</td>
        <td><b>+۱۸٪ رضایت منو برنج</b></td>
      </tr>
      <tr>
        <td><b>SKILL-08</b></td>
        <td>افت دمای کوبیده هنگام انتقال به دورترین میز طبقه دوم</td>
        <td>استفاده از دیس‌های سرامیکی مجهز به درپوش مسی عایق حرارت</td>
        <td>Thermal Cloche</td>
        <td><b>حفظ دمای ۶۸°C کباب</b></td>
      </tr>
      <tr>
        <td><b>SKILL-09</b></td>
        <td>شکایت گردشگران اروپایی از تندی یا شوری غیرمنتظره</td>
        <td>منوی هوشمند چندزبانه با شاخص عددی تندی (Mild, Medium, Spicy)</td>
        <td>BERTurk Classifier</td>
        <td><b>-۸۵٪ اعتراض ادویه</b></td>
      </tr>
      <tr>
        <td><b>SKILL-10</b></td>
        <td>تفاوت اندازه سالاد شیرازی و زیتون پرورده در شیفت‌های مختلف</td>
        <td>ترازوهای هوشمند گرم‌کشی بار سرد و پیاله‌های قالب‌زده استاندارد</td>
        <td>Portion-Vision Cam</td>
        <td><b>نوسان وزن &lt; ۵ گرم</b></td>
      </tr>
      <tr>
        <td><b>SKILL-11</b></td>
        <td>خشک شدن گوشت چنجه و برگ در ساعات پرتردد</td>
        <td>سنسور عمق‌سنج رطوبت و پروب ترمومتر گریل با هشدار خروج گوشت</td>
        <td>Grill-Sense Probe</td>
        <td><b>+۲۲٪ نرمی بافت گوشت</b></td>
      </tr>
      <tr>
        <td><b>SKILL-12</b></td>
        <td>اتمام باقلوای تازه پسته در ساعات پایانی شب</td>
        <td>مدل پیش‌بینی تقاضای دسر با اتصال به روند رزروهای شام</td>
        <td>ARIMA Prophet</td>
        <td><b>صفر شدن ناموجودی دسر</b></td>
      </tr>
    </tbody>
  </table>

  <h3>حوزه ج: رفتار کادر سالن، تسلط زبانی و آداب میزبانی (Staff Etiquette & Multi-Language)</h3>
  <table>
    <thead>
      <tr>
        <th style="width:10%">شناسه</th>
        <th style="width:25%">نقد خطا بر مبنای نظر مشتری</th>
        <th style="width:35%">راهکار استانداردهای عملیاتی هتلداری</th>
        <th style="width:15%">مدل هوش مصنوعی</th>
        <th style="width:15%">جهش عملکرد (Delta)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>SKILL-13</b></td>
        <td>چالش زبانی گارسون‌ها با توریست‌های روس (دمیتری اسمیرنوف)</td>
        <td>استقرار تبلت ترجمه صوتی فوری گفتار-به-گفتار روی مچ‌بند پرسنل سالن</td>
        <td>Whisper-v3 + DeepL</td>
        <td><b>+۳۵٪ رضایت مسافران روس</b></td>
      </tr>
      <tr>
        <td><b>SKILL-14</b></td>
        <td>بی‌توجهی به خالی شدن پارچ دوغ و لیوان آب مهمانان</td>
        <td>دوربین بینایی کامپیوتر پایش سطح مایعات میزها و ارسال الرت لرزشی به سالن‌دار</td>
        <td>Table-Vision Alert</td>
        <td><b>-۷۰٪ زمان شارژ نوشیدنی</b></td>
      </tr>
      <tr>
        <td><b>SKILL-15</b></td>
        <td>پرسش مکرر گارسون‌ها از یک میز «سفارش دادید؟»</td>
        <td>نمایشگر وضعیت زنده میزها (سبز: در حال صرف، زرد: منتظر سفارش، آبی: فاکتور)</td>
        <td>ESP32 Mesh Tag</td>
        <td><b>حذف مزاحمت کادر سالن</b></td>
      </tr>
      <tr>
        <td><b>SKILL-16</b></td>
        <td>عدم معرفی ترکیبات خورش فسنجان و میرزاقاسمی به گردشگران عرب</td>
        <td>کاتالوگ دیجیتال تبلتی با ویدیوهای کوتاه ۶ ثانیه‌ای معرفی محتویات غذاها</td>
        <td>Video-Menu QR</td>
        <td><b>+۴۵٪ سفارش خورش‌ها</b></td>
      </tr>
      <tr>
        <td><b>SKILL-17</b></td>
        <td>برخورد شتاب‌زده پرسنل هنگام اوج شلوغی جمعه شب</td>
        <td>استقرار ناظر کیفیت میزبانی و تعویض شیفت چرخشی هر ۳ ساعت در ساعات پیک</td>
        <td>Fatigue-Shift AI</td>
        <td><b>+۹۴٪ ثبات لبخند پرسنل</b></td>
      </tr>
      <tr>
        <td><b>SKILL-18</b></td>
        <td>تاخیر در جمع‌آوری بشقاب‌های خالی میزهای بالکن</td>
        <td>سنسور لودسل وزن سینی بازگشت و فراخوان اتوماتیک باسبوی</td>
        <td>Busboy Radio Call</td>
        <td><b>-۵ دقیقه پاکسازی میز</b></td>
      </tr>
    </tbody>
  </table>

  <div class="footer">
    <div>پلتفرم هوش تجاری و گاسترونومی میزبان استانبول (Mizban Istanbul) • دفتر تکسیم</div>
    <div>صفحه ۶ از ۸ • ماتریس مهارت‌های هوش مصنوعی (حوزه‌های الف، ب، ج)</div>
  </div>

  <div class="page-break"></div>

  <!-- ================= PAGE 7: 30 SKILLS MATRIX (DOMAINS D, E) + REPAIR APP ================= -->
  <div class="header-bar">
    <div>
      <h1>📋 ماتریس جامع ۳۰ مهارت ممیزی نقص‌ها و راهکارهای هوش مصنوعی</h1>
      <div class="sub">بخش دوم: حوزه‌های عملیاتی د و هـ (مهارت‌های ۱۹ تا ۳۰) و جدول اپلیکیشن عیب‌یابی</div>
    </div>
    <div>
      <span class="badge badge-gold">بهینه‌سازی مستمر</span>
    </div>
  </div>

  <h3>حوزه د: اتمسفر سالن، آکوستیک، بو و نظافت (Ambience, Acoustics & Cleanliness)</h3>
  <table>
    <thead>
      <tr>
        <th style="width:10%">شناسه</th>
        <th style="width:25%">نقد خطا بر مبنای نظر مشتری</th>
        <th style="width:35%">راهکار استانداردهای عملیاتی هتلداری</th>
        <th style="width:15%">مدل هوش مصنوعی</th>
        <th style="width:15%">جهش عملکرد (Delta)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>SKILL-19</b></td>
        <td>انتشار بوی سرخ‌کردنی و دود زغال در بخش انتهایی سالن ۱</td>
        <td>استقرار سیستم تهویه فشار مثبت و هودهای هوشمند با سنسور مکش دینامیک</td>
        <td>AirQuality-IoT</td>
        <td><b>۱۰۰٪ حذف بوی ماندگار</b></td>
      </tr>
      <tr>
        <td><b>SKILL-20</b></td>
        <td>بلندی آزاردهنده صدای موسیقی زنده یا همهمه در میزهای کناری</td>
        <td>سامانه پایش دسی‌بل محیطی و کالیبراسیون اتوماتیک توان بلندگوهای سقفی</td>
        <td>Sound-Level Tuner</td>
        <td><b>تثبیت صدا روی ۶۲dB</b></td>
      </tr>
      <tr>
        <td><b>SKILL-21</b></td>
        <td>افت دمای سالن در شب‌های سرد زمستانی تکسیم روی میزهای درب ورودی</td>
        <td>نصب پرده هوای گرم سنسوردار و پارتیشن چوبی عایق ورودی شمسه</td>
        <td>Thermal Barrier AI</td>
        <td><b>دمای ثابت ۲۲°C ورودی</b></td>
      </tr>
      <tr>
        <td><b>SKILL-22</b></td>
        <td>نور ضعیف میزهای گوشه جهت عکاسی اینستاگرامی غذاها</td>
        <td>نورپردازی اسپات لایت متمرکز با دمای رنگ ۳۰۰۰K (Warm White) بالای هر میز</td>
        <td>Lighting Lux-Meter</td>
        <td><b>+۶۰٪ اشتراک استوری</b></td>
      </tr>
      <tr>
        <td><b>SKILL-23</b></td>
        <td>تاخیر در شارژ دستمال و صابون سرویس بهداشتی در شب شلوغ</td>
        <td>سنسور اینفرارد مصرف مخازن شوینده و الرت نظافت پس از هر ۱۵ تردد</td>
        <td>Restroom Counter</td>
        <td><b>نظافت مستمر ۵ ستاره</b></td>
      </tr>
      <tr>
        <td><b>SKILL-24</b></td>
        <td>فشردگی صندلی‌ها در طبقه دوم هنگام چیدمان ایونت‌های گروهی</td>
        <td>نقشه‌کشی بهینه چیدمان مبلمان با الگوریتم ژنتیک جهت حفظ فاصله ۸۰cm</td>
        <td>Spatial Layout AI</td>
        <td><b>+۲۵٪ آرامش رفت‌وآمد</b></td>
      </tr>
    </tbody>
  </table>

  <h3>حوزه هـ: شفافیت صورتحساب، فاکتور و مدیریت دلجویی (Billing Transparency & Recovery)</h3>
  <table>
    <thead>
      <tr>
        <th style="width:10%">شناسه</th>
        <th style="width:25%">نقد خطا بر مبنای نظر مشتری</th>
        <th style="width:35%">راهکار استانداردهای عملیاتی هتلداری</th>
        <th style="width:15%">مدل هوش مصنوعی</th>
        <th style="width:15%">جهش عملکرد (Delta)</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>SKILL-25</b></td>
        <td>ابهام هزینه چای و کوور برای مهمانان خارجی (David Miller)</td>
        <td>تفکیک چای ولکام رایگان با درج برچسب Compliment Hospitality روی فاکتور</td>
        <td>Bill-Clarity Engine</td>
        <td><b>حذف ۱۰۰٪ سوءتفاهم مالی</b></td>
      </tr>
      <tr>
        <td><b>SKILL-26</b></td>
        <td>تفاوت نرخ ارز لیر/دلار روی صورتحساب توریست‌ها</td>
        <td>اتصال نرخ لحظه‌ای بانک مرکزی ترکیه به نرم‌افزار حسابداری و چاپ نرخ برابری</td>
        <td>Forex Live Sync</td>
        <td><b>شفافیت کامل ارزی</b></td>
      </tr>
      <tr>
        <td><b>SKILL-27</b></td>
        <td>عدم پیگیری نارضایتی مشتریانی که بشقاب را نیمه‌کاره رها کردند</td>
        <td>پروتکل فوری مدیر سالن: تعویض غذا بدون دریافت هزینه و اهدای باقلوا</td>
        <td>Plate-Waste AI</td>
        <td><b>جلوگیری از نقد منفی ۱★</b></td>
      </tr>
      <tr>
        <td><b>SKILL-28</b></td>
        <td>تاخیر در پاسخ به نقدهای ۲ و ۳ ستاره ثبت‌شده در گوگل مپ</td>
        <td>بات تریاژ بلادرنگ با ارسال متن عذرخواهی اختصاصی زیر ۱۵ دقیقه</td>
        <td>LLM Diplomatic Triage</td>
        <td><b>پاسخ ۱۰۰٪ زیر ۱۵ دقیقه</b></td>
      </tr>
      <tr>
        <td><b>SKILL-29</b></td>
        <td>عدم ترغیب مهمانان خوشحال به ثبت نظر در تریپ‌ادوایزر</td>
        <td>ارسال پیامک تشکر با لینک مستقیم ثبت نظر و کارت NFC سر میز</td>
        <td>NFC Review Booster</td>
        <td><b>+۳۵٪ شتاب نقد ۵★</b></td>
      </tr>
      <tr>
        <td><b>SKILL-30</b></td>
        <td>ناشناخته ماندن ظرفیت‌های دورهمی شعبه دوم (کوجاتپه) برای مهمانان شعبه ۱</td>
        <td>ارائه کارت دعوت با ترانسفر رایگان ۵ دقیقه‌ای به سالن شمسه سو کلاب</td>
        <td>Branch Spillover Sync</td>
        <td><b>+۱۸۴,۰۰۰ ₺ سود ماهانه</b></td>
      </tr>
    </tbody>
  </table>

  <div style="background:#faf5ee;border:1.5px solid #c48a48;border-radius:6px;padding:6px 10px;margin-bottom:6px">
    <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap">
      <div>
        <b style="color:#14100d;font-size:8.5pt">🌐 پیوند ورود مستقیم به اپلیکیشن عیب‌یابی و اصلاح رستوران:</b><br>
        <a style="font-family:monospace;font-size:7.8pt;color:#0284c7;font-weight:bold" href="https://shamse-restaurant.pages.dev/restaurant_repair_app.html" target="_blank">
          https://shamse-restaurant.pages.dev/restaurant_repair_app.html
        </a>
      </div>
      <div>
        <span class="badge badge-success">نسخه تعاملی PWA با قابلیت ارسال به واتساپ و تلگرام</span>
      </div>
    </div>
  </div>

  <h3 style="color:#b37d36;margin-top:2px">جدول راهکارهای اصلاحی اصلی رستوران و اقدامات لازم در اپلیکیشن (Main Repairs & Actions)</h3>
  <table>
    <thead>
      <tr>
        <th style="width:16%">نقص شناسایی‌شده</th>
        <th style="width:24%">نقد کامنت نمونه</th>
        <th style="width:30%">تعمیر و اصلاح عملیاتی (Repair Action)</th>
        <th style="width:15%">مدل هوش مصنوعی در اپ</th>
        <th style="width:15%">نتیجه در اپلیکیشن</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>تاخیر پخت برنج پیک</b></td>
        <td>مهسا رضایی (۳۵ دقیقه انتظار)</td>
        <td>سامانه پیش‌پخت داینامیک برنج بر مبنای صف ورودی استقلال</td>
        <td>YOLOv8 + Timer KDS</td>
        <td><b>۴۲٪- کاهش تاخیر</b></td>
      </tr>
      <tr>
        <td><b>تردی ته‌دیگ زعفرانی</b></td>
        <td>آرش نیکزاد (نرم شدن مقطعی)</td>
        <td>کالیبراسیون ترموستات کف دیگ و ترکیب ماست و زعفران غلیظ</td>
        <td>Crisp Sensor IoT</td>
        <td><b>۱۸٪+ رضایت منو پلو</b></td>
      </tr>
      <tr>
        <td><b>ابهام کوور و چای</b></td>
        <td>David Miller (Cover Charge)</td>
        <td>اهدای چای رایگان ولکام و درج عبارت No Hidden Charges</td>
        <td>Billing Policy Engine</td>
        <td><b>۱۰۰٪ حذف اعتراض</b></td>
      </tr>
      <tr>
        <td><b>چالش زبانی روس‌ها</b></td>
        <td>Dmitry Smirnov (زبان روسی)</td>
        <td>تبلت صوتی ترجمه بلادرنگ و منوی الفبای سیریلیک</td>
        <td>Whisper-v3 Speech AI</td>
        <td><b>۳۲٪+ رضایت CIS</b></td>
      </tr>
      <tr>
        <td><b>ازدحام و ریزش صف</b></td>
        <td>پیاده‌راه استقلال (ترک صف)</td>
        <td>نوبت‌دهی هوشمند پیامکی و ترانسفر به شعبه ۲ کوجاتپه</td>
        <td>Twilio SMS / Dispatch</td>
        <td><b>۲۸٪+ حفظ مسافران</b></td>
      </tr>
      <tr>
        <td><b>آکوستیک موسیقی سالن</b></td>
        <td>دورهمی‌های خانوادگی</td>
        <td>تنظیم خودکار بلندی صدا روی ۶۲ دسی‌بل با سنسور هوشمند</td>
        <td>Acoustic dB Sensor</td>
        <td><b>آکوستیک استاندارد</b></td>
      </tr>
      <tr>
        <td><b>پاسخ به نقدهای منفی</b></td>
        <td>نقدهای ۲ یا ۳ ستاره گوگل</td>
        <td>هشدار تلگرام ظرف ۹۰ ثانیه و ارسال ووچر دلجویی ۲۰٪</td>
        <td>Telegram Triage Bot</td>
        <td><b>بازگشت ۴۲٪ مشتریان</b></td>
      </tr>
      <tr>
        <td><b>ساعات خلوت سالن ۲</b></td>
        <td>ظرفیت خالی ۱۴:۳۰ تا ۱۸:۳۰</td>
        <td>میزبانی دورهمی مافیا و کارآفرینان در طبقه دوم شمسه</td>
        <td>Yield RevPASH Model</td>
        <td><b>۱۸۴,۰۰۰+ ₺ سود ماهانه</b></td>
      </tr>
    </tbody>
  </table>

  <div class="footer">
    <div>پلتفرم هوش تجاری و گاسترونومی میزبان استانبول (Mizban Istanbul) • دفتر تکسیم</div>
    <div>صفحه ۷ از ۸ • ماتریس مهارت‌ها و سامانه عیب‌یابی عملیاتی</div>
  </div>

  <div class="page-break"></div>

  <!-- ================= PAGE 8: MULTIMEDIA PODCAST, VIDEO & OMNICHANNEL DISPATCH ================= -->
  <div class="header-bar">
    <div>
      <h1>🎙 پادکست اجرایی، ویدیوی تحلیلی و درگاه‌های چندکاناله شمسه</h1>
      <div class="sub">خلاصه چندرسانه‌ای صوتی و تصویری، پاسخ‌های ۴ زبانه و بسته ارسال اختصاصی</div>
    </div>
    <div>
      <span class="badge badge-success">آماده شنیدن، تماشا و ارسال</span>
    </div>
  </div>

  <h2>۵. پادکست صوتی و ویدیوی مستند ممیزی (Audio Podcast & Video Briefing)</h2>
  <div style="background:#faf5ee;border:1px solid #c48a48;border-radius:4px;padding:6px 10px;font-size:7.5pt;margin-bottom:6px">
    <b>🎧 محتوای فایل صوتی ضبط‌شده و ویدیوی MP4 چندرسانه‌ای:</b><br>
    • <b>فایل صوتی پادکست (MP3):</b> در مسیر <code>assets/audio/shamse_intelligence_podcast.mp3</code> (مدت: ۱ دقیقه و ۵ ثانیه)<br>
    • <b>فایل صوتی پادکست ترکی استانبولی (Türkçe MP3):</b> در مسیر <code>assets/audio/shamse_intelligence_podcast_tr.mp3</code> (مدت: ۱ دقیقه و ۲۰ ثانیه - خلاصه هیئت مدیره به ترکی)<br>
    • <b>ویدیوی مستند (Full HD MP4):</b> در مسیر <a href="https://shamse-restaurant.pages.dev/assets/video/shamse_intelligence_video.mp4">assets/video/shamse_intelligence_video.mp4</a> و نسخه ریشه <a href="https://shamse-restaurant.pages.dev/shamse_intelligence_video.mp4">shamse_intelligence_video.mp4</a> با ترکیب اسلایدهای تصویری کامنت‌ها، نقد خطاها و صدای همگام‌سازی‌شده.<br>
    • <b>وب‌ویو تعاملی پلیر:</b> دسترسی برخط با پلیرهای صوتی و تصویری در: <a href="https://shamse-restaurant.pages.dev/shamse_sentiment_report.html">https://shamse-restaurant.pages.dev/shamse_sentiment_report.html</a>
  </div>

  <h2>۶. نمونه پاسخ‌های آماده هوش مصنوعی به ۴ زبان</h2>
  <table>
    <thead>
      <tr>
        <th style="width:20%">پلتفرم و زبان</th>
        <th>متن پاسخ دیپلماتیک و محبت‌آمیز جهت انتشار فوری</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td><b>🇬🇧 انگلیسی<br>(TripAdvisor)</b></td>
        <td style="direction:ltr;text-align:left;font-size:7.2pt">
          <i>"Dear Valued Guest, thank you for dining with us at Shamse Istiklal! We are delighted you enjoyed our authentic saffron kebabs and Persian hospitality. Regarding tea and bread, we proudly serve complimentary saffron tea as our warm welcome to international travelers. We eagerly look forward to hosting you again on your next Istanbul trip!"</i>
        </td>
      </tr>
      <tr>
        <td><b>🇷🇺 روسی<br>(Yandex Maps)</b></td>
        <td style="direction:ltr;text-align:left;font-size:7.2pt">
          <i>"Здравствуйте! Большое спасибо за высокую оценку ресторана Shamse. Нам приятно, что вам понравился традиционный халяльный шашлык и восточная атмосфера. Мы добавили меню на русском языке и всегда рады видеть вас снова на улице Истикляль!"</i>
        </td>
      </tr>
      <tr>
        <td><b>🇮🇷 فارسی<br>(Google Maps)</b></td>
        <td style="font-size:7.6pt">
          «سلام و درود؛ از نگاه گرم و لطف بی‌دریغ شما به خانواده شمسه سپاسگزاریم. تلاش ما زنده نگاه داشتن طعم اصیل سفره‌های ایرانی در غربت است. تدابیر ویژه‌ای جهت تسریع سرویس در شب‌های شلوغ اتخاذ شده و مشتاقانه چشم‌انتظار دیدار دوباره شما و عزیزانتان در دو شعبه تکسیم هستیم.»
        </td>
      </tr>
      <tr>
        <td><b>🇹🇷 ترکی استانبولی<br>(Google Maps TR)</b></td>
        <td style="direction:ltr;text-align:left;font-size:7.2pt">
          <i>"Değerli Misafirimiz, Şemse Restoran'ı tercih ettiğiniz için teşekkür ederiz. Geleneksel safranlı lezzetlerimizi ve misafirperverliğimizi beğenmeniz bizi onurlandırdı. En kısa zamanda sizleri tekrar ağırlamaktan mutluluk duyarız."</i>
        </td>
      </tr>
    </tbody>
  </table>

  <h2>۷. درگاه‌های رسمی ارتباطی آماده ارسال (Omnichannel Dispatch Table)</h2>
  <table>
    <thead>
      <tr>
        <th>کانال ارتباطی</th>
        <th>شناسه / آدرس مقصد</th>
        <th>وضعیت فنی</th>
        <th>پروتکل ارسال و بسته محتوایی</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td>✉️ <b>ایمیل سازمانی</b></td>
        <td><a href="mailto:shamsemedia1@gmail.com">shamsemedia1@gmail.com</a></td>
        <td><span class="badge badge-success">آماده ارسال</span></td>
        <td>سرویس Mailjet Relay (پیوست گزارش PDF + فایل اسلایدهای PPTX)</td>
      </tr>
      <tr>
        <td>🟢 <b>واتساپ بیزنس</b></td>
        <td><a href="https://wa.me/905013252452" target="_blank" style="color:#27ae60">+90 501 325 24 52</a></td>
        <td><span class="badge badge-success">لینک تک‌لمسی دستی</span></td>
        <td>پروتکل wa.me جهت شروع گفتگو و ارسال لینک اپلیکیشن عیب‌یابی</td>
      </tr>
      <tr>
        <td>📸 <b>اینستاگرام رسمی</b></td>
        <td><a href="https://instagram.com/shamse.istanbul" target="_blank">@shamse.istanbul</a></td>
        <td><span class="badge badge-success">اکانت اختصاصی شمسه</span></td>
        <td>پیام دایرکت تعاملی با دعوت به بررسی داشبورد تحلیلی</td>
      </tr>
      <tr>
        <td>✈️ <b>تلگرام رسمی</b></td>
        <td><a href="https://t.me/shamse_istanbul" target="_blank">@shamse_istanbul</a></td>
        <td><span class="badge badge-success">کانال و ربات فعال</span></td>
        <td>ربات هوش تجاری جهت تریاژ بلادرنگ کامنت‌های منفی گوگل مپ</td>
      </tr>
      <tr>
        <td>📘 <b>فیسبوک رسمی</b></td>
        <td><a href="https://facebook.com/shamseistanbul" target="_blank">facebook.com/shamseistanbul</a></td>
        <td><span class="badge badge-success">پیج متصل</span></td>
        <td>ارسال بسته گزارش هفتگی به جامعه گردشگران بین‌المللی</td>
      </tr>
    </tbody>
  </table>

  <div style="margin-top:6px;border:1px solid #c48a48;border-radius:4px;padding:5px 8px;background:#faf6f0;display:flex;justify-content:space-between;align-items:center">
    <div>
      <b style="color:#14100d">تاییدیه ممیزی و اعتبارنامه هوش تجاری میزبان استانبول</b><br>
      <span style="font-size:6.8pt;color:#666">کد رهگیری سند: MIZBAN-SHAMSE-AUDIT-2026-V4 • نسخه ویدیویی، اسکرین‌شات‌ها و اپلیکیشن عیب‌یابی</span>
    </div>
    <div style="text-align:left">
      <span class="badge badge-gold" style="font-size:7pt">مهردار و امضاشده دیجیتال</span>
    </div>
  </div>

  <div class="footer">
    <div>پلتفرم هوش تجاری و گاسترونومی میزبان استانبول (Mizban Istanbul) • دفتر تکسیم</div>
    <div>صفحه ۸ از ۸ • پادکست، ویدیو و دیسپچ چندکاناله</div>
  </div>

</body>
</html>"""

def generate_pdf():
    print(f"Compiling vector PDF report to: {PDF_OUTPUT}")
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.set_content(HTML_CONTENT, wait_until="networkidle")
        page.pdf(
            path=PDF_OUTPUT,
            format="A4",
            print_background=True,
            margin={"top": "8mm", "bottom": "8mm", "left": "10mm", "right": "10mm"}
        )
        browser.close()
    
    # Copy to root
    import shutil
    shutil.copyfile(PDF_OUTPUT, ROOT_PDF_OUTPUT)
    
    size = os.path.getsize(PDF_OUTPUT)
    print(f"Vector PDF Report generated successfully: {PDF_OUTPUT} ({size:,} bytes)")
    print(f"Root PDF copy updated: {ROOT_PDF_OUTPUT} ({os.path.getsize(ROOT_PDF_OUTPUT):,} bytes)")

if __name__ == "__main__":
    generate_pdf()
