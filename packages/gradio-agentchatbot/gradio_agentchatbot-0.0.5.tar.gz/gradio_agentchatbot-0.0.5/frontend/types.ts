import type { FileData } from "@gradio/client";

export type MessageRole = "system" | "user";


export interface Metadata {
  error: boolean;
  tool_name: string;
}


export interface FileMessage {
  file: FileData;
  alt_text?: string | null;
}


export interface Message {
  role: MessageRole;
  metadata: Metadata;
  content: string | FileMessage
}


export interface ChatFileMessage extends Message {
  content: FileMessage;
}

export interface ChatStringMessage extends Message {
  content: string;
}