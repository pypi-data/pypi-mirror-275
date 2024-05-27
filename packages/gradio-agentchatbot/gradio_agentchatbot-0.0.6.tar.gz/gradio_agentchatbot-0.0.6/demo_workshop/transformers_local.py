import gradio as gr
from transformers import AutoModelForCausalLM, AutoTokenizer, TextIteratorStreamer
from threading import Thread
import spaces

tokenizer = AutoTokenizer.from_pretrained("mistralai/Mistral-7B-Instruct-v0.3")
model = AutoModelForCausalLM.from_pretrained(
    "mistralai/Mistral-7B-Instruct-v0.3", device_map="auto"
)
terminators = [tokenizer.eos_token_id, tokenizer.convert_tokens_to_ids("<|eot_id|>")]


@spaces.GPU(duration=120)
def chat_mistral7b_v0dot3(
    message: str, history: list, temperature: float, max_new_tokens: int
) -> str:
    conversation = []
    for user, assistant in history:
        conversation.extend(
            [
                {"role": "user", "content": user},
                {"role": "assistant", "content": assistant},
            ]
        )
    conversation.append({"role": "user", "content": message})

    input_ids = tokenizer.apply_chat_template(conversation, return_tensors="pt").to(
        model.device
    )

    streamer = TextIteratorStreamer(
        tokenizer, timeout=10.0, skip_prompt=True, skip_special_tokens=True
    )

    generate_kwargs = dict(
        input_ids=input_ids,
        streamer=streamer,
        max_new_tokens=max_new_tokens,
        do_sample=True,
        temperature=temperature,
        eos_token_id=terminators,
    )
    # This will enforce greedy generation (do_sample=False) when the temperature is passed 0, avoiding the crash.
    if temperature == 0:
        generate_kwargs["do_sample"] = False

    t = Thread(target=model.generate, kwargs=generate_kwargs)
    t.start()

    outputs = []
    for text in streamer:
        outputs.append(text)
        # print(outputs)
        yield "".join(outputs)


# Gradio block
with gr.Blocks() as demo:
    gr.Markdown("# ChatInterface with Mistral and Transformers 🤗")
    gr.ChatInterface(
        fn=chat_mistral7b_v0dot3,
        fill_height=True,
        additional_inputs_accordion=gr.Accordion(
            label="⚙️ Parameters", open=False, render=False
        ),
        additional_inputs=[
            gr.Slider(
                minimum=0,
                maximum=1,
                step=0.1,
                value=0.95,
                label="Temperature",
                render=False,
            ),
            gr.Slider(
                minimum=128,
                maximum=4096,
                step=1,
                value=512,
                label="Max new tokens",
                render=False,
            ),
        ],
    )


if __name__ == "__main__":
    demo.launch()
