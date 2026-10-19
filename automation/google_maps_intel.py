#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
ماژول تحلیل داده‌های عمیق گوگل مپ و تولید پیام آمادهٔ همکاری B2B رستوران‌ها.
Google Maps Deep Intelligence & B2B Partnership Outreach Generator.

شامل:
۱) اطلاعات اعتبارسنجی‌شده گوگل مپ ۱۹ رستوران (Place ID, CID, ریتینگ، نظرات، مختصات، تصاویر)
۲) بنچ‌مارک پروژه‌های برتر گیت‌هاب برای اسکرپ داده‌ها و ستاره‌های آن‌ها (GitHub Stars)
۳) ژنراتور هوشمند پیام‌های آمادهٔ همکاری و دعوت به تیم هوش مصنوعی میزبان استانبول
"""

import json
import os
import urllib.parse

DATA_FILE = os.path.join(os.path.dirname(__file__), "google_maps_intel.json")

GITHUB_SCRAPERS_BENCHMARK = [
    {
        "repo": "gosom/google-maps-scraper",
        "url": "https://github.com/gosom/google-maps-scraper",
        "stars": "6.6k+",
        "stars_num": 6600,
        "language": "Go",
        "license": "MIT",
        "status": "Active / Maintained",
        "extracted_fields": [
            "Place ID", "CID", "Rating", "Review Count", "Full Reviews",
            "Owner Responses", "Coordinates (Lat/Lng)", "Photos", "Phone", "Email", "Website"
        ],
        "strengths": "سرعت و همروندی خارق‌العاده به زبان Go، پشتیبانی از CLI، رابط تحت وب (Web UI) و REST API، قابلیت اجرا در کانتینر Docker و بدون نیاز به کلید تجاری گوگل."
    },
    {
        "repo": "omkarcloud/google-maps-scraper",
        "url": "https://github.com/omkarcloud/google-maps-scraper",
        "stars": "3.6k+",
        "stars_num": 3600,
        "language": "Python / JavaScript",
        "license": "Freemium / Open-source",
        "status": "Active / Maintained",
        "extracted_fields": [
            "50+ Data Points", "Social Profiles (IG/FB)", "Review Sentiments", "Business Emails", "Opening Hours"
        ],
        "strengths": "استخراج بیش از ۵۰ نقطه داده تجاری، کشف خودکار ایمیل و پروفایل شبکه‌های اجتماعی رستوران‌ها جهت کمپین‌های ایمیل مارکتینگ و ارتباط مستقیم با مالکان."
    },
    {
        "repo": "gaspa93/googlemaps-scraper",
        "url": "https://github.com/gaspa93/googlemaps-scraper",
        "stars": "522+",
        "stars_num": 522,
        "language": "Python / Selenium",
        "license": "MIT",
        "status": "Active",
        "extracted_fields": [
            "Deep Historical Reviews", "Review Timestamps", "Reviewer Profiles", "MongoDB Sync"
        ],
        "strengths": "تخصصی‌ترین پروژه برای واکشی عمیق کامنت‌ها و ذخیره‌سازی افزایشی (Incremental) در پایگاه داده MongoDB برای پایش دوره‌ای تغییرات احساسات مشتریان."
    },
    {
        "repo": "noworneverev/google-maps-scraper",
        "url": "https://github.com/noworneverev/google-maps-scraper",
        "stars": "380+",
        "stars_num": 380,
        "language": "Node.js / Headless",
        "license": "MIT",
        "status": "Active",
        "extracted_fields": [
            "Places Details", "Reviews without API Keys", "Sub-ratings (Food, Service, Atmosphere)"
        ],
        "strengths": "سرعت بالا در استخراج جزئیات تفکیکی ریتینگ شامل کیفیت غذا، کیفیت سرویس، و اتمسفر بدون پرداخت هزینه‌های دلاری Google Places API."
    },
    {
        "repo": "omkarcloud/google-maps-reviews-scraper",
        "url": "https://github.com/omkarcloud/google-maps-reviews-scraper",
        "stars": "189+",
        "stars_num": 189,
        "language": "Python",
        "license": "MIT",
        "status": "Active",
        "extracted_fields": [
            "Review Filtering by Rating", "Keyword Search in Reviews", "Sentiment Scoring"
        ],
        "strengths": "فیلتر پیشرفته بر اساس بدترین نظرات (Lowest Rating) و کلیدواژه‌های بحرانی نظیر تاخیر، قیمت و مسمومیت غذایی جهت تریاژ سریع بحران‌ها."
    },
    {
        "repo": "Petey1337/google-review-scraper",
        "url": "https://github.com/Petey1337/google-review-scraper",
        "stars": "150+",
        "stars_num": 150,
        "language": "TypeScript / Puppeteer",
        "license": "MIT",
        "status": "Active",
        "extracted_fields": [
            "reviewId", "Reviewer Profile Pictures", "Review Food Photos", "Owner Response Sync"
        ],
        "strengths": "اسکرپر مدرن ضد شناسایی (Stealth Mode) که عکس‌های پیوست‌شده توسط مشتریان به نظرات و پاسخ‌های مدیر رستوران را به طور کامل دانلود و ثبت می‌کند."
    }
]


def load_gmaps_intel():
    """بارگذاری پایگاه داده کامل گوگل مپ ۱۹ رستوران."""
    with open(DATA_FILE, "r", encoding="utf-8") as f:
        return json.load(f)


def get_gmaps_by_id(restaurant_id):
    """یافتن اطلاعات گوگل مپ یک رستوران بر اساس شناسه."""
    data = load_gmaps_intel()
    for r in data:
        if r["id"] == restaurant_id:
            return r
    return None


def get_github_scrapers():
    """دریافت لیست و بنچ‌مارک پروژه‌های برتر گیت‌هاب با تعداد ستاره‌ها."""
    return GITHUB_SCRAPERS_BENCHMARK


def generate_b2b_outreach(restaurant_id):
    """تولید پکیج کامل پیام آمادهٔ همکاری B2B شامل لینک واتس‌اپ و متغیرهای شخصی‌سازی‌شده."""
    r = get_gmaps_by_id(restaurant_id)
    if not r:
        return None
    
    msg = r.get("outreach_message_fa", "")
    encoded_msg = urllib.parse.quote(msg)
    wa_num = r.get("whatsapp", "").replace("+", "").replace(" ", "")
    wa_url = f"https://wa.me/{wa_num}?text={encoded_msg}" if wa_num else ""
    
    return {
        "restaurant_id": r["id"],
        "name_fa": r["name_fa"],
        "name_en": r["name_en"],
        "google_rating": r["google_rating"],
        "google_review_count": r["google_review_count"],
        "google_place_id": r["google_place_id"],
        "neighborhood_fa": r["neighborhood_fa"],
        "collaboration_angle": r["collaboration_angle"],
        "message_text": msg,
        "whatsapp_url": wa_url,
        "phone": r["phone"]
    }


if __name__ == "__main__":
    items = load_gmaps_intel()
    print(f"Loaded {len(items)} restaurants with Google Maps intelligence.")
    scrapers = get_github_scrapers()
    print(f"Loaded {len(scrapers)} top GitHub scraper repos with up to {scrapers[0]['stars']} stars.")
