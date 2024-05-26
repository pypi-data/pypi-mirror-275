from langchain import hub
from langchain.agents import AgentExecutor, create_openai_tools_agent, load_tools
import gradio as gr
from gradio_agentchatbot import AgentChatbot, Message

from langchain_openai import ChatOpenAI

from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(temperature=0, streaming=True)

tools = load_tools(["serpapi"])

prompt = hub.pull("hwchase17/openai-tools-agent")
agent = create_openai_tools_agent(
    model.with_config({"tags": ["agent_llm"]}), tools, prompt
)
langchain_agent = AgentExecutor(agent=agent, tools=tools).with_config(
    {"run_name": "Agent"}
)


async def interact_with_langchain_agent(prompt, messages):
    messages.append(Message(role="user", content=prompt))
    yield messages
    async for chunk in langchain_agent.astream({"input": prompt}):
        if "steps" in chunk:
            for step in chunk["steps"]:
                messages.append(
                    dict(
                        role="assistant",
                        content=step.action.log,
                        metadata={"tool_name": step.action.tool},
                    )
                )
                yield messages
        if "output" in chunk:
            messages.append(Message(role="assistant", content=chunk["output"]))
            yield messages


with gr.Blocks() as demo:
    gr.Markdown("# Chat with a LangChain Agent 🦜⛓️ and see its thoughts 💭")
    chatbot_2 = AgentChatbot(
        label="Agent",
        avatar_images=(
            None,
            "https://em-content.zobj.net/source/twitter/141/parrot_1f99c.png",
        ),
    )
    input_2 = gr.Textbox(lines=1, label="Chat Message")
    input_2.submit(interact_with_langchain_agent, [input_2, chatbot_2], [chatbot_2])

if __name__ == "__main__":
    demo.launch()
