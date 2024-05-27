import gradio as gr
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


from hf_agent_demo import demo as hf_agent
from hf_chatinterface import demo as hf_chatinterface
from langchain_agent_demo import demo as langchain_agent
from openai_stream_demo import demo as openai_stream
from open_ai_function_calling_demo import demo as openai_agent
from transformers_local import demo as transformers_local


with gr.Blocks() as demo:
    with gr.Tabs():
        for file_name, sub_demo, name in [
            ("hf_chatinterface", hf_chatinterface, "Inference API 🤗"),
            ("transformers_local", transformers_local, "Transformers Local 🤗"),
            ("openai_stream_demo", openai_stream, "OpenAI API Chatbot"),
            ("hf_agent_demo", hf_agent, "Transformers Agent 🤖"),
            ("langchain_agent_demo", langchain_agent, "LangChain Agent 🦜⛓️"),
            ("open_ai_function_calling_demo", openai_agent, "OpenAI Function Calling"),
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