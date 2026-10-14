# 🚀 راهنمای استقرار — وب‌سایت رستوران شمسه

سایت روی **سه پلتفرم** به‌صورت هم‌زمان منتشر شده است و همه از **یک مخزن** تغذیه می‌شوند:

## 🌐 لینک‌های زنده

| # | پلتفرم | نشانی | نحوهٔ استقرار |
|---|---|---|---|
| 1 | 🐙 **GitHub Pages** | https://websites-by-ai.github.io/shamse-restaurant/ | خودکار از برنچ `main` |
| 2 | 🌩 **Cloudflare Pages** | https://shamse-restaurant.pages.dev | خودکار با GitHub Actions |
| 3 | 🤗 **Hugging Face Space** | https://huggingface.co/spaces/Sosa654321/shamse-restaurant | خودکار با GitHub Actions |

📦 **مخزن اصلی:** https://github.com/Websites-by-AI/shamse-restaurant

---

## ⚙️ انتشار خودکار (CI/CD)

فایل `.github/workflows/deploy.yml` با هر **push روی برنچ main** دو کار انجام می‌دهد:

**۱) 🌩 Cloudflare Pages**
- پوشهٔ `_site/` ساخته می‌شود (index.html + preview.html + assets)
- فایل `_headers` برای کش یک‌سالهٔ تصاویر و هدرهای امنیتی تولید می‌شود
- انتشار با `cloudflare/wrangler-action@v3` روی پروژهٔ `shamse-restaurant`

**۲) 🤗 Hugging Face Space**
- پوشهٔ `_space/` به‌همراه `README.md` (کارت اسپیس با `sdk: static`) ساخته می‌شود
- آپلود با کتابخانهٔ `huggingface_hub` + `hf_xet` (الزام جدید هاب برای فایل‌های باینری)

**اجرای دستی:** GitHub → تب **Actions** → «Deploy website (Cloudflare Pages + Hugging Face Space)» → **Run workflow**

---

## 🔑 سکرت‌های مخزن (تنظیم‌شده ✅)

مسیر: `Settings → Secrets and variables → Actions`

| نام سکرت | کاربرد | وضعیت |
|---|---|---|
| `CLOUDFLARE_API_TOKEN` | انتشار روی Cloudflare Pages | ✅ تنظیم شد |
| `CLOUDFLARE_ACCOUNT_ID` | شناسهٔ اکانت کلادفلر | ✅ تنظیم شد |
| `HF_TOKEN` | آپلود روی Hugging Face Space | ✅ تنظیم شد |

> ⚠️ **مهم:** این سکرت‌ها در GitHub **رمزنگاری‌شده** ذخیره می‌شوند (`libsodium sealed box`) و در کد یا مخزن قابل مشاهده نیستند.
> اگر توکن‌ها را Revoke/Roll کردید، مقدار سکرت‌ها را همین‌جا به‌روز کنید، وگرنه ورک‌فلو خطا می‌دهد:
> `Settings → Secrets and variables → Actions → Update`

---

## 📊 وضعیت آخرین انتشار

| مورد | نتیجه |
|---|---|
| ورک‌فلوی GitHub Actions | ✅ **موفق** (هر دو جاب) |
| 🌩 job کلادفلر | ✅ `Publish to Cloudflare Pages` |
| 🤗 job هاگینگ‌فیس | ✅ `Publish to Hugging Face Space` |
| تست مرورگر (رندر + کنسول) | ✅ ۰ خطای کنسول · عنوان و همهٔ بخش‌ها سالم · ارتفاع کامل صفحه ۱۲٬۸۸۶px |
| تصاویر | ✅ همه به‌جز جای‌نگهدارِ خالی لایت‌باکس (طبیعی) |
| هدرها روی CF | ✅ `cache-control: public, max-age=31536000, immutable` + `nosniff` |

---

## 🧩 ساختار انتشار

```
shamse-restaurant/                    ← مخزن
├── index.html                        ← سایت اصلی
├── preview.html                      ← نسخهٔ تک‌فایل (تصاویر base64)
├── assets/img/*.jpg                  ← ۱۰ تصویر
├── build.py                          ← ساخت هر دو فایل بالا
├── .github/workflows/deploy.yml      ← CI/CD → Cloudflare + Hugging Face
└── README.md
```

**پلتفرم‌ها چه چیزی را سرو می‌کنند؟**
- **GitHub Pages:** کل مخزن از ریشه (`/` → `index.html`)
- **Cloudflare Pages:** پوشهٔ `_site` (index, preview, assets, _headers)
- **HF Space:** `_space` (index, preview, assets, README کارت اسپیس)
