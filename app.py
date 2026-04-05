import gradio as gr

def run():
    return "MedAssist OpenEnv is running successfully!"

iface = gr.Interface(
    fn=run,
    inputs=[],
    outputs="text"
)

iface.launch()