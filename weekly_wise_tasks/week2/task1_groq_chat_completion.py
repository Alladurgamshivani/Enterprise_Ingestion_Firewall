"""Week 2 / Task 1: Basic Groq chat completion."""

from groq import Groq

import os
from pathlib import Path
from dotenv import load_dotenv

PROJECT_ROOT = Path(__file__).resolve().parent.parent
load_dotenv(PROJECT_ROOT / ".env")

def main() -> None:
    api_key = os.getenv("GROQ_API_KEY")
    model = os.getenv("GROQ_MODEL", "llama-3.3-70b-versatile")
    if not api_key:
        raise SystemExit("GROQ_API_KEY is missing. Copy .env.example to .env and add your key locally.")
    client = Groq(api_key=api_key)
    response = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": "You are a concise and helpful assistant."},
            {"role": "user", "content": "Explain what an API is in two simple sentences."},
        ],
        temperature=0.2,
        max_tokens=150,
    )
    print(response.choices[0].message.content or "")

if __name__ == "__main__":
    main()
