"""Week 3: FastAPI chat endpoint with in-memory conversation history."""
import os
import uuid
from datetime import datetime, timezone
from threading import Lock
from typing import Literal

from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, Field

from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parents[3]
load_dotenv(PROJECT_ROOT / ".env")
app = FastAPI(title="Week 3 Conversation Memory Practice", version="1.0.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=False,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)

SESSIONS: dict[str, list[dict[str, str]]] = {}
SESSIONS_LOCK = Lock()
SYSTEM_PROMPT = (
    "You are a helpful AI workshop assistant. Use the conversation history to "
    "answer follow-up questions accurately. If you do not know something, say so."
)

class CreateSessionResponse(BaseModel):
    session_id: str

class ChatRequest(BaseModel):
    session_id: str | None = Field(default=None)
    message: str = Field(min_length=1, max_length=5000)

class ChatMessage(BaseModel):
    role: Literal["user", "assistant"]
    content: str
    timestamp: str

class ChatResponse(BaseModel):
    session_id: str
    response: str
    history: list[ChatMessage]

def _now() -> str:
    return datetime.now(timezone.utc).isoformat()

def _create_session() -> str:
    session_id = str(uuid.uuid4())
    with SESSIONS_LOCK:
        SESSIONS[session_id] = []
    return session_id

def _generate_reply(messages: list[dict[str, str]]) -> str:
    """Call Groq; separated so tests can mock this function."""
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    if not api_key:
        raise RuntimeError("GROQ_API_KEY is not configured.")
    from groq import Groq
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[{"role": "system", "content": SYSTEM_PROMPT}, *messages],
        temperature=0.3,
        max_tokens=500,
    )
    content = response.choices[0].message.content
    if not content:
        raise RuntimeError("The LLM returned an empty response.")
    return content.strip()

@app.get("/health")
def health_check() -> dict[str, str]:
    return {"status": "ok", "message": "Week 3 chat API is running"}

@app.post("/api/sessions", response_model=CreateSessionResponse)
def create_session() -> CreateSessionResponse:
    return CreateSessionResponse(session_id=_create_session())

@app.get("/api/sessions/{session_id}/history", response_model=list[ChatMessage])
def get_history(session_id: str) -> list[ChatMessage]:
    with SESSIONS_LOCK:
        if session_id not in SESSIONS:
            raise HTTPException(status_code=404, detail="Session not found.")
        history = list(SESSIONS[session_id])
    return [ChatMessage(**item) for item in history]

@app.post("/api/chat", response_model=ChatResponse)
def chat(request: ChatRequest) -> ChatResponse:
    message = request.message.strip()
    if not message:
        raise HTTPException(status_code=422, detail="Message cannot be empty.")

    session_id = request.session_id or _create_session()
    with SESSIONS_LOCK:
        if session_id not in SESSIONS:
            raise HTTPException(status_code=404, detail="Session not found. Create a new session first.")
        history = list(SESSIONS[session_id])

    history.append({"role": "user", "content": message, "timestamp": _now()})
    provider_messages = [{"role": item["role"], "content": item["content"]} for item in history]
    try:
        reply = _generate_reply(provider_messages)
    except Exception as exc:
        raise HTTPException(
            status_code=502,
            detail="LLM request failed. Check GROQ_API_KEY, GROQ_MODEL, network, and provider limits.",
        ) from exc

    history.append({"role": "assistant", "content": reply, "timestamp": _now()})
    with SESSIONS_LOCK:
        if session_id not in SESSIONS:
            raise HTTPException(status_code=404, detail="Session not found.")
        SESSIONS[session_id] = history

    return ChatResponse(
        session_id=session_id,
        response=reply,
        history=[ChatMessage(**item) for item in history],
    )
