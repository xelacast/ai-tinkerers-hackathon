"use client";

import { CornerDownLeft, Mic, Paperclip } from "lucide-react";
import {
  type Dispatch,
  type FormEvent,
  type SetStateAction,
  useEffect,
  useState,
} from "react";
import type { ChatMessage } from "~/app/page";

import { Button } from "~/components/ui/button";
import { Label } from "~/components/ui/label";
import { Textarea } from "~/components/ui/textarea";
import {
  Tooltip,
  TooltipContent,
  TooltipTrigger,
} from "~/components/ui/tooltip";
// const socket = io("ws://localhost:8000/ws");

export default function ChatBox({
  setChat,
}: {
  setChat: Dispatch<SetStateAction<ChatMessage[]>>;
}) {
  // const [chat, setChat] = useState<
  //   { message_type: "ai" | "human"; message: string }[]
  // >([]);
  const [message, setMessage] = useState("");
  const [aiMessage, setAiMessage] = useState("");
  const [ws, _] = useState<WebSocket>(new WebSocket("ws://localhost:8000/ws"));
  const [messageId, setMessageId] = useState(0);
  useEffect(() => {
    ws.onmessage = function (event) {
      // console.log(event.data);
      // const message = JSON.parse(event.data) as ChatMessage;
      // console.log(message);
      setAiMessage((prev) => prev + event.data);
      console.log("EVEMT", event);
    };
    // @ts-expect-error types are wrong
    setChat((prev) => [...prev, { message_type: "ai", message: aiMessage }]);
  }, [ws]);

  useEffect(() => {
    console.log(aiMessage);
  }, [aiMessage, messageId]);
  // get chat from server
  const sendMessage = (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    ws.send(message);
    setChat((prev) => [
      ...prev,
      { message_type: "human", message, id: Math.random() * 100 },
    ]);
    setMessage("");
  };
  // send message to server
  const onMessageChange = (e: React.ChangeEvent<HTMLTextAreaElement>) => {
    setMessage(e.target.value);
  };

  return (
    <form
      onSubmit={sendMessage}
      className="relative overflow-hidden rounded-lg border bg-background focus-within:ring-1 focus-within:ring-ring"
    >
      <Label htmlFor="message" className="sr-only">
        Message
      </Label>
      <Textarea
        id="message"
        placeholder="Type your message here..."
        className="min-h-12 resize-none border-0 p-3 shadow-none focus-visible:ring-0"
        value={message}
        onChange={onMessageChange}
      />
      <div className="flex items-center p-3 pt-0">
        <Tooltip>
          <TooltipTrigger asChild>
            <Button variant="ghost" size="icon">
              <Paperclip className="size-4" />
              <span className="sr-only">Attach file</span>
            </Button>
          </TooltipTrigger>
          <TooltipContent side="top">Attach File</TooltipContent>
        </Tooltip>
        <Tooltip>
          <TooltipTrigger asChild>
            <Button variant="ghost" size="icon">
              <Mic className="size-4" />
              <span className="sr-only">Use Microphone</span>
            </Button>
          </TooltipTrigger>
          <TooltipContent side="top">Use Microphone</TooltipContent>
        </Tooltip>
        <Button type="submit" size="sm" className="ml-auto gap-1.5">
          Send Message
          <CornerDownLeft className="size-3.5" />
        </Button>
      </div>
    </form>
  );
}
