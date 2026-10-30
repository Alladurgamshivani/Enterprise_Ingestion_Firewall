# AI Engineer Workshop — Weeks 1, 2, and 3 Practice Pack

This is a practice starter kit, not a verified copy of the trainer's exact assignments. Week 3 follows the workshop email shared in chat. Week 1 and Week 2 are practice examples based on topics discussed previously; compare them with the official task instructions before submission.

## Layout
- `week1/`: Python, JSON, and HTTP API basics
- `week2/`: Groq chat completion, API topology concepts, Instructor/Pydantic structured output
- `week3/`: session IDs, in-memory chat history, FastAPI endpoint, React chat UI, and tests
- `docs/`: setup and GitHub checklist

## Setup (Windows PowerShell)
```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install --upgrade pip
pip install -r requirements.txt
Copy-Item .env.example .env
```
Add your Groq API key to `.env` locally. Never commit `.env`.

Run Week 1:
```powershell
python week1/task1_python_basics.py
python week1/task2_json_basics.py
python week1/task3_api_request_basics.py
```

Run Week 2 (valid Groq key and currently supported model required for tasks 1 and 3):
```powershell
python week2/task1_groq_chat_completion.py
python week2/task2_api_topologies.py
python week2/task3_instructor_structured_output.py
```

Run Week 3 backend from the extracted pack's root:
```powershell
uvicorn week3.backend.app.main:app --reload
```
Open `http://127.0.0.1:8000/docs`.

Run tests in another terminal:
```powershell
pytest week3/tests -q
```

Run React frontend:
```powershell
cd week3/frontend-react
npm install
Copy-Item .env.example .env
npm run dev
```

**Important:** Keep your existing Enterprise Ingestion Firewall intact. Review these examples and merge Week 3 features into your actual project carefully; do not overwrite existing files blindly. The exact Week 1 and Week 2 assignment list has not been verified from the trainer's syllabus.
