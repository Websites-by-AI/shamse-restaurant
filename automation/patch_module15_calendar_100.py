#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Injects the 100-Lead Collaboration Calendar and live country/domain filter
into Module 15 in intelligence.html.
"""

import os
import json

REPO_ROOT = "/home/user/shamse-restaurant"
INTEL_HTML = os.path.join(REPO_ROOT, "intelligence.html")
CALENDAR_JSON = os.path.join(REPO_ROOT, "automation", "collaboration_calendar_100.json")

with open(CALENDAR_JSON, "r", encoding="utf-8") as f:
    cal_data = json.load(f)

leads = cal_data.get("leads", [])

# Let's generate the table rows in HTML
leads_rows_html = ""
for lead in leads:
    c_flag = cal_data["countries"][lead["country"]]["flag"]
    c_name = cal_data["countries"][lead["country"]]["name_fa"]
    d_name = cal_data["domains"][lead["domain"]]["title_fa"]
    q_name = cal_data["domains"][lead["domain"]]["quarter"]
    
    leads_rows_html += f'''
      <tr class="cal-row" data-domain="{lead['domain']}" data-country="{lead['country']}">
        <td style="font-family:monospace;font-size:.74rem;color:var(--copper)">{lead['id']}</td>
        <td><b>{c_flag} {c_name}</b></td>
        <td><span class="badge" style="background:var(--ink-3);border:1px solid var(--line);font-size:.72rem">{d_name}</span></td>
        <td><b style="color:var(--cream);font-size:.85rem">{lead['entity_name']}</b><br><span style="font-size:.72rem;color:var(--muted)">{lead['contact_title']} • {lead['website']}</span></td>
        <td style="font-size:.76rem;color:var(--text);max-width:240px;line-height:1.5">{lead['pain']}</td>
        <td style="font-size:.74rem;color:#2ecc71;max-width:220px;line-height:1.5">{lead['v2_hook']}</td>
        <td><span style="font-size:.72rem;background:rgba(210,154,90,0.15);color:var(--copper);padding:2px 6px;border-radius:2px">{q_name}</span></td>
        <td>
          <button class="btn btn--ghost" onclick="loadLeadToV2Sim('{lead['id']}', '{lead['entity_name'].replace("'", "\\'")}')" style="font-size:.7rem;padding:2px 8px">
            تست v2 ↗
          </button>
        </td>
      </tr>
'''

CALENDAR_SECTION_HTML = f'''
      <!-- 100-LEAD INTERNATIONAL COLLABORATION CALENDAR (10 DOMAINS x 10 COUNTRIES) -->
      <div style="background:var(--ink-2);border:1px solid var(--line-copper);border-radius:6px;padding:22px;margin-top:24px">
        <div style="display:flex;justify-content:space-between;align-items:center;margin-bottom:14px;flex-wrap:wrap;gap:12px">
          <div>
            <h4 style="color:var(--cream);font-size:1.15rem;margin:0 0 4px 0;font-weight:800;display:flex;align-items:center;gap:8px">
              <span>🌍 سالنامه جامع و بانک ۱۰۰ لید بین‌المللی در ۱۰ حوزه و ۱۰ کشور جهان</span>
            </h4>
            <p style="font-size:.82rem;color:var(--muted);margin:0">
              ۱۰ حوزه تخصصی (برندها، یوتیوبرها، دانشگاه‌ها، دولت، سرآشپزها، بیمارستان‌ها، کرادفاندینگ، شتاب‌دهنده‌ها، سمن‌ها، اکسپوها) × ۱۰ کشور کلیدی
            </p>
          </div>
          <div style="display:flex;gap:8px">
            <span style="background:rgba(46,204,113,0.15);color:#2ecc71;border:1px solid #2ecc71;padding:3px 10px;border-radius:12px;font-size:.76rem;font-weight:bold">
              ۱۰۰ لید فعال و آماده ارسال
            </span>
          </div>
        </div>

        <!-- 4-QUARTER CALENDAR ROADMAP -->
        <div style="display:grid;grid-template-columns:repeat(auto-fit,minmax(220px,1fr));gap:10px;margin-bottom:18px">
          <div style="background:var(--ink-1);border:1px solid var(--line);border-right:3px solid #38bdf8;padding:10px;border-radius:4px">
            <b style="color:#38bdf8;font-size:.82rem">فصل اول (Q1) - بهار</b>
            <div style="font-size:.74rem;color:var(--cream);margin-top:2px">برندهای غذایی و نهادهای دولتی / شهرداری‌ها</div>
            <div style="font-size:.7rem;color:var(--muted)">توسعه فرانچایز و ساماندهی توریسم حلال</div>
          </div>
          <div style="background:var(--ink-1);border:1px solid var(--line);border-right:3px solid #2ecc71;padding:10px;border-radius:4px">
            <b style="color:#2ecc71;font-size:.82rem">فصل دوم (Q2) - تابستان</b>
            <div style="font-size:.74rem;color:var(--cream);margin-top:2px">یوتیوبرها، سرآشپزهای بین‌المللی و سمن‌ها</div>
            <div style="font-size:.7rem;color:var(--muted)">مستندسازی طعم اصیل و ایونت‌های دیپلماسی غذا</div>
          </div>
          <div style="background:var(--ink-1);border:1px solid var(--line);border-right:3px solid #ffd21e;padding:10px;border-radius:4px">
            <b style="color:#ffd21e;font-size:.82rem">فصل سوم (Q3) - پاییز</b>
            <div style="font-size:.74rem;color:var(--cream);margin-top:2px">دانشگاه‌ها، بیمارستان‌ها و اکسپوهای فرانچایز</div>
            <div style="font-size:.7rem;color:var(--muted)">مدیکال توریسم، غرفه‌های نمایشگاهی و کارآموزی</div>
          </div>
          <div style="background:var(--ink-1);border:1px solid var(--line);border-right:3px solid #e1306c;padding:10px;border-radius:4px">
            <b style="color:#e1306c;font-size:.82rem">فصل چهارم (Q4) - زمستان</b>
            <div style="font-size:.74rem;color:var(--cream);margin-top:2px">کرادفاندینگ و شتاب‌دهنده‌های فودتک</div>
            <div style="font-size:.7rem;color:var(--muted)">تأمین مالی شعب و جذب استارتاپ‌های نرم‌افزاری</div>
          </div>
        </div>

        <!-- FILTERS -->
        <div style="display:flex;gap:12px;margin-bottom:14px;flex-wrap:wrap;background:var(--ink-1);padding:12px;border-radius:4px;border:1px solid var(--line)">
          <div style="flex:1;min-width:180px">
            <label style="display:block;font-size:.76rem;color:var(--muted);margin-bottom:4px">فیلتر بر اساس کشور:</label>
            <select id="calCountryFilter" onchange="filterCalRows()" style="width:100%;background:var(--ink-2);border:1px solid var(--line);color:var(--cream);padding:6px;border-radius:4px;font-size:.8rem">
              <option value="ALL">همه کشورها (۱۰ کشور)</option>
              <option value="TR">🇹🇷 ترکیه (Turkey)</option>
              <option value="IR">🇮🇷 ایران (Iran)</option>
              <option value="DE">🇩🇪 آلمان (Germany)</option>
              <option value="SE">🇸🇪 سوئد (Sweden)</option>
              <option value="AE">🇦🇪 امارات (UAE)</option>
              <option value="US">🇺🇸 آمریکا (USA)</option>
              <option value="CA">🇨🇦 کانادا (Canada)</option>
              <option value="GB">🇬🇧 انگلیس (UK)</option>
              <option value="FR">🇫🇷 فرانسه (France)</option>
              <option value="NL">🇳🇱 هلند (Netherlands)</option>
            </select>
          </div>

          <div style="flex:1;min-width:200px">
            <label style="display:block;font-size:.76rem;color:var(--muted);margin-bottom:4px">فیلتر بر اساس حوزه همکاری:</label>
            <select id="calDomainFilter" onchange="filterCalRows()" style="width:100%;background:var(--ink-2);border:1px solid var(--line);color:var(--cream);padding:6px;border-radius:4px;font-size:.8rem">
              <option value="ALL">همه حوزه‌ها (۱۰ حوزه)</option>
              <option value="brands">برندها و زنجیره‌های غذایی</option>
              <option value="creators">یوتیوبرها و فودبلاگرها</option>
              <option value="universities">دانشگاه‌ها و آکادمی‌های هتلداری</option>
              <option value="government">دولت، شهرداری‌ها و گردشگری</option>
              <option value="specialists">سرآشپزها و متخصصین هتلداری</option>
              <option value="medical">بیمارستان‌ها و مدیکال توریسم</option>
              <option value="crowdfunding">پلتفرم‌های تأمین مالی و کرادفاندینگ</option>
              <option value="accelerators">شتاب‌دهنده‌ها و هاب‌های فودتک</option>
              <option value="ngos">انجمن‌های صنفی و سمن‌ها</option>
              <option value="events">اکسپوهای فرانچایز و فستیوال‌ها</option>
            </select>
          </div>

          <div style="display:flex;align-items:flex-end">
            <span id="calCountBadge" style="font-size:.8rem;color:var(--copper);padding:6px 12px;background:var(--ink-3);border:1px solid var(--line-copper);border-radius:4px">
              نمایش ۱۰۰ از ۱۰۰ لید
            </span>
          </div>
        </div>

        <!-- LEADS TABLE -->
        <div class="table-wrap" style="max-height:480px;overflow-y:auto">
          <table class="bench-table" style="font-size:.82rem">
            <thead>
              <tr>
                <th>شناسه</th>
                <th>کشور</th>
                <th>حوزه</th>
                <th>نام سازمان / مخاطب</th>
                <th>درد عملیاتی شناسایی‌شده</th>
                <th>پیشنهاد ارزش نسخه ۲</th>
                <th>فصل</th>
                <th>عملیات</th>
              </tr>
            </thead>
            <tbody id="calTableBody">
              {leads_rows_html}
            </tbody>
          </table>
        </div>

      </div>
'''

JS_ADDITION = '''
      function filterCalRows() {
        var country = document.getElementById('calCountryFilter').value;
        var domain = document.getElementById('calDomainFilter').value;
        var rows = document.querySelectorAll('.cal-row');
        var visibleCount = 0;

        rows.forEach(function(row) {
          var rCountry = row.getAttribute('data-country');
          var rDomain = row.getAttribute('data-domain');

          var matchCountry = (country === 'ALL' || rCountry === country);
          var matchDomain = (domain === 'ALL' || rDomain === domain);

          if (matchCountry && matchDomain) {
            row.style.display = '';
            visibleCount++;
          } else {
            row.style.display = 'none';
          }
        });

        document.getElementById('calCountBadge').textContent = 'نمایش ' + visibleCount + ' از ۱۰۰ لید';
      }

      function loadLeadToV2Sim(leadId, leadName) {
        var sel = document.getElementById('v2EntitySelect');
        var exists = false;
        for (var i = 0; i < sel.options.length; i++) {
          if (sel.options[i].value === leadName) {
            sel.selectedIndex = i;
            exists = true;
            break;
          }
        }
        if (!exists) {
          var opt = document.createElement('option');
          opt.value = leadName;
          opt.textContent = leadName + ' (' + leadId + ')';
          sel.appendChild(opt);
          sel.value = leadName;
        }
        updateV2Simulation();
        var card = document.getElementById('v2SimSubject');
        if (card) {
          card.scrollIntoView({ behavior: 'smooth', block: 'center' });
        }
      }
'''

with open(INTEL_HTML, "r", encoding="utf-8") as f:
    html = f.read()

# Target insertion before </section> of Module 15
target_section_end = '</section>\n\n    <!-- JAVASCRIPT LOGIC FOR MODULE 15 -->'
if 'CALENDAR_SECTION_HTML' not in html and '100-LEAD INTERNATIONAL COLLABORATION CALENDAR' not in html:
    html = html.replace(target_section_end, CALENDAR_SECTION_HTML + '\n    </section>\n\n    <!-- JAVASCRIPT LOGIC FOR MODULE 15 -->', 1)
    # Also add JS functions
    html = html.replace('document.addEventListener("DOMContentLoaded", function() {', JS_ADDITION + '\n\n      document.addEventListener("DOMContentLoaded", function() {', 1)
    
    with open(INTEL_HTML, "w", encoding="utf-8") as f:
        f.write(html)
    print("Injected 100-Lead Collaboration Calendar into Module 15!")
else:
    print("Calendar already present in Module 15!")
