

import "../AppChatDark.css";
import ChatBox from "../components/ChatBox";
import { useOpenAIChat } from "../hooks/useOpenAIChat";

export default function ChatPage() {
  const { messages, sendMessage, loading, error } = useOpenAIChat();

  return (
    <div className="chatpage-dark">
  <ChatBox messages={messages} sendMessage={sendMessage} loading={loading} />
      {/* Empty space on the right for future content or layout */}
      <div style={{ flex: 1 }}>
        {error && <div style={{ color: 'red', marginTop: 24 }}>{error}</div>}
      </div>
    </div>
  );
}
