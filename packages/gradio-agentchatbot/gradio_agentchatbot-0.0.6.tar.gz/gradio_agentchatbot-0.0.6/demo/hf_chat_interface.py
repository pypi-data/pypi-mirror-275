from huggingface_hub import InferenceClient
from gradio_agentchatbot import ChatInterface, AgentChatbot
import gradio as gr

client = InferenceClient("HuggingFaceH4/zephyr-7b-beta")


def respond(
    message,
    history: list[dict],
    system_message: str,
):
    messages = [{"role": "system", "content": system_message}] + history
    messages.append({"role": "user", "content": message})

    for chunk in client.chat_completion(
        messages,
        stream=True,
    ):
        yield chunk.choices[0].delta.content


chat = ChatInterface(
    respond,
    chatbot=AgentChatbot(height=400),
    additional_inputs=[
        gr.Textbox(value="You are a friendly Chatbot.", label="System message"),
    ],
)

with gr.Blocks() as demo:
    gr.Markdown("# ChatInterface with Hugging Face Zephyr 7b 🤗")
    chat.render()


if __name__ == "__main__":
    demo.launch()
