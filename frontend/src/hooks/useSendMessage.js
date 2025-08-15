import { useState } from "react";

export function useSendMessage() {
  const [messages, setMessages] = useState([]);

  const sendMessage = (text) => {
    if (text.trim() === "") return;
    setMessages((prev) => [
      ...prev,
      { text, timestamp: Date.now() }
    ]);
  };

  return { messages, sendMessage };
}
