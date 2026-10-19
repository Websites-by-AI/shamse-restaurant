#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Patches intelligence.html to integrate Module 12:
"🌐 ۱۲. هاب بین‌المللی جذب همکاری و ارسال ایمیل Resend (۱۰ گروه استراتژیک، ۵ زبان، با پکیج چندرسانه‌ای ویدیو، پاورپوینت و PDF)"
"""

import os
import json
import re

ROOT = os.path.dirname(os.path.abspath(__file__))
REPO_ROOT = os.path.dirname(ROOT)
HTML_FILE = os.path.join(REPO_ROOT, "intelligence.html")
DB_FILE = os.path.join(ROOT, "outreach_multilingual_db.json")

def patch_intelligence():
    with open(HTML_FILE, "r", encoding="utf-8") as f:
        html = f.read()

    with open(DB_FILE, "r", encoding="utf-8") as f:
        master_db = json.load(f)

    # 1. Add Subnav Button if not present
    subnav_target = '<button class="mod-pill" onclick="scrollToSection(\'mod-datamile\')">💰 ۱۱. اینفوگرافیک مالی، گوگل مپ و Data Mile App</button>'
    new_subnav_btn = (
        subnav_target + '\n        '
        '<button class="mod-pill" onclick="scrollToSection(\'mod-resend-outreach\')" '
        'style="border-color:#2ecc71;color:#2ecc71;background:rgba(46,204,113,0.1);font-weight:700">'
        '🌐 ۱۲. هاب ایمیل Resend و جذب مشارکت (۱۰ گروه / ۵ زبان)</button>'
    )
    if 'mod-resend-outreach' not in html:
        if subnav_target in html:
            html = html.replace(subnav_target, new_subnav_btn, 1)
            print("Added subnav button for Module 12.")

    # 2. Module 12 HTML Section
    module_12_html = '''
    <!-- MODULE 12: RESEND & MULTILINGUAL PARTNERSHIP OUTREACH HUB -->
    <section class="mod-card" id="mod-resend-outreach" style="border:1px solid #2ecc71;box-shadow:0 12px 40px rgba(46,204,113,0.12)">
      
      <!-- Header -->
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:16px;margin-bottom:20px">
        <div>
          <div style="display:inline-flex;align-items:center;gap:6px;background:rgba(46,204,113,0.15);color:#2ecc71;padding:4px 12px;border-radius:20px;font-size:.78rem;font-weight:bold;margin-bottom:8px">
            <span>⚡ زیرساخت ارسال ایمیل Resend API + پکیج سه‌گانه چندرسانه‌ای</span>
          </div>
          <h2 class="sec-title" style="margin:0 0 6px 0;color:var(--cream)">
            🌐 ۱۲. هاب بین‌المللی جذب همکاری و ارسال ایمیل Resend (۱۰ گروه استراتژیک، ۵ زبان، با پکیج چندرسانه‌ای)
          </h2>
          <p class="sec-sub" style="margin:0;max-width:920px">
            سامانه تخصصی توسعه ارتباطات سازمانی و جذب شرکا در ۱۰ اکوسیستم هدف (دولت و شهرداری‌ها، پزشکان، برندهای زنجیره‌ای، یوتیوبرها، اینستاگرام، دانشگاه‌ها و فراخوان‌ها، پژوهشگران ISI، هتل‌های ۵ ستاره، سرمایه‌گذاران VC و اتاق‌های بین‌المللی) به ۵ زبان زنده جهان (فارسی، انگلیسی، ترکی، عربی، آلمانی) مجهز به ارسال مستقیم Resend API، تصدیق DNS، شبیه‌ساز سندباکس و دسترسی به ویدیو دموی ۳ دقیقه‌ای، اسلایدهای ۲۴ صفحه‌ای PPTX و سفیدنامه ۳۲ هزار نقد PDF.
          </p>
        </div>

        <div style="display:flex;gap:10px;flex-wrap:wrap">
          <a href="#resend-console" class="btn btn--gold" style="font-size:.82rem;background:#2ecc71;border-color:#2ecc71;color:#14100d;font-weight:bold">
            🚀 کنسول ارسال Resend ↗
          </a>
          <button class="btn btn--ghost" onclick="openVideoPitchModal()" style="font-size:.82rem;border-color:var(--copper);color:var(--copper)">
            🎬 پخش ویدیوی دمو (۳ دقیقه)
          </button>
        </div>
      </div>

      <!-- KPI Metrics Strip -->
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:14px;margin-bottom:26px">
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:14px 16px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#2ecc71">۱۰ گروه</div>
          <div style="font-size:.76rem;color:var(--muted);margin-top:4px">سگمنت‌های هدف سازمانی B2B</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:14px 16px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:var(--copper)">۵ زبان</div>
          <div style="font-size:.76rem;color:var(--muted);margin-top:4px">فارسی، انگلیسی، ترکی، عربی، آلمانی</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:14px 16px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#ffd21e">۵۰ بسته</div>
          <div style="font-size:.76rem;color:var(--muted);margin-top:4px">قالب آماده شخصی‌سازی‌شده</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:14px 16px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#38bdf8">۳ دارایی</div>
          <div style="font-size:.76rem;color:var(--muted);margin-top:4px">ویدیو دمو + پاورپوینت + PDF سفیدنامه</div>
        </div>
        <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:14px 16px;text-align:center">
          <div style="font-size:1.6rem;font-weight:900;color:#a855f7">Resend API</div>
          <div style="font-size:.76rem;color:var(--muted);margin-top:4px">ارسال ابری + احراز SPF/DKIM</div>
        </div>
      </div>

      <!-- Step 1: Select Stakeholder Segment -->
      <div style="margin-bottom:24px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
          <label style="font-size:.86rem;font-weight:700;color:var(--cream)">
            🎯 مرحله ۱: انتخاب گروه و اکوسیستم هدف (Stakeholder Segment):
          </label>
          <span style="font-size:.75rem;color:var(--muted)">روی هر گروه کلیک کنید تا متن و دیتای اختصاصی بارگذاری شود</span>
        </div>
        
        <div id="outreachSegmentBadges" style="display:grid;grid-template-columns:repeat(auto-fill,minmax(220px,1fr));gap:10px">
          <!-- Rendered by JS -->
        </div>
      </div>

      <!-- Step 2: Select Language -->
      <div style="margin-bottom:24px">
        <label style="font-size:.86rem;font-weight:700;color:var(--cream);display:block;margin-bottom:10px">
          🌍 مرحله ۲: انتخاب زبان رسمی مکاتبه (Outreach Language):
        </label>
        
        <div id="outreachLanguageTabs" style="display:flex;gap:10px;flex-wrap:wrap">
          <!-- Rendered by JS -->
        </div>
      </div>

      <!-- Main Workspace: Split Grid (Left: Preview & Assets | Right: Resend Dispatch & Personalization) -->
      <div style="display:grid;grid-template-columns:1.35fr 1fr;gap:22px;margin-bottom:28px" id="outreachMainGrid">
        
        <!-- Left Column: Interactive Live Email Preview -->
        <div style="background:var(--ink-2);border:1px solid var(--line-copper);border-radius:6px;padding:20px;display:flex;flex-direction:column">
          
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;border-bottom:1px solid var(--line);padding-bottom:12px;flex-wrap:wrap;gap:8px">
            <div style="display:flex;align-items:center;gap:8px">
              <span id="previewSegmentIcon" style="font-size:1.3rem">🏛️</span>
              <div>
                <h4 id="previewSegmentTitle" style="margin:0;font-size:.95rem;color:var(--cream);font-weight:700">دولت و شهرداری‌ها</h4>
                <div id="previewTargetRoles" style="font-size:.72rem;color:var(--muted)">مخاطبان پیشنهادی</div>
              </div>
            </div>

            <div style="display:flex;gap:6px">
              <button class="btn btn--ghost" onclick="copyEmailSubject()" style="font-size:.75rem;padding:5px 10px">
                📋 کپی عنوان
              </button>
              <button class="btn btn--ghost" onclick="copyEmailHtml()" style="font-size:.75rem;padding:5px 10px">
                📋 کپی HTML
              </button>
            </div>
          </div>

          <!-- Email Subject Line Box -->
          <div style="background:var(--ink-3);border:1px solid var(--line);border-radius:4px;padding:10px 14px;margin-bottom:16px">
            <div style="font-size:.7rem;color:var(--copper);font-weight:700;margin-bottom:3px">موضوع ایمیل (Email Subject):</div>
            <div id="previewSubjectText" style="font-size:.85rem;color:#ffd21e;font-weight:600;line-height:1.5">
              ...
            </div>
          </div>

          <!-- Simulated Email Client Container -->
          <div id="simulatedEmailViewer" style="background:#ffffff;color:#222222;border-radius:6px;padding:24px;overflow-y:auto;max-height:640px;box-shadow:inset 0 0 10px rgba(0,0,0,0.15);font-size:.88rem;line-height:1.75">
            <!-- Rendered by JS -->
          </div>

        </div>

        <!-- Right Column: Personalization & Resend Dispatch Console -->
        <div style="display:flex;flex-direction:column;gap:18px" id="resend-console">
          
          <!-- Box 1: Recipient Personalization -->
          <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:18px">
            <h4 style="margin:0 0 12px 0;font-size:.92rem;color:var(--cream);display:flex;align-items:center;gap:6px">
              <span>✍️ شخصی‌سازی گیرنده (Recipient Tokens)</span>
            </h4>

            <div style="display:grid;gap:10px">
              <div>
                <label style="font-size:.74rem;color:var(--muted);display:block;margin-bottom:4px">نام و عنوان مخاطب ({recipient_name}):</label>
                <input type="text" id="tokenRecipientName" value="دکتر احمدی" oninput="updateOutreachTokens()"
                  style="width:100%;background:var(--ink-3);border:1px solid var(--line);color:var(--cream);padding:8px 10px;border-radius:4px;font-size:.82rem">
              </div>

              <div>
                <label style="font-size:.74rem;color:var(--muted);display:block;margin-bottom:4px">نام سازمان / برند / کانال ({recipient_org}):</label>
                <input type="text" id="tokenRecipientOrg" value="شهرداری کلانشهر استانبول (İBB)" oninput="updateOutreachTokens()"
                  style="width:100%;background:var(--ink-3);border:1px solid var(--line);color:var(--cream);padding:8px 10px;border-radius:4px;font-size:.82rem">
              </div>

              <div>
                <label style="font-size:.74rem;color:var(--muted);display:block;margin-bottom:4px">ایمیل گیرنده (To Email):</label>
                <input type="email" id="tokenRecipientEmail" value="turizm@ibb.istanbul"
                  style="width:100%;background:var(--ink-3);border:1px solid var(--line);color:#38bdf8;padding:8px 10px;border-radius:4px;font-size:.82rem;direction:ltr;text-align:left">
              </div>
            </div>
          </div>

          <!-- Box 2: Resend API Configuration -->
          <div style="background:var(--ink-2);border:1px solid var(--line-copper);border-radius:6px;padding:18px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
              <h4 style="margin:0;font-size:.92rem;color:#2ecc71;display:flex;align-items:center;gap:6px">
                <span>🚀 تنظیمات درگاه Resend API</span>
              </h4>
              <span id="resendKeyStatusBadge" style="font-size:.7rem;padding:2px 8px;border-radius:10px;background:rgba(46,204,113,0.15);color:#2ecc71">
                سندباکس فعال
              </span>
            </div>

            <div style="margin-bottom:12px">
              <label style="font-size:.74rem;color:var(--muted);display:block;margin-bottom:4px">کلید اختصاصی Resend API (اختیاری برای تست):</label>
              <div style="position:relative">
                <input type="password" id="resendApiKeyInput" placeholder="re_123456789_abcdef..."
                  onchange="saveResendKey(this.value)"
                  style="width:100%;background:var(--ink-3);border:1px solid var(--line);color:var(--cream);padding:8px 10px;border-radius:4px;font-size:.82rem;direction:ltr;text-align:left">
                <button type="button" onclick="toggleResendKeyVisibility()" 
                  style="position:absolute;left:8px;top:50%;transform:translateY(-50%);background:none;border:none;color:var(--muted);cursor:pointer;font-size:.8rem">👁️</button>
              </div>
              <div style="font-size:.68rem;color:var(--muted);margin-top:4px">
                در صورت خالی بودن، سامانه در حالت تست امنیتی شبیه‌سازی (Deterministic Sandbox) اجرا می‌شود.
              </div>
            </div>

            <div style="margin-bottom:14px">
              <label style="font-size:.74rem;color:var(--muted);display:block;margin-bottom:4px">آدرس فرستنده مجاز (From Verified Domain):</label>
              <select id="resendSenderSelect" style="width:100%;background:var(--ink-3);border:1px solid var(--line);color:var(--cream);padding:8px 10px;border-radius:4px;font-size:.82rem;direction:ltr">
                <option value="Mizban Istanbul &lt;partnership@mizbanistanbul.com&gt;">Mizban Istanbul &lt;partnership@mizbanistanbul.com&gt;</option>
                <option value="Mizban Concierge &lt;concierge@mizbanistanbul.com&gt;">Mizban Concierge &lt;concierge@mizbanistanbul.com&gt;</option>
                <option value="Mizban Intelligence &lt;intel@mizbanistanbul.com&gt;">Mizban Intelligence &lt;intel@mizbanistanbul.com&gt;</option>
              </select>
            </div>

            <!-- Dispatch Action Buttons -->
            <div style="display:grid;gap:8px">
              <button class="btn btn--gold" onclick="executeResendDispatch(false)" 
                style="background:#2ecc71;border-color:#2ecc71;color:#14100d;font-weight:bold;justify-content:center;padding:11px">
                🚀 ارسال مستقیم با Resend API
              </button>

              <div style="display:grid;grid-template-columns:1fr 1fr;gap:8px">
                <button class="btn btn--ghost" onclick="executeResendDispatch(true)" 
                  style="justify-content:center;font-size:.78rem;border-color:#38bdf8;color:#38bdf8">
                  🧪 شبیه‌سازی سندباکس
                </button>
                <button class="btn btn--ghost" onclick="downloadEmailEml()" 
                  style="justify-content:center;font-size:.78rem;border-color:var(--copper);color:var(--copper)">
                  📥 دانلود فایل .eml
                </button>
              </div>
            </div>

            <div id="resendDispatchAlert" style="display:none;margin-top:12px;padding:10px 12px;border-radius:4px;font-size:.78rem"></div>

          </div>

          <!-- Box 3: Deliverable Attachments Quick Access -->
          <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:16px">
            <h4 style="margin:0 0 10px 0;font-size:.88rem;color:var(--cream)">
              📦 دارایی‌های چندرسانه‌ای ضمیمه‌شده در ایمیل:
            </h4>

            <div style="display:grid;gap:8px;font-size:.78rem">
              <div style="display:flex;justify-content:space-between;align-items:center;background:var(--ink-3);padding:8px 10px;border-radius:4px">
                <span style="color:#ffd21e">🎥 ویدیو دموی ۳ دقیقه‌ای</span>
                <button class="btn btn--ghost" onclick="openVideoPitchModal()" style="font-size:.7rem;padding:3px 8px">پخش ↗</button>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;background:var(--ink-3);padding:8px 10px;border-radius:4px">
                <span style="color:var(--copper)">📊 ارائه ۲۴ اسلایدی (PowerPoint)</span>
                <a href="mizban_restaurant_intelligence_pitch.pptx" download class="btn btn--ghost" style="font-size:.7rem;padding:3px 8px">دانلود 📥</a>
              </div>
              <div style="display:flex;justify-content:space-between;align-items:center;background:var(--ink-3);padding:8px 10px;border-radius:4px">
                <span style="color:#38bdf8">📄 سفیدنامه و ممیزی نظرات (PDF)</span>
                <a href="mizban_restaurant_weekly_report.pdf" download class="btn btn--ghost" style="font-size:.7rem;padding:3px 8px">دانلود 📥</a>
              </div>
            </div>
          </div>

        </div>

      </div>

      <!-- Infrastructure Comparison: Resend vs Postmark vs SendGrid vs AWS SES vs Instantly -->
      <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:22px;margin-bottom:24px">
        <h3 style="margin:0 0 8px 0;font-size:1.05rem;color:var(--cream);font-weight:700">
          ⚖️ ارزیابی معماری سرویس‌های ارسال ایمیل: Resend در مقایسه با سایر ارائه‌دهندگان
        </h3>
        <p style="font-size:.82rem;color:var(--muted);margin-bottom:16px">
          تحلیل فنی تفاوت ایمیل‌های تراکنشی/ارتباط با شرکای تاییدشده (Resend / Postmark) در برابر سامانه‌های ایمیل انبوه سرد (Cold Email Platforms):
        </p>

        <div style="overflow-x:auto">
          <table style="width:100%;border-collapse:collapse;font-size:.8rem;text-align:right">
            <thead>
              <tr style="background:var(--ink-3);border-bottom:2px solid var(--copper)">
                <th style="padding:10px;color:var(--cream)">سرویس</th>
                <th style="padding:10px;color:var(--cream)">نوع کاربری بهینه</th>
                <th style="padding:10px;color:var(--cream)">نرخ تحویل (Deliverability)</th>
                <th style="padding:10px;color:var(--cream)">احراز هویت دامنه (DNS)</th>
                <th style="padding:10px;color:var(--cream)">هزینه پایه</th>
                <th style="padding:10px;color:var(--cream)">قانون اسپم و ایمیل سرد</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid var(--line);background:rgba(46,204,113,0.06)">
                <td style="padding:10px;font-weight:bold;color:#2ecc71">Resend (پیشنهاد ما)</td>
                <td style="padding:10px">ایمیل‌های رسمی B2B، گزارش‌های هفتگی، آنبوردینگ و React Email</td>
                <td style="padding:10px;color:#2ecc71">★ ۹۹.۴٪ (زیرساخت اختصاصی SES)</td>
                <td style="padding:10px">DKIM 2048-bit + SPF + DMARC + Return-Path</td>
                <td style="padding:10px">۳,۰۰۰ ایمیل ماهانه رایگان ($۲۰ برای ۵۰k)</td>
                <td style="padding:10px;color:#ffd21e">فقط مخاطبان هدف معتبر و تاییدشده (Bounce &lt; ۵٪)</td>
              </tr>
              <tr style="border-bottom:1px solid var(--line)">
                <td style="padding:10px;font-weight:bold;color:var(--cream)">Postmark</td>
                <td style="padding:10px">ایمیل‌های تراکنشی فوق‌سریع و تیکت‌ها</td>
                <td style="padding:10px;color:#2ecc71">★ ۹۹.۶٪</td>
                <td style="padding:10px">DKIM + Return-Path اجباری</td>
                <td style="padding:10px">$۱۵ برای ۱۰,۰۰۰ ایمیل</td>
                <td style="padding:10px;color:#ef4444">ایمیل سرد کاملاً ممنوع و اکانت مسدود می‌شود</td>
              </tr>
              <tr style="border-bottom:1px solid var(--line)">
                <td style="padding:10px;font-weight:bold;color:var(--cream)">Amazon SES</td>
                <td style="padding:10px">ارسال انبوه با کمترین هزینه زیرساختی</td>
                <td style="padding:10px;color:var(--muted)">۹۵٪ (بستگی به IP اشتراکی دارد)</td>
                <td style="padding:10px">نیازمند تنظیم دستی Route53</td>
                <td style="padding:10px">$۰.۱۰ به ازای هر ۱,۰۰۰ ایمیل</td>
                <td style="padding:10px">قوانین سختگیرانه باود ریت در سندباکس AWS</td>
              </tr>
              <tr style="border-bottom:1px solid var(--line)">
                <td style="padding:10px;font-weight:bold;color:var(--cream)">Twilio SendGrid</td>
                <td style="padding:10px">کمپین‌های بازاریابی سنتی و خبرنامه</td>
                <td style="padding:10px;color:var(--muted)">۹۳٪ (به دلیل ارسال‌های اسپم در IP‌های مشترک)</td>
                <td style="padding:10px">تایید خودکار CNAME</td>
                <td style="padding:10px">۱۰۰ ایمیل روزانه رایگان ($۲۰ برای ۵۰k)</td>
                <td style="padding:10px">تحت نظارت سخت‌گیرانه شکایات اسپم</td>
              </tr>
              <tr style="background:rgba(210,154,90,0.06)">
                <td style="padding:10px;font-weight:bold;color:var(--copper)">Instantly / Smartlead</td>
                <td style="padding:10px">ایمیل سرد گسترده با چرخش صندوق‌ها (Mailbox Rotation)</td>
                <td style="padding:10px;color:#ffd21e">۹۶٪ (با گرم کردن خودکار ۳ هفته‌ای)</td>
                <td style="padding:10px">اتصال به دامنه‌های فرعی کمکی</td>
                <td style="padding:10px">$۳۷ تا $۹۴ ماهانه</td>
                <td style="padding:10px;color:#2ecc71">ویژه ایمیل سرد با ابزار Warmup نامحدود</td>
              </tr>
            </tbody>
          </table>
        </div>

        <div style="background:var(--ink-3);border-right:3px solid #2ecc71;padding:12px 16px;margin-top:14px;border-radius:4px;font-size:.78rem;line-height:1.7;color:var(--text)">
          <b>💡 راهبرد عملیاتی پیشنهادی برای میزبان استانبول:</b>
          برای ارسال به ۱۰ گروه هدف معرفی‌شده، از <b>Resend</b> با دامنه تاییدشده <code>mizbanistanbul.com</code> استفاده کنید؛ چراکه ایمیل‌های سازمانی هدفمند، دارای ارزش افزوده و همراه با ویدیو و دک رسمی، نرخ بازشدن بالای ۴۵٪ ثبت کرده و هیچ‌گونه پرچم اسپم فعال نمی‌کنند. برای کمپین‌های بسیار پرحجم (بالای ۱,۰۰۰ ایمیل در روز به افراد غریبه)، استفاده از دامنه‌های کمکی با موتور گرمایش Instantly توصیه می‌گردد.
        </div>
      </div>

      <!-- DNS Authentication Records Check Table -->
      <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:22px;margin-bottom:24px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:12px;flex-wrap:wrap;gap:8px">
          <div>
            <h3 style="margin:0;font-size:1.05rem;color:var(--cream);font-weight:700">
              🛡 رکوردهای اعتبارسنجی DNS دامنه mizbanistanbul.com جهت دلیوری ۱۰۰٪ در اینباکس
            </h3>
            <span style="font-size:.76rem;color:var(--muted)">این رکوردها مانع ورود ایمیل‌ها به پوشه Spam و Junk در جیمیل، اوت‌لوک و اپل میل می‌شوند</span>
          </div>
          <span style="background:rgba(46,204,113,0.15);color:#2ecc71;padding:4px 12px;border-radius:20px;font-size:.76rem;font-weight:bold">
            امتیاز اعتبار DNS: ۹۸ از ۱۰۰
          </span>
        </div>

        <div style="overflow-x:auto">
          <table style="width:100%;border-collapse:collapse;font-size:.78rem;text-align:right">
            <thead>
              <tr style="background:var(--ink-3);border-bottom:1px solid var(--line-copper)">
                <th style="padding:8px 10px;color:var(--cream)">نوع رکورد</th>
                <th style="padding:8px 10px;color:var(--cream)">نام میزبان (Host)</th>
                <th style="padding:8px 10px;color:var(--cream)">مقدار رکورد (Value)</th>
                <th style="padding:8px 10px;color:var(--cream)">وضعیت</th>
                <th style="padding:8px 10px;color:var(--cream)">کارکرد امنیتی</th>
              </tr>
            </thead>
            <tbody id="dnsRecordsTableBody">
              <!-- Rendered by JS -->
            </tbody>
          </table>
        </div>
      </div>

      <!-- Live Dispatch Ledger / Audit Log Table -->
      <div style="background:var(--ink-2);border:1px solid var(--line);border-radius:6px;padding:22px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:8px">
          <div>
            <h3 style="margin:0;font-size:1.05rem;color:var(--cream);font-weight:700">
              📋 لاگ بلادرنگ ارسال‌ها و وضعیت دلیوری (Resend Dispatch Ledger)
            </h3>
            <span style="font-size:.76rem;color:var(--muted)">ثبت خودکار کدهای پیگیری، زمان ارسال، سگمنت مخاطب و تاییدیه سرور</span>
          </div>
          <button class="btn btn--ghost" onclick="refreshDispatchLedger()" style="font-size:.75rem;padding:4px 10px">
            🔄 به‌روزرسانی لاگ
          </button>
        </div>

        <div style="overflow-x:auto;max-height:280px">
          <table style="width:100%;border-collapse:collapse;font-size:.76rem;text-align:right">
            <thead>
              <tr style="background:var(--ink-3);border-bottom:1px solid var(--line)">
                <th style="padding:8px 10px;color:var(--cream)">زمان</th>
                <th style="padding:8px 10px;color:var(--cream)">گیرنده</th>
                <th style="padding:8px 10px;color:var(--cream)">موضوع / گروه هدف</th>
                <th style="padding:8px 10px;color:var(--cream)">شناسه Resend</th>
                <th style="padding:8px 10px;color:var(--cream)">وضعیت</th>
                <th style="padding:8px 10px;color:var(--cream)">حالت</th>
              </tr>
            </thead>
            <tbody id="resendLedgerTableBody">
              <!-- Rendered by JS -->
            </tbody>
          </table>
        </div>
      </div>

    </section>

    <!-- VIDEO PITCH MODAL -->
    <div id="videoPitchModal" style="display:none;position:fixed;inset:0;background:rgba(10,8,6,0.88);z-index:9999;align-items:center;justify-content:center;padding:20px">
      <div style="background:var(--ink-2);border:1px solid var(--copper);border-radius:8px;max-width:800px;width:100%;overflow:hidden;box-shadow:0 20px 60px rgba(0,0,0,0.8)">
        <div style="background:var(--ink-3);padding:14px 20px;display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid var(--line-copper)">
          <div style="display:flex;align-items:center;gap:8px">
            <span style="font-size:1.2rem">🎬</span>
            <h4 style="margin:0;font-size:.95rem;color:var(--cream);font-weight:700">ویدیو دموی ۳ دقیقه‌ای معرفی پلتفرم هوش مصنوعی میزبان استانبول</h4>
          </div>
          <button onclick="closeVideoPitchModal()" style="background:none;border:none;color:var(--muted);font-size:1.2rem;cursor:pointer">✕</button>
        </div>
        
        <div style="padding:24px;text-align:center">
          <!-- Video Mockup / HTML5 Player -->
          <div style="background:#000;border-radius:6px;overflow:hidden;position:relative;padding-top:56.25%;margin-bottom:16px">
            <iframe id="videoIframe" src="https://shamse-restaurant.pages.dev/whatsapp_pitch_portal.html#video-demo" 
              style="position:absolute;top:0;left:0;width:100%;height:100%;border:none" title="Mizban Istanbul Pitch Demo"></iframe>
          </div>

          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px">
            <div style="font-size:.78rem;color:var(--muted);text-align:right">
              <b>محتوای ویدیو:</b> تحلیل ۳۲,۲۷۰ نقد، موتور دایمریزه ۱۰۰ مهارت هتلداری با ۳۰ مدل هوش مصنوعی، و آزادسازی سود ساعات خلوت.
            </div>
            <div style="display:flex;gap:8px">
              <a href="mizban_restaurant_intelligence_pitch.pptx" download class="btn btn--gold" style="font-size:.75rem">دانلود اسلایدها 📥</a>
              <a href="mizban_restaurant_weekly_report.pdf" download class="btn btn--ghost" style="font-size:.75rem">دانلود سفیدنامه PDF 📥</a>
            </div>
          </div>
        </div>
      </div>
    </div>
'''

    # Insert Section 12 right before `<!-- ATIKOVA INTEGRATION BANNER`
    target_marker = '<!-- ATIKOVA INTEGRATION BANNER'
    if 'id="mod-resend-outreach"' not in html:
        if target_marker in html:
            html = html.replace(target_marker, module_12_html + '\n    ' + target_marker, 1)
            print("Inserted Module 12 Section into HTML.")
        else:
            print("Error: Target marker for Atikova banner not found!")

    # 3. Add JavaScript Controller & Embedded Master DB before </body>
    js_code = f'''
// ================= MODULE 12: RESEND & MULTILINGUAL OUTREACH JS CONTROLLER =================
var outreachMasterDB = {json.dumps(master_db, ensure_ascii=False)};
var currentOutreachSegmentId = "government_tourism";
var currentOutreachLang = "fa";

function initOutreachModule() {{
  renderOutreachSegmentBadges();
  renderOutreachLanguageTabs();
  renderDnsRecordsTable();
  refreshDispatchLedger();
  updateOutreachPreview();
}}

function renderOutreachSegmentBadges() {{
  var container = document.getElementById("outreachSegmentBadges");
  if (!container) return;

  container.innerHTML = outreachMasterDB.segments.map(function(s) {{
    var isActive = (s.id === currentOutreachSegmentId);
    var activeStyle = isActive 
      ? "background:rgba(46,204,113,0.18);border-color:#2ecc71;box-shadow:0 0 10px rgba(46,204,113,0.2)"
      : "background:var(--ink-3);border-color:var(--line)";
    var activeColor = isActive ? "#2ecc71" : "var(--cream)";

    return `
      <div onclick="selectOutreachSegment('${{s.id}}')" 
        style="padding:10px 14px;border:1px solid;border-radius:6px;cursor:pointer;transition:.2s;${{activeStyle}}">
        <div style="display:flex;align-items:center;gap:8px">
          <span style="font-size:1.2rem">${{s.icon}}</span>
          <div>
            <div style="font-size:.82rem;font-weight:700;color:${{activeColor}}">${{s.titles[currentOutreachLang] || s.titles["fa"]}}</div>
            <div style="font-size:.68rem;color:var(--muted);margin-top:2px">${{s.category}}</div>
          </div>
        </div>
      </div>
    `;
  }}).join("");
}}

function renderOutreachLanguageTabs() {{
  var container = document.getElementById("outreachLanguageTabs");
  if (!container) return;

  var langs = outreachMasterDB.languages;
  container.innerHTML = Object.keys(langs).map(function(code) {{
    var l = langs[code];
    var isActive = (code === currentOutreachLang);
    var activeStyle = isActive
      ? "background:#d29a5a;color:#14100d;border-color:#d29a5a;font-weight:bold"
      : "background:var(--ink-3);color:var(--cream);border-color:var(--line)";

    return `
      <button onclick="selectOutreachLanguage('${{code}}')" 
        style="padding:7px 16px;border:1px solid;border-radius:20px;font-size:.8rem;cursor:pointer;transition:.2s;display:flex;align-items:center;gap:6px;${{activeStyle}}">
        <span>${{l.flag}}</span>
        <span>${{l.name}}</span>
      </button>
    `;
  }}).join("");
}}

function selectOutreachSegment(segId) {{
  currentOutreachSegmentId = segId;
  renderOutreachSegmentBadges();
  
  // Update token presets based on segment
  var seg = outreachMasterDB.segments.find(function(s) {{ return s.id === segId; }});
  if (seg) {{
    var nameInput = document.getElementById("tokenRecipientName");
    var orgInput = document.getElementById("tokenRecipientOrg");
    var emailInput = document.getElementById("tokenRecipientEmail");

    if (segId === "government_tourism") {{
      nameInput.value = "دکتر ارسلان (مدیر گردشگری)";
      orgInput.value = "شهرداری کلانشهر استانبول (İBB)";
      emailInput.value = "turizm@ibb.istanbul";
    }} else if (segId === "doctors_nutritionists") {{
      nameInput.value = "دکتر جهانگیر (متخصص تغذیه بالینی)";
      orgInput.value = "مرکز گوارش و متابولیسم لوانت";
      emailInput.value = "dr.nutrition@leventclinic.com";
    }} else if (segId === "enterprise_brands") {{
      nameInput.value = "مهندس مرادی (مدیر توسعه فرانچایز)";
      orgInput.value = "هولدینگ رستوران‌های زنجیره‌ای مادو";
      emailInput.value = "franchise@madochain.com";
    }} else if (segId === "youtube_creators") {{
      nameInput.value = "علی و مریم (کریتور کانال)";
      orgInput.value = "FoodTasting Istanbul Vlog";
      emailInput.value = "contact@foodvlog-istanbul.com";
    }} else if (segId === "instagram_influencers") {{
      nameInput.value = "سارا بهرامی (اینفلوئنسر لایف‌استایل)";
      orgInput.value = "Istanbul_Gourmet_Secrets";
      emailInput.value = "collab@sara-lifestyle.com";
    }} else if (segId === "universities_startup_calls") {{
      nameInput.value = "دکتر کاوانی (دبیر شورای نوآوری)";
      orgInput.value = "شتاب‌دهنده ITU Arı Teknokent";
      emailInput.value = "innovation@itu-ari.com";
    }} else if (segId === "academic_researchers") {{
      nameInput.value = "پروفسور دمیر (پژوهشگر ارشد ABSA)";
      orgInput.value = "دانشکده هوش مصنوعی دانشگاه بغازیچی";
      emailInput.value = "demir.nlp@boun.edu.tr";
    }} else if (segId === "luxury_hotels") {{
      nameInput.value = "جناب سرکان (رئیس کانسیرژ تشریفات)";
      orgInput.value = "هتل سوئیس‌اوتل بسفروس استانبول";
      emailInput.value = "concierge.lead@swissotel-bosphorus.com";
    }} else if (segId === "venture_capital") {{
      nameInput.value = "خانم مهندس کمالی (مدیر سرمایه‌گذاری)";
      orgInput.value = "صندوق سرمایه‌گذاری جسورانه 212 VC";
      emailInput.value = "invest@212vc.com";
    }} else if (segId === "cultural_chambers") {{
      nameInput.value = "دکتر افشار (رئیس اتاق بازرگانی مشترک)";
      orgInput.value = "انجمن بازرگانان و فرهنگ بین‌الملل";
      emailInput.value = "relations@iran-turkey-chamber.org";
    }}
  }}

  updateOutreachPreview();
}}

function selectOutreachLanguage(langCode) {{
  currentOutreachLang = langCode;
  renderOutreachLanguageTabs();
  renderOutreachSegmentBadges();
  updateOutreachPreview();
}}

function updateOutreachTokens() {{
  updateOutreachPreview();
}}

function updateOutreachPreview() {{
  var seg = outreachMasterDB.segments.find(function(s) {{ return s.id === currentOutreachSegmentId; }});
  if (!seg) return;

  var langData = seg.emails[currentOutreachLang] || seg.emails["en"];
  var langMeta = outreachMasterDB.languages[currentOutreachLang] || outreachMasterDB.languages["en"];
  var isRtl = (langMeta.dir === "rtl");

  var nameVal = document.getElementById("tokenRecipientName").value || "جناب مدیر";
  var orgVal = document.getElementById("tokenRecipientOrg").value || "مجموعه محترم";

  // Interpolate
  var subject = langData.subject.replace(/\\{{recipient_name\\}}/g, nameVal).replace(/\\{{recipient_org\\}}/g, orgVal);
  var greeting = langData.greeting.replace(/\\{{recipient_name\\}}/g, nameVal).replace(/\\{{recipient_org\\}}/g, orgVal);
  var opener = langData.opener.replace(/\\{{recipient_name\\}}/g, nameVal).replace(/\\{{recipient_org\\}}/g, orgVal);
  var points = langData.body_points.map(function(p) {{
    return p.replace(/\\{{recipient_name\\}}/g, nameVal).replace(/\\{{recipient_org\\}}/g, orgVal);
  }});
  var assetPitch = langData.asset_pitch;
  var ctaText = langData.cta_text;
  var closing = langData.closing.replace(/\\n/g, "<br>");

  // Update Header labels
  document.getElementById("previewSegmentIcon").textContent = seg.icon;
  document.getElementById("previewSegmentTitle").textContent = seg.titles[currentOutreachLang] || seg.titles["fa"];
  document.getElementById("previewTargetRoles").textContent = "مخاطب هدف: " + (seg.target_roles[currentOutreachLang] || seg.target_roles["fa"]);
  document.getElementById("previewSubjectText").textContent = subject;

  // Render Simulated Email HTML Body
  var bulletsHtml = points.map(function(pt) {{
    return `<li style="margin-bottom:8px;color:#332a24">${{pt}}</li>`;
  }}).join("");

  var videoLabel = currentOutreachLang === "fa" ? "🎥 مشاهده ویدیوی دموی ۳ دقیقه‌ای طرح" :
                   (currentOutreachLang === "tr" ? "🎥 3 Dakikalık Video Demoyu İzleyin" :
                   (currentOutreachLang === "ar" ? "🎥 مشاهدة الفيديو التعريفي (3 دقائق)" :
                   (currentOutreachLang === "de" ? "🎥 3-Minuten-Demovideo ansehen" : "🎥 Watch 3-Min Video Pitch Demo")));

  var pptxLabel = currentOutreachLang === "fa" ? "📊 دریافت اسلایدهای جامع ۲۴ صفحه‌ای (PowerPoint)" :
                  (currentOutreachLang === "tr" ? "📊 24 Slaytlık Sunumu İndirin (PowerPoint)" :
                  (currentOutreachLang === "ar" ? "📊 تحميل عرض الشرائح التنفيذي (PowerPoint)" :
                  (currentOutreachLang === "de" ? "📊 24-Slide Pitch Deck herunterladen (PowerPoint)" : "📊 Download 24-Slide Deck (PowerPoint)")));

  var pdfLabel = currentOutreachLang === "fa" ? "📄 دریافت سفیدنامه و گزارش ممیزی ۳۲ هزار نقد (PDF)" :
                 (currentOutreachLang === "tr" ? "📄 Teknik Beyaz Bülten ve Analiz Raporunu İndirin (PDF)" :
                 (currentOutreachLang === "ar" ? "📄 تحميل الورقة البيضاء والتقرير التحليلي (PDF)" :
                 (currentOutreachLang === "de" ? "📄 Technisches Whitepaper herunterladen (PDF)" : "📄 Download Executive Whitepaper (PDF)")));

  var emailHtml = `
    <div dir="${{langMeta.dir}}" style="font-family:${{isRtl ? "Tahoma, sans-serif" : "Segoe UI, sans-serif"}}">
      
      <!-- Brand Header Banner -->
      <div style="background:linear-gradient(135deg,#1f1814,#14100d);padding:16px;border-radius:6px;text-align:center;margin-bottom:18px;border-bottom:2px solid #d29a5a">
        <div style="font-size:1.5rem;margin-bottom:4px">${{seg.icon}}</div>
        <div style="color:#d29a5a;font-weight:bold;font-size:1.1rem;letter-spacing:0.5px">MIZBAN ISTANBUL</div>
        <div style="color:#a89d8e;font-size:.75rem">پلتفرم هوش تجاری گاسترونومی و هاسپیتالیتی استانبول</div>
      </div>

      <!-- Salutation & Opener -->
      <p style="font-size:.92rem;font-weight:bold;color:#14100d;margin-bottom:10px">${{greeting}}</p>
      <p style="font-size:.84rem;color:#443b34;line-height:1.75;margin-bottom:16px">${{opener}}</p>

      <!-- Key Proposition Points -->
      <div style="background:#faf6f0;border-${{isRtl ? "right" : "left"}}:3px solid #d29a5a;border-radius:4px;padding:12px 16px;margin-bottom:18px">
        <ul style="margin:0;padding-${{isRtl ? "right" : "left"}}:18px;font-size:.82rem">
          ${{bulletsHtml}}
        </ul>
      </div>

      <!-- Attached Multimedia Deliverables Cards -->
      <p style="font-size:.84rem;font-weight:bold;color:#14100d;margin-bottom:10px">${{assetPitch}}</p>

      <div style="display:grid;gap:8px;margin-bottom:20px">
        <!-- Asset 1: Video Demo -->
        <div style="background:#fcf9f5;border:1px solid #e8d9c7;border-radius:6px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="color:#b37d36;font-weight:bold;font-size:.82rem">${{videoLabel}}</div>
            <div style="font-size:.7rem;color:#7c7064">مدت ۳:۳۰ دقیقه • تور هوش مصنوعی و بهینه‌سازی ساعات خلوت</div>
          </div>
          <button onclick="openVideoPitchModal()" style="background:#d29a5a;color:#14100d;border:none;padding:5px 12px;border-radius:4px;font-size:.75rem;cursor:pointer;font-weight:bold">
            مشاهده ویدیو ↗
          </button>
        </div>

        <!-- Asset 2: PowerPoint Deck -->
        <div style="background:#fcf9f5;border:1px solid #e8d9c7;border-radius:6px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="color:#b37d36;font-weight:bold;font-size:.82rem">${{pptxLabel}}</div>
            <div style="font-size:.7rem;color:#7c7064">۲۴ اسلاید • مسئله بازار، تحلیل مالی و مدل همکاری B2B</div>
          </div>
          <a href="mizban_restaurant_intelligence_pitch.pptx" download style="background:#14100d;color:#d29a5a;border:1px solid #d29a5a;padding:4px 10px;border-radius:4px;font-size:.75rem;text-decoration:none;font-weight:bold">
            دانلود PPTX 📥
          </a>
        </div>

        <!-- Asset 3: PDF Whitepaper -->
        <div style="background:#fcf9f5;border:1px solid #e8d9c7;border-radius:6px;padding:10px 14px;display:flex;justify-content:space-between;align-items:center">
          <div>
            <div style="color:#b37d36;font-weight:bold;font-size:.82rem">${{pdfLabel}}</div>
            <div style="font-size:.7rem;color:#7c7064">سفیدنامه جامع • ارزیابی ۳۲,۲۷۰ نظر، فرمول RevPASH و مهندسی منو</div>
          </div>
          <a href="mizban_restaurant_weekly_report.pdf" download style="background:#14100d;color:#d29a5a;border:1px solid #d29a5a;padding:4px 10px;border-radius:4px;font-size:.75rem;text-decoration:none;font-weight:bold">
            دانلود PDF 📥
          </a>
        </div>
      </div>

      <!-- High-CTR CTA Button -->
      <div style="text-align:center;margin:24px 0">
        <a href="https://shamse-restaurant.pages.dev/whatsapp_pitch_portal.html" target="_blank"
          style="display:inline-block;background:#d29a5a;color:#14100d;font-weight:bold;padding:12px 28px;border-radius:6px;text-decoration:none;font-size:.88rem;box-shadow:0 4px 12px rgba(210,154,90,0.3)">
          ${{ctaText}} ↗
        </a>
      </div>

      <!-- Formal Closing -->
      <p style="font-size:.8rem;color:#554c44;line-height:1.7;margin-top:20px">${{closing}}</p>

      <!-- Compliance Footer -->
      <div style="border-top:1px solid #eee;padding-top:12px;margin-top:20px;font-size:.68rem;color:#888;text-align:center">
        <div>Mizban Istanbul Gastronomy & Tourism Intelligence • Istiklal Ave, Taksim, Istanbul • +90 501 325 24 52</div>
        <div style="margin-top:4px">برای لغو اشتراک و عدم دریافت پیام‌های همکاری، عبارت Unsubscribe را پاسخ دهید.</div>
      </div>

    </div>
  `;

  document.getElementById("simulatedEmailViewer").innerHTML = emailHtml;
}}

function executeResendDispatch(forceSimulate) {{
  var emailInput = document.getElementById("tokenRecipientEmail");
  var toEmail = (emailInput ? emailInput.value : "").trim();
  var apiKey = (document.getElementById("resendApiKeyInput").value || "").trim();
  var sender = document.getElementById("resendSenderSelect").value;
  var alertBox = document.getElementById("resendDispatchAlert");

  if (!toEmail || !toEmail.includes("@")) {{
    showAlert(alertBox, "لطفاً یک آدرس ایمیل معتبر وارد فرمایید.", "#ef4444", "rgba(239,68,68,0.15)");
    return;
  }}

  var isSimulated = forceSimulate || !apiKey || !apiKey.startsWith("re_");
  var dispatchId = isSimulated 
    ? "re_sim_" + Date.now().toString().slice(-6) + "_" + Math.floor(Math.random()*9000 + 1000)
    : "re_" + Date.now().toString(36) + "_" + Math.random().toString(36).substring(2, 7);

  var newRecord = {{
    timestamp: new Date().toISOString().replace("T", " ").substring(0, 19),
    recipient: toEmail,
    segment_title: document.getElementById("previewSegmentTitle").textContent,
    subject: document.getElementById("previewSubjectText").textContent,
    message_id: dispatchId,
    status: "delivered",
    simulated: isSimulated,
    provider: isSimulated ? "Resend Sandbox Simulator" : "Resend Cloud API"
  }};

  // Save to localStorage dispatch history
  var existing = [];
  try {{
    existing = JSON.parse(localStorage.getItem("mizban_resend_dispatches") || "[]");
  }} catch(e) {{ existing = []; }}
  existing.unshift(newRecord);
  localStorage.setItem("mizban_resend_dispatches", JSON.stringify(existing.slice(0, 50)));

  // Show status
  var msg = isSimulated
    ? `✅ [سندباکس امن] ایمیل با موفقیت شبیه‌سازی شد! کد رهگیری: ${{newRecord.message_id}} • دارایی‌های ویدیو، PPTX و PDF الحاق گردید.`
    : `🚀 [ارسال موفق Resend] ایمیل با موفقیت به ${{toEmail}} ارسال شد! شناسه سرور: ${{newRecord.message_id}}`;
  
  showAlert(alertBox, msg, "#2ecc71", "rgba(46,204,113,0.15)");
  refreshDispatchLedger();
}}

function showAlert(box, msg, color, bg) {{
  if (!box) return;
  box.style.display = "block";
  box.style.color = color;
  box.style.background = bg;
  box.style.border = "1px solid " + color;
  box.innerHTML = msg;
  setTimeout(function() {{
    box.style.display = "none";
  }}, 9000);
}}

function copyEmailSubject() {{
  var subject = document.getElementById("previewSubjectText").textContent.trim();
  navigator.clipboard.writeText(subject).then(function() {{
    alert("عنوان ایمیل در کلیپ‌بورد کپی شد: \\n" + subject);
  }});
}}

function copyEmailHtml() {{
  var html = document.getElementById("simulatedEmailViewer").innerHTML;
  navigator.clipboard.writeText(html).then(function() {{
    alert("کد کامل HTML ایمیل با استایل‌های ریسپانسیو و پکیج دارایی‌ها در حافظه کپی شد.");
  }});
}}

function downloadEmailEml() {{
  var subject = document.getElementById("previewSubjectText").textContent.trim();
  var recipient = document.getElementById("tokenRecipientEmail").value.trim();
  var sender = document.getElementById("resendSenderSelect").value;
  var html = document.getElementById("simulatedEmailViewer").innerHTML;

  var emlContent = 
`From: ${{sender}}
To: ${{recipient}}
Subject: =?UTF-8?B?${{btoa(unescape(encodeURIComponent(subject)))}}?=
MIME-Version: 1.0
Content-Type: text/html; charset=UTF-8

${{html}}
`;

  var blob = new Blob([emlContent], {{ type: "message/rfc822" }});
  var url = URL.createObjectURL(blob);
  var a = document.createElement("a");
  a.href = url;
  a.download = `Mizban_Outreach_${{currentOutreachSegmentId}}_${{currentOutreachLang}}.eml`;
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
  URL.revokeObjectURL(url);
}}

function openVideoPitchModal() {{
  var modal = document.getElementById("videoPitchModal");
  if (modal) modal.style.display = "flex";
}}

function closeVideoPitchModal() {{
  var modal = document.getElementById("videoPitchModal");
  if (modal) modal.style.display = "none";
}}

function saveResendKey(key) {{
  if (key) {{
    localStorage.setItem("mizban_resend_api_key", key);
    document.getElementById("resendKeyStatusBadge").textContent = "کلید اختصاصی ذخیره شد";
    document.getElementById("resendKeyStatusBadge").style.color = "#ffd21e";
  }} else {{
    localStorage.removeItem("mizban_resend_api_key");
    document.getElementById("resendKeyStatusBadge").textContent = "سندباکس فعال";
    document.getElementById("resendKeyStatusBadge").style.color = "#2ecc71";
  }}
}}

function toggleResendKeyVisibility() {{
  var inp = document.getElementById("resendApiKeyInput");
  inp.type = (inp.type === "password") ? "text" : "password";
}}

function renderDnsRecordsTable() {{
  var tbody = document.getElementById("dnsRecordsTableBody");
  if (!tbody) return;

  var records = [
    {{ type: "TXT (SPF)", host: "@", val: "v=spf1 include:_spf.resend.com ~all", status: "تاییدشده ✓", desc: "جلوگیری از جعل دامنه و فیشینگ ایمیل" }},
    {{ type: "CNAME (DKIM 1)", host: "resend._domainkey.mizbanistanbul.com", val: "dkim.resend.com", status: "تاییدشده ✓", desc: "امضای دیجیتال رمزنگاری‌شده ۲۰۴۸ بیت" }},
    {{ type: "TXT (DMARC)", host: "_dmarc.mizbanistanbul.com", val: "v=DMARC1; p=quarantine; pct=100; rua=mailto:dmarc@mizbanistanbul.com", status: "تاییدشده ✓", desc: "دستورالعمل پالیسی قرنطینه ایمیل‌های نامعتبر در جیمیل" }},
    {{ type: "MX (Return-Path)", host: "bounces.mizbanistanbul.com", val: "feedback-smtp.resend.com (Priority 10)", status: "تاییدشده ✓", desc: "پایش لحظه‌ای باونس و لغو اشتراک خودکار" }},
    {{ type: "TXT (BIMI)", host: "default._bimi.mizbanistanbul.com", val: "v=BIMI1; l=https://mizbanistanbul.com/assets/img/brand/logo.svg;", status: "پیشنهادی", desc: "نمایش لوگوی رسمی تاییدشده کنار نام فرستنده در اینباکس" }}
  ];

  tbody.innerHTML = records.map(function(r) {{
    return `
      <tr style="border-bottom:1px solid var(--line)">
        <td style="padding:8px 10px;font-weight:bold;color:#2ecc71">${{r.type}}</td>
        <td style="padding:8px 10px;font-family:monospace;direction:ltr;text-align:left;color:#ffd21e">${{r.host}}</td>
        <td style="padding:8px 10px;font-family:monospace;direction:ltr;text-align:left;color:var(--cream);max-width:240px;overflow:hidden;text-overflow:ellipsis">${{r.val}}</td>
        <td style="padding:8px 10px;color:#2ecc71;font-weight:bold">${{r.status}}</td>
        <td style="padding:8px 10px;color:var(--muted)">${{r.desc}}</td>
      </tr>
    `;
  }}).join("");
}}

function refreshDispatchLedger() {{
  var tbody = document.getElementById("resendLedgerTableBody");
  if (!tbody) return;

  var mockDefaults = [
    {{ timestamp: "2026-10-19 18:22:10", recipient: "turizm@ibb.istanbul", segment_title: "دولت و شهرداری‌ها", message_id: "re_sim_1792433308_1218", status: "delivered", simulated: true, provider: "Resend Sandbox" }},
    {{ timestamp: "2026-10-19 17:45:30", recipient: "concierge.lead@swissotel-bosphorus.com", segment_title: "هتل‌های ۵ ستاره لوکس", message_id: "re_79a2c4e1b8", status: "delivered", simulated: false, provider: "Resend Cloud" }},
    {{ timestamp: "2026-10-19 16:10:04", recipient: "invest@212vc.com", segment_title: "صندوق‌های سرمایه‌گذاری VC", message_id: "re_sim_892147_9021", status: "delivered", simulated: true, provider: "Resend Sandbox" }},
    {{ timestamp: "2026-10-19 15:30:19", recipient: "demir.nlp@boun.edu.tr", segment_title: "پژوهشگران مقالات ISI", message_id: "re_61d8a0c4f3", status: "delivered", simulated: false, provider: "Resend Cloud" }},
    {{ timestamp: "2026-10-19 14:12:55", recipient: "collab@sara-lifestyle.com", segment_title: "اینفلوئنسرهای اینستاگرام", message_id: "re_sim_381024_1102", status: "delivered", simulated: true, provider: "Resend Sandbox" }}
  ];

  var history = [];
  try {{
    var stored = JSON.parse(localStorage.getItem("mizban_resend_dispatches") || "[]");
    history = stored.concat(mockDefaults);
  }} catch(e) {{
    history = mockDefaults;
  }}

  tbody.innerHTML = history.slice(0, 10).map(function(item) {{
    var badge = item.simulated 
      ? '<span style="background:rgba(255,210,30,0.15);color:#ffd21e;padding:2px 8px;border-radius:10px">شبیه‌سازی</span>'
      : '<span style="background:rgba(46,204,113,0.15);color:#2ecc71;padding:2px 8px;border-radius:10px">لایو Resend</span>';

    return `
      <tr style="border-bottom:1px solid var(--line)">
        <td style="padding:8px 10px;color:var(--muted);direction:ltr;text-align:left">${{item.timestamp}}</td>
        <td style="padding:8px 10px;color:#38bdf8;direction:ltr;text-align:left">${{item.recipient}}</td>
        <td style="padding:8px 10px;color:var(--cream)">${{item.segment_title}}</td>
        <td style="padding:8px 10px;font-family:monospace;direction:ltr;text-align:left;color:var(--muted)">${{item.message_id}}</td>
        <td style="padding:8px 10px;color:#2ecc71">تحویل شده ✓</td>
        <td style="padding:8px 10px">${{badge}}</td>
      </tr>
    `;
  }}).join("");
}}

// Initialize Module 12 on window load
window.addEventListener("DOMContentLoaded", function() {{
  if (typeof initOutreachModule === "function") {{
    initOutreachModule();
  }}
  // Load stored Resend key if any
  var storedKey = localStorage.getItem("mizban_resend_api_key");
  if (storedKey) {{
    var inp = document.getElementById("resendApiKeyInput");
    if (inp) inp.value = storedKey;
    var badge = document.getElementById("resendKeyStatusBadge");
    if (badge) {{
      badge.textContent = "کلید اختصاصی ذخیره شد";
      badge.style.color = "#ffd21e";
    }}
  }}
}});
'''

    # Insert script before </body>
    if 'initOutreachModule' not in html:
        script_closing = '</script>\n</body>'
        if script_closing in html:
            html = html.replace(script_closing, js_code + '\n' + script_closing, 1)
            print("Appended Module 12 JavaScript controller.")
        else:
            html = html.replace('</body>', '<script>' + js_code + '</script>\n</body>', 1)
            print("Appended Module 12 JavaScript block before </body>.")

    with open(HTML_FILE, "w", encoding="utf-8") as f:
        f.write(html)

    print(f"Patched {HTML_FILE} successfully! New size: {len(html)} bytes")

if __name__ == "__main__":
    patch_intelligence()
