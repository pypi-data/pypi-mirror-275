from huggingface_hub import InferenceClient
from gradio_agentchatbot import AgentChatbot
import gradio as gr

"""
For more information on `huggingface_hub` Inference API support, please check the docs: https://huggingface.co/docs/huggingface_hub/v0.22.2/en/guides/inference
"""
client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")


def respond(
    prompt: str,
    history,
):
    messages = [{"role": "system", "content": "You are a friendly chatbot"}]

    for val in history:
        if val[0]:
            messages.append({"role": "user", "content": val[0]})
        if val[1]:
            messages.append({"role": "assistant", "content": val[1]})

    yield messages
    messages.append({"role": "user", "content": prompt})
    history.append([prompt, None])

    response = ""
    for message in client.chat_completion(
        messages,
        stream=True,
    ):
        response += message.choices[0].delta.content or ""
        history[-1][1] = response
        yield history


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
