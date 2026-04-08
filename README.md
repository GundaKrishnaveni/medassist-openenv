---
title: MedAssist AI
emoji: 🏥
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.36.1"
python_version: "3.10"
app_file: app.py
pinned: false
---
# 🏥 MedAssist AI

MedAssist AI is a simple AI-powered medical triage system.

## Features
- Symptom-based diagnosis
- Risk classification (Low / Medium / High)
- Confidence score
- Explainable reasoning

## How it works
The system uses a rule-based scoring model:
- Each symptom contributes to a risk score
- Higher score = higher severity
- Output includes reasoning for transparency

## Example
Input:
- Chest Pain
- Shortness of Breath

Output:
- High Risk
- Immediate hospital recommendation

## Disclaimer
This is not a medical diagnosis tool.