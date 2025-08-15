import { useState } from "react";

export function useOpenAIChat() {
  const [messages, setMessages] = useState([]);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState(null);

  const sendMessage = async (text) => {
    if (text.trim() === "") return;
    const newMessages = [...messages, { text, sender: "user", timestamp: Date.now() }];
    setMessages(newMessages);
    setLoading(true);
    setError(null);
    try {
      const response = await fetch("http://localhost:8000/chat", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(newMessages)
      });
      const data = await response.json();
      if (data.text) {
        setMessages((prev) => [...prev, { text: data.text, sender: "assistant", timestamp: data.timestamp }]);
      } else {
        setError("No response from backend");
      }
    } catch (err) {
      setError("Error: " + err.message);
    }
    setLoading(false);
  };

  return { messages, sendMessage, loading, error };
}
