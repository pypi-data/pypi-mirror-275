from typing_extensions import NotRequired

from transformers.agents import ReactAgent, agent_types
from pydantic import Field
from gradio.data_classes import GradioModel, FileData, GradioRootModel
from typing import Literal, List, Generator, Optional, Protocol, TypedDict, Union, Any


class MetadataDict(TypedDict):
    tool_name: Union[str, None]
    error: bool


class FileDataDict(TypedDict):
    path: str  # server filepath
    url: Optional[str]  # normalised server url
    size: Optional[int]  # size in bytes
    orig_name: Optional[str]  # original filename
    mime_type: Optional[str]
    is_stream: bool
    meta: dict[Literal["_type"], Literal["gradio.FileData"]]


class MessageDict(TypedDict):
    content: str | FileDataDict
    role: Literal["user", "assistant", "system"]
    metadata: NotRequired[MetadataDict]


class ApiReturnObj(Protocol):
    @property
    def content(self) -> str: ...

    @property
    def role(self) -> Literal["user", "assistant", "system", "tool"]: ...


class Metadata(GradioModel):
    tool_name: Optional[str] = None
    error: bool = False


class FileMessage(GradioModel):
    file: FileData
    alt_text: Optional[str] = None


class Message(GradioModel):
    role: Literal["user", "assistant", "system", "tool"]
    metadata: Metadata = Field(default_factory=Metadata)
    content: str | FileMessage

    @staticmethod
    def matches_protocol(obj: Any):
        return hasattr(obj, "role") and hasattr(obj, "content")

    @classmethod
    def from_api(cls, obj: ApiReturnObj) -> "Message":
        return cls(role=obj.role, content=obj.content or "")

    def append(self, obj: ApiReturnObj):
        if isinstance(self.content, FileMessage):
            raise ValueError("Cannot append to a message with a file.")
        self.content += obj.content or ""
        return self


class ChatbotData(GradioRootModel):
    root: List[Message]


def convert_to_message_stream(message: dict) -> Generator[Message, None, None]:
    if message.get("rationale"):
        yield Message(role="assistant", content=message["rationale"])
    if message.get("tool_call"):
        used_code = message["tool_call"]["tool_name"] == "code interpreter"
        content = message["tool_call"]["tool_arguments"]
        if used_code:
            content = f"```py\n{content}\n```"
        yield Message(
            role="assistant",
            metadata=Metadata(tool_name=message["tool_call"]["tool_name"]),
            content=content,
        )
    if message.get("observation"):
        yield Message(role="assistant", content=message["observation"])
    if message.get("error"):
        yield Message(
            role="assistant",
            content=str(message["error"]),
            metadata=Metadata(error=True),
        )


def pull_messages(new_messages: List[dict]):
    for message in new_messages:
        if not len(message):
            continue
        if message.get("rationale"):
            yield Message(role="assistant", content=message["rationale"])
        if message.get("tool_call"):
            used_code = message["tool_call"]["tool_name"] == "code interpreter"
            content = message["tool_call"]["tool_arguments"]
            if used_code:
                content = f"```py\n{content}\n```"
            yield Message(
                role="assistant",
                metadata=Metadata(tool_name=message["tool_call"]["tool_name"]),
                content=content,
            )
        if message.get("observation"):
            yield Message(role="assistant", content=message["observation"])
        if message.get("error"):
            yield Message(
                role="assistant",
                content=str(message["error"]),
                metadata=Metadata(error=True),
            )


def stream_from_transformers_agent(
    agent: ReactAgent, prompt: str
) -> Generator[Message, None, None]:
    """Runs an agent with the given prompt and streams the messages from the agent as ChatMessages."""

    for message in agent.run(prompt, stream=True):  # type: ignore
        if isinstance(message, dict):
            for gradio_message in convert_to_message_stream(message):
                yield gradio_message
        elif isinstance(message, agent_types.AgentText):
            yield Message(role="assistant", content=message.to_string())
        elif isinstance(message, agent_types.AgentImage):
            yield Message(
                role="assistant",
                content=FileMessage(
                    file=FileData(path=message.to_string(), mime_type="image/png")
                ),  # type: ignore
            )
        elif isinstance(message, agent_types.AgentAudio):
            yield Message(
                role="assistant",
                content=FileMessage(
                    file=FileData(path=message.to_string(), mime_type="audio/wav")
                ),  # type: ignore
            )
        elif isinstance(message, str):
            yield Message(role="assistant", content=message)
