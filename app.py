import gradio as gr

def hello():
    return "MedAssist OpenEnv is running"

gr.Interface(fn=hello, inputs=[], outputs="text").launch()