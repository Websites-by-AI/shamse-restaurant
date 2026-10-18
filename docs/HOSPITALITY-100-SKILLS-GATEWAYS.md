# 🌐 سامانه گیت‌وی‌های چندکاناله و ۱۰۰ مهارت هوش تجاری و شهرت آنلاین رستوران‌ها
## (Omnichannel Gateways & 100 Hospitality Intelligence Skills)

این سند مرجع جامع معماری نرم‌افزاری، پایپ‌لاین‌های دریافت داده از شبکه‌های اجتماعی و **۱۰۰ مهارت عملیاتی هوش تجاری و مدیریت شهرت آنلاین** برای رستوران‌های ایرانی، فارسی و افغانستانی در استانبول است.

---

## 📡 ۱. معماری گیت‌وی‌های دریافت نظرات و شبکه‌های اجتماعی (Omnichannel Gateways)

پلتفرم از یک معماری چندگانه (Hybrid Webhook + Polling) برای اتصال به ۸ پلتفرم کلیدی استفاده می‌کند:

| نام گیت‌وی | پروتکل ارتباطی | فراوانی دریافت (Ingestion) | پشتیبانی از پاسخ ۲ طرفه | کانال‌های تحت پوشش |
|---|---|---|---|---|
| **Google Maps & GBP** | REST + Google Cloud Pub/Sub Webhook | آنی (Push) + پشتیبان ۶ ساعته | بله (API Reply) | Google Maps, Local 3-Pack, Google Search |
| **Yandex Maps & Sprav** | REST + Yandex Org Parser | هر ۴ ساعت | بله (Sprav Cabinet) | Yandex Maps, Yandex Navigator |
| **Meta Instagram Graph** | Graph API v20.0 + Webhooks | لحظه‌ای (Real-time) | بله (Comments & DM) | Reels, Posts, Stories, Direct Messages |
| **Meta Facebook Page** | Graph API v20.0 Webhooks | لحظه‌ای | بله (Review Reply) | Page Recommendations, Reviews, Feed |
| **Tripadvisor Content** | REST Partner Content API | روزانه | خیر (پورتال مستقیم) | رتبه‌بندی رستوران‌های بیواوغلو و استانبول |
| **Turkish Food Delivery** | Partner Portal API / Webhook | هر ۲ ساعت در شیفت کاری | بله | Yemeksepeti, Trendyol Yemek, GetirYemek |
| **In-Venue QR & Web** | Fast HTTP Webhook (`/api/feedback/qr`) | آنی حین اسکن سر میز | بله (پیامک/تلگرام) | کیوآرکد روی میز، فرم آنلاین سایت |
| **Telegram Bot Concierge** | Telegram Bot API Webhook | آنی | بله (چت مستقیم کاربر) | بات @shamse_restaurant_bot، نظرسنجی بعد از غذا |

---

## 🏛 ۲. ماتریس کامل ۱۰۰ مهارت هوش تجاری در ۱۰ خوشه تخصصی

### ۱. گیت‌وی‌ها و تجمیع داده‌های چندکاناله (Omnichannel Gateways)
*اتصال مستقیم، وب‌هوک و دریافت لحظه‌ای نظرات از گوگل مپ، یاندکس، اینستاگرام، فیسبوک، تریپ‌ادوایزر و سایت اختصاصی.*

| کد مهارت | نام فارسی و انگلیسی | ابزار / موتور هوش مصنوعی | شرط فعال‌سازی (Trigger) | اقدام عملیاتی (Action) |
|---|---|---|---|---|
| **SKILL-001** | اتصال وب‌هوک گوگل بیزینس (GBP Realtime Webhook)<br>*Google Business Profile Real-time Webhook* | `Google Cloud Pub/Sub + GBP API v4` | زمان دریافت نظر جدید در گوگل مپ | بررسی بلافاصله امتیاز، ایجاد تیکت بررسی و محاسبه SLA پاسخ |
| **SKILL-002** | همگام‌سازی دوره‌ای Google Places API v1<br>*Google Places API v1 Batch Ingestion* | `Google Places API v1 / New Place Details` | اجرای خودکار هر ۶ ساعت | تطبیق دیتابیس داخلی و شناسایی نظرات ویرایش‌شده یا حذف‌شده |
| **SKILL-003** | گیت‌وی پایش و استخراج نظرات یاندکس (Yandex Sprav)<br>*Yandex Maps & Sprav Review Harvester* | `Yandex Sprav API + Org Harvester` | هر ۴ ساعت یک‌بار | استخراج متن نظر، پاسخ‌های رسمی صاحب کسب‌وکار و امتیاز ستاره‌ای |
| **SKILL-004** | گیت‌وی کامنت‌های اینستاگرام (Instagram Graph API)<br>*Instagram Graph API Comments & Media* | `Meta Graph API v20 /instagram_business_account` | وب‌هوک زنده وب‌هوک Meta | ثبت متن کامنت، نام کاربری و استخراج حس اولیه |
| **SKILL-005** | رصد منشن‌ها و تگ‌های اینستاگرام (Mention & Tag Listening)<br>*Instagram Mention & Tag Ingestion* | `Instagram Graph API /mentioned_comment & /tags` | اعلان رویداد Mention در اینستاگرام | تحلیل محتوای استوری یا پست و ارسال پیام تشکر یا بازنشر |
| **SKILL-006** | گیت‌وی رتبه‌بندی و نظرات فیسبوک (Facebook Page Reviews)<br>*Facebook Page Ratings & Recommendations* | `Facebook Graph API /{page-id}/ratings` | وب‌هوک Ratings فیسبوک | ارزیابی توصیه (Recommended/Not Recommended) و ایجاد پیش‌نویس پاسخ |
| **SKILL-007** | گیت‌وی نظرات تریپ‌ادوایزر (Tripadvisor Content API)<br>*Tripadvisor Review Harvester* | `Tripadvisor Partner API /location/{id}/reviews` | پولینگ روزانه | بررسی جایگاه رستوران در رتبه‌بندی Beyoglu / Istanbul |
| **SKILL-008** | گیت‌وی نظرات پلتفرم‌های دلیوری ترکی (Yemeksepeti & Trendyol)<br>*Turkish Delivery Portals Review Ingestion* | `Merchant Portal Ingestion Gateway` | هر ۲ ساعت در شیفت کاری | هشدار فوری در صورت نشت غذا، سردی یا جا افتادن نان و سالاد |
| **SKILL-009** | گیت‌وی نظرسنجی کیوآرکد روی میز و سایت (QR & Direct Web)<br>*In-Venue QR & Direct Website Review Gateway* | `FastAPI Webhook /api/feedback/qr` | اسکن فوری کیوآرکد حین پرداخت یا انتظار | فیلتر نارضایتی سر میز و حل مشکل توسط مدیر سالن قبل از خروج |
| **SKILL-010** | شناسایی و یکپارچه‌سازی هویت مهمان در چند کانال (Unified Guest ID)<br>*Cross-Platform Guest De-anonymization & Matching* | `Entity Matching & Phone/Handle Graph` | هنگام دریافت هر پیام از هر کانال | تشکیل پرونده ۳۶۰ درجه تجربه مهمان در دیتابیس CRM |

---

### ۲. پردازش زبان طبیعی و احساسات ۴ زبانه (Multilingual NLP)
*تحلیل عمیق متون به زبان‌های فارسی، ترکی، انگلیسی و عربی با تشخیص طعنه، جنبه‌های کیفی و اعتبارسنجی نقدها.*

| کد مهارت | نام فارسی و انگلیسی | ابزار / موتور هوش مصنوعی | شرط فعال‌سازی (Trigger) | اقدام عملیاتی (Action) |
|---|---|---|---|---|
| **SKILL-011** | تحلیل احساسات زبان عامیانه و اصطلاحات فارسی (Persian Slang NLP)<br>*Persian Colloquial Dining Sentiment NLP* | `Persian Rule-based & Transformer Embeddings` | دریافت متن فارسی از گوگل مپ/اینستا | امتیازدهی احساسی از ۱- (بسیار منفی) تا ۱+ (بسیار مثبت) |
| **SKILL-012** | پردازش واژگان رستورانی ترکی استانبولی (Turkish Gastronomy NLP)<br>*Turkish Dining Sentiment & Food Tagger* | `Turkish BERT / Lexicon Matcher` | نظرات با کد زبان tr در گوگل و یاندکس | استخراج تم‌های رضایت ترک‌زبانان مقیم استانبول |
| **SKILL-013** | تحلیل بازخورد گردشگران بین‌المللی انگلیسی‌زبان (English Tourist NLP)<br>*English Tourist Sentiment Classifier* | `VADER / Transformer NLP` | نظرات به زبان انگلیسی در گوگل و تریپ‌ادوایزر | سنجش درک گردشگران خارجی از سنت‌های غذاخوری ایرانی |
| **SKILL-014** | پردازش نظرات مهمانان عرب‌زبان (Arabic Review Parser)<br>*Arabic Gulf & Levantine Sentiment Parser* | `Arabic NLP Tokenizer` | نظرات با کد زبان ar | دسته‌بندی انتظارات گردشگران عرب از طعم برنج و گوشت حلال |
| **SKILL-015** | تحلیل احساسات تفکیکی جنبه‌های رستوران (Aspect-Based Sentiment)<br>*Aspect-Based Sentiment Analysis (ABSA)* | `Multi-Label Classification Pipeline` | تمام نظرات بلندتر از ۱۵ کلمه | تولید ماتریس راداری نمرات ۵ گانه برای هر شیفت کاری |
| **SKILL-016** | استخراج احساسات به تفکیک آیتم‌های منو (Dish-Level Sentiment)<br>*Dish-Specific Sentiment Extraction* | `Fuzzy Dish Entity Linker` | متن‌های حاوی اسامی خوراک‌ها | به‌روزرسانی امتیاز لحظه‌ای هر بشقاب غذا در سیستم آشپزخانه |
| **SKILL-017** | تشخیص هوشمند کنایه، طعنه و تمسخر (Sarcasm & Irony Detector)<br>*Sarcasm & Irony Detection in Reviews* | `Contextual Contrast & Punctuation Classifier` | نظرات با تضاد معنایی بین امتیاز و متن | اصلاح برچسب احساسی و جلوگیری از ارسال پیام تشکر اشتباه |
| **SKILL-018** | شناسایی نقدها و کامنت‌های فیک و رباتی (Fake Review Detector)<br>*Fake Review & Bot Pattern Detector* | `Profile Age & Linguistic Entropy Model` | نظرات ۱ ستاره یا ۵ ستاره بدون جزئیات | علامت‌گذاری جهت ثبت گزارش تخلف در گوگل یا ریپورت به مدیر |
| **SKILL-019** | تحلیل احساسی و اعتبارسنجی تصاویر ارسالی مشتریان (Photo Review Vision)<br>*Review Photo Computer Vision Sentiment* | `Image Recognition & Object Detection` | نظرات حاوی عکس آپلودشده | تطبیق ادعای مشتری در متن با واقعیت بصری عکس ارسالی |
| **SKILL-020** | محاسبه‌گر لحظه‌ای شاخص ترویج‌کنندگان (Net Promoter Score Estimator)<br>*Real-time NPS & CSAT Estimator* | `NPS Mathematical Aggregator` | پایان هر روز کاری و هفتگی | محاسبه درصد خالص NPS برای ارائه به مدیران و سرمایه‌گذاران |

---

### ۳. سیستم پاسخ‌دهی خودکار و هوشمند (AI Smart Auto-Responder)
*پاسخ‌گویی اختصاصی به تمجیدها، نقدها، معطلی صف، کامنت‌های شبکه‌های اجتماعی و تزریق کلیدواژه‌های سئو.*

| کد مهارت | نام فارسی و انگلیسی | ابزار / موتور هوش مصنوعی | شرط فعال‌سازی (Trigger) | اقدام عملیاتی (Action) |
|---|---|---|---|---|
| **SKILL-021** | مولد پاسخ تشکر اختصاصی به نظرات ۵ ستاره (5-Star Gratitude Generator)<br>*Personalized 5-Star Gratitude Generator* | `GPT Generative Persona with Brand Voice` | ثبت نظر ۵ ستاره با متن | ارسال پاسخ در کمتر از ۱۵ دقیقه با امضای مدیر سالن |
| **SKILL-022** | پروتکل همدلی و عذرخواهی برای نقدهای ۱ تا ۳ ستاره (Empathy Protocol)<br>*1-to-3 Star Empathy & De-escalation Protocol* | `Non-Defensive Empathy Script Engine` | ثبت نظر ۱ یا ۲ یا ۳ ستاره | انتشار پاسخ آرام‌بخش و پیشنهاد پیگیری در کانال خصوصی |
| **SKILL-023** | پاسخ هوشمند به شکایات معطلی و صف شلوغی (Peak-Hour Queue Responder)<br>*Peak-Hour Waiting & Queue Empathy Responder* | `Context-Aware Wait Mitigation Template` | نظرات حاوی کلمات «صف»، «معطلی»، «انتظار» | هدایت مخاطب به دستور /reserve در ربات تلگرام جهت رزرو دفعه بعد |
| **SKILL-024** | تطبیق لحن فرهنگی و زبانی پاسخ‌ها (Multilingual Tone Adapter)<br>*Multilingual Cultural Tone Adapter* | `Cultural Tone Policy Matrix` | تمام پاسخ‌های تولیدی هوش مصنوعی | رعایت آداب و رسوم زبانی و القاب محترمانه در زبان مقصد |
| **SKILL-025** | هدایت هوشمند گفتگوی حل اختلاف به کانال خصوصی (Off-Platform Router)<br>*Off-Platform Resolution Router* | `Private Channel Escalation Linker` | نظرات با اعتراض شدید مالی یا کیفی | ارائه شماره مستقیم واتساپ با کد پیگیری اختصاصی |
| **SKILL-026** | تزریق ارگانیک کلمات کلیدی سئو در پاسخ‌ها (SEO Review Responder)<br>*SEO-Optimized Review Response Generator* | `Local SEO Entity Injector` | پاسخ‌های نظرات مثبت گوگل مپ | ارتقای رتبه رستوران در الگوریتم‌های رتبه‌بندی نقشه گوگل |
| **SKILL-027** | پروموت آیتم‌های جدید منو و رویدادها در پاسخ (Menu Upsell in Replies)<br>*Seasonal Special & Event Upsell in Replies* | `Event & Dish Cross-Selling Engine` | نظرات ۵ ستاره مشتریان محلی مقیم استانبول | افزایش مراجعه مجدد برای ایونت‌های فرهنگی آتی |
| **SKILL-028** | پاسخ‌گویی خودکار به کامنت‌های اینستاگرام (Instagram Comment Auto-Replier)<br>*Instagram Comment AI Auto-Replier* | `Social Graph Comment Dispatcher` | کامنت جدید زیر پست‌ها یا ریلزهای پیج | پاسخ عمومی + ارسال پیام دایرکت با منو و لینک لوکیشن |
| **SKILL-029** | صدور هوشمند بن تخفیف و ووچر جبرانی (Comp Voucher Generator)<br>*Dynamic Recovery Voucher Generator* | `Promo Code Engine with CRM Validation` | تأیید نارضایتی مشتری توسط مدیر | ارسال کد تخفیف ۲۰٪ به همراه پیام عذرخواهی اختصاصی |
| **SKILL-030** | پایشگر مهلت پاسخ‌گویی به نظرات طبق SLA (Response Time Monitor)<br>*Automated Response SLA Compliance Monitor* | `SLA Timer & Telegram Alert Bot` | گذشت ۵۰ دقیقه از ثبت نظر بی‌پاسخ | ارسال پیامک یا نوتیفیکیشن تلگرام فوری به مدیر داخلی |

---

### ۴. مدیریت بحران، هشدارهای فوری و SLA (Reputation Crisis)
*شناسایی زودهنگام مسمومیت، هجمه‌های فیک، تخلفات بهداشتی، هشدار به سرآشپز و جبران خسارت مهمان.*

| کد مهارت | نام فارسی و انگلیسی | ابزار / موتور هوش مصنوعی | شرط فعال‌سازی (Trigger) | اقدام عملیاتی (Action) |
|---|---|---|---|---|
| **SKILL-031** | سیستم هشدار فوری مسمومیت و بهداشت (Food Safety Early Warning)<br>*Food Safety & Hygiene Early-Warning Trigger* | `High-Severity Regex & NLP Alerting` | ثبت هر نظری با کلمات بهداشتی/مسمومیت | آژیر هشدار در تلگرام مدیر، مسدودسازی موقت مواد اولیه و تماس فوری |
| **SKILL-032** | هشدار رفتار نامناسب پرسنل و سوءتفاهم (Staff Conduct Flare-up Alert)<br>*Staff Behavior & Rude Service Alert* | `Staff Entity Extractor & Audit Logger` | نقد منفی حاوی اشاره به رفتار پرسنل | تخصیص بازآموزی به سرپرست سالن و تماس دلجویی با مشتری |
| **SKILL-033** | پیش‌بینی احتمال وایرال شدن نقد منفی (Virality Risk Predictor)<br>*Viral Negative Review Predictor* | `Influence Scoring & Social Virality Model` | نقد منفی با پروفایل‌های با نفوذ بالا | فعال‌سازی پروتکل ارتباطات بحران و تماس تلفنی مستقیم |
| **SKILL-034** | سیستم دفاع در برابر حملات فیک سازمان‌یافته (Smear Campaign Defense)<br>*Review Bombing & Smear Attack Defense* | `Spike Anomaly Detection & Geolocation Audit` | افزایش ناگهانی نرخ نظرات ۱ ستاره در ۱ ساعت | مستندسازی حملات و ارسال درخواست رسمی حذف گروهی به پشتیبانی گوگل |
| **SKILL-035** | ارجاع خودکار مشکلات پخت به سرآشپز (Head Chef Escalation)<br>*Head Chef Quality Escalation Workflow* | `Kitchen Display System (KDS) Dispatcher` | نقد منفی متمرکز بر دستور پخت مشخص | چاپ رسید هشدار در آشپزخانه جهت بررسی فورس‌ماژور مواد غذایی |
| **SKILL-036** | اتوماسیون گزارش نقض قوانین به گوگل (Google Policy Flagging)<br>*Google Review Policy Violation Automation* | `Google Review Policy Compliance Engine` | شناسایی کلمات رکیک یا تبلیغ نامربوط | ثبت درخواست Flag as Inappropriate در پنل بیزینس |
| **SKILL-037** | فرایند احیا و بازگشت مشتری آسیب‌دیده (Guest Recovery Follow-up)<br>*Post-Incident Guest Recovery Workflow* | `CRM Recovery Pipeline` | پس از حل مشکل مهمان معترض | پیگیری نهایی و در صورت تمایل مهمان، درخواست آپدیت نقد در گوگل |
| **SKILL-038** | پروتکل بحران غذای حلال و آلرژی غذایی (Halal & Allergy Protocol)<br>*Dietary & Halal Emergency Protocol* | `Halal & Allergen Certified Knowledge Base` | سوال یا نقد درباره حلال بودن یا حساسیت | ارائه مستندات تأییدشده ذبح اسلامی و اعلام عدم وجود گوشت غیرحلال |
| **SKILL-039** | رسیدگی سریع به ابهام فاکتور و صورت‌حساب (Bill Dispute Resolution)<br>*Overcharging & Bill Dispute Resolution* | `POS System Receipt Cross-Matcher` | کامنت منفی حاوی ادعای گران‌فروشی/خطای فاکتور | بررسی لاگ فاکتور و در صورت اثبات خطا، استرداد سریع وجه اضافی |
| **SKILL-040** | تدوین‌گر بیانیه روابط عمومی در بحران‌های عمومی (PR Statement Drafter)<br>*Reputation Crisis Public Relations Drafter* | `Executive PR Policy Engine` | بحران‌های گسترده در سطح شبکه‌های اجتماعی | تولید نسخه سه‌زبانه بیانیه با نظارت مدیریت عامل |

---

### ۵. مهندسی منو و تحلیل خوراک بر اساس بازخوردها (Menu Engineering)
*پایش محبوبیت غذاها، افت کیفیت دستورپخت، رضایت از حجم به قیمت، تحلیل دلیوری و ماتریس BCG اقلام منو.*

| کد مهارت | نام فارسی و انگلیسی | ابزار / موتور هوش مصنوعی | شرط فعال‌سازی (Trigger) | اقدام عملیاتی (Action) |
|---|---|---|---|---|
| **SKILL-041** | شاخص فراوانی نام غذاها در دیدگاه‌ها (Dish Mention Indexer)<br>*Dish Mention Frequency & Popularity Indexer* | `Entity Frequency Aggregator` | پایان هر ماه میلادی | رتبه‌بندی محبوبیت غذاها و کشف اقلامی که نیاز به پروموت دارند |
| **SKILL-042** | تحلیل تناسب حجم غذا با قیمت پرداختی (Portion vs Price Analytics)<br>*Portion Size vs Price Perception Analytics* | `Portion-to-Price Sentiment Correlator` | نظرات حاوی کلمات «حجم»، «سیر نشدیم»، «زیاد بود» | تنظیم گرم گوشت یا برنج در دستورالعمل استاندارد سرآشپز |
| **SKILL-043** | ردیابی تغییر کیفیت پخت با تغییر آشپز (Recipe Quality Drift)<br>*Recipe Quality Drift & Cook Consistency Radar* | `Shift-to-Rating Correlation Model` | تحلیل تغییرات امتیاز هفتگی به تفکیک شیفت | برگزاری تست کور طعم (Blind Taste Test) برای هماهنگی دستور پخت |
| **SKILL-044** | پایش دمای غذا و ماندگاری در دلیوری (Delivery Temperature Monitor)<br>*Delivery Freshness & Temperature Tracker* | `Delivery Feedback Keyword Extractor` | نظرات مربوط به سفارشات آنلاین بیرون‌بر | ارتقای ظروف آلومینیومی حرارتی و عایق‌بندی باکس‌های پیک |
| **SKILL-045** | پیگیری عدم تطابق سفارش و اقلام فراموش‌شده (Missing Item Tracker)<br>*Missing Item & Packaging Error Tracker* | `Order Accuracy Incident Log` | نظرات با مضمون فراموشی قلم غذایی | افزایش دقت چک‌لیست بسته‌بندی نهایی قبل از تحویل به پیک |
| **SKILL-046** | دسته‌بندی اقلام منو بر اساس ماتریس BCG (BCG Menu Engineering)<br>*BCG Menu Matrix Classifier* | `BCG Matrix Calculation (Volume x Margin)` | بازبینی فصلی منو | تغییر جایگاه بصری ستاره‌ها در صفحه اول منوی فیزیکی و سایت |
| **SKILL-047** | همبستگی بهای تمام‌شده غذا با امتیاز رضایت (Food Cost vs Rating)<br>*Food Cost vs Review Rating Correlation* | `Cost-Benefit Regression Analytics` | تحلیل داده‌های حسابداری صنعتی و کامنت‌ها | کاهش هزینه آیتم‌های پرتنش و افزایش تنوع پیش‌غذاهای پرسود |
| **SKILL-048** | بنچ‌مارک طعم چلوکباب با برترین رقبای استانبول (Signature Dish Benchmark)<br>*Signature Dish Taste & Price Benchmarking* | `Competitive Dish Sentiment Scraper` | ماهیانه بر اساس کامنت‌های تطبیقی رقبا | بهینه‌سازی درصد چربی قلوه‌گاه و ادویه‌جات بر اساس سلیقه بازار |
| **SKILL-049** | پیش‌بینی تقاضای غذاهای گیاهی و رژیمی (Plant-Based Demand Radar)<br>*Vegan & Vegetarian Demand Forecaster* | `Dietary Trend Keyword Scraper` | کامنت‌ها و سوالات در گوگل مپ و اینستاگرام | طراحی بخش ویژه گیاه‌خواری در منو برای جذب توریست‌های غربی |
| **SKILL-050** | موتور پیشنهاد حذف یا اصلاح آیتم‌های ضعیف (Menu Pruning Engine)<br>*Menu Pruning & Optimization Recommender* | `Underperforming Menu Item Detector` | پایان هر فصل کاری | پیشنهاد رسمی به مدیر رستوران برای جایگزینی خوراک ضعیف |

---

### ۶. پایش شبکه‌های اجتماعی و اینستاگرام (Instagram & Social Listening)
*رصد ریلزها، ارزیابی اینفلوئنسرها، بازنشر محتوای تولیدی مهمانان (UGC)، تبدیل دایرکت به رزرو و رصد رقبا.*

| کد مهارت | نام فارسی و انگلیسی | ابزار / موتور هوش مصنوعی | شرط فعال‌سازی (Trigger) | اقدام عملیاتی (Action) |
|---|---|---|---|---|
| **SKILL-051** | تحلیل احساسات ویدیوها و ریلزهای اینستاگرام (Instagram Reel Sentiment)<br>*Instagram Reel & Short Video Sentiment Harvester* | `Instagram Media Insights & Comments NLP` | پس از انتشار هر ریلز ویدئویی | شناسایی پلان‌های جذاب ویدیو برای تکرار در کمپین‌های بعدی |
| **SKILL-052** | ارزیابی بازدهی واقعی فودبلاگرها (Influencer ROI Evaluator)<br>*Food Influencer Campaign ROI Tracker* | `Spike Attribution Analytics` | انتشار استوری یا پست تبلیغاتی توسط بلاگر | محاسبه هزینه به ازای هر مشتری جذب‌شده (CPA) و رتبه‌بندی بلاگرها |
| **SKILL-053** | درخواست خودکار مجوز بازنشر عکس‌های مهمانان (UGC Rights Requester)<br>*User-Generated Content Rights Automation* | `Automated UGC Rights Commenter` | تشخیص عکس باکیفیت مهمان با تگ لوکیشن رستوران | ذخیره عکس‌های دارای مجوز در آرشیو و بازنشر با ذکر نام عکاس |
| **SKILL-054** | رصد هشتگ‌ها و ساندترک‌های ترند غذا در استانبول (Viral Trend Tracker)<br>*Trending Food Hashtag & Audio Tracker* | `Trend Discovery & Audio Scraper` | هفتگی روزهای دوشنبه | ارائه ۳ ایده ساخت محتوای ترند به تیم رسانه‌ای رستوران |
| **SKILL-055** | بنچ‌مارک نرخ تعامل شبکه‌های اجتماعی رقبا (Social Engagement Benchmark)<br>*Competitor Social Engagement Benchmark* | `Social Analytics Scraping Engine` | هفتگی | محاسبه رتبه تعاملی (Engagement Rank) و تعیین استراتژی محتوا |
| **SKILL-056** | پاسخ سریع و بازنشر منشن‌های استوری (Story Mention Auto-Thanker)<br>*Instagram Story Mention Auto-Thanker* | `Meta Webhook /story_insights & Direct API` | لحظه انتشار استوری توسط مشتری | ارسال پیام محبت‌آمیز + بازنشر استوری برای افزایش تعامل |
| **SKILL-057** | امتیازدهی به جذابیت بصری تزیین بشقاب با هوش مصنوعی (Plating Aesthetic Score)<br>*Food Plating Aesthetic AI Scorer* | `Computer Vision Aesthetic Quality Assessor` | عکس‌های بارگذاری شده در شبکه‌های اجتماعی | ارائه بازخورد به آشپزخانه برای چیدمان زیباتر و فتوژنیک بشقاب |
| **SKILL-058** | فیلتر کامنت‌های منفی در کمپین‌های پولی اینستاگرام (Ad Comment Negative Shield)<br>*Paid Ads Negative Comment Shield* | `Real-time Ad Comments Moderation Bot` | کمپین‌های فعال Meta Ads | پایش ۲۴ ساعته تبلیغات و هدایت سوالات به دایرکت |
| **SKILL-059** | تبدیل دایرکت به رزرو قطعی با ربات فروش هوشمند (DM to Booking Converter)<br>*Instagram DM to Reservation Converter* | `Conversational AI Sales Bot for Instagram DM` | دریافت دایرکت با قصد خرید/رزرو | بررسی تقویم ظرفیت خالی و اخذ بیعانه یا ثبت نام مهمان |
| **SKILL-060** | موتور دعوت از میکرو-اینفلوئنسرهای هدفمند (Micro-Influencer Outreach)<br>*Micro-Influencer Tasting Outreach Engine* | `Creator Search & DM Outreach Pipeline` | ماهیانه بر اساس معیارهای تعامل | تولید جریان مستمر محتوای ارگانیک و عکس‌های جدید بدون هزینه سنگین |

---

### ۷. سئوی محلی و صدرنشینی در گوگل مپ (Local SEO & 3-Pack)
*ردیابی رتبه در Local 3-Pack، تراکم کلمات کلیدی، آپلود عکس‌های ژئوتگ‌شده، پست‌های هفتگی و بهینه‌سازی Near Me.*

| کد مهارت | نام فارسی و انگلیسی | ابزار / موتور هوش مصنوعی | شرط فعال‌سازی (Trigger) | اقدام عملیاتی (Action) |
|---|---|---|---|---|
| **SKILL-061** | ردیابی رتبه در پک ۳تایی محلی گوگل (Google 3-Pack Position Tracker)<br>*Google 3-Pack Local Ranking Tracker* | `Geo-located SERP Rank Tracker` | روزانه از ۵ مختصات جغرافیایی مختلف استانبول | ثبت موقعیت در نقشه و هشدار در صورت افت رتبه |
| **SKILL-062** | سرعت و شتاب کلمات کلیدی در نظرات کاربران (Keyword Velocity in Reviews)<br>*Keyword Velocity in Customer Reviews* | `NLP Keyword Frequency Tracker` | ماهیانه بر اساس کامنت‌های جدید | تشویق هوشمند مهمانان به نام بردن از غذای اختصاصی در نظرات |
| **SKILL-063** | بهینه‌ساز دسته‌بندی و ویژگی‌های پروفایل بیزینس (GBP Attributes Optimizer)<br>*Google Business Profile Category & Attribute Optimizer* | `GBP Attributes API Syncer` | ماهیانه با معرفی قابلیت‌های جدید گوگل | بهینه‌سازی کامل پروفایل و افزایش شانس دیده‌شدن در فیلترها |
| **SKILL-064** | اتوماسیون بارگذاری عکس‌های ژئوتگ‌شده (Geotagged Photo Uploader)<br>*Geotagged High-Res Photo Upload Automation* | `EXIF Geotagging & GBP Media API` | هفتگی ۲ تصویر حرفه‌ای جدید | افزایش اعتبار سئوی محلی تصاویر در موتور جستجوی گوگل ایمیج |
| **SKILL-065** | ممیزی یکپارچگی اطلاعات آدرس و تلفن در کل وب (NAP Consistency Audit)<br>*NAP (Name, Address, Phone) Consistency Auditor* | `Web Citation Scraper & Validator` | ماهیانه | کشف و اصلاح مغایرت‌های آدرس که باعث تضعیف رتبه سئو می‌شوند |
| **SKILL-066** | انتشار خودکار پست‌ها و رویدادهای هفتگی در گوگل مپ (GBP Posts Automation)<br>*Google Business Profile Updates Automation* | `GBP LocalPost API Scheduler` | دوشنبه و پنجشنبه هر هفته | ایجاد سیگنال پویایی به الگوریتم گوگل و جذب کلیک کاربران نقشه |
| **SKILL-067** | ردیابی سرعت رشد نظرات رقبا (Review Velocity Tracker)<br>*Competitor Review Velocity & Momentum Tracker* | `Review Count Delta Scraper` | هفتگی | هشدار در صورتی که سرعت دریافت نظر رقیب ۲ برابر میانگین شود |
| **SKILL-068** | بهینه‌سازی برای جستجوهای اضطراری نزدیک من (Near Me Query Optimizer)<br>*Near Me Local Intent Optimization Engine* | `Local Proximity SEO Tuner` | پیوسته بر اساس لاگ جستجوها | بالا آمدن نام رستوران در سرچ‌های لحظه‌ای مسافران گرسنه |
| **SKILL-069** | پایش درخواست‌های مسیریابی در یاندکس و گوگل (Direction Request Tracker)<br>*Direction Requests & Footfall Intent Tracker* | `GBP & Yandex Insights Performance API` | هفتگی | تخمین دقیق تعداد مهمانان حضوری ورودی حاصل از تبلیغات نقشه |
| **SKILL-070** | ثبت در راهنماهای آنلاین و بلاگ‌های گردشگری استانبول (Tourism Directory Infiltration)<br>*Tourism Guide & Local Directory Infiltration* | `Backlink & Brand Mention Crawler` | ماهیانه | ارتباط با نویسندگان بلاگ‌های سفر جهت اضافه کردن لینک و معرفی منو |

---

### ۸. هوش رقابتی و بنچ‌مارک بازار استانبول (Competitive Intelligence)
*مقایسه درصد رضایت و قیمت‌ها با ریحون، فارسی و سفیر، ردیابی ضعف‌های رقیب، سهم صدا و جابجایی سرآشپزها.*

| کد مهارت | نام فارسی و انگلیسی | ابزار / موتور هوش مصنوعی | شرط فعال‌سازی (Trigger) | اقدام عملیاتی (Action) |
|---|---|---|---|---|
| **SKILL-071** | محاسبه تفاضل درصد رضایت با رقبا (Competitor Sentiment Differential)<br>*Competitor Net Sentiment Differential* | `Multi-Venue Sentiment Diff Calculator` | هفتگی | مشخص کردن دستاوردهای برند برای استفاده در تبلیغات بنری و کمپین‌ها |
| **SKILL-072** | ردیابی افزایش قیمت منوی رقبا (Competitor Menu Price Tracker)<br>*Competitor Menu Price Inflation Tracker* | `Menu OCR & Price Delta Scraper` | ماهیانه | تصمیم‌گیری آگاهانه برای تغییر قیمت منو بدون از دست دادن مزیت رقابتی |
| **SKILL-073** | بهره‌برداری تبلیغاتی از نقاط ضعف رقیب (Competitor Flaw Exploitation)<br>*Competitor Weakness Counter-Marketing Engine* | `Competitive Vulnerability NLP Miner` | هنگام افزایش نارضایتی از صف رقیب | فعال‌سازی تبلیغات هدفمند اینستاگرام در محدوده ۵۰۰ متری رقیب |
| **SKILL-074** | سهم صدای برند در فضای آنلاین استانبول (Share of Voice - SOV)<br>*Online Share of Voice (SOV) Analytics* | `Social & Search Volume Aggregator` | ماهیانه | ارزیابی نفوذ نام برند در میان مهاجران و گردشگران ایرانی |
| **SKILL-075** | تحلیل کشش قیمتی بین محله‌های استانبول (Cross-Neighborhood Price Elasticity)<br>*Cross-Neighborhood Price Elasticity Analytics* | `Econometric Sentiment Elasticity Model` | فصلی | تعیین استراتژی قیمت‌گذاری شعب مرکزی در برابر مناطق مسکونی |
| **SKILL-076** | رادار جابجایی سرآشپزها و پرسنل کلیدی (Staff & Chef Turnover Radar)<br>*Competitor Chef & Key Staff Turnover Radar* | `HR & Social Mention Tracker` | ماهیانه | شناسایی استعدادهای برتر برای جذب و استخدام در آشپزخانه شمسه |
| **SKILL-077** | مقایسه شعاع پوشش و زمان دلیوری (Delivery Radius Comparison)<br>*Delivery Radius & Courier Speed Benchmarking* | `Yemeksepeti / Trendyol Coverage Mapper` | فصلی | گسترش شعاع ارسال غذا و بهینه‌سازی مسیر پیک‌های موتوری |
| **SKILL-078** | تحلیل نسبت توریست به مشتری بومی (Tourist vs Local Demographic Ratio)<br>*Tourist-to-Local Customer Demographic Ratio* | `Reviewer Profile Demographics Estimator` | ماهیانه | تنظیم بودجه تبلیغات برای فصول پرتردد گردشگری و ایام نوروز |
| **SKILL-079** | نقشه حرارتی ساعات اوج شلوغی رقبا (Peak Hours Heatmap Benchmark)<br>*Peak Hours & Capacity Heatmap Benchmark* | `Google Popular Times Scraper` | هفتگی | تنظیم ساعت رویدادهای کلاب برای زمان‌هایی که رقبا ظرفیت پذیرش ندارند |
| **SKILL-080** | شناسایی زودهنگام رستوران‌ها و کیچن‌های ابری جدید (New Entrant Early Detector)<br>*New Competitor & Cloud Kitchen Early Detector* | `Entity Registration & Social Radar` | پیوسته | اتخاذ راهبردهای پیشگیرانه بازاریابی قبل از تثبیت رقبای تازه‌وارد |

---

### ۹. درآمدزایی از فضای خالی و رویدادها (Yield Management)
*مونتایز ساعات خلوت ۱۴:۳۰ تا ۱۸:۳۰، قیمت‌گذاری تیکت‌های مافیا و شعر، پکیج کار اشتراکی و پیش‌فاکتور ضیافت‌های شرکتی.*

| کد مهارت | نام فارسی و انگلیسی | ابزار / موتور هوش مصنوعی | شرط فعال‌سازی (Trigger) | اقدام عملیاتی (Action) |
|---|---|---|---|---|
| **SKILL-081** | شناسایی ظرفیت‌های صندلی مرده و ساعات خلوت (Dead-Hour Capacity Auditor)<br>*Dead-Hour Capacity & Lost Revenue Auditor* | `POS Footfall & Seating Analytics` | روزانه پس از اتمام شیفت ناهار | گزارش تعداد دقیق صندلی‌های در دسترس جهت برنامه‌ریزی ایونت |
| **SKILL-082** | محاسبه‌گر حداقل سفارش دورهمی‌های اختصاصی (Minimum Spend Estimator)<br>*Dynamic Minimum Spend & Buyout Calculator* | `Yield Management Margin Calculator` | درخواست سالن دربست برای تولد یا جشن | تولید رقم حداقل سفارش بهینه که سود ناخالص را تضمین کند |
| **SKILL-083** | قیمت‌گذاری هوشمند بلیت میتاپ‌های مافیا و شعر (Meetup Ticket Dynamic Pricing)<br>*Club Meetup Dynamic Ticket Pricing* | `Dynamic Capacity Pricing Engine` | لحظه ثبت‌نام در ربات تلگرام | ارائه تخفیف ثبت‌نام زودهنگام (Early Bird) جهت تکمیل سریع ظرفیت |
| **SKILL-084** | پکیج کار اشتراکی و جلسات فریلنسری بعدازظهر (Coworking & Coffee Package)<br>*Coworking & Remote Worker Afternoon Engine* | `Off-Peak Workspace Offer Generator` | روزهای دوشنبه تا چهارشنبه | افزایش جریان نقدی در ساعاتی که آشپزخانه سفارش سنگین ندارد |
| **SKILL-085** | جذب لیدهای ضیافت شرکتی و B2B (Corporate Dining Lead Ingestion)<br>*Corporate B2B Private Dining Lead Ingestion* | `B2B Inquiry Funnel & Web Form` | دریافت فرم در intelligence.html | ارجاع به مدیر فروش تشریفات و ارسال بروشور سه‌زبانه |
| **SKILL-086** | تولید خودکار پیش‌فاکتور رسمی رویداد در ۶۰ ثانیه (Instant Event Proposal)<br>*RestauRent / Tripleseat Style Event Proposal Generator* | `Automated PDF & HTML Quote Builder` | تکمیل درخواست در فرم رزرو رویداد | ارسال سریع به متقاضی که نرخ عقد قرارداد را تا ۷ برابر افزایش می‌دهد |
| **SKILL-087** | برنامه‌ریزی صفر-ضایعات در کترینگ ضیافت‌ها (Zero-Waste Banquet Planning)<br>*Banquet Food-Cost & Waste Minimization Planner* | `Atikova Zero-Waste Recipe & Portion Algorithm` | پذیرش سفارشات بالای ۲۰ نفر | محاسبه دقیق گرم برنج و گوشت و اهدای باقی‌مانده‌های بهداشتی |
| **SKILL-088** | پروموت بوفه برانچ و شیفت‌های کم‌فروش آخر هفته (Weekend Brunch Promo)<br>*Weekend Brunch & Off-Peak Shift Promotion* | `Breakfast Footfall Generator` | پنجشنبه‌ها و جمعه‌ها در کانال‌های اجتماعی | ایجاد شیفت درآمدی جدید قبل از آغاز سرویس ناهار |
| **SKILL-089** | فروش خدمات جانبی پروژکتور، صوتی و فیلم‌برداری (AV Add-on Upselling)<br>*Audio/Visual & Event Add-on Upselling* | `Add-on Recommendation Matrix` | حین تکمیل فرم رزرو رویداد | افزایش میانگین سبد خرید هر مراسم تا ۴۰٪ |
| **SKILL-090** | مدیریت بیعانه و قوانین کنسلی هوشمند (Deposit & Cancellation Policy)<br>*Event Deposit & No-Show Mitigation* | `Payment Gateway / Secure Escrow Notifier` | ثبت اولیه رزرو بالای ۶ نفر | تثبیت تاریخ و جلوگیری از رزروهای غیرواقعی |

---

### ۱۰. وفادارسازی، باشگاه مشتریان و CRM (Guest Retention & CRM)
*درخواست ثبت نظر بعد از پرداخت، پروفایل علایق VIP، یادآور سالگرد و تولد، بازگرداندن مشتریان دورشده و سنجش LTV.*

| کد مهارت | نام فارسی و انگلیسی | ابزار / موتور هوش مصنوعی | شرط فعال‌سازی (Trigger) | اقدام عملیاتی (Action) |
|---|---|---|---|---|
| **SKILL-091** | درخواست هوشمند ثبت نظر بعد از غذا (Post-Dining Review Request)<br>*Post-Dining Automated Review Request via Telegram/SMS* | `Post-Visit Trigger & Link Generator` | ۲ ساعت پس از پایان ساعت رزرو مهمان | افزایش نرخ تبدیل مشتری راضی به نقد ۵ ستاره در گوگل مپ |
| **SKILL-092** | ثبت ترجیحات و علایق اختصاصی مشتریان VIP (VIP Preference Memory)<br>*VIP Diner Profile & Preference Memory* | `CRM Guest Attributes Store` | هنگام پذیرش و سفارش‌گیری مهمان | خلق تجربه غافلگیرکننده و احساس احترام فوق‌العاده برای مهمان |
| **SKILL-093** | یادآور سالگرد ازدواج و تولد با هدیه (Birthday & Anniversary Reminders)<br>*Birthday & Milestone Dining Reminders* | `Calendar Milestone Scheduler` | روزانه ساعت ۱۰ صبح برای مناسبت‌های هفته آینده | تبدیل رستوران به انتخاب اول جشن‌های خانوادگی |
| **SKILL-094** | شناسایی مهمانان وفادار در معرض ریزش (Churn Risk Diner Detector)<br>*Churn Risk Diner Identification* | `RFM (Recency, Frequency, Monetary) Engine` | تحلیل ماهیانه تاریخچه خرید | ارسال پیام دلتنگی شخصی‌سازی‌شده و انگیزاننده بازگشت |
| **SKILL-095** | سیستم امتیازدهی و ارتقای سطح باشگاه مشتریان (Gamified Loyalty Tiers)<br>*Gamified Loyalty Points & Tier Progression* | `Loyalty Tier Ledger & Gamification` | ثبت فاکتور در ربات یا سیستم پوز | افزایش بازگشت دوره‌ای مشتریان تا ۳۵٪ |
| **SKILL-096** | پاداش ویژه هماهنگ‌کنندگان رویدادهای شرکتی (Corporate Planner Rewards)<br>*Corporate Secretary & Planner Reward Program* | `B2B Referral & Incentive Tracker` | تسویه فاکتور رویداد شرکتی | وفادارسازی برنامه‌ریزان رویداد و تضمین تکرار سالانه |
| **SKILL-097** | کمپین بازگشت مشتریان از دست رفته (Lost-Guest Win-Back Campaign)<br>*Automated Lost-Guest Win-Back Campaign* | `Reactivation Funnel Dispatcher` | فصلی برای لیست مخاطبان غیرفعال | احیای ۱۵٪ تا ۲۰٪ از مشتریان غیرفعال بدون هزینه تبلیغاتی جدید |
| **SKILL-098** | پرونده یکپارچه ۳۶۰ درجه تعاملات مهمان (Omnichannel Interaction Log)<br>*Omnichannel Guest Interaction Timeline* | `Guest Timeline Aggregator` | پیوسته بر روی شناسه مشترک مهمان | تسلط کامل مدیر رستوران بر سوابق هر مهمان قبل از حضور سر میز |
| **SKILL-099** | ردیابی بازگشت مشتری پس از پاسخ به نقد منفی (Reviewer Recovery Tracker)<br>*Reviewer-to-Diner Conversion Tracking* | `Sentiment Recovery Cohort Analytics` | هر ۶ ماه یک‌بار | اثبات بازگشت سرمایه (ROI) پاسخ‌گویی به نقدها و نجات مشتری |
| **SKILL-100** | پیش‌بینی ارزش مادام‌العمر مهمان و تریاژ VIP (Customer Lifetime Value - LTV)<br>*Guest Lifetime Value (LTV) Prediction & VIP Triage* | `Predictive LTV Machine Learning Model` | هنگام پردازش رزرو در سیستم | اختصاص بهترین پرسنل و هدایای ویژه سرآشپز به مهمانان کلیدی |

---

## 🚨 ۳. پروتکل‌های مدیریت بحران و SLA پاسخ‌گویی

1. **پروتکل هشدار قرمز بهداشت و مسمومیت (SKILL-031):**
   - به محض شناسایی کلمات کلیدی بحرانی (`مسموم`, `دل‌درد`, `کثیف`, `zehirlen`, `food poisoning`)، تیکت قرمز با اولویت P0 در کمتر از ۳۰ ثانیه در تلگرام مدیر داخلی و سرآشپز صادر می‌شود.
   - ثبت شماره تلفن و زمان مراجعه مهمان جهت تماس فوری دلجویی و استرداد وجه قبل از انتشار در رسانه‌های عمومی.

2. **پروتکل مدیریت صف و شلوغی پیاده‌راه استقلال (SKILL-023 & SKILL-081):**
   - تبدیل نقد منفی معطلی به فرصت رزرو برای دفعات بعدی از طریق راهنمایی به بات تلگرام (`/reserve`).
   - تحلیل ظرفیت صندلی‌های خالی ساعات بعدازظهر (۱۴:۳۰ تا ۱۸:۳۰) برای انتقال بار ترافیکی به ساعات خلوت.

3. **پروتکل تطبیق لحن فرهنگی ۴ زبانه (SKILL-011 تا SKILL-014):**
   - زبان فارسی: لحن صمیمانه، گرم و سرشار از تعارفات اصیل ایرانی و دعوت به باقلوای تازه.
   - زبان ترکی: لحن رسمی و صمیمانه با تکیه بر «Afiyet olsun» و «Ellerinize sağlık».
   - زبان انگلیسی: تمرکز بر معرفی اصالت زعفران ایرانی، غذای حلال و تاریخچه غذاها.
   - زبان عربی: تأکید بر ذبح حلال، فضای خانوادگی و احترام ویژه به گردشگران خلیج فارس.
