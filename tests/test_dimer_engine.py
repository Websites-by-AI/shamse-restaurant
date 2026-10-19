#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Test Suite for Dimer Intelligence Engine (v2.0):
Verifies the coupling (dimerization) of 100 Hospitality Intelligence Skills
with 30 Specialized Hugging Face AI Models, Lead Prescriptions, and Admin Panel Integration.
"""

import os
import sys
import pytest
import json

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "automation"))

import dimer_intelligence_engine as die
import academic_ai_engine as aae

def test_huggingface_30_models_catalog():
    """Verify that exactly 30 specialized Hugging Face AI models exist with complete metadata."""
    models = die.HUGGINGFACE_30_MODELS
    assert len(models) == 30, f"Expected exactly 30 Hugging Face models, got {len(models)}"
    
    # Check key models presence
    model_ids = [m["hf_id"] for m in models]
    assert "yangheng/deberta-v3-base-absa-v1.1" in model_ids
    assert "dbmdz/bert-base-turkish-cased" in model_ids
    assert "HooshvareLab/bert-fa-zwnj-base" in model_ids
    assert "cardiffnlp/twitter-xlm-roberta-base-sentiment-multilingual" in model_ids
    assert "meta-llama/Meta-Llama-3-8B-Instruct" in model_ids
    assert "mistralai/Mistral-7B-Instruct-v0.3" in model_ids
    assert "aubmindlab/bert-base-arabertv02" in model_ids
    assert "DeepPavlov/rubert-base-cased" in model_ids
    assert "intfloat/multilingual-e5-large" in model_ids

    # Check academic_ai_engine registry reflects all 30 models
    reg = aae.get_huggingface_model_registry()
    assert len(reg) == 30, f"academic_ai_engine must return 30 models, got {len(reg)}"

def test_hospitality_100_skills_integrity():
    """Verify that all 100 hospitality skills across 10 clusters are loaded properly."""
    skills_data = die.load_skills()
    skills = skills_data.get("skills", [])
    clusters = skills_data.get("clusters", [])

    assert len(skills) == 100, f"Expected 100 hospitality skills, found {len(skills)}"
    assert len(clusters) == 10, f"Expected 10 clusters, found {len(clusters)}"

    # Every cluster has 10 skills
    for c in clusters:
        c_skills = [s for s in skills if s.get("cluster_id") == c.get("id")]
        assert len(c_skills) == 10, f"Cluster {c.get('id')} must contain 10 skills, got {len(c_skills)}"

def test_dimerization_coupling_efficiency():
    """Verify that all 100 skills are coupled with HF models without any orphaned units."""
    dimers = die.dimerize_cluster_skills()
    assert len(dimers) == 100, f"Expected 100 dimer pairs, got {len(dimers)}"

    # Check dimer structure
    for d in dimers:
        assert d["skill_id"].startswith("SKILL-"), "Must have valid skill_id"
        assert "/" in d["hf_model_id"], "Must have valid Hugging Face repo path"
        assert d["domain_action"], "Must specify business domain action"
        assert d["neural_acceleration"], "Must specify neural acceleration description"

    summary = die.get_dimer_system_summary()
    assert summary["version"] == "2.0-dimerized-nextgen"
    assert summary["total_dimer_pairs"] == 100
    assert "100%" in summary["coupling_efficiency"]

def test_restaurant_dimer_prescription():
    """Verify automated AI diagnosis and dimer prescription for a given restaurant lead."""
    presc = die.get_restaurant_dimer_prescription("shamse-taksim")
    assert "رستوران شمسه" in presc["venue_name"]
    assert len(presc["prescribed_dimers"]) >= 3
    for p in presc["prescribed_dimers"]:
        assert "SKILL-" in p["skill"]
        assert "/" in p["model"]
        assert p["goal"]

def test_admin_panel_dimer_ui():
    """Verify that intelligence.html contains the Dimerization Engine section and scripts."""
    with open(os.path.join(ROOT, "intelligence.html"), "r", encoding="utf-8") as f:
        html = f.read()

    assert "۱۰.۳ سامانه هوش پیوندی و دایمریزاسیون" in html
    assert "۱۰۰ جفت دایمریزه" in html
    assert "۳۰ مدل HF" in html
    assert "dimerMatrixGridContainer" in html
    assert "renderDimerMatrix" in html
    assert "filterDimerCluster" in html
