import gradio as gr

def medassist(symptoms_list):
    score = 0
    reasons = []

    if len(symptoms_list) == 0:
        return "⚠️ Please select at least one symptom."

    # Core symptoms
    if "Chest Pain" in symptoms_list:
        score += 5
        reasons.append("Chest pain indicates possible cardiac issue")

    if "Shortness of Breath" in symptoms_list:
        score += 4
        reasons.append("Breathing difficulty increases risk")

    if "Fatigue" in symptoms_list:
        score += 2
        reasons.append("Fatigue suggests metabolic or chronic condition")

    if "Fever" in symptoms_list:
        score += 1
        reasons.append("Fever indicates infection")

    # Additional symptoms
    if "Headache" in symptoms_list:
        score += 1
        reasons.append("Headache may indicate neurological or viral condition")

    if "Nausea" in symptoms_list:
        score += 2
        reasons.append("Nausea indicates digestive or systemic issue")

    if "Dizziness" in symptoms_list:
        score += 2
        reasons.append("Dizziness may indicate blood pressure issues")

    if "Cough" in symptoms_list:
        score += 2
        reasons.append("Cough suggests respiratory infection")

    if "Sore Throat" in symptoms_list:
        score += 1
        reasons.append("Sore throat indicates infection")

    if "Abdominal Pain" in symptoms_list:
        score += 3
        reasons.append("Abdominal pain may indicate internal organ issues")

    if "Back Pain" in symptoms_list:
        score += 1
        reasons.append("Back pain may be muscular or structural")

    if "Loss of Appetite" in symptoms_list:
        score += 1
        reasons.append("Loss of appetite indicates systemic illness")

    # Confidence
    confidence = min(95, score * 10)

    # Decision
    if score >= 8:
        diagnosis = "🚨 Possible Critical Condition"
        action = "Go to Hospital Immediately"
        risk = "HIGH 🔴"
    elif score >= 4:
        diagnosis = "⚠️ Moderate Condition"
        action = "Consult Doctor"
        risk = "MEDIUM 🟡"
    else:
        diagnosis = "✅ Mild Condition (Flu/Cold)"
        action = "Rest & Hydration"
        risk = "LOW 🟢"

    explanation = "\n• " + "\n• ".join(reasons)

    return f"""
### 🧠 Diagnosis
{diagnosis}

### ⚡ Risk Level
{risk}

### 📊 Confidence
{confidence}%

### 💊 Recommended Action
{action}

### 🧾 Reasoning
{explanation}

---
⚠️ *This is not a medical diagnosis. Consult a doctor.*
"""

# 🎨 Custom CSS for PRO UI
custom_css = """
body {background: linear-gradient(135deg, #eef2ff, #f8fafc);}
h1 {text-align: center; color: #1e3a8a;}
.container {border-radius: 20px;}
button {background: linear-gradient(90deg, #2563eb, #22c55e) !important; color: white !important; font-weight: bold;}
"""

with gr.Blocks(css=custom_css) as demo:

    gr.Markdown("""
    # 🏥 MedAssist AI
    ### Intelligent Medical Triage System  
    _Analyze symptoms with AI-powered reasoning and confidence scoring_
    """)

    with gr.Row():
        with gr.Column(scale=1):
            gr.Markdown("### 🧾 Select Symptoms")

            symptoms = gr.CheckboxGroup(
                [
                    "Chest Pain", "Shortness of Breath", "Fatigue", "Fever",
                    "Headache", "Nausea", "Dizziness", "Cough",
                    "Sore Throat", "Abdominal Pain", "Back Pain", "Loss of Appetite"
                ],
                label=""
            )

            analyze_btn = gr.Button("🔍 Analyze Patient")

        with gr.Column(scale=1):
            gr.Markdown("### 📊 Analysis Result")

            output = gr.Markdown()

    analyze_btn.click(fn=medassist, inputs=symptoms, outputs=output)

demo.launch()