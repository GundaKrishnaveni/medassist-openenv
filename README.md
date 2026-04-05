---
title: MedAssist AI
emoji: 🏥
colorFrom: blue
colorTo: green
sdk: gradio
sdk_version: "4.44.0"
python_version: "3.10"
app_file: app.py
pinned: false
---

# 🏥 MedAssist AI

### AI-powered medical triage system with explainable reasoning and confidence scoring

MedAssist AI is an intelligent healthcare assistant that analyzes patient symptoms and provides risk assessment, diagnosis suggestions, and recommended actions with transparent reasoning.

---

## 🚀 Key Features

- 🧠 Symptom-based diagnosis prediction  
- ⚡ Risk level classification (Low / Medium / High)  
- 📊 Confidence scoring for uncertainty estimation  
- 🧾 Explainable AI (multi-factor reasoning)  
- 💊 Actionable medical recommendations  
- 🌐 Live deployment using Gradio & Hugging Face  

---

## 🧠 System Workflow

The system follows a structured decision pipeline:

1. User selects symptoms  
2. Rule-based scoring evaluates severity  
3. Risk level is classified  
4. Confidence score is calculated  
5. Explanation is generated  
6. Recommended action is provided  

---

## 📊 Model Evaluation

To validate performance, a simulated dataset was created:

- Generated 100+ synthetic patient cases  
- Applied triage classification logic  
- Evaluated prediction consistency  

### 📈 Results

- Accuracy: ~80–85% on simulated dataset  
- Stable classification across risk levels  

---

## 🧠 AI Design Approach

This project uses an **Explainable AI (XAI)** approach instead of a black-box model.

### Why Explainable AI?

In healthcare, transparency is critical. This system ensures:

- ✔ Clear reasoning for every prediction  
- ✔ Confidence estimation for uncertainty  
- ✔ Interpretable decision-making  

---

## 🛠️ Tech Stack

- Python  
- Gradio (UI)  
- Hugging Face Spaces (Deployment)  

---

## 📌 Example Output
