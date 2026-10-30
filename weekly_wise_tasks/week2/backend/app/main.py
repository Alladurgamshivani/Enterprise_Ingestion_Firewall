import os
from dotenv import load_dotenv
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from groq import APIConnectionError, APIStatusError, RateLimitError

from app.schemas.chat import RespondRequest, RespondResponse
from app.services.intent_service import detect_intent
from app.services.llm_service import generate_markdown_response

load_dotenv()

app = FastAPI(title="Week 2 — LLM Integration & Response Generation", version="1.0.0")
origin = os.getenv("FRONTEND_ORIGIN", "http://localhost:5173")
app.add_middleware(
    CORSMiddleware,
    allow_origins=[origin],
    allow_credentials=True,
    allow_methods=["GET", "POST"],
    allow_headers=["*"],
)


@app.get("/api/health")
def health():
    return {"status": "ok"}


@app.post("/api/respond", response_model=RespondResponse)
def respond(payload: RespondRequest):
    analysis = detect_intent(payload.message)
    try:
        markdown = generate_markdown_response(payload.message, analysis)
    except RuntimeError as exc:
        raise HTTPException(status_code=503, detail=str(exc)) from exc
    except RateLimitError as exc:
        raise HTTPException(status_code=503, detail="LLM rate limit reached. Try again shortly.") from exc
    except APIConnectionError as exc:
        raise HTTPException(status_code=502, detail="Could not connect to the LLM provider.") from exc
    except APIStatusError as exc:
        raise HTTPException(status_code=502, detail=f"LLM provider returned HTTP {exc.status_code}. Check model access and API settings.") from exc
    except Exception as exc:
        raise HTTPException(status_code=500, detail="Response generation failed. Check backend logs.") from exc

    return RespondResponse(analysis=analysis, markdown_response=markdown)
