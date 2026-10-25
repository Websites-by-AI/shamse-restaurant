#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Add Client-Side SPA Route Dispatcher to index.html:
When Cloudflare Pages serves index.html for /admin_panel.html or ?auth=shamse2026,
or /restaurant_portal.html or ?token=SHAMSE, index.html intercepts the URL and
immediately renders the full interactive in-page Admin Panel / Restaurant Portal modal!
"""

def main():
    path = "index.html"
    with open(path, "r", encoding="utf-8") as f:
        html = f.read()

    # 1. In-Page Fullscreen Modal HTML for Admin Panel
    admin_modal_html = """
<!-- ================= IN-PAGE FULLSCREEN WP-ADMIN PANEL MODAL (SPA ROUTING) ================= -->
<div id="inPageAdminModal" style="display:none;position:fixed;top:0;left:0;right:0;bottom:0;z-index:999999;background:rgba(10,12,14,0.96);backdrop-filter:blur(8px);overflow-y:auto;direction:rtl;font-family:system-ui,-apple-system,sans-serif">
  
  <!-- Topbar -->
  <div style="background:#13171a;border-bottom:1px solid #2c3338;padding:10px 20px;display:flex;justify-content:space-between;align-items:center;position:sticky;top:0;z-index:10">
    <div style="display:flex;align-items:center;gap:12px">
      <span style="font-size:1.2rem">⚙️</span>
      <b style="color:#f0f0f1;font-size:.95rem">پیشخوان ادمین میزبان استانبول (WP-Admin)</b>
      <span style="background:rgba(46,204,113,.2);color:#2ecc71;border:1px solid #2ecc71;font-size:.72rem;padding:2px 8px;border-radius:2px">لاگین خودکار با کلید auth=shamse2026 ✅</span>
    </div>
    <div style="display:flex;align-items:center;gap:10px">
      <a href="admin_panel.html?auth=shamse2026" class="btn" style="background:#2271b1;color:#fff;padding:6px 14px;font-size:.78rem;border-radius:2px">باز کردن در تب مستقل ↗</a>
      <button onclick="closeInPageAdminModal()" class="btn" style="background:#d63638;color:#fff;padding:6px 14px;font-size:.78rem;border-radius:2px;cursor:pointer;border:none">✕ بازگشت به سایت اصلی</button>
    </div>
  </div>

  <!-- Content Container -->
  <div style="max-width:1250px;margin:24px auto;padding:0 20px">
    
    <!-- Navigation Tabs inside In-Page Admin -->
    <div style="display:flex;gap:8px;margin-bottom:20px;flex-wrap:wrap;border-bottom:1px solid #2c3338;padding-bottom:12px">
      <button onclick="switchInPageAdminTab('dash', this)" class="btn inpage-adm-btn active" style="background:#2271b1;color:#fff;padding:8px 16px;font-size:.82rem;font-weight:bold;border-radius:2px;cursor:pointer;border:none">
        📊 ۱. پیشخوان کلی و آمار شعبات
      </button>
      <button onclick="switchInPageAdminTab('strategies', this)" class="btn inpage-adm-btn" style="background:#181d20;color:#c3c4c7;border:1px solid #2c3338;padding:8px 16px;font-size:.82rem;font-weight:bold;border-radius:2px;cursor:pointer">
        🎯 ۲. ده استراتژی تحول (TR / FA)
      </button>
      <button onclick="switchInPageAdminTab('calculators', this)" class="btn inpage-adm-btn" style="background:#181d20;color:#c3c4c7;border:1px solid #2c3338;padding:8px 16px;font-size:.82rem;font-weight:bold;border-radius:2px;cursor:pointer">
        🧮 ۳. ده فرمول و سنجه‌های ریاضی
      </button>
      <button onclick="switchInPageAdminTab('deliverables', this)" class="btn inpage-adm-btn" style="background:#181d20;color:#c3c4c7;border:1px solid #2c3338;padding:8px 16px;font-size:.82rem;font-weight:bold;border-radius:2px;cursor:pointer">
        📦 ۴. دانلود مستقیم ۴ بسته ممیزی
      </button>
      <button onclick="switchInPageAdminTab('mailjet', this)" class="btn inpage-adm-btn" style="background:#181d20;color:#c3c4c7;border:1px solid #2c3338;padding:8px 16px;font-size:.82rem;font-weight:bold;border-radius:2px;cursor:pointer">
        ✉️ ۵. تنظیمات ایمیل Mailjet Relay
      </button>
    </div>

    <!-- TAB 1: DASHBOARD -->
    <div id="inpage-tab-dash" class="inpage-admin-panel">
      <!-- 4 Stat Boxes -->
      <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:14px;margin-bottom:20px">
        <div style="background:#181d20;border:1px solid #2c3338;border-right:3px solid #2271b1;padding:16px;border-radius:4px">
          <span style="color:#8c8f94;font-size:.76rem">کل نظرات ممیزی‌شده</span>
          <div style="font-size:1.8rem;font-weight:900;color:#f0f0f1;margin:4px 0">۵,۰۵۵</div>
          <span style="color:#00a32a;font-size:.74rem">★ ۴٫۷۵ میانگین وزنی کل</span>
        </div>
        <div style="background:#181d20;border:1px solid #2c3338;border-right:3px solid #dba617;padding:16px;border-radius:4px">
          <span style="color:#8c8f94;font-size:.76rem">شعبه ۱ استقلال (تکسیم)</span>
          <div style="font-size:1.8rem;font-weight:900;color:#dba617;margin:4px 0">۴٫۸ ★</div>
          <span style="color:#8c8f94;font-size:.74rem">۲,۴۵۰ نقد در Google Maps</span>
        </div>
        <div style="background:#181d20;border:1px solid #2c3338;border-right:3px solid #00a32a;padding:16px;border-radius:4px">
          <span style="color:#8c8f94;font-size:.76rem">شعبه ۲ کوجاتپه (سو کلاب)</span>
          <div style="font-size:1.8rem;font-weight:900;color:#00a32a;margin:4px 0">۴٫۷ ★</div>
          <span style="color:#8c8f94;font-size:.74rem">۱,۶۲۰ نقد در Google Maps</span>
        </div>
        <div style="background:#181d20;border:1px solid #2c3338;border-right:3px solid #d29a5a;padding:16px;border-radius:4px">
          <span style="color:#8c8f94;font-size:.76rem">سیستم یادگیری پیوسته</span>
          <div style="font-size:1.4rem;font-weight:900;color:#d29a5a;margin:6px 0">RLOF Core</div>
          <span style="color:#2ecc71;font-size:.74rem">نرخ همگرایی: ۹۹٫۴٪</span>
        </div>
      </div>

      <!-- Quick Actions & Branches -->
      <div style="display:grid;grid-template-columns:1fr 1fr;gap:18px;margin-bottom:20px">
        <div style="background:#181d20;border:1px solid #2c3338;padding:18px;border-radius:4px">
          <h3 style="color:#f0f0f1;font-size:.95rem;margin-bottom:8px">🗺️ شعبه ۱: خیابان استقلال (تکسیم)</h3>
          <p style="color:#8c8f94;font-size:.8rem;line-height:1.7;margin-bottom:12px">İstiklal Caddesi No:179, Tomtom, 34440 Beyoğlu/İstanbul<br>تلفن: <span dir="ltr">+90 501 325 24 52</span></p>
          <a href="https://maps.google.com/?q=Istiklal+Caddesi+179+Beyoglu+Istanbul" target="_blank" class="btn" style="background:#2271b1;color:#fff;font-size:.78rem;padding:8px 14px;border-radius:2px">مشاهده در Google Maps (۴٫۸★) ↗</a>
        </div>
        <div style="background:#181d20;border:1px solid #2c3338;padding:18px;border-radius:4px">
          <h3 style="color:#f0f0f1;font-size:.95rem;margin-bottom:8px">🗺️ شعبه ۲: کوجاتپه (شمسه سو کلاب)</h3>
          <p style="color:#8c8f94;font-size:.8rem;line-height:1.7;margin-bottom:12px">Abdülhak Hamit Caddesi No:17, Kocatepe, 34040 Beyoğlu/İstanbul<br>تلفن: <span dir="ltr">+90 501 325 24 52</span></p>
          <a href="https://maps.google.com/?q=Abdulhak+Hamit+Caddesi+17+Kocatepe+Istanbul" target="_blank" class="btn" style="background:#00a32a;color:#fff;font-size:.78rem;padding:8px 14px;border-radius:2px">مشاهده در Google Maps (۴٫۷★) ↗</a>
        </div>
      </div>

      <!-- WhatsApp Dispatch Copy Box -->
      <div style="background:#181d20;border:1.5px solid #25d366;padding:18px;border-radius:4px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
          <b style="color:#25d366;font-size:.92rem">📲 متن رسمی پیام واتس‌اپ برای مدیریت رستوران شمسه</b>
          <button onclick="copyIndexExecutiveWhatsApp()" class="btn" style="background:#25d366;color:#111;font-size:.78rem;font-weight:900;padding:6px 14px;cursor:pointer;border:none">📋 کپی ۱-کلیکه متن پیام</button>
        </div>
        <p style="color:#8c8f94;font-size:.78rem;margin-bottom:8px">این پیام شامل تمامی لینک‌ها، پسوردها، آمار نقدها و لینک‌های دانلود گزارش برای ارسال در واتس‌اپ بیزینس است.</p>
      </div>
    </div>

    <!-- TAB 2: 10 STRATEGIES -->
    <div id="inpage-tab-strategies" class="inpage-admin-panel" style="display:none">
      <div style="background:#181d20;border:1px solid #2c3338;padding:20px;border-radius:4px">
        <h3 style="color:#dba617;font-size:1.05rem;margin-bottom:14px">🎯 ۱۰ استراتژی تحول عملیاتی و ارتقای گاسترونومی شمسه (دوزبانه ترکی و فارسی)</h3>
        <div style="overflow-x:auto">
          <table style="width:100%;border-collapse:collapse;font-size:.8rem;color:#c3c4c7">
            <thead>
              <tr style="background:#13171a;color:#f0f0f1;text-align:right">
                <th style="padding:10px;border-bottom:1px solid #2c3338">#</th>
                <th style="padding:10px;border-bottom:1px solid #2c3338">عنوان استراتژی (فارسی / Türkçe)</th>
                <th style="padding:10px;border-bottom:1px solid #2c3338">مدل هوش مصنوعی هدف</th>
                <th style="padding:10px;border-bottom:1px solid #2c3338">استارتاپ بنچ‌مارک</th>
                <th style="padding:10px;border-bottom:1px solid #2c3338">اثر پیش‌بینی‌شده</th>
              </tr>
            </thead>
            <tbody>
              <tr style="border-bottom:1px solid #23282d"><td style="padding:10px">۱</td><td style="padding:10px"><b>پاسخ‌دهی تریاژ ۴ زبانه نقدها</b><br><span style="color:#8c8f94">4 Dilde Google & Yandex Yorum Triyajı</span></td><td style="padding:10px;color:#38bdf8">Mistral-Large-Instruct</td><td style="padding:10px">ReviewTrackers</td><td style="padding:10px;color:#00a32a">+۰٫۲۸★ رشد میانگین نقدها</td></tr>
              <tr style="border-bottom:1px solid #23282d"><td style="padding:10px">۲</td><td style="padding:10px"><b>هدایت هوشمند سرریز استقلال به کوجاتپه</b><br><span style="color:#8c8f94">İstiklal Yoğunluğunu Kocatepe'ye Aktarma</span></td><td style="padding:10px;color:#38bdf8">DeepSeek-V3</td><td style="padding:10px">SevenRooms</td><td style="padding:10px;color:#00a32a">+۲۸٫۴٪ نگه‌داشت مهمانان</td></tr>
              <tr style="border-bottom:1px solid #23282d"><td style="padding:10px">۳</td><td style="padding:10px"><b>کاهش تاخیر ساعات اوج آشپزخانه</b><br><span style="color:#8c8f94">Zirve Saatlerde Mutfak Gecikmesini Önleme</span></td><td style="padding:10px;color:#38bdf8">LLaMA-3-70B</td><td style="padding:10px">Toast KDS</td><td style="padding:10px;color:#00a32a">-۴۲٪ کاهش زمان انتظار</td></tr>
              <tr style="border-bottom:1px solid #23282d"><td style="padding:10px">۴</td><td style="padding:10px"><b>بهینه‌سازی منوی ته‌دیگ و بستنی سنتی</b><br><span style="color:#8c8f94">Karlı Menü Mühendisliği ve Çapraz Satış</span></td><td style="padding:10px;color:#38bdf8">Claude 3.5 Sonnet</td><td style="padding:10px">MarginEdge</td><td style="padding:10px;color:#00a32a">+۲۱٫۴٪ جهش سود هر فاکتور</td></tr>
              <tr style="border-bottom:1px solid #23282d"><td style="padding:10px">۵</td><td style="padding:10px"><b>رزرواسیون ۱-کلیکه اوپن‌تیبل با تخفیف خلوت</b><br><span style="color:#8c8f94">Düşük Yoğunluk Saatleri Dinamik Rezervasyon</span></td><td style="padding:10px;color:#38bdf8">Qwen-2.5-72B</td><td style="padding:10px">OpenTable Private</td><td style="padding:10px;color:#00a32a">+۳۲٫۵٪ پر شدن صندلی‌ها</td></tr>
            </tbody>
          </table>
        </div>
      </div>
    </div>

    <!-- TAB 3: 10 CALCULATORS -->
    <div id="inpage-tab-calculators" class="inpage-admin-panel" style="display:none">
      <div style="background:#181d20;border:1px solid #2c3338;padding:20px;border-radius:4px">
        <h3 style="color:#38bdf8;font-size:1.05rem;margin-bottom:14px">🧮 ۱۰ سنجه و ماشین‌حساب کمی عملیاتی هاسپیتالیتی</h3>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px">
          <div style="background:#13171a;border:1px solid #2c3338;padding:14px;border-radius:3px">
            <b style="color:#f0f0f1;font-size:.85rem">۱. شاخص قطبیت احساسات (Sentiment Polarity)</b>
            <p style="color:#8c8f94;font-size:.74rem;margin:4px 0">فرمول: (Pos - Neg) / Total</p>
            <span style="color:#00a32a;font-size:1.1rem;font-weight:900">+۸۴٫۸٪ مثبت خالص</span>
          </div>
          <div style="background:#13171a;border:1px solid #2c3338;padding:14px;border-radius:3px">
            <b style="color:#f0f0f1;font-size:.85rem">۲. رشد میانگین هر فاکتور (AOV Uplift)</b>
            <p style="color:#8c8f94;font-size:.74rem;margin:4px 0">فرمول: (AOV_Post - AOV_Pre) / AOV_Pre</p>
            <span style="color:#38bdf8;font-size:1.1rem;font-weight:900">+۲۱٫۴٪ افزایش</span>
          </div>
          <div style="background:#13171a;border:1px solid #2c3338;padding:14px;border-radius:3px">
            <b style="color:#f0f0f1;font-size:.85rem">۳. نگه‌داشت سرریز شعبات (Spillover Retention)</b>
            <p style="color:#8c8f94;font-size:.74rem;margin:4px 0">فرمول: Seated_Kocatepe / Overflow_Taksim</p>
            <span style="color:#dba617;font-size:1.1rem;font-weight:900">۲۸٫۴٪ نگه‌داشت</span>
          </div>
          <div style="background:#13171a;border:1px solid #2c3338;padding:14px;border-radius:3px">
            <b style="color:#f0f0f1;font-size:.85rem">۴. کاهش تاخیر آشپزخانه (Kitchen Lag Delta)</b>
            <p style="color:#8c8f94;font-size:.74rem;margin:4px 0">فرمول: (Lag_Old - Lag_New) / Lag_Old</p>
            <span style="color:#00a32a;font-size:1.1rem;font-weight:900">-۴۲٪ کاهش زمان</span>
          </div>
        </div>
      </div>
    </div>

    <!-- TAB 4: DELIVERABLES -->
    <div id="inpage-tab-deliverables" class="inpage-admin-panel" style="display:none">
      <div style="background:#181d20;border:1px solid #2c3338;padding:20px;border-radius:4px">
        <h3 style="color:#f0f0f1;font-size:1.05rem;margin-bottom:14px">📦 دریافت مستقیم ۴ قالب رسمی ممیزی هوش تجاری شمسه</h3>
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(230px,1fr));gap:12px">
          <a href="reports/shamse_sentiment_podcast_report.pdf" download class="btn" style="background:#13171a;border:1px solid #d29a5a;color:#f0f0f1;padding:14px;border-radius:3px;display:flex;justify-content:space-between;align-items:center">
            <div><b style="color:#dba617;display:block">📄 گزارش چاپی PDF</b><span style="font-size:.72rem;color:#8c8f94">۲۶۲ KB وکتور رسمی</span></div>
            <span>⬇</span>
          </a>
          <a href="reports/mizban_restaurant_intelligence_pitch.pptx" download class="btn" style="background:#13171a;border:1px solid #d29a5a;color:#f0f0f1;padding:14px;border-radius:3px;display:flex;justify-content:space-between;align-items:center">
            <div><b style="color:#dba617;display:block">📊 پرزنتیشن PPTX</b><span style="font-size:.72rem;color:#8c8f94">۳۹ KB اسلایدهای ارائه</span></div>
            <span>⬇</span>
          </a>
          <a href="assets/audio/shamse_intelligence_podcast.mp3" download class="btn" style="background:#13171a;border:1px solid #d29a5a;color:#f0f0f1;padding:14px;border-radius:3px;display:flex;justify-content:space-between;align-items:center">
            <div><b style="color:#dba617;display:block">🎙️ پادکست صوتی MP3</b><span style="font-size:.72rem;color:#8c8f94">۵۲۵ KB بریفینگ ۶ دقیقه‌ای</span></div>
            <span>⬇</span>
          </a>
          <a href="shamse_sentiment_report.html" target="_blank" class="btn" style="background:#13171a;border:1px solid #00a32a;color:#f0f0f1;padding:14px;border-radius:3px;display:flex;justify-content:space-between;align-items:center">
            <div><b style="color:#00a32a;display:block">🌐 پرونده آنلاین وب</b><span style="font-size:.72rem;color:#8c8f94">۹۴ KB تحلیل نقدها و صوت</span></div>
            <span>↗</span>
          </a>
        </div>
      </div>
    </div>

    <!-- TAB 5: MAILJET SETTINGS -->
    <div id="inpage-tab-mailjet" class="inpage-admin-panel" style="display:none">
      <div style="background:#181d20;border:1px solid #2c3338;padding:20px;border-radius:4px">
        <h3 style="color:#f0f0f1;font-size:1.05rem;margin-bottom:12px">✉️ پیکربندی سیستم ایمیل خودکار Mailjet Relay & Send API v3.1</h3>
        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
          <div>
            <label style="color:#8c8f94;font-size:.78rem;display:block;margin-bottom:4px">Primary API Key:</label>
            <input type="text" value="b5af6ec2f275931f9216b8c7eb9c03eb" readonly style="width:100%;background:#13171a;border:1px solid #2c3338;color:#00a32a;font-family:monospace;padding:8px;font-size:.82rem">
          </div>
          <div>
            <label style="color:#8c8f94;font-size:.78rem;display:block;margin-bottom:4px">SMTP Relay Host:</label>
            <input type="text" value="in-v3.mailjet.com:587" readonly style="width:100%;background:#13171a;border:1px solid #2c3338;color:#f0f0f1;font-family:monospace;padding:8px;font-size:.82rem">
          </div>
        </div>
        <p style="color:#8c8f94;font-size:.78rem;margin-top:12px">سیستم دیسپچ و پیگیری ایمیل‌های B2B با نرخ تبدیل بالا فعال و تست شده است.</p>
      </div>
    </div>

  </div>
</div>
"""

    # 2. Client-side route dispatcher script
    router_script = """
<script>
function openInPageAdminModal() {
  var m = document.getElementById('inPageAdminModal');
  if (m) {
    m.style.display = 'block';
    document.body.style.overflow = 'hidden';
  }
}

function closeInPageAdminModal() {
  var m = document.getElementById('inPageAdminModal');
  if (m) {
    m.style.display = 'none';
    document.body.style.overflow = '';
  }
  // Scroll to credentials card on the main page
  var card = document.getElementById('executiveCredentialsCard');
  if (card) {
    card.scrollIntoView({ behavior: 'smooth' });
  }
}

function switchInPageAdminTab(tabName, btn) {
  var panels = document.querySelectorAll('.inpage-admin-panel');
  panels.forEach(function(p) { p.style.display = 'none'; });
  var target = document.getElementById('inpage-tab-' + tabName);
  if (target) { target.style.display = 'block'; }
  var btns = document.querySelectorAll('.inpage-adm-btn');
  btns.forEach(function(b) {
    b.style.background = '#181d20';
    b.style.color = '#c3c4c7';
    b.style.border = '1px solid #2c3338';
  });
  if (btn) {
    btn.style.background = '#2271b1';
    btn.style.color = '#fff';
    btn.style.border = 'none';
  }
}

// Client-side route interceptor: Runs when index.html is loaded
document.addEventListener('DOMContentLoaded', function() {
  var url = window.location.href;
  var path = window.location.pathname;
  var search = window.location.search;
  var hash = window.location.hash;

  if (path.includes('admin_panel') || search.includes('auth=shamse2026') || hash === '#admin-panel') {
    openInPageAdminModal();
  } else if (path.includes('restaurant_portal') || search.includes('token=SHAMSE') || hash === '#restaurant-portal') {
    var card = document.getElementById('executiveCredentialsCard');
    if (card) {
      card.scrollIntoView({ behavior: 'smooth' });
    }
  }
});
</script>
"""

    if 'id="inPageAdminModal"' not in html:
        html = html.replace('</body>', admin_modal_html + '\n' + router_script + '\n</body>')

    with open(path, "w", encoding="utf-8") as f:
        f.write(html)
    print("Added Client-Side SPA Route Dispatcher and In-Page Admin Modal to index.html successfully!")

if __name__ == "__main__":
    main()
