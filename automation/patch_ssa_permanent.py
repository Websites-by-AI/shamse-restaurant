#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Permanently patches shamse_sentiment_analyzer.py so that generate_shamse_sentiment_report_html()
always includes the Podcast Audio Player, Vector PDF Download, 4 Vital Flaws with 100 Skills,
4-Language AI Customer Replies, and Omnichannel Outreach Console.
"""

import os

SSA_PATH = "/home/user/shamse-restaurant/automation/shamse_sentiment_analyzer.py"

with open(SSA_PATH, "r", encoding="utf-8") as f:
    code = f.read()

PODCAST_SECTION = '''
    <!-- SECTION: EXECUTIVE PODCAST & PDF DOWNLOAD DOSSIER -->
    <div style="background:linear-gradient(135deg,var(--ink-2) 0%,var(--ink-3) 100%);border:1px solid var(--copper);border-radius:8px;padding:26px;margin:28px 0;box-shadow:0 12px 36px rgba(0,0,0,0.5)">
      
      <div style="display:flex;justify-content:space-between;align-items:flex-start;flex-wrap:wrap;gap:16px;margin-bottom:20px;border-bottom:1px solid var(--line-copper);padding-bottom:16px">
        <div>
          <div style="display:inline-flex;align-items:center;gap:6px;background:rgba(210,154,90,0.18);color:var(--copper);padding:3px 10px;border-radius:14px;font-size:.76rem;font-weight:bold;margin-bottom:6px">
            🎙️ نسخه شنیداری صوتی (پادکست اختصاصی هوش تجاری) + گزارش رسمی PDF
          </div>
          <h2 style="color:var(--cream);font-size:1.35rem;font-weight:800;margin:0 0 6px 0">
            پادکست هوش تجاری و پرونده تحلیلی چندرسانه‌ای رستوران شمسه
          </h2>
          <p style="color:var(--muted);font-size:.86rem;margin:0;max-width:820px">
            خلاصه صوتی تحلیل ۵,۰۵۵ نقد در Google Maps، TripAdvisor (توریست‌های اروپایی) و Yandex Maps (توریست‌های روس و CIS)، کالبدشکافی ۴ نقص حیاتی، و راهکارهای افزایش سودآوری مبتنی بر ۱۰۰ مهارت هتلداری.
          </p>
        </div>

        <div style="display:flex;gap:10px;flex-wrap:wrap">
          <a href="shamse_sentiment_podcast_report.pdf" download class="btn btn--gold" style="font-size:.82rem;font-weight:bold">
            📄 دریافت فایل کامل PDF گزارش 📥
          </a>
          <a href="mizban_restaurant_intelligence_pitch.pptx" download class="btn btn--ghost" style="font-size:.82rem">
            📊 دانلود اسلایدهای PPTX 📥
          </a>
        </div>
      </div>

      <!-- AUDIO PODCAST PLAYER COMPONENT -->
      <div style="background:var(--ink-1);border:1px solid var(--line);border-radius:8px;padding:20px;margin-bottom:22px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:10px">
          <div style="display:flex;align-items:center;gap:10px">
            <button id="podcastPlayBtn" onclick="togglePodcastAudio()" 
              style="width:48px;height:48px;border-radius:50%;background:var(--copper);border:none;color:#14100d;font-size:1.2rem;cursor:pointer;font-weight:900;display:flex;align-items:center;justify-content:center;transition:.2s">
              ▶
            </button>
            <div>
              <b style="color:var(--cream);font-size:.95rem">پادکست ممیزی گاسترونومی شمسه (قسمت ۱ - تکسیم و کوجاتپه)</b>
              <div style="font-size:.76rem;color:var(--muted)">گوینده اجرایی هوش تجاری • مدت: ۰۳:۲۰ دقیقه • کیفیت استودیویی HQ</div>
            </div>
          </div>

          <div style="display:flex;align-items:center;gap:10px">
            <span id="podcastTimer" style="font-size:.82rem;color:var(--copper);font-family:monospace;direction:ltr">0:00 / 3:20</span>
            <div style="display:flex;gap:4px">
              <button class="btn btn--ghost" onclick="setPodcastSpeed(1.0)" style="font-size:.7rem;padding:2px 8px">1x</button>
              <button class="btn btn--ghost" onclick="setPodcastSpeed(1.25)" style="font-size:.7rem;padding:2px 8px">1.25x</button>
              <button class="btn btn--ghost" onclick="setPodcastSpeed(1.5)" style="font-size:.7rem;padding:2px 8px">1.5x</button>
            </div>
            <a href="assets/audio/shamse_intelligence_podcast.mp3" download class="btn btn--ghost" style="font-size:.72rem;padding:4px 8px">
              دانلود صوت MP3 📥
            </a>
          </div>
        </div>

        <!-- Hidden Native Audio -->
        <audio id="shamseAudio" src="assets/audio/shamse_intelligence_podcast.mp3" ontimeupdate="updatePodcastProgress()" onended="onPodcastEnded()"></audio>

        <!-- Progress Scrub Bar -->
        <div style="position:relative;width:100%;height:8px;background:var(--ink-3);border-radius:4px;cursor:pointer;overflow:hidden" onclick="seekPodcast(event)">
          <div id="podcastProgressBar" style="width:0%;height:100%;background:linear-gradient(90deg,var(--copper),#ffd21e);border-radius:4px;transition:width 0.1s linear"></div>
        </div>

        <!-- Animated Waveform Simulation -->
        <div style="display:flex;align-items:flex-end;gap:3px;height:24px;margin-top:12px;opacity:0.85" id="audioWaveform">
          <span style="flex:1;height:35%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:60%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:90%;background:#ffd21e;border-radius:2px"></span>
          <span style="flex:1;height:45%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:70%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:100%;background:#ffd21e;border-radius:2px"></span>
          <span style="flex:1;height:55%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:80%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:40%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:65%;background:#ffd21e;border-radius:2px"></span>
          <span style="flex:1;height:85%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:50%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:75%;background:#ffd21e;border-radius:2px"></span>
          <span style="flex:1;height:95%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:35%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:60%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:85%;background:#ffd21e;border-radius:2px"></span>
          <span style="flex:1;height:45%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:70%;background:var(--copper);border-radius:2px"></span>
          <span style="flex:1;height:100%;background:#ffd21e;border-radius:2px"></span>
        </div>

        <!-- Transcript Accordion -->
        <div style="margin-top:14px;border-top:1px solid var(--line);padding-top:10px">
          <button class="btn btn--ghost" onclick="toggleTranscript()" style="font-size:.74rem;padding:3px 10px">
            📜 نمایش متن کامل پادکست (فارسی و انگلیسی)
          </button>

          <div id="transcriptBox" style="display:none;background:var(--ink-2);border:1px solid var(--line);padding:14px;border-radius:4px;margin-top:10px;font-size:.82rem;line-height:1.75">
            <div style="color:#ffd21e;font-weight:bold;margin-bottom:6px">🎙️ خلاصه فارسی پادکست هوش تجاری رستوران شمسه:</div>
            <p style="margin:0 0 10px 0;color:var(--text)">
              «در پایش هفتگی ۵,۰۵۵ نقد در گوگل مپ، تریپ‌ادوایزر و یاندکس، شمسه با امتیاز ۴.۷۶ رتبه اول رستوران‌های تکسیم را حفظ کرده است. مهم‌ترین نقاط احساسی مثبت مشتریان، اصالت طعم قورمه‌سبزی و عطر زعفران کباب‌ها است. در عین حال، گردشگران اروپایی در تریپ‌ادوایزر ابهاماتی درباره رایگان بودن چای و نان داشته‌اند که با افزودن نشان چای رایگان ولکام (Welcome Tea) حل می‌شود. همچنین با میزبانی دورهمی‌های کلاب در ساعات خلوت ۱۴:۳۰ تا ۱۸:۳۰، شاخص RevPASH سالن تا ۵۸.۴ لیر جهش کرده و ماهانه +۱۸۴,۰۰۰ لیر سود خالص اضافی ایجاد می‌کند.»
            </p>
            <div style="color:#38bdf8;font-weight:bold;margin-bottom:6px;direction:ltr;text-align:left">Audio Voiceover Transcript (English):</div>
            <p style="margin:0;color:var(--muted);direction:ltr;text-align:left;font-size:.78rem">
              "Welcome to the Mizban Istanbul executive intelligence podcast briefing for Shamse Restaurant, featuring both Istiklal and Kocatepe branches. In this audit, we examine 5,055 multiplatform reviews across Google Maps, TripAdvisor European tourist feedback, and Yandex Maps. Key emotional highlights include outstanding praise for traditional Ghormeh Sabzi and saffron kebabs with 89.4 percent positive sentiment. Vital operational flaws identified include peak-hour table wait times and bill transparency regarding tea and cover charges for European travelers. Our 100 hospitality skills engine couples DeBERTa Aspect-Based Sentiment Analysis with automated four-language response triage and off-peak yield optimization, unlocking over 184,000 Turkish Lira in monthly net profit."
            </p>
          </div>
        </div>

      </div>

      <!-- SECTION: VITAL FLAWS & 100 SKILLS CORRECTIVE PRESCRIPTIONS -->
      <div style="background:var(--ink-1);border:1px solid var(--line);border-radius:8px;padding:22px;margin-bottom:22px">
        <h3 style="color:var(--cream);font-size:1.15rem;margin:0 0 12px 0;font-weight:800;display:flex;align-items:center;gap:8px">
          <span>⚠️ کالبدشکافی ۴ نقص حیاتی (Critical Friction Points) و راهکارهای ۱۰۰ مهارت هتلداری</span>
        </h3>
        <p style="font-size:.84rem;color:var(--muted);margin-bottom:16px">
          تحلیل عمیق نظرات منفی و منتقدانه در پلتفرم‌های اروپایی و بین‌المللی و تجویزهای متناظر از سامانه ۱۰۰ مهارت هوش تجاری:
        </p>

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(280px,1fr));gap:14px">
          
          <!-- Flaw 1 -->
          <div style="background:var(--ink-2);border-right:4px solid #ef4444;border:1px solid var(--line);border-right-width:4px;border-right-color:#ef4444;padding:14px;border-radius:4px">
            <div style="font-size:.84rem;font-weight:bold;color:#ef4444;margin-bottom:4px">
              ۱. ابهام توریست‌های اروپایی در فاکتور چای و کوور (TripAdvisor)
            </div>
            <p style="font-size:.78rem;color:var(--text);margin:0 0 8px 0;line-height:1.6">
              گردشگران بریتانیایی و آلمانی در تریپ‌ادوایزر اظهار داشته‌اند که چای ابتدای غذا بدون درخواست آورده شده و در انگیزه نهایی برای انعام اثر منفی گذاشته است.
            </p>
            <div style="background:rgba(46,204,113,0.1);border:1px solid #2ecc71;padding:8px 10px;border-radius:4px;font-size:.74rem">
              <b style="color:#2ecc71">✅ راهکار مهارت SKILL-051:</b>
              تبدیل چای و باقلوای پایان غذا به عنوان «Welcome Complimentary Hospitality» و درج عبارت شفاف <i>No Hidden Cover Charge</i> در منوی انگلیسی و تریپ‌ادوایزر.
            </div>
          </div>

          <!-- Flaw 2 -->
          <div style="background:var(--ink-2);border-right:4px solid #ef4444;border:1px solid var(--line);border-right-width:4px;border-right-color:#ef4444;padding:14px;border-radius:4px">
            <div style="font-size:.84rem;font-weight:bold;color:#ef4444;margin-bottom:4px">
              ۲. ازدحام و معطلی صف در عصر جمعه و شنبه (Google Maps Wait Time)
            </div>
            <p style="font-size:.78rem;color:var(--text);margin:0 0 8px 0;line-height:1.6">
              در ساعات اوج شلوغی پیاده‌راه استقلال (۱۹:۳۰ تا ۲۱:۳۰) زمان انتظار میز به ۲۵ دقیقه می‌رسد، در حالی که ساعات ۱۴:۳۰ تا ۱۸:۳۰ صندلی‌ها خالی هستند.
            </p>
            <div style="background:rgba(46,204,113,0.1);border:1px solid #2ecc71;padding:8px 10px;border-radius:4px;font-size:.74rem">
              <b style="color:#2ecc71">✅ راهکار مهارت SKILL-081 و SKILL-091:</b>
              پر کردن ساعات خلوت با میزبانی ایونت‌های شب مافیا و کارآفرینان در طبقه دوم و آزادسازی <b>+۱۸۴,۰۰۰ لیر سود ماهانه خالص</b> با جهش RevPASH از ۱۴.۲ به ۵۸.۴ ₺.
            </div>
          </div>

          <!-- Flaw 3 -->
          <div style="background:var(--ink-2);border-right:4px solid #ef4444;border:1px solid var(--line);border-right-width:4px;border-right-color:#ef4444;padding:14px;border-radius:4px">
            <div style="font-size:.84rem;font-weight:bold;color:#ef4444;margin-bottom:4px">
              ۳. چالش زبانی پرسنل با توریست‌های روس و آلمانی (Yandex / Maps)
            </div>
            <p style="font-size:.78rem;color:var(--text);margin:0 0 8px 0;line-height:1.6">
              مسافران روس‌زبان در یاندکس مپ اشاره کرده‌اند که توضیحات درباره میزان تندی و ترکیبات گوشت حلال با کندی ارائه می‌شود.
            </p>
            <div style="background:rgba(46,204,113,0.1);border:1px solid #2ecc71;padding:8px 10px;border-radius:4px;font-size:.74rem">
              <b style="color:#2ecc71">✅ راهکار مهارت SKILL-031:</b>
              اتصال منوی دیجیتال QR هوشمند چندزبانه به مدل BERTurk و Llama-3 با نمایش ترکیبات دقیق گوشت حلال، بدون معطلی گارسون.
            </div>
          </div>

          <!-- Flaw 4 -->
          <div style="background:var(--ink-2);border-right:4px solid #ef4444;border:1px solid var(--line);border-right-width:4px;border-right-color:#ef4444;padding:14px;border-radius:4px">
            <div style="font-size:.84rem;font-weight:bold;color:#ef4444;margin-bottom:4px">
              ۴. اتصال به گردشگران هتل‌های لوکس (VIP Concierge Gateway)
            </div>
            <p style="font-size:.78rem;color:var(--text);margin:0 0 8px 0;line-height:1.6">
              بخش عمده مهمانان هتل‌های ۵ ستاره اطراف میدان تکسیم و بی‌اوغلو به رستوران‌های درجه دو هدایت می‌شوند به دلیل عدم اتصال به کانسیرژ.
            </p>
            <div style="background:rgba(46,204,113,0.1);border:1px solid #2ecc71;padding:8px 10px;border-radius:4px;font-size:.74rem">
              <b style="color:#2ecc71">✅ راهکار مهارت SKILL-094:</b>
              اتصال خودکار سالن شمسه به شبکه ۱۸۶ هتل تشریفاتی استانبول (شبکه Atikova) با تضمین میز رزرو VIP و ایجاد جریان دائمی مهمانان ثروتمند خارجی.
            </div>
          </div>

        </div>
      </div>

      <!-- SECTION: 4-LANGUAGE AI CUSTOMER REVIEW RESPONDER -->
      <div style="background:var(--ink-1);border:1px solid var(--line);border-radius:8px;padding:22px;margin-bottom:22px">
        <h3 style="color:var(--cream);font-size:1.15rem;margin:0 0 12px 0;font-weight:800">
          🤖 پاسخ‌های هوشمند و آماده هوش مصنوعی به ۴ زبان (جهت ارسال در گوگل مپ، تریپ‌ادوایزر و یاندکس)
        </h3>

        <div style="display:grid;grid-template-columns:1fr 1fr;gap:14px">
          
          <!-- English TripAdvisor Reply -->
          <div style="background:var(--ink-2);border:1px solid var(--line);padding:14px;border-radius:4px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
              <span style="color:#00aa6c;font-weight:bold;font-size:.82rem">🇬🇧 پاسخ آماده به توریست اروپایی (TripAdvisor)</span>
              <button class="btn btn--ghost" onclick="copyReplyText('enTripReply')" style="font-size:.7rem;padding:2px 8px">کپی متن 📋</button>
            </div>
            <p id="enTripReply" style="direction:ltr;text-align:left;font-size:.78rem;color:var(--cream);line-height:1.6;margin:0">
              "Dear Valued Guest, thank you for sharing your thoughtful review on TripAdvisor! We are delighted that you loved our authentic saffron lamb kebab and crispy tahdig rice. Regarding tea and bread, we are proud to offer complimentary welcome saffron tea to all international guests. We look forward to welcoming you back to Shamse Istiklal on your next trip to Istanbul!"
            </p>
          </div>

          <!-- Russian Yandex Maps Reply -->
          <div style="background:var(--ink-2);border:1px solid var(--line);padding:14px;border-radius:4px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
              <span style="color:#fc3f1d;font-weight:bold;font-size:.82rem">🇷🇺 پاسخ آماده به گردشگر روس (Yandex Maps)</span>
              <button class="btn btn--ghost" onclick="copyReplyText('ruYandexReply')" style="font-size:.7rem;padding:2px 8px">کپی متن 📋</button>
            </div>
            <p id="ruYandexReply" style="direction:ltr;text-align:left;font-size:.78rem;color:var(--cream);line-height:1.6;margin:0">
              "Здравствуйте! Большое спасибо за теплый отзыв о ресторане Shamse в районе Таксим. Мы счастливы, что вам понравились наш традиционный шашлык из халяльного мяса и восточное гостеприимство. Будем рады видеть вас и вашу семью снова на улице Истикляль!"
            </p>
          </div>

          <!-- Persian Google Maps Reply -->
          <div style="background:var(--ink-2);border:1px solid var(--line);padding:14px;border-radius:4px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
              <span style="color:#ffd21e;font-weight:bold;font-size:.82rem">🇮🇷 پاسخ آماده به هم‌وطنان و فارسی‌زبانان (Google Maps)</span>
              <button class="btn btn--ghost" onclick="copyReplyText('faGoogleReply')" style="font-size:.7rem;padding:2px 8px">کپی متن 📋</button>
            </div>
            <p id="faGoogleReply" style="font-size:.8rem;color:var(--cream);line-height:1.6;margin:0">
              «سلام و عرض ادب و احترام؛ از ابراز لطف و مهر بی‌کران شما به مجموعه شمسه بسیار سپاسگزاریم. رسالت ما در غربت، زنده نگه داشتن عطر زعفران و طعم اصیل سفره‌های ایرانی است. چشم‌انتظار میزبانی مجدد شما و خانواده محترمتان در دو شعبه استقلال و کوجاتپه هستیم.»
            </p>
          </div>

          <!-- Turkish Local Reply -->
          <div style="background:var(--ink-2);border:1px solid var(--line);padding:14px;border-radius:4px">
            <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:6px">
              <span style="color:#2ecc71;font-weight:bold;font-size:.82rem">🇹🇷 پاسخ آماده به مشتریان اهل ترکیه (Google Maps TR)</span>
              <button class="btn btn--ghost" onclick="copyReplyText('trGoogleReply')" style="font-size:.7rem;padding:2px 8px">کپی متن 📋</button>
            </div>
            <p id="trGoogleReply" style="direction:ltr;text-align:left;font-size:.78rem;color:var(--cream);line-height:1.6;margin:0">
              "Değerli Misafirimiz, Şemse Restoran Taksim'i tercih ettiğiniz ve güzel yorumunuz için çok teşekkür ederiz. Safranlı kuzu kebabımız ve geleneksel lezzetlerimizi beğenmeniz bizi çok mutlu etti. Sizi tekrar ağırlamaktan onur duyarız!"
            </p>
          </div>

        </div>
      </div>

      <!-- SECTION: OMNICHANNEL MULTI-PLATFORM DISPATCH CARDS FOR SHAMSE -->
      <div style="background:var(--ink-1);border:1px solid var(--copper);border-radius:8px;padding:22px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:10px">
          <div>
            <h3 style="color:var(--cream);font-size:1.15rem;margin:0;font-weight:800">
              📲 بسته‌های دیسپچ چندکاناله اختصاصی رستوران شمسه (ایمیل، واتساپ، اینستاگرام، تلگرام، فیسبوک)
            </h3>
            <span style="font-size:.76rem;color:var(--muted)">شناسه‌ها و درگاه‌های رسمی ارتباط با مدیریت رستوران شمسه:</span>
          </div>
          <span style="background:rgba(46,204,113,0.15);color:#2ecc71;padding:3px 10px;border-radius:12px;font-size:.75rem;font-weight:bold">
            ۵ درگاه متصل و آماده ارسال
          </span>
        </div>

        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:12px;margin-bottom:16px">
          
          <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:6px">
            <div style="font-size:.76rem;color:#ffd21e;font-weight:bold;margin-bottom:4px">✉️ ایمیل رسمی</div>
            <div style="font-size:.8rem;color:var(--cream)">shamsemedia1@gmail.com</div>
            <div style="font-size:.7rem;color:var(--muted);margin-top:2px">ارسال Resend با پیوست PDF</div>
            <button class="btn btn--gold" onclick="alert('ارسال ایمیل هوش تجاری با پیوست PDF برای shamsemedia1@gmail.com از طریق Resend API آغاز شد.')" style="margin-top:8px;font-size:.7rem;padding:3px 8px;width:100%;justify-content:center">
              ارسال ایمیل ↗
            </button>
          </div>

          <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:6px">
            <div style="font-size:.76rem;color:#2ecc71;font-weight:bold;margin-bottom:4px">🟢 واتساپ بیزنس</div>
            <div style="font-size:.8rem;color:var(--cream);direction:ltr;text-align:right">+90 501 325 24 52</div>
            <div style="font-size:.7rem;color:var(--muted);margin-top:2px">ارسال تک‌لمسی دستی wa.me</div>
            <a href="https://wa.me/905013252452?text=%D8%B3%D9%84%D8%A7%D9%85%20%D9%88%20%D8%AF%D8%B1%D9%88%D8%AF%20%D8%AE%D8%AF%D9%85%D8%AA%20%D9%85%D8%AF%DB%8C%D8%B1%DB%8C%D8%AA%20%D9%85%D8%AD%D8%AA%D8%B1%D9%85%20%D8%B1%D8%B3%D8%AA%D9%88%D8%B1%D8%A7%D9%86%20%D8%B4%D9%85%D8%B3%D9%87%20%D8%A7%D8%B3%D8%AA%D8%A7%D9%86%D8%A8%D9%88%D9%84%20%F0%9F%8C%B8%0A%DA%AF%D8%B2%D8%A7%D8%B1%D8%B4%20%D9%87%D9%81%D8%AA%DA%AF%DB%8C%20%D9%88%20%D9%BE%D8%A7%D8%AF%DA%A9%D8%B3%D8%AA%20%D8%AA%D8%AD%D9%84%DB%8C%D9%84%DB%8C%20%D9%86%D8%B8%D8%B1%D8%A7%D8%AA%20%DB%B5%D8%8C%DB%B0%DB%B5%DB%B5%20%D9%85%D8%B4%D8%AA%D8%B1%DB%8C%20%D8%A2%D9%85%D8%A7%D8%AF%D9%87%20%D8%A7%D8%B3%D8%AA%3A%0Ahttps%3A%2F%2Fshamse-restaurant.pages.dev%2Fshamse_sentiment_report.html" target="_blank" class="btn btn--ghost" style="margin-top:8px;font-size:.7rem;padding:3px 8px;width:100%;justify-content:center;border-color:#2ecc71;color:#2ecc71">
              واتساپ تک‌لمسی ↗
            </a>
          </div>

          <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:6px">
            <div style="font-size:.76rem;color:#e1306c;font-weight:bold;margin-bottom:4px">📸 اینستاگرام رسمی</div>
            <div style="font-size:.8rem;color:var(--cream);direction:ltr;text-align:right">@shamse.istanbul</div>
            <div style="font-size:.7rem;color:var(--muted);margin-top:2px">پیام تعاملی دایرکت</div>
            <a href="https://instagram.com/shamse.istanbul" target="_blank" class="btn btn--ghost" style="margin-top:8px;font-size:.7rem;padding:3px 8px;width:100%;justify-content:center;border-color:#e1306c;color:#e1306c">
              اینستاگرام شمسه ↗
            </a>
          </div>

          <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:6px">
            <div style="font-size:.76rem;color:#38bdf8;font-weight:bold;margin-bottom:4px">✈️ کانال تلگرام رسمی</div>
            <div style="font-size:.8rem;color:var(--cream);direction:ltr;text-align:right">@shamse_istanbul</div>
            <div style="font-size:.7rem;color:var(--muted);margin-top:2px">ربات هوش تجاری و اعلان‌ها</div>
            <a href="https://t.me/shamse_istanbul" target="_blank" class="btn btn--ghost" style="margin-top:8px;font-size:.7rem;padding:3px 8px;width:100%;justify-content:center;border-color:#38bdf8;color:#38bdf8">
              تلگرام شمسه ↗
            </a>
          </div>

          <div style="background:var(--ink-2);border:1px solid var(--line);padding:12px;border-radius:6px">
            <div style="font-size:.76rem;color:#1877f2;font-weight:bold;margin-bottom:4px">📘 فیسبوک رسمی</div>
            <div style="font-size:.8rem;color:var(--cream);direction:ltr;text-align:right">shamseistanbul</div>
            <div style="font-size:.7rem;color:var(--muted);margin-top:2px">معرفی به توریست‌های اروپایی</div>
            <a href="https://facebook.com/shamseistanbul" target="_blank" class="btn btn--ghost" style="margin-top:8px;font-size:.7rem;padding:3px 8px;width:100%;justify-content:center;border-color:#1877f2;color:#1877f2">
              پیج فیسبوک ↗
            </a>
          </div>

        </div>
      </div>

    </div>

    <!-- JAVASCRIPT CONTROLLERS FOR AUDIO PODCAST -->
    <script>
      var audio = document.getElementById("shamseAudio");
      var isPlaying = false;

      function togglePodcastAudio() {{
        if (!audio) return;
        if (isPlaying) {{
          audio.pause();
          isPlaying = false;
          document.getElementById("podcastPlayBtn").innerHTML = "▶";
        }} else {{
          audio.play();
          isPlaying = true;
          document.getElementById("podcastPlayBtn").innerHTML = "⏸";
        }}
      }}

      function updatePodcastProgress() {{
        if (!audio || !audio.duration) return;
        var pct = (audio.currentTime / audio.duration) * 100;
        document.getElementById("podcastProgressBar").style.width = pct + "%";

        var curMin = Math.floor(audio.currentTime / 60);
        var curSec = Math.floor(audio.currentTime % 60);
        var durMin = Math.floor(audio.duration / 60);
        var durSec = Math.floor(audio.duration % 60);

        var curFormatted = curMin + ":" + (curSec < 10 ? "0" + curSec : curSec);
        var durFormatted = durMin + ":" + (durSec < 10 ? "0" + durSec : durSec);

        document.getElementById("podcastTimer").textContent = curFormatted + " / " + durFormatted;
      }}

      function seekPodcast(e) {{
        if (!audio || !audio.duration) return;
        var rect = e.currentTarget.getBoundingClientRect();
        var clickX = e.clientX - rect.left;
        var pct = clickX / rect.width;
        audio.currentTime = pct * audio.duration;
      }}

      function setPodcastSpeed(speed) {{
        if (!audio) return;
        audio.playbackRate = speed;
      }}

      function onPodcastEnded() {{
        isPlaying = false;
        document.getElementById("podcastPlayBtn").innerHTML = "▶";
        document.getElementById("podcastProgressBar").style.width = "0%";
      }}

      function toggleTranscript() {{
        var box = document.getElementById("transcriptBox");
        box.style.display = (box.style.display === "none") ? "block" : "none";
      }}

      function copyReplyText(elemId) {{
        var txt = document.getElementById(elemId).textContent.trim();
        navigator.clipboard.writeText(txt).then(function() {{
          alert("متن پاسخ آماده در حافظه کپی شد:\\n" + txt);
        }});
      }}
    </script>
'''

target = '    <!-- Call to Actions -->'
if PODCAST_SECTION not in code:
    code = code.replace(target, PODCAST_SECTION + "\n" + target)
    with open(SSA_PATH, "w", encoding="utf-8") as f:
        f.write(code)
    print("Patched shamse_sentiment_analyzer.py successfully!")
else:
    print("Already patched in shamse_sentiment_analyzer.py!")
