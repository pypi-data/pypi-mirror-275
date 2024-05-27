import gradio as gr
from pathlib import Path

from hf_chatinterface import demo as hf_chatinterface
from hf_stream_demo import demo as hf_stream
from transformers_local import demo as transformers_local


with gr.Blocks() as demo:
    with gr.Tabs():
        for file_name, sub_demo, name in [
            (
                "hf_chatinterface",
                hf_chatinterface,
                "ChatInterface with HF Inference API 🤗",
            ),
            (
                "transformers_local",
                transformers_local,
                "ChatInterface with Transformers Local 🤗",
            ),
            ("hf_stream_demo", hf_stream, "Blocks with HF Inference API 🤗"),
        ]:
            with gr.Tab(name):
                with gr.Tabs():
                    with gr.Tab("Demo"):
                        sub_demo.render()
                    with gr.Tab("Code"):
                        gr.Code(
                            value=Path(f"{file_name}.py").read_text(), language="python"
                        )


if __name__ == "__main__":
    demo.launch()
