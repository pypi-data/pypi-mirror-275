import gradio as gr
from fastapi import FastAPI, Request
from fastapi.templating import Jinja2Templates
import uvicorn
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()


from hf_agent_demo import demo as hf_agent
from hf_chatinterface import demo as hf_chatinterface
from langchain_agent_demo import demo as langchain_agent
from openai_stream_demo import demo as openai_stream
from open_ai_function_calling_demo import demo as openai_agent


def all_demos():
    for file_name, demo, name in [
        ("hf_chatinterface", hf_chatinterface, "HF Chat Interface 🤗"),
        ("openai_stream_demo", openai_stream, "OpenAI API Chatbot"),
        ("hf_agent_demo", hf_agent, "Transformers Agent 🤖"),
        ("langchain_agent_demo", langchain_agent, "LangChain Agent 🦜⛓️"),
        ("open_ai_function_calling_demo", openai_agent, "OpenAI Function Calling"),
    ]:
        with gr.Blocks() as new_demo:
            with gr.Tabs():
                with gr.Tab("Demo"):
                    demo.render()
                with gr.Tab("Code"):
                    gr.Code(
                        value=Path(f"{file_name}.py").read_text(), language="python"
                    )
        yield new_demo, file_name, name


demo_and_name = [tup for tup in all_demos()]


app = FastAPI()

templates = Jinja2Templates(directory="templates")


@app.get("/")
def index(request: Request):
    names = [(p[2], p[1]) for p in demo_and_name]
    return templates.TemplateResponse(
        "index.html",
        {
            "request": request,
            "names": names,
            "initial_demo": names[0][1],
            "is_space": False,
        },
    )


for demo, name, _ in demo_and_name:
    app = gr.mount_gradio_app(app, demo, f"/demo/{name}")


if __name__ == "__main__":
    uvicorn.run(app, port=7860, host="0.0.0.0")
