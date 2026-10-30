# Week 2 — LLM Integration & Response Generation

A runnable reference implementation for the four Week 2 tasks:
1. Integrate a Python FastAPI backend with a cloud LLM API (Groq).
2. Use intent detection and a summary to generate context-aware answers.
3. Return Markdown and render it in React with `react-markdown`.
4. Validate the workflow and sync the code to Git.

> This is a standalone reference project because your current local workspace files were not provided. Integrate its services/routes into your existing application rather than blindly replacing your existing intent-detection logic.

## Architecture
React (Vite) → FastAPI `/api/respond` → intent detector + summary → Groq API → Markdown response → `react-markdown`

## Requirements
- Python 3.10+
- Node.js 18+
- A Groq API key

## 1. Backend setup (Windows PowerShell)
```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
```
Edit `backend/.env` and set `GROQ_API_KEY`. Never commit `.env`.

## 2. Run backend
From the `backend` folder:
```powershell
uvicorn app.main:app --reload
```
API docs: http://127.0.0.1:8000/docs

## 3. Run React frontend
Open a second terminal:
```powershell
cd frontend
npm install
npm run dev
```
Open the URL Vite prints (usually http://localhost:5173).

## 4. Test
```powershell
cd backend
.\.venv\Scripts\Activate.ps1
python -m pytest ../tests -q
```
Or send a POST request to `http://127.0.0.1:8000/api/respond`:
```json
{"message":"My payment failed, but money was deducted."}
```

## Environment variables
- `GROQ_API_KEY` — required
- `GROQ_MODEL` — optional; defaults to `llama-3.3-70b-versatile` (if this model is unavailable for your account, set a currently supported model in the Groq console)
- `FRONTEND_ORIGIN` — optional; defaults to `http://localhost:5173`

## What to adapt for your existing project
The sample `detect_intent()` is a simple demonstration, not a replacement for your trained/rule-based intent detector. Replace its internals with your existing workflow and pass its actual detected intent and summary into `generate_markdown_response()`. Align the response schema and endpoint names with your current app.
