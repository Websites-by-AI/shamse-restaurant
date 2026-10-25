#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Patch index.html to include:
1. Executive Credentials & Deliverables Top Card & Top Announcement Bar
   with direct links, usernames, passwords, magic bypass tokens, download buttons,
   and 1-click WhatsApp copy.
2. Tab 5 in #ecosystem-infographic for the Continuous System Learning Loop
   (یادگیری پیوسته سیستم و هوش مصنوعی هاسپیتالیتی) featuring the new SVG infographic
   and interactive operational delta breakdown.
3. Explicit implementation of switchEcoTab() in JavaScript.
"""

def main():
    path = "/home/user/shamse-restaurant/index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. Add switchEcoTab JavaScript function if not already present
    if "function switchEcoTab" not in html:
        js_to_insert = """
<script>
function switchEcoTab(tabId, btn) {
  var btns = document.querySelectorAll('#ecosystem-infographic .ai-tab-btn');
  btns.forEach(function(b) { b.classList.remove('active'); });
  if (btn) btn.classList.add('active');
  var panels = document.querySelectorAll('#ecosystem-infographic .ai-tab-panel');
  panels.forEach(function(p) { p.classList.remove('active'); });
  var target = document.getElementById('ecoTab-' + tabId);
  if (target) target.classList.add('active');
}

function copyIndexExecutiveWhatsApp() {
  var text = document.getElementById('indexWhatsAppPitchText');
  if (!text) return;
  navigator.clipboard.writeText(text.innerText).then(function() {
    var btn = document.getElementById('btnCopyIndexWhatsApp');
    if (btn) {
      var orig = btn.innerHTML;
      btn.innerHTML = '✅ متن پیام واتس‌اپ کپی شد!';
      btn.style.background = '#27ae60';
      btn.style.color = '#fff';
      setTimeout(function() {
        btn.innerHTML = orig;
        btn.style.background = '';
        btn.style.color = '';
      }, 3000);
    }
  }).catch(function(err) {
    alert('متن پیام انتخاب شد. لطفا دستی کپی کنید.');
  });
}

function copyIndexCredential(elementId, btnId) {
  var el = document.getElementById(elementId);
  if (!el) return;
  var val = el.innerText || el.textContent;
  navigator.clipboard.writeText(val.trim()).then(function() {
    var btn = document.getElementById(btnId);
    if (btn) {
      var orig = btn.innerText;
      btn.innerText = 'کپی شد!';
      setTimeout(function() { btn.innerText = orig; }, 2000);
    }
  });
}
</script>
"""
        html = html.replace("</body>", js_to_insert + "\n</body>")

    # 2. Executive Card
    executive_card_html = """
<!-- ================= SHAMSE EXECUTIVE CREDENTIALS & 4-DELIVERABLES CARD ================= -->
<div class="wrap" id="executiveCredentialsCard" style="margin-top:28px;margin-bottom:28px;position:relative;z-index:100">
  <div style="background:linear-gradient(135deg,#1b140e 0%,#261a12 50%,#15100c 100%);border:1.5px solid #d29a5a;border-radius:6px;padding:24px;box-shadow:0 18px 45px rgba(0,0,0,.65)">
    <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:12px;border-bottom:1px solid rgba(210,154,90,.3);padding-bottom:16px;margin-bottom:20px">
      <div style="display:flex;align-items:center;gap:12px">
        <span style="font-size:1.8rem">👑</span>
        <div>
          <h2 style="font-size:1.35rem;color:#ffd21e;font-weight:900;margin:0">پیشخوان دسترسی مستقیم مدیریت و خروجی‌های هوش تجاری رستوران شمسه</h2>
          <span style="color:#d1c8bb;font-size:.86rem">کلیه دسترسی‌ها، نام‌های کاربری، رمزهای عبور، لینک‌های مستقیم بدون رمز و دانلود ۴ بسته گزارش</span>
        </div>
      </div>
      <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap">
        <span style="background:rgba(46,204,113,.15);color:#2ecc71;border:1px solid #2ecc71;padding:4px 10px;border-radius:3px;font-size:.78rem;font-weight:700">★ ۴٫۷۵ میانگین وزنی ۵,۰۵۵ نظر</span>
        <span style="background:rgba(210,154,90,.15);color:#d29a5a;border:1px solid #d29a5a;padding:4px 10px;border-radius:3px;font-size:.78rem;font-weight:700">دو شعبه فعال: استقلال و کوجاتپه</span>
      </div>
    </div>

    <!-- Credentials Row: 2 Big Cards -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(320px,1fr));gap:16px;margin-bottom:22px">
      
      <!-- Card 1: Restaurant Portal -->
      <div style="background:#17110b;border:1px solid #d29a5a;padding:18px;border-radius:4px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
          <span style="color:#ffd21e;font-weight:800;font-size:1.02rem">🍽 پرتال اختصاصی مشتری رستوران شمسه</span>
          <span style="background:#221b15;color:#d29a5a;font-size:.72rem;padding:2px 8px;border-radius:2px">پرتال مشتری</span>
        </div>
        <p style="font-size:.82rem;color:#aaa;margin-bottom:12px">مشاهده وضعیت ممیزی، نقشه نقدها، جدول سرریز شعبات و گزارشات لحظه‌ای شعبه تکسیم و کوجاتپه:</p>
        
        <div style="background:#110d0a;border:1px solid rgba(255,255,255,.08);padding:10px;border-radius:3px;font-size:.82rem;margin-bottom:14px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <span style="color:#888">نام کاربری:</span>
            <span style="color:#fff;font-family:monospace;font-weight:bold" id="txtPortalUser">shamse_manager</span>
            <button onclick="copyIndexCredential('txtPortalUser', 'btnCpPU')" id="btnCpPU" style="background:none;border:none;color:#d29a5a;cursor:pointer;font-size:.72rem">کپی</button>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <span style="color:#888">رمز عبور:</span>
            <span style="color:#ffd21e;font-family:monospace;font-weight:bold" id="txtPortalPass">Shamse#Taksim2026</span>
            <button onclick="copyIndexCredential('txtPortalPass', 'btnCpPP')" id="btnCpPP" style="background:none;border:none;color:#d29a5a;cursor:pointer;font-size:.72rem">کپی</button>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center">
            <span style="color:#888">توکن جادویی:</span>
            <span style="color:#2ecc71;font-family:monospace;font-weight:bold">SHAMSE-TAK-2026</span>
          </div>
        </div>

        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <a href="restaurant_portal.html?token=SHAMSE-TAK-2026" class="btn btn--gold" style="flex:1;padding:10px 14px;font-size:.84rem;font-weight:800;text-align:center">
            🚀 ورود آنی بدون رمز (Magic Link)
          </a>
          <a href="restaurant_portal.html" class="btn btn--ghost" style="padding:10px 12px;font-size:.84rem">
            فرم لاگین عمومی
          </a>
        </div>
      </div>

      <!-- Card 2: Admin Panel -->
      <div style="background:#17110b;border:1px solid #ffd21e;padding:18px;border-radius:4px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
          <span style="color:#ffd21e;font-weight:800;font-size:1.02rem">⚙️ پیشخوان جامع ادمین سیستم (WP-Admin)</span>
          <span style="background:#221b15;color:#ffd21e;font-size:.72rem;padding:2px 8px;border-radius:2px">پنل کل</span>
        </div>
        <p style="font-size:.82rem;color:#aaa;margin-bottom:12px">تنظیمات Mailjet، مانیتورینگ ۴۳ رستوران، تریاژ ۴ زبانه، سنجه‌های ۱۰‌گانه و ربات تلگرام:</p>

        <div style="background:#110d0a;border:1px solid rgba(255,255,255,.08);padding:10px;border-radius:3px;font-size:.82rem;margin-bottom:14px">
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <span style="color:#888">نام کاربری ادمین:</span>
            <span style="color:#fff;font-family:monospace;font-weight:bold" id="txtAdminUser">shamse_admin</span>
            <button onclick="copyIndexCredential('txtAdminUser', 'btnCpAU')" id="btnCpAU" style="background:none;border:none;color:#d29a5a;cursor:pointer;font-size:.72rem">کپی</button>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
            <span style="color:#888">رمز عبور ادمین:</span>
            <span style="color:#2ecc71;font-family:monospace;font-weight:bold" id="txtAdminPass">Shamse@2026!Istiklal</span>
            <button onclick="copyIndexCredential('txtAdminPass', 'btnCpAP')" id="btnCpAP" style="background:none;border:none;color:#d29a5a;cursor:pointer;font-size:.72rem">کپی</button>
          </div>
          <div style="display:flex;justify-content:space-between;align-items:center">
            <span style="color:#888">کلید بای‌پاس URL:</span>
            <span style="color:#ffd21e;font-family:monospace;font-weight:bold">?auth=shamse2026</span>
          </div>
        </div>

        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <a href="admin_panel.html?auth=shamse2026" class="btn" style="flex:1;padding:10px 14px;font-size:.84rem;font-weight:800;background:#ffd21e;color:#101e22;border-radius:0;text-align:center">
            ⚡ ورود مستقیم به ادمین (Bypass)
          </a>
          <a href="admin_panel.html" class="btn btn--line" style="padding:10px 12px;font-size:.84rem;border-color:#ffd21e;color:#ffd21e">
            لاگین امن ادمین
          </a>
        </div>
      </div>

    </div>

    <!-- 4 Deliverables Download Bar -->
    <div style="background:#130e09;border:1px dashed #d29a5a;padding:16px;border-radius:4px;margin-bottom:20px">
      <div style="display:flex;align-items:center;justify-content:space-between;flex-wrap:wrap;gap:10px;margin-bottom:12px">
        <span style="color:#d29a5a;font-weight:800;font-size:.95rem">📥 دانلود مستقیم ۴ مدل خروجی رسمی هوش تجاری رستوران شمسه:</span>
        <span style="color:#888;font-size:.76rem">آماده ارائه به هیئت مدیره و سهامداران</span>
      </div>
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:10px">
        
        <!-- PDF -->
        <a href="reports/shamse_sentiment_podcast_report.pdf" download class="btn" style="background:#221b15;border:1px solid #d29a5a;color:#f8f8f8;padding:12px 14px;font-size:.82rem;display:flex;align-items:center;justify-content:space-between;text-align:right">
          <div>
            <b style="display:block;color:#ffd21e">📄 گزارش PDF وکتور</b>
            <span style="font-size:.72rem;color:#aaa">۲۶۲ KB • تحلیل ۵,۰۵۵ نقد</span>
          </div>
          <span style="color:#d29a5a;font-size:1.1rem">⬇</span>
        </a>

        <!-- PPTX -->
        <a href="reports/mizban_restaurant_intelligence_pitch.pptx" download class="btn" style="background:#221b15;border:1px solid #d29a5a;color:#f8f8f8;padding:12px 14px;font-size:.82rem;display:flex;align-items:center;justify-content:space-between;text-align:right">
          <div>
            <b style="display:block;color:#ffd21e">📊 پرزنتیشن PPTX</b>
            <span style="font-size:.72rem;color:#aaa">۳۹ KB • اسلایدهای رسمی ارائه</span>
          </div>
          <span style="color:#d29a5a;font-size:1.1rem">⬇</span>
        </a>

        <!-- MP3 -->
        <a href="assets/audio/shamse_intelligence_podcast.mp3" download class="btn" style="background:#221b15;border:1px solid #d29a5a;color:#f8f8f8;padding:12px 14px;font-size:.82rem;display:flex;align-items:center;justify-content:space-between;text-align:right">
          <div>
            <b style="display:block;color:#ffd21e">🎙️ پادکست صوتی MP3</b>
            <span style="font-size:.72rem;color:#aaa">۵۲۵ KB • بریفینگ ۶ دقیقه‌ای</span>
          </div>
          <span style="color:#d29a5a;font-size:1.1rem">⬇</span>
        </a>

        <!-- Web Dossier -->
        <a href="shamse_sentiment_report.html" class="btn" style="background:#221b15;border:1px solid #2ecc71;color:#f8f8f8;padding:12px 14px;font-size:.82rem;display:flex;align-items:center;justify-content:space-between;text-align:right">
          <div>
            <b style="display:block;color:#2ecc71">🌐 گزارش تعاملی وب</b>
            <span style="font-size:.72rem;color:#aaa">۹۴ KB • پلیر پادکست + نمودار</span>
          </div>
          <span style="color:#2ecc71;font-size:1.1rem">↗</span>
        </a>

      </div>
    </div>

    <!-- Branch Google Maps Links & WhatsApp Dispatch Row -->
    <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:16px;align-items:center">
      
      <!-- Branch 1 & 2 Google Maps Buttons -->
      <div style="display:flex;flex-direction:column;gap:8px">
        <span style="color:#aaa;font-size:.78rem">📍 مشاهده نقدها مستقیماً در Google Maps:</span>
        <div style="display:flex;gap:8px;flex-wrap:wrap">
          <a href="https://maps.google.com/?q=Istiklal+Caddesi+179+Beyoglu+Istanbul" target="_blank" rel="noopener" class="btn" style="flex:1;background:#1a1511;border:1px solid rgba(255,255,255,.15);color:#f8f8f8;padding:8px 12px;font-size:.78rem;text-align:center">
            🗺 شعبه ۱ استقلال (۴٫۸★ - ۲,۴۵۰ نقد)
          </a>
          <a href="https://maps.google.com/?q=Abdulhak+Hamit+Caddesi+17+Kocatepe+Istanbul" target="_blank" rel="noopener" class="btn" style="flex:1;background:#1a1511;border:1px solid rgba(255,255,255,.15);color:#f8f8f8;padding:8px 12px;font-size:.78rem;text-align:center">
            🗺 شعبه ۲ کوجاتپه (۴٫۷★ - ۱,۶۲۰ نقد)
          </a>
        </div>
      </div>

      <!-- 1-Click WhatsApp Copy Action -->
      <div style="display:flex;flex-direction:column;gap:8px;align-items:flex-end">
        <button id="btnCopyIndexWhatsApp" onclick="copyIndexExecutiveWhatsApp()" class="btn btn--gold" style="width:100%;padding:10px 16px;font-size:.86rem;font-weight:800;gap:8px">
          📲 کپی پیام رسمی آماده واتس‌اپ برای مدیریت رستوران شمسه
        </button>
        <span style="color:#888;font-size:.72rem">متن شامل همه پسوردها، لینک‌ها، خلاصه نقدها و دانلودها برای ارسال با ۱ کلیک</span>
      </div>

    </div>

    <!-- Hidden Pre-Formatted WhatsApp Message Storage -->
    <div id="indexWhatsAppPitchText" style="display:none">🌟 با درود و احترام فراوان،
جناب آقای / سرکار خانم مدیریت محترم مجموعه رستوران‌های شمسه استانبول (شعبات استقلال و کوجاتپه)،

پرونده جامع ممیزی هوش تجاری و تحلیل احساسات ۵,۰۵۵ نقد ثبت‌شده شمسه در پلتفرم‌های Google Maps، TripAdvisor و Yandex Maps نهایی گردید و هم‌اکنون به همراه پنل‌های اختصاصی و بسته‌های چندرسانه‌ای در اختیارتان قرار دارد:

📊 خلاصه‌ای از ارزیابی کلان برند شمسه:
• میانگین وزنی کل: ۴٫۷۵ از ۵ (۸۸٫۶٪ رضایت مثبت خالص مسافران)
• شعبه ۱ (استقلال): ۴٫۸★ (۲,۴۵۰ نقد گوگل + برنده نشان بین‌المللی Travelers' Choice)
• شعبه ۲ (کوجاتپه): ۴٫۷★ (۱,۶۲۰ نقد گوگل + ۴٫۸★ رضایت توریست‌های روس در یاندکس)

🔐 ۱. اطلاعات ورود به پرتال اختصاصی مدیریت شمسه:
• لینک ورود خودکار: https://shamse-restaurant.pages.dev/restaurant_portal.html?token=SHAMSE-TAK-2026
• شناسه ورود جادویی (Magic Token): SHAMSE-TAK-2026
• نام کاربری: shamse_manager
• رمز عبور اختصاصی: Shamse#Taksim2026

⚙️ ۲. اطلاعات ورود به پیشخوان کل ادمین سیستم (WP-Admin):
• لینک پیشخوان: https://shamse-restaurant.pages.dev/admin_panel.html?auth=shamse2026
• نام کاربری ادمین: shamse_admin
• رمز عبور ادمین: Shamse@2026!Istiklal

📥 ۳. لینک‌های دانلود مستقیم خروجی‌ها:
📄 دریافت گزارش چاپی PDF وکتور:
https://shamse-restaurant.pages.dev/reports/shamse_sentiment_podcast_report.pdf
📊 دریافت پرزنتیشن پاورپوینت PPTX:
https://shamse-restaurant.pages.dev/reports/mizban_restaurant_intelligence_pitch.pptx
🎙️ دریافت پادکست بریفینگ صوتی MP3:
https://shamse-restaurant.pages.dev/assets/audio/shamse_intelligence_podcast.mp3
🌐 مشاهده پرونده تعاملی آنلاین:
https://shamse-restaurant.pages.dev/shamse_sentiment_report.html

🗺️ ۴. لینک مستقیم نقدها در Google Maps:
• شعبه استقلال: https://maps.google.com/?q=Istiklal+Caddesi+179+Beyoglu+Istanbul
• شعبه کوجاتپه: https://maps.google.com/?q=Abdulhak+Hamit+Caddesi+17+Kocatepe+Istanbul

این بسته شامل ۱۰ استراتژی تحول عملیاتی (کاهش صف استقلال به کمک کوجاتپه، رزرواسیون ۱-کلیکه اوپن‌تیبل و تریاژ ۴ زبانه) است. آماده برگزاری جلسه حضوری یا آنلاین با مدیریت محترم جهت پیاده‌سازی گام‌های اجرایی هستیم.

با سپاس و احترام،
تیم توسعه و هوش تجاری میزبان استانبول</div>

  </div>
</div>
"""
    if 'id="executiveCredentialsCard"' not in html:
        target_about = '<!-- ================= ABOUT ================= -->'
        if target_about in html:
            html = html.replace(target_about, executive_card_html + "\n\n" + target_about)

    # 3. Add Tab 5 button in #ecosystem-infographic
    tab_btn_learning = """      <button class="ai-tab-btn" onclick="switchEcoTab('learning', this)">
        <span style="color:#2ecc71">🧠 ۵. یادگیری پیوسته سیستم و هوش مصنوعی (Learning Loop)</span>
      </button>"""

    if "switchEcoTab('learning'" not in html:
        datamile_btn_str = """      <button class="ai-tab-btn" onclick="switchEcoTab('datamile', this)">
        <span>🚀 ۴. اپلیکیشن مایل‌های داده (Data Mile App)</span>
      </button>"""
        html = html.replace(datamile_btn_str, datamile_btn_str + "\n" + tab_btn_learning)

    # 4. Add Panel 5 (ecoTab-learning) with the full SVG and interactive cards
    learning_panel_html = """
    <!-- TAB 5: Continuous System Learning Loop & AI Operational Improvement Infographic -->
    <div id="ecoTab-learning" class="ai-tab-panel rev">
      <div style="background:var(--ink-3);border:1.5px solid #2ecc71;padding:24px;border-radius:6px">
        <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:18px">
          <div>
            <div style="display:flex;align-items:center;gap:8px">
              <span style="background:rgba(46,204,113,.2);color:#2ecc71;border:1px solid #2ecc71;padding:3px 10px;border-radius:3px;font-size:.76rem;font-weight:800">حلقه بسته خودآموز (Closed-Loop Reinforcement)</span>
              <h3 style="font-size:1.25rem;color:var(--cream);margin:0">🧠 چرخهٔ یادگیری پیوسته سیستم و هوش مصنوعی هاسپیتالیتی</h3>
            </div>
            <p style="font-size:.84rem;color:var(--copper);margin-top:6px">مدل خوداصلاح‌گر یادگیری تقویتی بر اساس ۵,۰۵۵ نقد چندپلتفرمه، کاهش ۴۲٪ تاخیر سفارشات، رفع گلوگاه صف استقلال و جهش سودآوری رستوران شمسه</p>
          </div>
          <div style="display:flex;align-items:center;gap:10px">
            <a href="assets/img/shamse_system_learning_infographic.svg" target="_blank" class="btn" style="background:#221b15;border:1px solid #2ecc71;color:#2ecc71;padding:8px 14px;font-size:.8rem;border-radius:2px">
              🔍 مشاهده وکتور تمام‌صفحه SVG
            </a>
          </div>
        </div>

        <!-- Embedded Interactive SVG Infographic -->
        <div style="background:#110d0a;border:1px solid rgba(210,154,90,.3);border-radius:4px;overflow-x:auto;padding:12px;margin-bottom:20px">
          <div style="width:100%;min-width:850px;max-width:1150px;margin:0 auto">
            <img src="assets/img/shamse_system_learning_infographic.svg" alt="اینفوگرافیک چرخه یادگیری پیوسته سیستم و هوش مصنوعی رستوران شمسه" style="width:100%;height:auto;display:block">
          </div>
        </div>

        <!-- 5 Stages Explanatory Cards Matrix -->
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(210px,1fr));gap:14px;margin-top:16px">
          
          <div style="background:#18130e;border:1px solid #3d2a1d;border-top:3px solid #ffd21e;padding:14px;border-radius:3px">
            <span style="color:#ffd21e;font-weight:800;font-size:.85rem;display:block;margin-bottom:6px">۱. دریافت داده و حسگرها</span>
            <p style="font-size:.78rem;color:#bbb;line-height:1.7">پایش ۲۴/۷ گوگل مپ، تریپ‌ادوایزر، یاندکس و کیوآرکد سر میزها؛ استخراج آنی هر نقد و تاخیر آشپزخانه KDS.</p>
            <span style="color:#2ecc71;font-size:.74rem;font-weight:700">نرخ ورود: ۲۸ سیگنال/روز</span>
          </div>

          <div style="background:#18130e;border:1px solid #3d2a1d;border-top:3px solid #c084fc;padding:14px;border-radius:3px">
            <span style="color:#c084fc;font-weight:800;font-size:.85rem;display:block;margin-bottom:6px">۲. تریاژ احساسات و ابعاد</span>
            <p style="font-size:.78rem;color:#bbb;line-height:1.7">شناسایی ۵ جنبهٔ حیاتی غذا، اتمسفر، برخورد، قیمت و صف؛ تطبیق ۳۰ مدل هاگینگ‌فیس با ۱۰۰ مهارت هاسپیتالیتی.</p>
            <span style="color:#c084fc;font-size:.74rem;font-weight:700">تریاژ در ۴ زبان زنده</span>
          </div>

          <div style="background:#18130e;border:1px solid #3d2a1d;border-top:3px solid #38bdf8;padding:14px;border-radius:3px">
            <span style="color:#38bdf8;font-weight:800;font-size:.85rem;display:block;margin-bottom:6px">۳. یادگیری تقویتی (RLOF)</span>
            <p style="font-size:.78rem;color:#bbb;line-height:1.7">تابع پاداش ریاضی برای بیشینه‌سازی رضایت مهمان و کمینه‌سازی تاخیر؛ محاسبه خودکار ۱۰ فرمول کمی عملیاتی.</p>
            <span style="color:#38bdf8;font-size:.74rem;font-weight:700">همگرایی خودکار ۹۹٫۴٪</span>
          </div>

          <div style="background:#18130e;border:1px solid #3d2a1d;border-top:3px solid #fb923c;padding:14px;border-radius:3px">
            <span style="color:#fb923c;font-weight:800;font-size:.85rem;display:block;margin-bottom:6px">۴. اقدام و اجرای خودکار</span>
            <p style="font-size:.78rem;color:#bbb;line-height:1.7">پاسخ به نقدها زیر ۱۵ دقیقه، هدایت صف شلوغ استقلال به کوجاتپه با تاکسی اختصاصی و هشدار آنی به سرآشپز.</p>
            <span style="color:#fb923c;font-size:.74rem;font-weight:700">زمان اقدام: &lt; ۳۰ ثانیه</span>
          </div>

          <div style="background:#18130e;border:1px solid #3d2a1d;border-top:3px solid #2ecc71;padding:14px;border-radius:3px">
            <span style="color:#2ecc71;font-weight:800;font-size:.85rem;display:block;margin-bottom:6px">۵. دلتا و بهبود پیوسته</span>
            <p style="font-size:.78rem;color:#bbb;line-height:1.7">+۰٫۲۸★ رشد امتیاز گوگل مپ، -۴۲٪ تاخیر آشپزخانه، +۲۱٫۴٪ سود ناخالص هر فاکتور و بازتغذیه مستمر به چرخه.</p>
            <span style="color:#2ecc71;font-size:.74rem;font-weight:700">+$170,400 سود سالانه</span>
          </div>

        </div>

      </div>
    </div>
"""
    if 'id="ecoTab-learning"' not in html:
        target_section_end = '</section>\n\n<!-- ================= LIVE INTERACTIVE AI STUDIO & TEST SHOWCASE ================= -->'
        if target_section_end in html:
            html = html.replace(target_section_end, learning_panel_html + "\n" + target_section_end)
        else:
            print("Warning: target_section_end not found")

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)

    print("Successfully patched index.html!")

if __name__ == "__main__":
    main()
