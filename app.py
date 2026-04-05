import gradio as gr

def medassist(symptoms_list):
    if not symptoms_list:
        return "Please select at least one symptom."

    score = 0

    if "Chest Pain" in symptoms_list:
        score += 5
    if "Shortness of Breath" in symptoms_list:
        score += 4
    if "Fatigue" in symptoms_list:
        score += 2
    if "Fever" in symptoms_list:
        score += 1

    if score >= 7:
        return "HIGH RISK: Go to hospital immediately"
    elif score >= 4:
        return "MEDIUM RISK: Consult doctor"
    else:
        return "LOW RISK: Rest"

with gr.Blocks() as demo:
    gr.Markdown("# MedAssist AI")

    symptoms = gr.CheckboxGroup(
        ["Chest Pain", "Shortness of Breath", "Fatigue", "Fever"]
    )

    output = gr.Textbox()

    btn = gr.Button("Analyze")

    btn.click(medassist, symptoms, output)

demo.launch()