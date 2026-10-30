"""Week 2 / Task 3: Pydantic-validated response using Instructor + Groq."""
import os
from dotenv import load_dotenv
from groq import Groq
import instructor
from pydantic import BaseModel, Field

load_dotenv()

class SupportTicket(BaseModel):
    category: str = Field(description="Short ticket category")
    priority: str = Field(description="One of low, medium, high")
    summary: str = Field(description="One-sentence summary")
    requires_human: bool

def main() -> None:
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    if not api_key:
        raise SystemExit("GROQ_API_KEY is missing. Copy .env.example to .env and add your key locally.")
    client = instructor.from_groq(Groq(api_key=api_key), mode=instructor.Mode.TOOLS)
    ticket = client.chat.completions.create(
        model=model,
        response_model=SupportTicket,
        messages=[
            {"role": "system", "content": "Classify support tickets. Priority must be low, medium, or high."},
            {"role": "user", "content": "I was charged twice for the same order and need a refund."},
        ],
    )
    print(ticket.model_dump_json(indent=2))

if __name__ == "__main__":
    main()
