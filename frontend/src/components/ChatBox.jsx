
import React, { useState, useRef, useEffect } from "react";
import "../AppChatDark.css";

export default function ChatBox({ messages, sendMessage, loading }) {
  const [input, setInput] = useState("");
  const messagesEndRef = useRef(null);
  const boxRef = useRef(null);
  const [dragging, setDragging] = useState(false);
  const [position, setPosition] = useState({ x: 32, y: 48 });
  const [offset, setOffset] = useState({ x: 0, y: 0 });

  useEffect(() => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const handleSend = (e) => {
    e.preventDefault();
    sendMessage(input);
    setInput("");
  };

  const handleMouseDown = (e) => {
    setDragging(true);
    setOffset({ x: e.clientX - position.x, y: e.clientY - position.y });
  };

  const handleMouseMove = (e) => {
    if (!dragging) return;
    const chatboxWidth = boxRef.current ? boxRef.current.offsetWidth : 400;
    const chatboxHeight = boxRef.current ? boxRef.current.offsetHeight : 400;
    const minX = 0;
    const minY = 0;
    const maxX = window.innerWidth - chatboxWidth;
    const maxY = window.innerHeight - chatboxHeight;
    let newX = e.clientX - offset.x;
    let newY = e.clientY - offset.y;
    newX = Math.max(minX, Math.min(newX, maxX));
    newY = Math.max(minY, Math.min(newY, maxY));
    setPosition({ x: newX, y: newY });
  };

  const handleMouseUp = () => {
    setDragging(false);
  };

  useEffect(() => {
    if (dragging) {
      window.addEventListener("mousemove", handleMouseMove);
      window.addEventListener("mouseup", handleMouseUp);
    } else {
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("mouseup", handleMouseUp);
    }
    return () => {
      window.removeEventListener("mousemove", handleMouseMove);
      window.removeEventListener("mouseup", handleMouseUp);
    };
  }, [dragging, offset]);

  return (
    <div
      className="chatbox-dark"
      ref={boxRef}
  style={{ position: "absolute", left: position.x, top: position.y, zIndex: 100 }}
    >
      <div
        className="chatbox-drag-bar"
        onMouseDown={handleMouseDown}
        style={{
          position: "absolute",
          left: 12,
          right: 12,
          top: 12,
          height: 36,
          cursor: dragging ? "grabbing" : "grab",
          background: "#313543",
          borderTopLeftRadius: 12,
          borderTopRightRadius: 12,
          display: "flex",
          alignItems: "center",
          fontWeight: "bold",
          color: "#90caf9",
          fontSize: 18,
          userSelect: "none",
          boxShadow: "none",
          zIndex: 101,
          paddingLeft: 16
        }}
      >
        Chat
      </div>
      <div style={{ height: 36 }} />
      <div className="messages">
        {messages.length === 0 && (
          <div className="no-messages">No messages yet.</div>
        )}
        {messages.map((msg, idx) => (
          <div
            key={idx}
            className={
              msg.sender === "assistant"
                ? "message assistant-message"
                : "message user-message"
            }
            style={
              msg.sender === "assistant"
                ? { alignSelf: "flex-end", background: "#23272f", color: "#90caf9" }
                : { alignSelf: "flex-start" }
            }
          >
            <span>{msg.text}</span>
            <div className="timestamp">
              {new Date(msg.timestamp).toLocaleTimeString()}
            </div>
          </div>
        ))}
        {loading && (
          <div className="message assistant-message" style={{ alignSelf: "flex-end", background: "#23272f", color: "#90caf9" }}>
            <span>GPT is thinking...</span>
          </div>
        )}
        <div ref={messagesEndRef} />
      </div>
      <form onSubmit={handleSend} className="input-row">
        <input
          value={input}
          onChange={e => setInput(e.target.value)}
          placeholder="Type a message..."
        />
        <button type="submit">Send</button>
      </form>
    </div>
  );
}
