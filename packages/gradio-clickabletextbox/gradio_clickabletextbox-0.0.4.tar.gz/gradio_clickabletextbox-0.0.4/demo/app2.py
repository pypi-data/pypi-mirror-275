
import gradio as gr
from gradio_clickabletextbox import ClickableTextbox

with gr.Blocks() as demo:
    tb1 = ClickableTextbox(prompts=["This is a suffix",
                                    "This is another suffix", "This is a third suffix"], interactive=True)


if __name__ == "__main__":
    demo.launch(server_port=1236)
