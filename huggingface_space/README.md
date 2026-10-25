---
title: Cekicin AI - Car Damage & Repair Cost Estimator KAG
emoji: 🚗
colorFrom: blue
colorTo: emerald
sdk: gradio
sdk_version: 4.44.0
app_file: app.py
pinned: false
license: apache-2.0
short_description: Multi-tier car damage estimation with 100 cars, 1000 parts, OEM/Aftermarket pricing & COP31 CO2 metrics.
tags:
- automotive
- damage-detection
- cost-estimation
- kag
- rag
- green-mobility
- turkey
---

# 🚗 Çekicin AI: Vehicle Damage & Repair Cost Estimator (KAG / RAG Engine v2.0)

Çekicin AI is a multimodal Knowledge-Augmented Generation (KAG) and Retrieval-Augmented Generation (RAG) platform tailored for roadside assistance, vehicle towing networks, auto insurers, and repair shops (Sanayi Ekosistemi).

## 🌟 Key Features
- **100 Car Models Catalog**: Real-time part pricing indices for top Turkish & European vehicles (Fiat Egea, Renault Clio/Megane, Toyota Corolla, VW Golf, etc.).
- **1,000 Granular Parts & Areas**: Hierarchical ontology across 10 Macro Assemblies (Front End, Lighting, Glazing, Doors, Rear End, Chassis, Suspension, Cooling, ADAS Sensors, Restraints).
- **Repair vs. Replace Decision Engine**: Automatic threshold classification (PDR / Paintless Dent Repair, Plastic Welding, Sheet Metal Pulling, or Full OEM Replacement).
- **Multi-Tier Price Transparency**: Real-time estimates for **Orijinal (OEM)** vs. **Eşdeğer (Yan Sanayi A-Quality)** vs. **Çıkma Parça**.
- **ADAS Recalibration Detection**: Automatically flags radar and forward camera realignment requirements.
- **COP31 Green Carbon Savings**: Computes kilograms of CO2e avoided by choosing panel repair over virgin steel/plastic manufacturing.

## 📊 Dataset & Ontology Architecture
- Built on top of **CarDD (Car Damage Detection)** dataset annotations and Turkish automotive aftermarket pricing benchmarks.
- Covers hourly labor rates for sheet metal bodywork (Kaporta), professional oven spray paint, and paint material expenditure.

## 🚀 Deployment to Hugging Face Spaces
To deploy this Space:
1. Create a new Space on [Hugging Face](https://huggingface.co/new-space) with SDK `Gradio`.
2. Push `app.py`, `car_damage_kag_engine.py`, `car_damage_database.json`, and `requirements.txt`.
3. The Space will build and serve instantly!
