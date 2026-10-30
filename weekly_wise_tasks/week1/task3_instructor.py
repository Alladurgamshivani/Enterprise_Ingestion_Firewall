
import os
from pathlib import Path

import instructor
from dotenv import load_dotenv
from groq import Groq
from pydantic import BaseModel

# Load the API key from the existing Task 1 .env file
env_path = Path(__file__).resolve().parents[1] / "task1" / ".env"
load_dotenv(env_path)

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in task1/.env")


# Define the Pydantic schema
class UserProfile(BaseModel):
    name: str
    age: int
    email: str


# Connect Instructor to Groq
client = instructor.from_groq(
    Groq(api_key=api_key),
    mode=instructor.Mode.JSON,
)


# Generate a structured response
response = client.chat.completions.create(
    model="openai/gpt-oss-20b",
    response_model=UserProfile,
    temperature=0,
    max_retries=3,
    messages=[
        {
            "role": "system",
            "content": (
                "Extract the name, age, and email from the user message. "
                "Return data matching the required schema."
            ),
        },
        {
            "role": "user",
            "content": (
                "Create a profile for Ravi, age 25, "
                "email ravi@example.com."
            ),
        },
    ],
)


# Print the validated JSON response
print("Structured JSON Response:")
print(response.model_dump_json(indent=2))
