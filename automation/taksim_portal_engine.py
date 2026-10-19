#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Taksim Gastronomy Intelligence & Multi-Tenant Restaurant Portal Engine
Manages:
  1. Google Maps & Multiplatform Sentiment Analytics for Taksim Restaurants.
  2. Multi-Tenant Restaurant Access: Token verification and client portal data.
  3. Automated Email & 1-Touch WhatsApp Outreach with Magic Login Links (Atikova Model).
  4. Telegram Presence Tracking & Bot Deep-links.
  5. Follow-up Reminder Cadence (Day 1 -> Day 3 reminder -> WhatsApp push).
"""

import os
import json
import urllib.parse
from datetime import datetime

ROOT = os.path.dirname(os.path.abspath(__file__))
TAKSIM_FILE = os.path.join(ROOT, "taksim_restaurants_intel.json")
ATIKOVA_FILE = os.path.join(ROOT, "atikova_dispatch_db.json")

PORTAL_BASE_URL = "https://shamse-restaurant.pages.dev/restaurant_portal.html"
BOT_USERNAME = "mizban_bot"
SENDER_WHATSAPP_NUMBER = "+98 920 626 3218"

def load_taksim_restaurants():
    if not os.path.exists(TAKSIM_FILE):
        return []
    with open(TAKSIM_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def load_atikova_db():
    if not os.path.exists(ATIKOVA_FILE):
        return {}
    with open(ATIKOVA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def get_restaurant_by_token(token):
    """Authenticates a restaurant manager by their magic access token."""
    restaurants = load_taksim_restaurants()
    clean_token = str(token).strip().upper()
    for r in restaurants:
        if r.get("magic_token") == clean_token or r.get("id") == token.lower():
            return r
    return None

def get_taksim_district_summary():
    """Calculates overall gastronomy benchmark metrics for the Taksim district."""
    restaurants = load_taksim_restaurants()
    total_venues = len(restaurants)
    if total_venues == 0:
        return {}

    total_google_reviews = sum(r.get("google_review_count", 0) for r in restaurants)
    total_tripadvisor_reviews = sum(r.get("tripadvisor_review_count", 0) for r in restaurants)
    total_yandex_reviews = sum(r.get("yandex_review_count", 0) for r in restaurants)
    grand_total_reviews = total_google_reviews + total_tripadvisor_reviews + total_yandex_reviews

    avg_google_rating = round(sum(r.get("google_rating", 0) for r in restaurants) / total_venues, 2)
    avg_positive_pct = round(sum(r.get("sentiment_positive_pct", 0) for r in restaurants) / total_venues, 1)

    total_seats = sum(r.get("seat_capacity", 0) for r in restaurants)
    total_monthly_unlocked_try = sum(r.get("monthly_unlocked_revenue_try", 0) for r in restaurants)

    return {
        "district": "Taksim / Beyoğlu",
        "total_venues_tracked": total_venues,
        "total_google_reviews": total_google_reviews,
        "total_tripadvisor_reviews": total_tripadvisor_reviews,
        "total_yandex_reviews": total_yandex_reviews,
        "grand_total_reviews": grand_total_reviews,
        "average_google_rating": avg_google_rating,
        "average_positive_sentiment_pct": avg_positive_pct,
        "total_monitored_seat_capacity": total_seats,
        "district_monthly_unlocked_revenue_try": total_monthly_unlocked_try,
        "top_rated_venue": max(restaurants, key=lambda x: x.get("google_rating", 0))["name_fa"]
    }

def generate_restaurant_outreach_package(restaurant_id):
    """
    Generates personalized Email and 1-Touch WhatsApp outreach messages
    giving the restaurant manager their Magic Login Link and test credentials.
    """
    restaurants = load_taksim_restaurants()
    matched = [r for r in restaurants if r["id"] == restaurant_id or r.get("slug") == restaurant_id]
    if not matched:
        return None
    r = matched[0]

    magic_token = r.get("magic_token")
    magic_url = f"{PORTAL_BASE_URL}?token={magic_token}"
    phone_raw = r.get("phone", "")
    phone_clean = re_clean_phone(phone_raw)

    bot_url = f"https://t.me/{BOT_USERNAME}?start=rest_{magic_token}"

    # 1. Email Subject & Body
    email_subject = f"🏛 دسترسی اختصاصی به پنل هوش تجاری و ممیزی نظرات گوگل مپ: ویژه مدیریت محترم {r['name_fa']}"
    email_html = f"""
    <div dir="rtl" style="font-family:Tahoma,sans-serif;line-height:1.8;color:#222;max-width:640px;margin:0 auto;border:1px solid #d29a5a;padding:26px;border-radius:8px;background:#ffffff;">
      <div style="text-align:center;border-bottom:2px solid #d29a5a;padding-bottom:14px;margin-bottom:18px;">
        <h2 style="color:#14100d;margin:0;">🏛 پلتفرم هوش تجاری و گاسترونومی میزبان استانبول</h2>
        <span style="color:#d29a5a;font-weight:bold;font-size:14px;">گزارش اختصاصی منطقه تکسیم و اطلاعات ورود مدیریت {r['name_fa']}</span>
      </div>

      <p>سلام و احترام خدمت مدیریت محترم مجموعه <b>{r['name_fa']}</b>؛</p>
      <p>در پایش جامع گاسترونومی و رستوران‌های منطقه تکسیم، وضعیت عملکرد مجموعه شما در ۳ پلتفرم بین‌المللی ارزیابی شد:</p>

      <table style="width:100%;border-collapse:collapse;margin:16px 0;font-size:13px;">
        <tr style="background:#faf5ee;border-bottom:1px solid #d29a5a;">
          <th style="padding:8px;text-align:right;">پلتفرم</th>
          <th style="padding:8px;text-align:center;">تعداد نقدها</th>
          <th style="padding:8px;text-align:center;">امتیاز</th>
          <th style="padding:8px;text-align:right;">شاخص رضایت طعم</th>
        </tr>
        <tr>
          <td style="padding:8px;border-bottom:1px solid #eee;">🗺️ Google Maps</td>
          <td style="padding:8px;text-align:center;border-bottom:1px solid #eee;"><b>{r['google_review_count']:,}</b></td>
          <td style="padding:8px;text-align:center;border-bottom:1px solid #eee;color:#27ae60;">★ {r['google_rating']}</td>
          <td style="padding:8px;border-bottom:1px solid #eee;">{r['absa_scores']['taste']} از ۵٫۰</td>
        </tr>
        <tr>
          <td style="padding:8px;border-bottom:1px solid #eee;">🦉 TripAdvisor</td>
          <td style="padding:8px;text-align:center;border-bottom:1px solid #eee;"><b>{r['tripadvisor_review_count']}</b></td>
          <td style="padding:8px;text-align:center;border-bottom:1px solid #eee;color:#27ae60;">★ {r['tripadvisor_rating']}</td>
          <td style="padding:8px;border-bottom:1px solid #eee;">انتخاب توریست‌های خارجی</td>
        </tr>
        <tr>
          <td style="padding:8px;border-bottom:1px solid #eee;">🟡 Yandex Maps</td>
          <td style="padding:8px;text-align:center;border-bottom:1px solid #eee;"><b>{r['yandex_review_count']}</b></td>
          <td style="padding:8px;text-align:center;border-bottom:1px solid #eee;color:#27ae60;">★ {r['yandex_rating']}</td>
          <td style="padding:8px;border-bottom:1px solid #eee;">ناوبری مسافران روس و CIS</td>
        </tr>
      </table>

      <!-- Magic Login Box -->
      <div style="background:#fcf9f5;border:2px solid #2ecc71;border-radius:6px;padding:18px;margin:22px 0;">
        <h3 style="color:#2ecc71;margin:0 0 10px 0;font-size:15px;">🔑 دسترسی و ورود آزمایشی به پنل هوش تجاری رستوران شما:</h3>
        <p style="font-size:13px;color:#444;margin:0 0 12px 0;">برای مشاهده تحلیل کامل احساسات مشتریان، پاسخ‌دهی هوشمند ۴ زبانه به کامنت‌ها، و فعال‌سازی درآمد ساعات خلوت سالن وارد شوید:</p>
        
        <div style="background:#fff;border:1px solid #ddd;padding:12px;border-radius:4px;font-size:12.5px;line-height:1.8;">
          <div>• <b>لینک ورود تک‌کلیک (بدون رمز):</b> <a href="{magic_url}" target="_blank" style="color:#d29a5a;font-weight:bold;">ورود مستقیم به پنل اختصاصی ↗</a></div>
          <div>• <b>شناسه اختصاصی شما (Magic Token):</b> <code style="background:#f0ede8;padding:2px 6px;color:#14100d;">{magic_token}</code></div>
          <div>• <b>رمز عبور موقت مدیریت:</b> <code style="background:#f0ede8;padding:2px 6px;color:#14100d;">{r.get('temp_password', 'Mizban@Taksim2026')}</code></div>
        </div>

        <div style="text-align:center;margin-top:16px;">
          <a href="{magic_url}" target="_blank" style="display:inline-block;background:#2ecc71;color:#14100d;padding:12px 28px;text-decoration:none;font-weight:bold;border-radius:6px;font-size:14px;">
            ورود به داشبورد اختصاصی {r['name_fa']} ↗
          </a>
        </div>
      </div>

      <!-- Opportunity Points -->
      <h4 style="color:#d29a5a;margin-bottom:6px;">💡 پتانسیل درآمدی شناسایی‌شده برای سالن شما در تکسیم:</h4>
      <ul style="font-size:13px;color:#444;">
        <li><b>پر کردن ساعات خلوت ({r['off_peak_hours']}):</b> اشغال صندلی‌ها در این ساعات {r['off_peak_occupancy_pct']}٪ است که با برگزاری رویدادهای درآمدزا امکان جذب <b>+{r['monthly_unlocked_revenue_try']:,} لیر سود ماهانه خالص</b> وجود دارد.</li>
        <li><b>پاسخ‌دهی خودکار هوش مصنوعی به نظرات خارجی:</b> توریست‌های اروپایی و عرب با پاسخ‌های زیر ۱۵ دقیقه ترغیب به بازگشت می‌شوند.</li>
      </ul>

      <!-- Attachments note -->
      <p style="font-size:12px;color:#666;border-top:1px solid #eee;padding-top:12px;">
        📎 <b>پیوست‌های این گزارش:</b> اسلایدهای استراتژیک (PowerPoint) و سفیدنامه تحلیلی (PDF) به همراه دمو ضمیمه گردیده است.
      </p>

      <p style="font-size:12px;color:#888;text-align:center;margin-top:16px;">
        پلتفرم میزبان استانبول • خط ارتباط ویژه رستوران‌های تکسیم: 52 24 325 501 90+
      </p>
    </div>
    """

    # 2. WhatsApp 1-Touch Message (Bypassing Meta restriction with manual 1-touch sending)
    wa_text = f"""سلام و درود خدمت مدیریت محترم {r['name_fa']} 🌸

در پایش نظرات گوگل مپ، تریپ‌ادوایزر و یاندکس منطقه تکسیم، عملکرد مجموعه شما بررسی شد:
⭐ ریتینگ گوگل مپ: ★ {r['google_rating']} با {r['google_review_count']:,} نظر مشتریان
📊 پتانسیل درآمدی ساعات خلوت ({r['off_peak_hours']}): امکان کسب +{r['monthly_unlocked_revenue_try']:,} لیر سود ماهانه اضافی

🔑 برای مشاهده پنل اختصاصی و تحلیل دقیق کامنت‌های رستوران شما:
ورود مستقیم بدون نیاز به رمز:
{magic_url}

شناسه توکن: {magic_token}
رمز عبور موقت: {r.get('temp_password', 'Mizban@Taksim2026')}

(این دسترسی تستی و رایگان است و فایل PDF گزارش هفتگی نیز در پنل در دسترس شماست).
تیم پشتیبانی پلتفرم میزبان استانبول 🏛"""

    wa_encoded = urllib.parse.quote(wa_text)
    wa_action_url = f"https://wa.me/{phone_clean}?text={wa_encoded}" if phone_clean else ""

    return {
        "restaurant_id": r["id"],
        "name_fa": r["name_fa"],
        "phone": r["phone"],
        "email": r["email"],
        "magic_token": magic_token,
        "magic_url": magic_url,
        "bot_url": bot_url,
        "email_subject": email_subject,
        "email_html": email_html,
        "whatsapp_text": wa_text,
        "whatsapp_action_url": wa_action_url
    }

def re_clean_phone(phone_str):
    """Strips all non-digit characters except leading plus."""
    digits = "".join(c for c in phone_str if c.isdigit())
    if digits.startswith("0"):
        digits = digits[1:]
    if not digits.startswith("90") and len(digits) == 10:
        digits = "90" + digits
    return digits

if __name__ == "__main__":
    summary = get_taksim_district_summary()
    print("Taksim Gastronomy Benchmark:", json.dumps(summary, ensure_ascii=False, indent=2))
    sample_outreach = generate_restaurant_outreach_package("reyhun-taksim")
    print("\nSample Reyhun Outreach Magic URL:", sample_outreach["magic_url"])
    print("WhatsApp 1-Touch URL:", sample_outreach["whatsapp_action_url"][:90] + "...")
