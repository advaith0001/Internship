"use client";

import { useState } from "react";

export default function Home() {
  const [text, setText] = useState("");
  const [summary, setSummary] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSummarize() {
    setLoading(true);
    setSummary("");

    const res = await fetch("/api/summarize", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ text }),
    });

    const data = await res.json();
    setSummary(data.summary);
    setLoading(false);
  }

  return (
    <div style={{ padding: 20 }}>
      <h1>Groq Blog Summarizer</h1>

      <textarea
        rows={8}
        placeholder="Paste your blog text here..."
        value={text}
        onChange={(e) => setText(e.target.value)}
        style={{ width: "100%", marginBottom: 12 }}
      />

      <button onClick={handleSummarize}>
        {loading ? "Summarizing..." : "Summarize"}
      </button>

      {summary && (
        <div style={{ marginTop: 20, color: "#eee", padding: 12 }}>
          <h2>Summary</h2>
          <p>{summary}</p>
        </div>
      )}
    </div>
  );
}
