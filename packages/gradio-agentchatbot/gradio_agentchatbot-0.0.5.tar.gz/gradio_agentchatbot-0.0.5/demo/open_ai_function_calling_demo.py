from openai import OpenAI
import gradio as gr
from gradio_agentchatbot import AgentChatbot
from typing import Any
import json
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()


# Example dummy function hard coded to return the same weather
# In production, this could be your backend API or an external API
def get_current_weather(location, unit="fahrenheit"):
    """Get the current weather in a given location"""
    if "tokyo" in location.lower():
        return json.dumps({"location": "Tokyo", "temperature": "10", "unit": unit})
    elif "san francisco" in location.lower():
        return json.dumps(
            {"location": "San Francisco", "temperature": "72", "unit": unit}
        )
    elif "paris" in location.lower():
        return json.dumps({"location": "Paris", "temperature": "22", "unit": unit})
    else:
        return json.dumps({"location": location, "temperature": "unknown"})


tools = [
    {
        "type": "function",
        "function": {
            "name": "get_current_weather",
            "description": "Get the current weather in a given location",
            "parameters": {
                "type": "object",
                "properties": {
                    "location": {
                        "type": "string",
                        "description": "The city and state, e.g. San Francisco, CA",
                    },
                    "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
                },
                "required": ["location"],
            },
        },
    }
]


def gpt4o_function_calling(prompt: str, history: list):
    # Step 1: send the conversation and available functions to the model
    messages: list[Any] = [m for m in history]
    messages.append({"role": "user", "content": prompt})

    history.append({"role": "user", "content": prompt})
    yield history

    response = client.chat.completions.create(
        model="gpt-4o",
        messages=messages,
        tools=tools,
        tool_choice="auto",  # auto is default, but we'll be explicit
    )
    response_message = response.choices[0].message
    messages.append(response_message)
    if response_message.content:
        history.append(response_message)
        yield history

    tool_calls = response_message.tool_calls
    # Step 2: check if the model wanted to call a function
    if tool_calls:
        # Step 3: call the function
        # Note: the JSON response may not always be valid; be sure to handle errors
        available_functions = {
            "get_current_weather": get_current_weather,
        }  # only one function in this example, but you can have multiple
        # Step 4: send the info for each function call and function response to the model
        for tool_call in tool_calls:
            function_name = tool_call.function.name
            function_to_call = available_functions[function_name]
            function_args = json.loads(tool_call.function.arguments)
            function_response = function_to_call(
                location=function_args.get("location"),
                unit=function_args.get("unit"),
            )
            history.append(
                dict(
                    role="assistant",
                    content=function_response,
                    metadata={"tool_name": function_name},
                )
            )
            yield history
            messages.append(
                {
                    "tool_call_id": tool_call.id,
                    "role": "tool",
                    "name": function_name,
                    "content": function_response,
                }
            )  # extend conversation with function response
        second_response = client.chat.completions.create(
            model="gpt-4o",
            messages=messages,
        )  # get a new response from the model where it can see the function response
        history.append(second_response.choices[0].message)
        yield history


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
    prompt.submit(gpt4o_function_calling, [prompt, chatbot], [chatbot])
