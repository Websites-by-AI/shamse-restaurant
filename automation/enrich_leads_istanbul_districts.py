#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Enriches all 100 leads in automation/collaboration_calendar_100.json
with the top city and specific gastronomic district in each country
that mirrors Istanbul's restaurant scene (Taksim, İstiklal, Kadıköy).

City and Area Mapping:
  1. TR: Istanbul -> Beyoğlu (Taksim / İstiklal) & Kadıköy (Moda Çarşı)
  2. IR: Tehran -> Si-e Tir Street & Tajrish Bazaar / Sattarkhan
  3. DE: Berlin -> Kreuzberg (SO36 / Kottbusser Tor) & Neukölln (Sonnenallee - "Little Istanbul")
  4. SE: Malmö -> Möllevången ("Möllan") & Stockholm (Kista / Rinkeby)
  5. AE: Dubai -> Deira (Al Rigga & Al Muraqqabat) & Satwa (Al Dhiyafah)
  6. US: New York -> South Paterson, NJ ("Little Istanbul") & Astoria, Queens (Steinway St)
  7. CA: Toronto -> North York (Yonge St "Persian/Middle Eastern Corridor") & Mississauga (Ridgeway Plaza)
  8. GB: London / Leeds -> London Green Lanes (Harringay "Little Turkey") & Edgware Road / Leeds (Harehills)
  9. FR: Paris -> 10th Arrondissement (Faubourg Saint-Denis / Strasbourg Saint-Denis)
  10. NL: Rotterdam -> Oude Noorden / Zwart Janstraat ("Turkish/Mediterranean Corridor") & West-Kruiskade
"""

import os
import json

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
CAL_PATH = os.path.join(REPO_ROOT, "automation", "collaboration_calendar_100.json")

# Istanbul-like dining hubs metadata for each of the 10 countries
COUNTRY_DISTRICTS = {
    "TR": {
        "city": "استانبول (Istanbul)",
        "area": "بی‌اوغلو (تکسیم و خیابان استقلال) و کادیکوی",
        "area_en": "Beyoğlu (Taksim & İstiklal) & Kadıköy Çarşı",
        "istanbul_parallel": "خاستگاه و بنچ‌مارک اصلی؛ قلب تپنده کافه‌نشینی شبانه، کبابخانه‌های سنتی و ترافیک توریستی پیاده‌راه استقلال."
    },
    "IR": {
        "city": "تهران (Tehran)",
        "area": "خیابان سی تیر، بازار تجریش و ستارخان",
        "area_en": "30 Tir Street, Tajrish Bazaar & Sattarkhan",
        "istanbul_parallel": "مشابه‌ترین فضای شبانه با سنگ‌فرش‌های سی تیر، دود زغال کباب‌ها، سماورهای زغالی و حال‌وهوای کافه‌های خیابانی کاراکوی و تکسیم."
    },
    "DE": {
        "city": "برلین (Berlin)",
        "area": "کروزبرگ (Kottbusser Tor) و نویکلن (خیابان زونن‌آله Sonnenallee)",
        "area_en": "Kreuzberg (SO36) & Neukölln (Sonnenallee - 'Little Istanbul')",
        "istanbul_parallel": "معروف به «استانبول کوچک» در اروپا؛ شلوغ‌ترین راسته کباب‌های زغالی، باقلوای تازه و چایخانه‌هایی که تا ساعت ۴ صبح مثل استقلال فعالند."
    },
    "SE": {
        "city": "مالمو (Malmö) / استکهلم",
        "area": "مولوانگن (Möllevången - 'Möllan') در مالمو و شیستا در استکهلم",
        "area_en": "Möllevången ('Möllan', Malmö) & Kista (Stockholm)",
        "istanbul_parallel": "میدان مرکزی خوراک چندفرهنگی سوئد؛ بازار روزانه روباز و خیابان‌های پر از کبابخانه‌های زغالی و شاورما با حس‌وحال بازارهای تاریخی استانبول."
    },
    "AE": {
        "city": "دبی (Dubai)",
        "area": "دیره (خیابان‌های الرقه و المرقبات) و خیابان الضیافه سطوه",
        "area_en": "Deira (Al Rigga & Al Muraqqabat) & Satwa (Al Dhiyafah)",
        "istanbul_parallel": "پیاده‌راه‌های همیشه روشن و پر از توریست شبانه دبی، با رستوران‌های سنتی ایرانی و ترک و سرویس‌دهی ۲۴ ساعته مشابه تکسیم."
    },
    "US": {
        "city": "نیویورک / نیوجرسی (New York / NJ)",
        "area": "ساوت پترسون (South Paterson - 'Little Istanbul') و کوئینز (Steinway St آستوریا)",
        "area_en": "South Paterson, NJ ('Little Istanbul') & Steinway St (Astoria, Queens)",
        "istanbul_parallel": "پترسون رسماً با عنوان «استانبول کوچک» نام‌گذاری شده با بیشترین تراکم نانوایی‌های ترک و کباب؛ و خیابان اشتاین‌وی قطب کافه‌نشینی مدیترانه‌ای نیویورک است."
    },
    "CA": {
        "city": "تورنتو (Toronto)",
        "area": "نورث یورک (راسته یانگ بین فینچ و شپرد) و پلازای ریج‌وی میسیساگا",
        "area_en": "North York (Yonge St Corridor) & Ridgeway Plaza (Mississauga)",
        "istanbul_parallel": "راسته خیابان یانگ معروف به کوریدور خاورمیانه و طعم‌های اصیل، و پلازای ریج‌وی میدان غذاهای شبانه‌روزی با ترافیک پیاده مشابه میدان تکسیم."
    },
    "GB": {
        "city": "لندن و لیدز (London & Leeds)",
        "area": "گرین لینز (Green Lanes - هیرینگی لندن) و راسته هر Essas لیدز (Harehills)",
        "area_en": "London Green Lanes (Harringay 'Little Turkey') & Leeds (Harehills/Centre)",
        "istanbul_parallel": "راسته گرین لینز به عنوان «خیابان استقلال لندن» شناخته می‌شود؛ منقل‌های زغالی ۲۴ ساعته (Gokyuzu) و عطر پیده تازه و چای ترکی که لیدز و لندن را تغذیه می‌کند."
    },
    "FR": {
        "city": "پاریس (Paris)",
        "area": "منطقه ۱۰ (خیابان فوبورگ سن‌دنی Faubourg Saint-Denis و استراسبورگ)",
        "area_en": "10th Arrondissement (Faubourg Saint-Denis / Strasbourg Saint-Denis)",
        "istanbul_parallel": "کوچه پس‌کوچه‌های زنده و پرشور پاریس با بوی نان تازه، لاهماجون، تنورهای سنتی و کافه‌های متراکم که دقیقاً فضای محله‌های بی‌اوغلو را تداعی می‌کند."
    },
    "NL": {
        "city": "روتردام (Rotterdam) / آمستردام",
        "area": "محله اوده نوردن (خیابان Zwart Janstraat) و کروسکاده (West-Kruiskade)",
        "area_en": "Rotterdam (Zwart Janstraat - 'Turkish Corridor') & West-Kruiskade",
        "istanbul_parallel": "پایتخت گاسترونومی هلند و راسته زوارت یان‌استرات؛ زنجیره پیوسته کبابخانه‌ها، شیرینی‌پزی‌های سنتی و چایخانه‌های اصیل دقیقاً شبیه بازار کادیکوی."
    }
}

def enrich_leads_with_districts():
    with open(CAL_PATH, "r", encoding="utf-8") as f:
        data = json.load(f)

    # Add districts metadata to countries
    for code, info in COUNTRY_DISTRICTS.items():
        if code in data["countries"]:
            data["countries"][code]["top_city"] = info["city"]
            data["countries"][code]["top_area"] = info["area"]
            data["countries"][code]["top_area_en"] = info["area_en"]
            data["countries"][code]["istanbul_parallel"] = info["istanbul_parallel"]

    # Enrich each of the 100 leads
    for lead in data["leads"]:
        c_code = lead["country"]
        dist_info = COUNTRY_DISTRICTS.get(c_code, {})
        
        lead["city"] = dist_info.get("city", "مرکز گردشگری")
        lead["area"] = dist_info.get("area", "راسته پرتردد گاسترونومی")
        lead["area_en"] = dist_info.get("area_en", "Gastronomic Corridor")
        lead["istanbul_parallel"] = dist_info.get("istanbul_parallel", "")
        
        # Enrich the v2_hook with the district context
        original_hook = lead["v2_hook"]
        area_short = dist_info.get("area", "").split(" و ")[0].split(" (")[0]
        lead["district_context"] = f"اتصال به نبض غذایی {area_short} در مقایسه با تکسیم استانبول"

    with open(CAL_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=2)

    print(f"Successfully enriched all 100 leads with Istanbul-like cities and areas in {CAL_PATH}")

if __name__ == "__main__":
    enrich_leads_with_districts()
