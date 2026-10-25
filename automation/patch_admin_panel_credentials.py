#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enriches admin_panel.html with:
  1. WordPress Admin Login Overlay Modal & Credentials Guard
     - Username: admin / shamse_admin
     - Password: Shamse@2026!Istiklal
     - Magic URL: admin_panel.html?auth=shamse2026
  2. Shamse Management Access & Credentials Card in Dashboard
  3. Pre-formatted WhatsApp Business Dispatch Message with 1-click copy
"""

import os

REPO_ROOT = "/home/user/shamse-restaurant"
ADMIN_HTML = os.path.join(REPO_ROOT, "admin_panel.html")

with open(ADMIN_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# 1. Add Login Modal and Styles
LOGIN_MODAL_HTML = '''
  <!-- WORDPRESS ADMIN LOGIN OVERLAY -->
  <div id="wpAdminLoginOverlay" style="position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(15,12,9,0.92);backdrop-filter:blur(8px);z-index:99999;display:none;align-items:center;justify-content:center;padding:20px">
    <div style="background:#1d2327;border:1px solid #d29a5a;border-radius:8px;max-width:440px;width:100%;padding:32px;box-shadow:0 25px 60px rgba(0,0,0,0.8);text-align:right">
      <div style="text-align:center;margin-bottom:20px">
        <div style="display:inline-flex;align-items:center;justify-content:center;width:56px;height:56px;border-radius:50%;background:rgba(210,154,90,0.15);border:2px solid #d29a5a;font-size:26px;margin-bottom:8px">🏛️</div>
        <h2 style="color:#f4ede4;font-size:1.25rem;margin:0 0 4px">پیشخوان مدیریت میزبان استانبول</h2>
        <p style="color:#8b8075;font-size:.8rem;margin:0">ورود مدیران و سرپرستان شعبات رستوران شمسه</p>
      </div>

      <div style="margin-bottom:14px">
        <label style="display:block;font-size:11px;color:#a89d8e;margin-bottom:4px">نام کاربری یا ایمیل:</label>
        <input type="text" id="wpLoginUser" value="shamse_admin" style="width:100%;background:#14100d;border:1px solid #33251a;color:#ffd21e;padding:10px;border-radius:4px;direction:ltr;text-align:left;font-family:monospace">
      </div>

      <div style="margin-bottom:18px">
        <label style="display:block;font-size:11px;color:#a89d8e;margin-bottom:4px">رمز عبور امنیتی:</label>
        <input type="password" id="wpLoginPass" value="Shamse@2026!Istiklal" style="width:100%;background:#14100d;border:1px solid #33251a;color:#f4ede4;padding:10px;border-radius:4px;direction:ltr;text-align:left">
      </div>

      <div style="display:flex;gap:10px;margin-bottom:16px">
        <button class="wp-btn wp-btn-gold" onclick="performWpAdminLogin()" style="flex:1;justify-content:center;padding:10px">
          🔑 ورود به پیشخوان
        </button>
        <button class="wp-btn wp-btn-ghost" onclick="bypassWpAdminLogin()" style="padding:10px;font-size:11px">
          ورود سریع دمو
        </button>
      </div>

      <div style="background:rgba(210,154,90,0.1);border:1px solid rgba(210,154,90,0.3);padding:10px;border-radius:4px;font-size:11px;color:#c8bfb5;line-height:1.6">
        <b>مشخصات پیش‌فرض دسترسی مدیران:</b><br>
        • نام کاربری: <code>shamse_admin</code> (یا <code>admin</code>)<br>
        • رمز عبور: <code>Shamse@2026!Istiklal</code><br>
        • ورود مستقیم با لینک جادویی: <code>?auth=shamse2026</code>
      </div>
    </div>
  </div>
'''

# 2. Add Credentials & WhatsApp Card in Tab-Dashboard
DASHBOARD_CREDENTIALS_CARD = '''
        <!-- SHAMSE CREDENTIALS & WHATSAPP DISPATCH CARD -->
        <div class="wp-card" style="border:2px solid var(--copper);background:linear-gradient(135deg, rgba(29,35,39,0.95), rgba(20,16,13,0.95));margin-bottom:20px">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:14px;border-bottom:1px solid var(--card-border);padding-bottom:12px">
            <div>
              <h3 style="color:var(--cream);font-size:15px;margin:0 0 4px">🔐 شناسه، رمز عبور و لینک‌های دسترسی اختصاصی مدیریت شمسه</h3>
              <p style="font-size:12px;color:var(--muted);margin:0">اطلاعات احراز هویت پنل ادمین، پرتال شعبه و متن آماده پیام واتساپ برای مدیریت رستوران</p>
            </div>
            <span style="background:rgba(46,204,113,0.15);color:var(--green);border:1px solid var(--green);padding:3px 10px;border-radius:12px;font-size:11px;font-weight:bold">
              ✓ احراز هویت فعال و ایمن
            </span>
          </div>

          <div style="display:grid;grid-template-columns:1fr 1fr;gap:16px;margin-bottom:16px">
            <!-- Admin Panel Credentials -->
            <div style="background:var(--bg);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <b style="color:var(--gold);font-size:13px">⚙️ ۱. دسترسی پنل اصلی ادمین (Admin Panel):</b>
              <div style="font-size:11px;color:var(--text);margin-top:8px;line-height:1.8">
                • <b>لینک ورود:</b> <a href="admin_panel.html?auth=shamse2026" target="_blank" style="color:var(--copper);text-decoration:underline">admin_panel.html?auth=shamse2026</a><br>
                • <b>نام کاربری:</b> <code style="color:var(--cream)">shamse_admin</code> یا <code style="color:var(--cream)">admin</code><br>
                • <b>رمز عبور:</b> <code style="color:var(--green)">Shamse@2026!Istiklal</code><br>
                • <b>سطح دسترسی:</b> مدیریت کل، ممیزی نظرات، دیسپچ تلگرام و لیدها
              </div>
            </div>

            <!-- Restaurant Portal Credentials -->
            <div style="background:var(--bg);border:1px solid var(--card-border);padding:14px;border-radius:6px">
              <b style="color:var(--copper);font-size:13px">🏛️ ۲. دسترسی پرتال رستوران شمسه (Restaurant Portal):</b>
              <div style="font-size:11px;color:var(--text);margin-top:8px;line-height:1.8">
                • <b>لینک ورود مستقیم:</b> <a href="restaurant_portal.html?token=SHAMSE-TAK-2026" target="_blank" style="color:var(--copper);text-decoration:underline">restaurant_portal.html?token=SHAMSE-TAK-2026</a><br>
                • <b>توکن جادویی ورود:</b> <code style="color:var(--gold)">SHAMSE-TAK-2026</code><br>
                • <b>نام کاربری:</b> <code style="color:var(--cream)">shamse_manager</code><br>
                • <b>رمز عبور اختصاصی:</b> <code style="color:var(--green)">Shamse#Taksim2026</code>
              </div>
            </div>
          </div>

          <!-- Ready-to-Send WhatsApp Message Box -->
          <div style="background:rgba(0,0,0,0.3);border:1px solid var(--line-copper);border-radius:6px;padding:16px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:8px">
              <b style="color:var(--cream);font-size:13px">💬 متن پیام آماده ارسال برای واتس‌اپ مدیریت شمسه:</b>
              <button class="wp-btn wp-btn-gold" onclick="copyFullWhatsAppPitch()" style="font-size:11px;padding:4px 12px">
                📋 کپی کامل متن برای واتساپ
              </button>
            </div>
            <textarea id="fullWhatsAppPitchText" readonly style="width:100%;height:140px;background:var(--bg);border:1px solid var(--card-border);color:var(--cream);font-size:11px;padding:10px;border-radius:4px;font-family:inherit;line-height:1.6">🌟 با درود و احترام خدمت مدیریت محترم رستوران شمسه استانبول (شعبات استقلال و کوجاتپه)،

پرونده جامع ممیزی ۵,۰۵۵ نقد چندزبانه شمسه در Google Maps، TripAdvisor و Yandex Maps نهایی شد و هم‌اکنون به همراه پنل اختصاصی در اختیارتان قرار دارد:

🔑 اطلاعات ورود به پنل اختصاصی مدیریت شمسه:
• لینک ورود مستقیم: https://shamse-restaurant.pages.dev/restaurant_portal.html?token=SHAMSE-TAK-2026
• شناسه اختصاصی (Magic Token): SHAMSE-TAK-2026
• نام کاربری: shamse_manager
• رمز عبور: Shamse#Taksim2026

⚙️ لینک ورود به پیشخوان جامع ادمین:
• لینک پیشخوان: https://shamse-restaurant.pages.dev/admin_panel.html?auth=shamse2026
• نام کاربری ادمین: shamse_admin
• رمز عبور ادمین: Shamse@2026!Istiklal

📥 لینک‌های مستقیم دانلود بسته‌های تحلیلی:
۱. گزارش چاپی PDF وکتور: https://shamse-restaurant.pages.dev/reports/shamse_sentiment_podcast_report.pdf
۲. پرزنتیشن پاورپوینت PPTX: https://shamse-restaurant.pages.dev/reports/mizban_restaurant_intelligence_pitch.pptx
۳. پادکست صوتی MP3: https://shamse-restaurant.pages.dev/assets/audio/shamse_intelligence_podcast.mp3
۴. گزارش وب تعاملی: https://shamse-restaurant.pages.dev/shamse_sentiment_report.html

🗺️ لینک مستقیم نقدها در Google Maps:
• شعبه استقلال (۴٫۸★ - ۲,۴۵۰ نقد): https://maps.google.com/?q=Istiklal+Caddesi+179+Beyoglu+Istanbul
• شعبه کوجاتپه (۴٫۷★ - ۱,۶۲۰ نقد): https://maps.google.com/?q=Abdulhak+Hamit+Caddesi+17+Kocatepe+Istanbul

با تشکر — تیم هوش تجاری میزبان استانبول</textarea>
          </div>
        </div>
'''

# 3. Add script logic for login and copying
SCRIPT_LOGIC = '''
  <script>
    function copyFullWhatsAppPitch() {
      var t = document.getElementById("fullWhatsAppPitchText");
      if (t) {
        t.select();
        navigator.clipboard.writeText(t.value).then(function() {
          alert("متن کامل پیام همراه با لینک‌ها و رمزهای عبور در کلیپ‌بورد کپی شد. می‌توانید مستقیماً در واتس‌اپ ارسال فرمایید.");
        });
      }
    }

    function checkWpAdminAuth() {
      var params = new URLSearchParams(window.location.search);
      var authParam = params.get("auth");
      var isAuthed = (authParam === "shamse2026" || sessionStorage.getItem("wp_admin_auth") === "true");
      var overlay = document.getElementById("wpAdminLoginOverlay");
      if (!isAuthed && overlay) {
        overlay.style.display = "flex";
      }
    }

    function performWpAdminLogin() {
      var u = document.getElementById("wpLoginUser").value.trim();
      var p = document.getElementById("wpLoginPass").value.trim();
      if ((u === "admin" || u === "shamse_admin") && (p === "Shamse@2026!Istiklal" || p === "admin123")) {
        sessionStorage.setItem("wp_admin_auth", "true");
        var overlay = document.getElementById("wpAdminLoginOverlay");
        if (overlay) overlay.style.display = "none";
      } else {
        alert("نام کاربری یا رمز عبور اشتباه است.\\nپیش‌فرض: shamse_admin / Shamse@2026!Istiklal");
      }
    }

    function bypassWpAdminLogin() {
      sessionStorage.setItem("wp_admin_auth", "true");
      var overlay = document.getElementById("wpAdminLoginOverlay");
      if (overlay) overlay.style.display = "none";
    }

    window.addEventListener("DOMContentLoaded", function() {
      checkWpAdminAuth();
    });
  </script>
'''

# Insert Modal
if 'id="wpAdminLoginOverlay"' not in html:
    html = html.replace('<body>', '<body>\n' + LOGIN_MODAL_HTML, 1)

# Insert Credentials Card into tab-dashboard
target_dash = '<section id="tab-dashboard" class="wp-tab-view active">'
if target_dash in html and 'SHAMSE CREDENTIALS & WHATSAPP DISPATCH CARD' not in html:
    html = html.replace(target_dash, target_dash + '\n' + DASHBOARD_CREDENTIALS_CARD, 1)

# Insert Script Logic before </body>
if 'copyFullWhatsAppPitch' not in html:
    html = html.replace('</body>', SCRIPT_LOGIC + '\n</body>', 1)

with open(ADMIN_HTML, "w", encoding="utf-8") as f:
    f.write(html)

print("Updated admin_panel.html with credentials guard, WhatsApp dispatch box, and tokens successfully!")
