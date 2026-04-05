import gradio as gr

def medassist(symptoms_list):
    score = 0
    reasons = []

    if len(symptoms_list) == 0:
        return "⚠️ Please select at least one symptom."

    if "Chest Pain" in symptoms_list:
        score += 5
        reasons.append("Chest pain indicates possible cardiac issue")

    if "Shortness of Breath" in symptoms_list:
        score += 4
        reasons.append("Breathing difficulty increases risk")

    if "Fatigue" in symptoms_list:
        score += 2
        reasons.append("Fatigue suggests metabolic condition")

    if "Fever" in symptoms_list:
        score += 1
        reasons.append("Fever indicates infection")

    confidence = min(95, score * 10)

    if score >= 7:
        diagnosis = "Possible Heart Attack"
        action = "Go to Hospital Immediately"
        risk = "HIGH 🔴"
    elif score >= 4:
        diagnosis = "Moderate Condition"
        action = "Consult Doctor"
        risk = "MEDIUM 🟡"
    else:
        diagnosis = "Mild Condition"
        action = "Rest"
        risk = "LOW 🟢"

    explanation = "\n".join(reasons)

    return f"""
Diagnosis: {diagnosis}

Risk: {risk}

Confidence: {confidence}%

Action: {action}

Reasoning:
{explanation}
"""

with gr.Blocks() as demo:
    gr.Markdown("# MedAssist AI")

    symptoms = gr.CheckboxGroup(
        ["Chest Pain", "Shortness of Breath", "Fatigue", "Fever"]
    )

    output = gr.Textbox()

    btn = gr.Button("Analyze")

    btn.click(fn=medassist, inputs=symptoms, outputs=output)

demo.launch()