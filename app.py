import gradio as gr

# smarter logic
def medassist(symptoms_text):
    symptoms = symptoms_text.lower()

    score = 0
    result = {}

    # scoring system
    if "chest pain" in symptoms:
        score += 5
    if "shortness of breath" in symptoms:
        score += 4
    if "fatigue" in symptoms:
        score += 2
    if "fever" in symptoms:
        score += 1

    # decision
    if score >= 7:
        diagnosis = "Possible Heart Attack"
        action = "Go to Hospital Immediately"
        risk = "HIGH"
    elif score >= 4:
        diagnosis = "Possible Diabetes / Moderate Condition"
        action = "Consult Doctor"
        risk = "MEDIUM"
    else:
        diagnosis = "Mild Illness (Flu/Cold)"
        action = "Rest & Hydration"
        risk = "LOW"

    return f"""
Diagnosis: {diagnosis}

Recommended Action: {action}

Risk Level: {risk}
"""

# UI
with gr.Blocks() as demo:
    gr.Markdown("# MedAssist AI 🏥")
    gr.Markdown("Enter patient symptoms to get diagnosis and recommendation")

    inp = gr.Textbox(
        label="Enter Symptoms",
        placeholder="e.g. chest pain, shortness of breath, fatigue"
    )

    out = gr.Textbox(label="Result")

    btn = gr.Button("Analyze")

    btn.click(fn=medassist, inputs=inp, outputs=out)

demo.launch()