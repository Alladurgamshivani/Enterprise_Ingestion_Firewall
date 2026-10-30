import { useState } from "react";
import ReactMarkdown from "react-markdown";

const API_BASE = import.meta.env.VITE_API_BASE || "http://127.0.0.1:8000";

export default function App() {
  const [message, setMessage] = useState("");
  const [result, setResult] = useState(null);
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event) {
    event.preventDefault();
    setResult(null);
    setError("");
    setLoading(true);

    try {
      const response = await fetch(`${API_BASE}/api/respond`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message })
      });
      const data = await response.json();
      if (!response.ok) {
        throw new Error(data.detail || `Request failed (${response.status})`);
      }
      setResult(data);
    } catch (err) {
      setError(err.message || "Could not reach the backend.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <main className="page">
      <section className="panel">
        <p className="eyebrow">WEEK 2 · LLM INTEGRATION</p>
        <h1>Context-aware response generator</h1>
        <p className="intro">
          Enter a message. The backend detects intent, builds context, and asks
          the LLM to produce a Markdown response.
        </p>

        <form onSubmit={handleSubmit}>
          <label htmlFor="message">Your message</label>
          <textarea
            id="message"
            value={message}
            onChange={(event) => setMessage(event.target.value)}
            placeholder="Example: My payment failed, but money was deducted."
            minLength={1}
            maxLength={8000}
            required
          />
          <button type="submit" disabled={loading || !message.trim()}>
            {loading ? "Generating…" : "Generate response"}
          </button>
        </form>

        {error && <div className="error" role="alert">{error}</div>}

        {result && (
          <section className="result" aria-live="polite">
            <h2>Detected context</h2>
            <dl className="metadata">
              <dt>Intent</dt><dd>{result.analysis.intent}</dd>
              <dt>Summary</dt><dd>{result.analysis.summary}</dd>
              <dt>Priority</dt><dd>{result.analysis.priority}</dd>
              <dt>Requires action</dt><dd>{result.analysis.requires_action ? "Yes" : "No"}</dd>
            </dl>
            <h2>Generated response</h2>
            <article className="markdown">
              <ReactMarkdown>{result.markdown_response}</ReactMarkdown>
            </article>
          </section>
        )}
      </section>
    </main>
  );
}
