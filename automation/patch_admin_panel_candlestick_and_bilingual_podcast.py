#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Patch Admin Panel, Web Dossier, and PDF Generator with:
1. Forex-Style Candlestick Sentiment Chart (6 Sessions, Open, High, Low, Close, Volume)
2. Dual Calendar Timestamps (Shamsi & Miladi) + Peak Hours
3. High-Tech AI Frontier vs. Easy Quick Fix (Cost, Timeline, Tags, 100 Skills Mapping)
4. Bilingual Executive Podcast Audio Player (Farsi 65.6s + Turkish 80.6s) with Transcripts
5. Direct Access Links to Admin Panel, Portal, Telegram Bot, and Vector PDF
"""

import os
import re
import sys

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(REPO_ROOT, "automation"))

import candlestick_sentiment_engine as cse

ADMIN_PANEL_PATH = os.path.join(REPO_ROOT, "admin_panel.html")
WEB_DOSSIER_PATH = os.path.join(REPO_ROOT, "shamse_sentiment_report.html")
PDF_GEN_PATH = os.path.join(REPO_ROOT, "automation", "generate_shamse_dossier_pdf.py")

candlestick_svg = cse.generate_candlestick_svg(width=900, height=360)
sessions = cse.get_candlestick_sessions()

def build_candlestick_and_hightech_easyfix_html() -> str:
    """تولید کامپوننت HTML نمودار شمعی و جدول مقایسه های‌تک در برابر فیکس سریع با تقویم دوگانه"""
    rows_html = []
    for s in sessions:
        rows_html.append(f"""
        <tr>
          <td>
            <b style="color:var(--gold)">{s['id']}</b><br>
            <span style="font-size:10px;color:var(--cream)">{s['session_name']}</span><br>
            <span style="font-size:9.5px;color:var(--muted)">{s['session_name_en']}</span>
          </td>
          <td>
            <span class="wp-badge" style="background:#2ecc71;color:#000;font-size:9.5px">📅 {s['date_shamsi']}</span><br>
            <span class="wp-badge" style="background:#3498db;color:#fff;font-size:9.5px;margin-top:2px">🌐 {s['date_miladi']}</span><br>
            <span style="font-size:9.5px;color:var(--muted)">⏰ {s['time_slot']}</span>
          </td>
          <td>
            <div style="font-size:10.5px;direction:ltr;text-align:left;font-family:monospace">
              O: <b>{s['open']:.2f}</b> | H: <b style="color:#2ecc71">{s['high']:.2f}</b><br>
              L: <b style="color:#e74c3c">{s['low']:.2f}</b> | C: <b>{s['close']:.2f}</b>
            </div>
            <div style="font-size:9.5px;color:var(--muted);margin-top:2px">👥 {s['volume_guests']} مسافر</div>
          </td>
          <td>
            <span style="color:#e74c3c;font-weight:bold;font-size:11px">⚠️ {s['primary_flaw']}</span>
          </td>
          <td style="background:rgba(231,76,60,0.06);border-right:2px solid #e74c3c">
            <span class="wp-badge" style="background:#e74c3c;color:#fff;font-size:9px">🚀 {s['high_tech_tag']}</span>
            <div style="font-size:10.5px;color:var(--cream);margin-top:3px">{s['high_tech_solution']}</div>
            <div style="font-size:9.5px;color:#f39c12;margin-top:3px">
              <b>هزینه:</b> {s['high_tech_cost']} • <b>زمان:</b> {s['high_tech_timeline']}
            </div>
          </td>
          <td style="background:rgba(46,204,113,0.06);border-right:2px solid #2ecc71">
            <span class="wp-badge" style="background:#2ecc71;color:#000;font-weight:bold;font-size:9px">⚡ {s['easy_fix_tag']}</span>
            <div style="font-size:10.5px;color:var(--cream);margin-top:3px">{s['easy_fix_solution']}</div>
            <div style="font-size:9.5px;color:#2ecc71;margin-top:3px">
              <b>هزینه:</b> {s['easy_fix_cost']} • <b>زمان:</b> {s['easy_fix_timeline']}
            </div>
          </td>
          <td style="text-align:center">
            <span class="wp-badge" style="background:#d29a5a;color:#101e22;font-weight:bold">{s['skill_code']}</span><br>
            <span style="font-size:9.5px;color:var(--muted)">{s['skill_domain']}</span>
          </td>
        </tr>
        """)

    html = f"""
        <!-- SECTION: FOREX CANDLESTICK SENTIMENT & HIGH-TECH VS EASY FIX -->
        <div class="wp-card" style="border:2px solid #3498db;background:linear-gradient(135deg,rgba(20,24,28,0.98),rgba(15,18,20,0.98));margin-bottom:20px">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:14px;border-bottom:1px solid rgba(52,152,219,0.3);padding-bottom:10px">
            <div>
              <span class="wp-badge" style="background:#3498db;color:#fff;font-weight:bold;margin-bottom:4px">Forex-Style Candlestick Sentiment v2.4</span>
              <h3 style="margin:2px 0;color:var(--cream);font-size:16px">📈 نمودار شمعی فارکس تحلیل نوسان احساسات و جدول مقایسه های‌تک سنگین در برابر فیکس سریع</h3>
              <p style="margin:0;font-size:11px;color:var(--muted)">تحلیل نوسان امتیاز در ۶ شیفت حساس به همراه تاریخ‌های دوگانه (شمسی و میلادی) و نگاشت به ۱۰۰ مهارت هاسپیتالیتی</p>
            </div>
            <div style="display:flex;gap:8px">
              <span class="wp-badge" style="background:rgba(46,204,113,0.15);color:#2ecc71;border:1px solid #2ecc71">همبستگی احساسات: ۹۶٫۸٪</span>
              <span class="wp-badge" style="background:rgba(210,154,90,0.15);color:var(--gold);border:1px solid var(--gold)">۶ کندل پایش‌شده</span>
            </div>
          </div>

          <!-- THE SVG CANDLESTICK CHART CONTAINER -->
          <div style="background:#13171a;border:1px solid #252f36;border-radius:6px;padding:12px;margin-bottom:16px;overflow-x:auto">
            {candlestick_svg}
          </div>

          <!-- THE COMPARISON TABLE -->
          <h4 style="color:var(--gold);font-size:13px;margin:14px 0 8px">⚖️ جدول مقایسه راهکارهای فناورانه سنگین (High-Tech AI) در برابر فیکس‌های سریع ۵ دقیقه‌ای (Easy Quick Fix):</h4>
          <div style="overflow-x:auto">
            <table class="wp-table" style="font-size:11px">
              <thead>
                <tr>
                  <th style="width:13%">شناسه و نام شیفت</th>
                  <th style="width:14%">تقویم دوگانه و ساعت اوج</th>
                  <th style="width:11%">شاخص‌های شمعی (OHLC)</th>
                  <th style="width:15%">نقص و گلوگاه شناسایی‌شده</th>
                  <th style="width:20%">راهکار های‌تک سنگین (High-Tech AI)</th>
                  <th style="width:18%">فیکس سریع و کم‌هزینه (Easy Quick Fix)</th>
                  <th style="width:9%">مهارت ۱۰۰ گانه</th>
                </tr>
              </thead>
              <tbody>
                {"".join(rows_html)}
              </tbody>
            </table>
          </div>
        </div>
    """
    return html

def build_bilingual_podcast_widget_html() -> str:
    """تولید پلیر صوتی دوزبانه (فارسی و ترکی) با متن ترانسکریپت و دکمه‌های دانلود"""
    html = """
        <!-- SECTION: BILINGUAL EXECUTIVE AUDIO PODCAST (FARSI & TURKISH) -->
        <div class="wp-card" style="border:2px solid var(--gold);background:linear-gradient(135deg,rgba(28,20,14,0.98),rgba(20,16,13,0.98));margin-bottom:20px">
          <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:12px;margin-bottom:14px;border-bottom:1px solid rgba(210,154,90,0.3);padding-bottom:10px">
            <div>
              <span class="wp-badge" style="background:var(--gold);color:#101e22;font-weight:bold;margin-bottom:4px">Bilingual Audio Briefing v2.4</span>
              <h3 style="margin:2px 0;color:var(--cream);font-size:16px">🎙️ پادکست اختصاصی هوش تجاری شمسه به دو زبان فارسی و ترکی (Türkçe)</h3>
              <p style="margin:0;font-size:11px;color:var(--muted)">خلاصه صوتی تحلیل ۵,۰۵۵ نقد، راهکارهای عملیاتی و جهش درآمد ماهانه برای هیئت مدیره</p>
            </div>
            <div style="display:flex;gap:6px">
              <button id="btnPodcastFa" class="wp-btn wp-btn-gold" onclick="switchAdminPodcastLang('fa')" style="padding:5px 12px;font-size:11px">
                🇮🇷 پادکست فارسی (۶۵ ثانیه)
              </button>
              <button id="btnPodcastTr" class="wp-btn wp-btn-ghost" onclick="switchAdminPodcastLang('tr')" style="padding:5px 12px;font-size:11px">
                🇹🇷 Türkçe Podcast (۸۰ ثانیه)
              </button>
            </div>
          </div>

          <!-- AUDIO PLAYERS & CONTROLS -->
          <div style="background:rgba(0,0,0,0.4);border:1px solid rgba(255,255,255,0.1);border-radius:6px;padding:14px;margin-bottom:14px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:10px">
              <div style="display:flex;align-items:center;gap:10px">
                <button id="adminAudioPlayBtn" class="wp-btn wp-btn-gold" onclick="toggleAdminPodcastPlay()" style="width:42px;height:42px;border-radius:50%;padding:0;display:flex;align-items:center;justify-content:center;font-size:16px">
                  ▶
                </button>
                <div>
                  <b id="adminAudioTitle" style="color:#fff;font-size:13px">پادکست فارسی هوش تجاری شمسه (Persian Audio Briefing)</b>
                  <div id="adminAudioMeta" style="font-size:11px;color:var(--muted)">مدت: ۰۱:۰۵ • کیفیت: MP3 128kbps Stereo • گوینده: هوش مصنوعی فارسی</div>
                </div>
              </div>
              <div style="display:flex;gap:8px">
                <a id="adminAudioDownloadLink" href="assets/audio/shamse_intelligence_podcast.mp3" download class="wp-btn wp-btn-ghost" style="font-size:11px;padding:5px 10px">
                  📥 دانلود MP3
                </a>
                <a href="reports/shamse_sentiment_podcast_report.pdf" download class="wp-btn" style="background:#e74c3c;color:#fff;font-size:11px;padding:5px 10px">
                  📄 دانلود فایل PDF
                </a>
              </div>
            </div>

            <!-- Audio Elements -->
            <audio id="adminAudioPlayerFa" src="assets/audio/shamse_intelligence_podcast.mp3" preload="metadata"></audio>
            <audio id="adminAudioPlayerTr" src="assets/audio/shamse_intelligence_podcast_tr.mp3" preload="metadata"></audio>

            <!-- Progress Bar -->
            <div style="width:100%;height:8px;background:#252f36;border-radius:4px;cursor:pointer;position:relative;overflow:hidden;margin-bottom:8px" onclick="seekAdminPodcast(event)">
              <div id="adminAudioProgressBar" style="width:0%;height:100%;background:linear-gradient(90deg,var(--copper),#ffd21e);border-radius:4px"></div>
            </div>
            <div style="display:flex;justify-content:space-between;font-size:10px;color:var(--muted);font-family:monospace">
              <span id="adminAudioCurrTime">00:00</span>
              <span id="adminAudioTotalTime">01:05</span>
            </div>
          </div>

          <!-- TRANSCRIPTS BOX -->
          <div style="background:rgba(0,0,0,0.3);border:1px solid rgba(255,255,255,0.06);border-radius:6px;padding:12px;font-size:11.5px;line-height:1.7">
            <div id="transcriptFaBox">
              <b style="color:var(--gold)">📜 متن کامل پادکست فارسی:</b>
              <p style="color:var(--cream);margin:6px 0 0">
                «در پایش هفتگی ۵,۰۵۵ نقد در گوگل مپ، تریپ‌ادوایزر و یاندکس، شمسه با امتیاز ۴.۷۶ رتبه اول رستوران‌های تکسیم را حفظ کرده است. مهم‌ترین نقاط احساسی مثبت مشتریان، اصالت طعم قورمه‌سبزی و عطر زعفران کباب‌ها است. در عین حال، گردشگران اروپایی در تریپ‌ادوایزر ابهاماتی درباره رایگان بودن چای و نان داشته‌اند که با افزودن نشان چای رایگان ولکام (Welcome Tea) حل می‌شود. همچنین با میزبانی دورهمی‌های کلاب در ساعات خلوت ۱۴:۳۰ تا ۱۸:۳۰، شاخص RevPASH سالن تا ۵۸.۴ لیر جهش کرده و ماهانه +۱۸۴,۰۰۰ لیر سود خالص اضافی ایجاد می‌کند.»
              </p>
            </div>
            <div id="transcriptTrBox" style="display:none">
              <b style="color:#38bdf8">📜 Türkçe Podcast Metni (Turkish Transcript):</b>
              <p style="color:var(--cream);margin:6px 0 0;direction:ltr;text-align:left">
                “Mizban İstanbul ve Şemse Restoran Yönetim Kurulu için haftalık yapay zeka gastronomi brifingi. Google Maps, TripAdvisor ve Yandex üzerinde incelenen 5.055 misafir yorumuna göre, Şemse Restoran 4.76 puanla Taksim bölgesindeki liderliğini koruyor. Misafirlerimizin en yüksek memnuniyet duyduğu alanlar, geleneksel safranlı kebaplarımız ve otantik İran misafirperverliğidir. İstiklal Caddesi şubemizdeki yoğun saatlerde yaşanan pirinç gecikmesi, dinamik ön pişirme sistemiyle çözüme kavuşturuldu. Avrupalı turistler için ücretsiz ikram çayı kuver karmaşası netleştirildi ve Rus misafirlerimiz için Kiril alfabeli dijital menü devreye alındı. Kocatepe şubemizdeki canlı müzik geceleri ve saat 14:30 ile 17:30 arasındaki özel indirimler sayesinde aylık net 184.000 TL ek gelir sağlandı. Şemse, otantik lezzet ve yüksek teknolojiyle İstanbul'da fark yaratmaya devam ediyor.”
              </p>
            </div>
          </div>
        </div>

        <script>
          var currentAudioLang = 'fa';
          function switchAdminPodcastLang(lang) {
            currentAudioLang = lang;
            var playerFa = document.getElementById('adminAudioPlayerFa');
            var playerTr = document.getElementById('adminAudioPlayerTr');
            var btnFa = document.getElementById('btnPodcastFa');
            var btnTr = document.getElementById('btnPodcastTr');
            var title = document.getElementById('adminAudioTitle');
            var meta = document.getElementById('adminAudioMeta');
            var tFa = document.getElementById('transcriptFaBox');
            var tTr = document.getElementById('transcriptTrBox');
            var dLink = document.getElementById('adminAudioDownloadLink');
            var playBtn = document.getElementById('adminAudioPlayBtn');

            playerFa.pause();
            playerTr.pause();
            playBtn.innerText = '▶';

            if (lang === 'fa') {
              btnFa.className = 'wp-btn wp-btn-gold';
              btnTr.className = 'wp-btn wp-btn-ghost';
              title.innerText = 'پادکست فارسی هوش تجاری شمسه (Persian Audio Briefing)';
              meta.innerText = 'مدت: ۰۱:۰۵ • کیفیت: MP3 128kbps Stereo • گوینده: هوش مصنوعی فارسی';
              tFa.style.display = 'block';
              tTr.style.display = 'none';
              dLink.href = 'assets/audio/shamse_intelligence_podcast.mp3';
              document.getElementById('adminAudioTotalTime').innerText = '01:05';
            } else {
              btnTr.className = 'wp-btn wp-btn-gold';
              btnFa.className = 'wp-btn wp-btn-ghost';
              title.innerText = 'Şemse Restoran Türkçe Yönetici Brifingi (Turkish Audio Briefing)';
              meta.innerText = 'Süre: 01:20 • Kalite: MP3 128kbps Stereo • Seslendirme: Yapay Zeka Türkçe';
              tFa.style.display = 'none';
              tTr.style.display = 'block';
              dLink.href = 'assets/audio/shamse_intelligence_podcast_tr.mp3';
              document.getElementById('adminAudioTotalTime').innerText = '01:20';
            }
          }

          function toggleAdminPodcastPlay() {
            var activeAudio = currentAudioLang === 'fa' ? document.getElementById('adminAudioPlayerFa') : document.getElementById('adminAudioPlayerTr');
            var playBtn = document.getElementById('adminAudioPlayBtn');
            if (activeAudio.paused) {
              activeAudio.play();
              playBtn.innerText = '⏸';
            } else {
              activeAudio.pause();
              playBtn.innerText = '▶';
            }
          }

          function setupAdminAudioListeners() {
            ['Fa', 'Tr'].forEach(function(suffix) {
              var a = document.getElementById('adminAudioPlayer' + suffix);
              if (!a) return;
              a.ontimeupdate = function() {
                if ((suffix === 'Fa' && currentAudioLang !== 'fa') || (suffix === 'Tr' && currentAudioLang !== 'tr')) return;
                var pct = (a.currentTime / a.duration) * 100;
                document.getElementById('adminAudioProgressBar').style.width = pct + '%';
                var m = Math.floor(a.currentTime / 60);
                var s = Math.floor(a.currentTime % 60);
                document.getElementById('adminAudioCurrTime').innerText = (m < 10 ? '0' + m : m) + ':' + (s < 10 ? '0' + s : s);
              };
              a.onended = function() {
                document.getElementById('adminAudioPlayBtn').innerText = '▶';
                document.getElementById('adminAudioProgressBar').style.width = '0%';
              };
            });
          }
          document.addEventListener('DOMContentLoaded', setupAdminAudioListeners);
        </script>
    """
    return html

def patch_admin_panel():
    with open(ADMIN_PANEL_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    candlestick_html = build_candlestick_and_hightech_easyfix_html()
    podcast_html = build_bilingual_podcast_widget_html()

    # درج کامپوننت‌ها درون tab-jarchi-menu قبل از <!-- SECTION 1: 10 STREET BARKER SLOGANS -->
    target = '<!-- SECTION 1: 10 STREET BARKER SLOGANS -->'
    if "Forex-Style Candlestick Sentiment v2.4" not in html and target in html:
        combined_addition = podcast_html + "\n\n" + candlestick_html + "\n\n        " + target
        html = html.replace(target, combined_addition, 1)
        print("Admin panel patched with Candlestick Chart & Bilingual Podcast.")

    # افزودن دکمه پادکست ترکی به دانلودهای هدر ادمین
    if "shamse_intelligence_podcast_tr.mp3" not in html:
        target_dl = '<a href="assets/audio/shamse_intelligence_podcast.mp3" download class="wp-btn wp-btn-ghost"'
        replacement = '<a href="assets/audio/shamse_intelligence_podcast_tr.mp3" download class="wp-btn wp-btn-ghost" style="border-color:#38bdf8;color:#38bdf8">🎙️ پادکست ترکی (Türkçe)</a>\n            ' + target_dl
        html = html.replace(target_dl, replacement, 1)

    with open(ADMIN_PANEL_PATH, "w", encoding="utf-8") as f:
        f.write(html)


def patch_web_dossier():
    """افزودن امکان پادکست ترکی و چارت کندل‌استیک به پرونده وب shamse_sentiment_report.html"""
    with open(WEB_DOSSIER_PATH, "r", encoding="utf-8") as f:
        html = f.read()

    # افزودن دکمه پادکست ترکی
    if "shamse_intelligence_podcast_tr.mp3" not in html:
        target_dl = '<a href="assets/audio/shamse_intelligence_podcast.mp3" download class="btn btn--ghost" style="font-size:.72rem;padding:4px 8px">'
        replacement = '<a href="assets/audio/shamse_intelligence_podcast_tr.mp3" download class="btn btn--ghost" style="font-size:.72rem;padding:4px 8px;border-color:#38bdf8;color:#38bdf8">🇹🇷 پادکست ترکی (Türkçe)</a>\n            ' + target_dl
        html = html.replace(target_dl, replacement, 1)

    # افزودن چارت کندل‌استیک بالای گالری اسکرین‌شات‌ها
    candlestick_embed = f"""
    <!-- FOREX CANDLESTICK SENTIMENT CHART -->
    <div class="card" style="margin-bottom:28px;border:1.5px solid #3498db;background:#14171a">
      <div style="display:flex;justify-content:space-between;align-items:center;flex-wrap:wrap;gap:10px;margin-bottom:12px;border-bottom:1px solid #252f36;padding-bottom:10px">
        <div>
          <span class="badge" style="background:#3498db;color:#fff">تحلیل تکنیکال فارکس احساسات (Forex Candlestick Sentiment)</span>
          <h3 style="margin:4px 0 0;color:#fff;font-size:1.05rem">📈 نوسان امتیاز شمسه در ۶ شیفت حساس به همراه تاریخ‌های دوگانه شمسی و میلادی</h3>
        </div>
        <span class="badge" style="background:#2ecc71;color:#000;font-weight:bold">★ ۴٫۷۶ ریتینگ بسته شده</span>
      </div>
      <div style="overflow-x:auto">
        {candlestick_svg}
      </div>
    </div>
    """
    if "تحلیل تکنیکال فارکس احساسات" not in html:
        target_card = '<h5 style="color:var(--copper-bright);font-size:.95rem;margin:16px 0 10px 0;font-weight:800">'
        if target_card in html:
            html = html.replace(target_card, candlestick_embed + "\n          " + target_card, 1)

    with open(WEB_DOSSIER_PATH, "w", encoding="utf-8") as f:
        f.write(html)
    print("shamse_sentiment_report.html patched with Turkish podcast link and Candlestick Chart.")


def patch_pdf_generator():
    """افزودن پادکست ترکی و ردیف مقایسه های‌تک در برابر فیکس سریع به گزارش PDF"""
    with open(PDF_GEN_PATH, "r", encoding="utf-8") as f:
        content = f.read()

    if "shamse_intelligence_podcast_tr.mp3" not in content:
        target_farsi = '• <b>فایل صوتی پادکست (MP3):</b> در مسیر <code>assets/audio/shamse_intelligence_podcast.mp3</code> (مدت: ۱ دقیقه و ۵ ثانیه)<br>'
        replacement = target_farsi + '\n    • <b>فایل صوتی پادکست ترکی استانبولی (Türkçe MP3):</b> در مسیر <code>assets/audio/shamse_intelligence_podcast_tr.mp3</code> (مدت: ۱ دقیقه و ۲۰ ثانیه - خلاصه هیئت مدیره به ترکی)<br>'
        content = content.replace(target_farsi, replacement, 1)

    with open(PDF_GEN_PATH, "w", encoding="utf-8") as f:
        f.write(content)
    print("generate_shamse_dossier_pdf.py patched with Turkish podcast briefing.")


if __name__ == "__main__":
    patch_admin_panel()
    patch_web_dossier()
    patch_pdf_generator()
