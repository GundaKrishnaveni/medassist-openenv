import gradio as gr

def medassist(symptoms_list):
    if not symptoms_list:
        return "⚠️ Please select at least one symptom."

    score = 0
    reasons = []

    if "Chest Pain" in symptoms_list:
        score += 5
        reasons.append("Chest pain may indicate cardiac issue")

    if "Shortness of Breath" in symptoms_list:
        score += 4
        reasons.append("Breathing difficulty increases risk")

    if "Fatigue" in symptoms_list:
        score += 2
        reasons.append("Fatigue may indicate chronic condition")

    if "Fever" in symptoms_list:
        score += 1
        reasons.append("Fever indicates infection")

    confidence = min(95, score * 10)

    if score >= 7:
        diagnosis = "Possible Heart Attack"
        risk = "HIGH 🔴"
        action = "Go to hospital immediately"
    elif score >= 4:
        diagnosis = "Moderate Condition"
        risk = "MEDIUM 🟡"
        action = "Consult doctor"
    else:
        diagnosis = "Mild Condition"
        risk = "LOW 🟢"
        action = "Rest and hydrate"

    return f"""
Diagnosis: {diagnosis}

Risk Level: {risk}

Confidence: {confidence}%

Recommended Action: {action}

Reasoning:
- {"\n- ".join(reasons)}

Disclaimer: Not a medical diagnosis.
"""

with gr.Blocks() as demo:
    gr.Markdown("# 🏥 MedAssist AI")
    gr.Markdown("AI-powered symptom checker")

    symptoms = gr.CheckboxGroup(
        choices=[
            "Chest Pain",
            "Shortness of Breath",
            "Fatigue",
            "Fever"
        ],
        label="Select Symptoms"
    )

    output = gr.Textbox(label="Result")

    btn = gr.Button("Analyze")

    btn.click(fn=medassist, inputs=symptoms, outputs=output)

# ✅ REQUIRED FOR HF SPACES
demo.launch(share=True)