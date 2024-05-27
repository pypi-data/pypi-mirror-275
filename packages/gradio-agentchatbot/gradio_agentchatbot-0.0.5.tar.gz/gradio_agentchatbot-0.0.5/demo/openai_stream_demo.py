from openai import OpenAI
from gradio_agentchatbot import AgentChatbot
import gradio as gr

from dotenv import load_dotenv

load_dotenv()


client = OpenAI()


def openai_stream_response(prompt: str, history):
    history.append({"role": "user", "content": prompt})
    yield history

    response = client.chat.completions.create(
        model="gpt-4o", messages=history, stream=True
    )

    message = {"role": "assistant", "content": ""}
    for chunk in response:
        message["content"] += chunk.choices[0].delta.content or ""
        yield history + [message]


with gr.Blocks() as demo:
    gr.Markdown("# Chat with GPT-4o")
    chatbot = AgentChatbot(
        label="Agent",
        avatar_images=(
            None,
            "https://huggingface.co/spaces/KingNish/OpenGPT-4o/resolve/main/OpenAI_logo.png",
        ),
    )
    prompt = gr.Textbox(lines=1, label="Chat Message")
    prompt.submit(openai_stream_response, [prompt, chatbot], [chatbot])


if __name__ == "__main__":
    pass
