import anvil.server
import gradio as gr

def greet(name, intensity):
    return "Hello, " + name + "!" * int(intensity)

@anvil.server.callable
def get_interface():
  demo = gr.Interface(
    fn=greet,
    inputs=["text", "slider"],
    outputs=["text"],
  )
  return demo

