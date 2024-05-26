from huggingface_hub import InferenceClient
from gradio_agentchatbot import Message, AgentChatbot
import gradio as gr

"""
For more information on `huggingface_hub` Inference API support, please check the docs: https://huggingface.co/docs/huggingface_hub/v0.22.2/en/guides/inference
"""
client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")


def respond(
    prompt: str,
    history,
):
    if not history:
        history = [{"role": "system", "content": "You are a friendly chatbot"}]
    history.append({"role": "user", "content": prompt})

    yield history

    response = {"role": "assistant", "content": ""}
    for message in client.chat_completion(
        history,
        stream=True,
    ):
        response["content"] += message.choices[0].delta.content or ""

        yield history + [response]


with gr.Blocks() as demo:
    gr.Markdown("# Chat with Hugging Face Zephyr 7b 🤗")
    chatbot = AgentChatbot(
        label="Agent",
        avatar_images=(
            None,
            "https://em-content.zobj.net/source/twitter/376/hugging-face_1f917.png",
        ),
    )
    prompt = gr.Textbox(lines=1, label="Chat Message")
    prompt.submit(respond, [prompt, chatbot], [chatbot])


if __name__ == "__main__":
    demo.launch()
