# Week 3 — Conversation memory and chat history

Implements the tasks described in the Week 3 reminder email:
1. Create session IDs.
2. Keep session histories separate in in-memory storage.
3. Store user messages and assistant replies.
4. Send conversation history to Groq for context-aware answers.
5. Provide a chat endpoint for React.
6. Include New Chat support, basic errors, and tests.

This is a standalone learning example. Merge relevant parts into your existing Enterprise Ingestion Firewall only after reviewing your current files. Do not overwrite existing working endpoints.

Run backend from the extracted pack root:
`uvicorn week3.backend.app.main:app --reload`

Open `http://127.0.0.1:8000/docs`.

Endpoints: `GET /health`, `POST /api/sessions`, `GET /api/sessions/{session_id}/history`, `POST /api/chat`.

Example request body: `{"session_id": null, "message": "My name is Maya."}`. Use the returned session ID for a follow-up such as `What is my name?`.

In-memory history is lost when the backend restarts; this is expected for the Week 3 task.
