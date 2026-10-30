"""Week 3 tests. Groq is mocked; no API key is needed."""
from fastapi.testclient import TestClient
from week3.backend.app import main

client = TestClient(main.app)

def setup_function():
    main.SESSIONS.clear()

def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_new_session_is_created():
    response = client.post("/api/sessions")
    assert response.status_code == 200
    assert response.json()["session_id"]

def test_chat_stores_user_and_assistant_messages(monkeypatch):
    monkeypatch.setattr(main, "_generate_reply", lambda messages: "Hello! How can I help?")
    response = client.post("/api/chat", json={"session_id": None, "message": "Hello"})
    assert response.status_code == 200
    data = response.json()
    assert data["session_id"]
    assert data["response"] == "Hello! How can I help?"
    assert [m["role"] for m in data["history"]] == ["user", "assistant"]

def test_follow_up_receives_prior_context(monkeypatch):
    captured = {}
    def fake_reply(messages):
        captured["messages"] = messages
        return "Your name is Maya."
    monkeypatch.setattr(main, "_generate_reply", fake_reply)
    first = client.post("/api/chat", json={"session_id": None, "message": "My name is Maya."})
    session_id = first.json()["session_id"]
    second = client.post("/api/chat", json={"session_id": session_id, "message": "What is my name?"})
    assert second.status_code == 200
    assert captured["messages"][0]["content"] == "My name is Maya."
    assert captured["messages"][-1]["content"] == "What is my name?"

def test_session_isolation(monkeypatch):
    monkeypatch.setattr(main, "_generate_reply", lambda messages: "ok")
    first = client.post("/api/chat", json={"session_id": None, "message": "Session A"})
    second = client.post("/api/chat", json={"session_id": None, "message": "Session B"})
    assert first.json()["session_id"] != second.json()["session_id"]
    assert [m["content"] for m in first.json()["history"]] == ["Session A", "ok"]
    assert [m["content"] for m in second.json()["history"]] == ["Session B", "ok"]

def test_unknown_session_returns_404():
    response = client.post("/api/chat", json={"session_id": "not-a-real-session", "message": "Hello"})
    assert response.status_code == 404

def test_blank_message_rejected():
    response = client.post("/api/chat", json={"session_id": None, "message": "   "})
    assert response.status_code == 422
