#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Tests for Automotive Damage & Repair Cost KAG / RAG Engine:
  - Database schema integrity (100 car models, 1,000 parts)
  - Decision engine (Repair vs. Replace, PDR, Paint)
  - Cost calculations (OEM vs Aftermarket vs Labor vs Paint)
  - Green COP31 Carbon Savings metrics
  - 5-Case Benchmark verification
  - Hugging Face Space packaging
"""

import os
import sys
import json
import pytest

REPO_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.append(os.path.join(REPO_ROOT, "automation"))

from car_damage_kag_engine import CarDamageKAGEngine
from verify_car_damage_rag import run_benchmarks

def test_database_integrity_100_cars_1000_parts():
    engine = CarDamageKAGEngine()
    assert len(engine.cars) == 100, "Must contain exactly 100 car models"
    assert len(engine.parts) == 1000, "Must contain exactly 1,000 granular parts"

    # Verify key Turkish market models
    brands = {c["brand"] for c in engine.cars}
    assert "Fiat" in brands and "Renault" in brands and "Toyota" in brands and "TOGG" in brands

    # Verify macro assemblies
    macro_assemblies = {p["macro_assembly"] for p in engine.parts.values()}
    assert len(macro_assemblies) == 10

def test_repair_vs_replace_decision_logic():
    engine = CarDamageKAGEngine()
    part_hood = [p for p in engine.parts.values() if "hood_bonnet" in p["sub_assembly"]][0]

    # Light dent on hood should be PDR candidate
    dec_pdr = engine.evaluate_repair_vs_replace(part_hood, "dent_light")
    assert dec_pdr["pdr"] is True
    assert dec_pdr["replace"] is False

    # Broken hood should trigger replacement
    dec_replace = engine.evaluate_repair_vs_replace(part_hood, "broken")
    assert dec_replace["replace"] is True
    assert dec_replace["pdr"] is False

def test_damage_estimation_and_carbon_savings():
    engine = CarDamageKAGEngine()
    res = engine.estimate_damage(
        "Toyota Corolla",
        [
            {"part": "rear_bumper_skin", "severity": "dent_light"},
            {"part": "trunk_tailgate_lid", "severity": "scratch"}
        ]
    )
    assert res["vehicle"]["matched_model"].startswith("Toyota Corolla")
    assert res["summary"]["total_oem_invoice_try"] > 0
    assert res["summary"]["total_aftermarket_invoice_try"] > 0
    # Both are repairs -> carbon should be saved
    assert res["summary"]["total_co2_saved_kg"] > 0
    assert len(res["breakdown"]) == 2
    assert len(res["suppliers_matching_tr"]) >= 2

def test_benchmark_suite_100_percent_pass():
    bench = run_benchmarks()
    assert bench["passed"] == 5
    assert bench["success_rate_percent"] == 100.0

def test_huggingface_space_packaging():
    hf_dir = os.path.join(REPO_ROOT, "huggingface_space")
    assert os.path.exists(os.path.join(hf_dir, "app.py"))
    assert os.path.exists(os.path.join(hf_dir, "README.md"))
    assert os.path.exists(os.path.join(hf_dir, "requirements.txt"))
    assert os.path.exists(os.path.join(hf_dir, "car_damage_database.json"))
    assert os.path.exists(os.path.join(hf_dir, "car_damage_kag_engine.py"))

    with open(os.path.join(hf_dir, "README.md"), "r", encoding="utf-8") as f:
        readme = f.read()
    assert "sdk: gradio" in readme
    assert "Çekicin AI" in readme
