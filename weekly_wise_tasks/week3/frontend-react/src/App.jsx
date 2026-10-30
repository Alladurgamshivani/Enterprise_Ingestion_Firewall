import { useEffect, useRef, useState } from "react";

const API_BASE = import.meta.env.VITE_API_BASE_URL || "http://127.0.0.1:8000";

export default function App() {
  const [sessionId, setSessionId] = useState(null);
  const [messages, setMessages] = useState([]);
  const [input, setInput] = useState("");
  const [busy, setBusy] = useState(false);
  const [error, setError] = useState("");
  const bottomRef = useRef(null);

useEffect(() => {
  bottomRef.current?.scrollIntoView({ behavior: "smooth" });
}, [messages, busy]);

  function newChat() {
    setError("");
    setMessages([]);
    setInput("");
    setSessionId(null);
  }

  async function sendMessage(event) {
    event.preventDefault();
    const message = input.trim();
    if (!message || busy) return;
    setError("");
    setInput("");
    setMessages((current) => [...current, { role: "user", content: message }]);
    setBusy(true);
    try {
      const response = await fetch(`${API_BASE}/api/chat`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ session_id: sessionId, message }),
      });
      const data = await response.json();
      if (!response.ok) throw new Error(data.detail || "Request failed. Is the backend running?");
      setSessionId(data.session_id);
      setMessages(data.history.map(({ role, content }) => ({ role, content })));
    } catch (err) {
      setError(err.message || "Could not reach the backend.");
    } finally {
      setBusy(false);
    }
  }

  return (
    <main className="page">
      <section className="chat-card">
        <header className="header">
          <div>
            <p className="eyebrow">AI ENGINEER WORKSHOP · WEEK 3</p>
            <h1>Conversation Memory</h1>
            <p className="subtitle">A chat app with session-based history.</p>
          </div>
          <button className="secondary" onClick={newChat} disabled={busy}>+ New Chat</button>
        </header>
        <div className="session-line"><span>Session ID</span><code>{sessionId || "Created when you send your first message"}</code></div>
        <section className="messages" aria-live="polite">
          {messages.length === 0 && <div className="empty"><strong>Start a conversation</strong><p>Try “My name is Maya” and then ask “What is my name?”</p></div>}
          {messages.map((message, index) => (
            <article className={`message ${message.role}`} key={`${index}-${message.role}`}>
              <span className="role">{message.role === "user" ? "You" : "Assistant"}</span>
              <p>{message.content}</p>
            </article>
          ))}
          {busy && <p className="typing">Thinking…</p>}
          <div ref={bottomRef} />
        </section>
        {error && <p className="error" role="alert">{error}</p>}
        <form className="composer" onSubmit={sendMessage}>
          <label className="sr-only" htmlFor="message">Your message</label>
          <textarea id="message" rows="2" maxLength="5000" placeholder="Write a message…" value={input}
            onChange={(event) => setInput(event.target.value)}
            onKeyDown={(event) => {
              if (event.key === "Enter" && !event.shiftKey) {
                event.preventDefault();
                event.currentTarget.form?.requestSubmit();
              }
            }} />
          <button type="submit" disabled={busy || !input.trim()}>{busy ? "Sending…" : "Send"}</button>
        </form>
        <footer>Practice project · History clears when the backend restarts.</footer>
      </section>
    </main>
  );
}
