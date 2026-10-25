#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Hugging Face Space: Çekicin AI — Car Damage & Repair Cost Estimator (KAG/RAG)
Multi-tier bodywork, parts, labor, ADAS calibration & COP31 carbon estimation engine.
"""

import json
import os
import sys

try:
    import gradio as gr
    GRADIO_AVAILABLE = True
except ImportError:
    GRADIO_AVAILABLE = False

from car_damage_kag_engine import CarDamageKAGEngine

engine = CarDamageKAGEngine()

def predict_damage_cost(car_selection, damaged_zone_1, severity_1, damaged_zone_2, severity_2, damaged_zone_3, severity_3):
    damages = []
    if damaged_zone_1 and damaged_zone_1 != "None / Yok":
        damages.append({"part": damaged_zone_1, "severity": severity_1})
    if damaged_zone_2 and damaged_zone_2 != "None / Yok":
        damages.append({"part": damaged_zone_2, "severity": severity_2})
    if damaged_zone_3 and damaged_zone_3 != "None / Yok":
        damages.append({"part": damaged_zone_3, "severity": severity_3})

    if not damages:
        return "⚠️ Lütfen en az bir hasarlı parça seçiniz.", "{}", ""

    est = engine.estimate_damage(car_selection, damages)

    # Format human-friendly summary report
    summary = f"""### 🚗 Araç Ekspertiz & Onarım Maliyet Raporu (KAG Engine v2.0)
**Seçilen Araç Modeli:** {est['vehicle']['matched_model']} (Segment: {est['vehicle']['segment']})

---
#### 💰 Maliyet Özeti:
* **Orijinal (OEM) Parçalı Toplam Fatura:** `{est['summary']['total_oem_invoice_try']:,.2f} ₺`
* **Eşdeğer (A-Kalite Yan Sanayi) Toplam Fatura:** `{est['summary']['total_aftermarket_invoice_try']:,.2f} ₺`
* **İşçilik (Kaporta & Fırın Boya):** `{est['summary']['total_labor_try']:,.2f} ₺`
* **Boya Malzemesi & Sarfiyat:** `{est['summary']['total_paint_materials_try']:,.2f} ₺`
* **ADAS Radar / Kamera Kalibrasyon:** `{est['summary']['total_adas_calibration_try']:,.2f} ₺` {'(Zorunlu)' if est['summary']['adas_recalibration_required'] else '(Gerekmiyor)'}

---
#### 🌱 Çevre & COP31 Karbon Tasarrufu:
* **Önlenen Karbon Salınımı (Onarım Tercihi ile):** `{est['summary']['total_co2_saved_kg']} kg CO2e`
* *Yeni çelik/plastik üretimi yerine onarım yapılarak atmosfere salınmayan emisyon miktarı.*

---
#### 🔍 Parça Bazlı Karar & İşlem Detayları:
"""
    for it in est['breakdown']:
        summary += f"- **{it['part_name_tr']}**: Hasar: `{it['severity']}` ➔ **Karar:** `{it['decision']}`\n"
        if it['is_replacement']:
            summary += f"  - OEM Parça Fiyatı: `{it['oem_part_cost_try']:,.2f} ₺` | Yan Sanayi: `{it['aftermarket_part_cost_try']:,.2f} ₺`\n"
        summary += f"  - Kaporta İşçilik: `{it['labor_kaporta_try']:,.2f} ₺` | Boya İşçilik: `{it['labor_boya_try']:,.2f} ₺`\n"

    summary += "\n#### 📦 Eşleşen Parça Tedarikçileri (Türkiye Sanayi Ağı):\n"
    for s in est['suppliers_matching_tr']:
        summary += f"- **{s['name']}** ({s['type']}): Teslimat süresi ~{s['delivery_hours']} saat | Durum: `{s['stock_status']}`\n"

    json_str = json.dumps(est, ensure_ascii=False, indent=2)
    return summary, json_str

# Common options
CAR_OPTIONS = [f"{c['brand']} {c['model']}" for c in engine.cars]
PART_OPTIONS = [
    "None / Yok",
    "front_bumper_skin (Ön Tampon)",
    "hood_bonnet (Motor Kaputu)",
    "left_front_fender (Sol Ön Çamurluk)",
    "right_front_fender (Sağ Ön Çamurluk)",
    "left_headlight_led (Sol LED Far)",
    "right_headlight_led (Sağ LED Far)",
    "front_grille (Ön Panjur Izgara)",
    "windshield_acoustic (Ön Cam)",
    "left_side_mirror_complete (Sol Dikiz Aynası)",
    "right_side_mirror_complete (Sağ Dikiz Aynası)",
    "front_left_door_shell (Sol Ön Kapı)",
    "rear_bumper_skin (Arka Tampon)",
    "trunk_tailgate_lid (Bagaj Kapağı)",
    "left_taillight_outer (Sol Arka Stop Lambası)",
    "front_radar_acc_sensor (Ön ACC Radar Sensörü)",
    "front_left_lower_control_arm (Sol Ön Salıncak/Süspansiyon)"
]
SEVERITY_OPTIONS = ["scratch", "dent_light", "dent_heavy", "crack", "broken"]

if GRADIO_AVAILABLE:
    with gr.Blocks(title="Çekicin AI - Hasar ve Onarım Maliyet Tahmini") as demo:
        gr.Markdown("# 🚗 Çekicin AI: Oto Hasar & Onarım Maliyet Hesaplayıcı (KAG/RAG)")
        gr.Markdown("Türkiye ve Avrupa pazarındaki 100 popüler araç ve 1.000 parça veri tabanına dayalı yapay zeka ekspertiz motoru.")

        with gr.Row():
            with gr.Column():
                car_dropdown = gr.Dropdown(choices=CAR_OPTIONS, value=CAR_OPTIONS[0], label="Araç Modeli Seçin")

                gr.Markdown("#### Hasar Gören Parça 1:")
                p1 = gr.Dropdown(choices=PART_OPTIONS, value=PART_OPTIONS[1], label="1. Parça")
                s1 = gr.Dropdown(choices=SEVERITY_OPTIONS, value="crack", label="Hasar Türü (Severity)")

                gr.Markdown("#### Hasar Gören Parça 2:")
                p2 = gr.Dropdown(choices=PART_OPTIONS, value=PART_OPTIONS[5], label="2. Parça")
                s2 = gr.Dropdown(choices=SEVERITY_OPTIONS, value="broken", label="Hasar Türü")

                gr.Markdown("#### Hasar Gören Parça 3:")
                p3 = gr.Dropdown(choices=PART_OPTIONS, value=PART_OPTIONS[2], label="3. Parça")
                s3 = gr.Dropdown(choices=SEVERITY_OPTIONS, value="dent_light", label="Hasar Türü")

                btn_calc = gr.Button("🔍 Ekspertiz & Maliyet Analizi Yap", variant="primary")

            with gr.Column():
                output_report = gr.Markdown(label="Ekspertiz Raporu")
                output_json = gr.Code(language="json", label="JSON Çıktısı (API Entegrasyonu için)")

        btn_calc.click(
            fn=predict_damage_cost,
            inputs=[car_dropdown, p1, s1, p2, s2, p3, s3],
            outputs=[output_report, output_json]
        )

if __name__ == "__main__":
    if GRADIO_AVAILABLE:
        demo.launch()
    else:
        print("Gradio not installed locally; app.py ready for HuggingFace deployment.")
