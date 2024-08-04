"use client";

import { useEffect, useState } from "react";
import ChatBox from "~/components/ui/chat-box";
import { Input } from "~/components/ui/input";
import { TooltipProvider } from "~/components/ui/tooltip";

export type ChatMessage = {
  message_type: "ai" | "human";
  message: string;
  id: number;
};

export default function HomePage() {
  const [chat, setChat] = useState<ChatMessage[]>([]);

  useEffect(() => {
    console.log(chat);
  }, [chat]);
  return (
    <main className="flex min-h-screen flex-col items-center justify-center bg-gradient-to-b text-black">
      <Input type="text" placeholder="Insert YouTube URL" />
      {chat.map((message, index) => (
        <div key={index} className="flex flex-col gap-2">
          {message.message_type === "ai" && (
            <div className="text-white">{message.message}</div>
          )}
          {message.message_type === "human" && (
            <div className="text-white">{message.message}</div>
          )}
        </div>
      ))}
      <TooltipProvider>
        <ChatBox setChat={setChat} />
      </TooltipProvider>
    </main>
  );
}
