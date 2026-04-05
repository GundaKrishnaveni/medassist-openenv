import gradio as gr

def medassist(symptoms_list):
    score = 0
    reasons = []

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

    # Confidence calculation
    confidence = min(95, score * 12)

    # Uncertainty handling
    if len(symptoms_list) == 0:
        return "⚠️ Please select at least one symptom."

    if score >= 7:
        diagnosis = "Possible Heart Attack"
        action = "Go to Hospital Immediately"
        risk = "HIGH 🔴"
    elif score >= 4:
        diagnosis = "Possible Moderate Condition"
        action = "Consult Doctor"
        risk = "MEDIUM 🟡"
    else:
        diagnosis = "Mild Illness (Flu/Cold)"
        action = "Rest & Hydration"
        risk = "LOW 🟢"

    explanation = "\n".join(reasons)

    return f"""🧠 Diagnosis: {diagnosis}

⚡ Risk Level: {risk}

📊 Confidence: {confidence}%

💊 Recommended Action: {action}

🧾 Reasoning:
{explanation}

⚠️ Disclaimer: This is not a medical diagnosis. Consult a doctor.
"""


with gr.Blocks() as demo:

    gr.Markdown("# 🏥 MedAssist AI")
    gr.Markdown("### AI-powered medical triage system with explainable reasoning")

    symptoms = gr.CheckboxGroup(
        ["Chest Pain", "Shortness of Breath", "Fatigue", "Fever"],
        label="Select Symptoms"
    )

    output = gr.Textbox(label="Analysis Result")

    btn = gr.Button("Analyze Patient")

    btn.click(fn=medassist, inputs=symptoms, outputs=output)

demo.launch()