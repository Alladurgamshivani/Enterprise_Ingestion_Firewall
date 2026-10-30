# Enterprise Structured Ingestion Firewall

An AI-powered customer-support chatbot that classifies user questions, validates structured LLM outputs, generates helpful responses, and maintains session-based conversation history.

The project demonstrates how to build a structured AI application using **FastAPI, Groq, Instructor, Pydantic, SQLite, and React**.

## Overview

The application processes user messages through a structured AI pipeline:

- **Week 1 — Intent Classification:** An LLM classifies user messages into predefined categories and produces structured output. Pydantic validates the result before the application uses it.
- **Week 2 — LLM Integration & Response Generation:** A second LLM call generates a user-friendly answer in Markdown based on the classified message.
- **Week 3 — Conversation Memory:** SQLite stores conversation messages, allowing users to continue previous sessions and retrieve conversation history.

The application follows a structured ingestion approach: incoming data is validated, model outputs are checked against defined schemas, and responses are returned in a predictable format.

> **Important:** Schema validation checks whether data follows the expected structure. It does not guarantee that an AI-generated answer is factually correct.

## Features

- AI-powered customer-support question classification.
- Structured LLM output using Instructor and Pydantic.
- Groq API integration for language-model inference.
- Separate services for conversation handling, database operations, LLM integration, and response generation.
- Session-based conversation management.
- Persistent conversation history using SQLite.
- FastAPI backend with interactive API documentation.
- React and Vite frontend.
- Token-count estimation for incoming messages.
- Automated tests for API endpoints and application services.
- Environment-based configuration for API credentials.

## Technology Stack

| Component | Technology |
|---|---|
| Backend language | Python |
| Backend framework | FastAPI |
| API server | Uvicorn |
| LLM provider | Groq |
| Structured LLM output | Instructor |
| Data validation | Pydantic |
| Database | SQLite |
| Frontend | React |
| Frontend build tool | Vite |
| Package manager | npm |
| Testing | pytest |
| Version control | Git and GitHub |

## Project Architecture

The application separates request handling, validation, LLM integration, response generation, and conversation persistence into distinct components.

### Message Processing Workflow

```text
                  USER
                    |
                    v
          React + Vite Frontend
                    |
                    v
             FastAPI Backend
                    |
                    v
          Request Schema Validation
                    |
                    v
           Intent Classification
                    |
                    v
               LLM Service
                    |
                    v
          Structured Output Validation
                    |
                    v
         Conversation Session Handling
                    |
                    v
            Response Generation
                    |
                    v
             Response Service
                    |
                    v
          Database Service (SQLite)
                    |
                    v
          Structured API Response
                    |
                    v
          React Chat Interface
```

The workflow represents the application's main processing stages. The exact execution order depends on the implementation in the backend.

## Backend Service Architecture

The backend uses a service-oriented structure to separate application responsibilities.

### 1. Conversation Service

**File:** `backend/app/services/conversation_service.py`

Responsible for conversation-related operations.

Its role in the application includes organizing conversation handling and coordinating session-related functionality.

Expected responsibilities include:

- Managing conversation sessions.
- Associating messages with their corresponding sessions.
- Supporting the retrieval of previous conversation messages.
- Helping maintain context across follow-up questions.

The exact responsibilities depend on the implemented functions in this module.

### 2. Database Service

**File:** `backend/app/services/database_service.py`

Handles database-related operations.

Its responsibilities include the database interactions implemented by the application, such as:

- Persisting conversation messages.
- Retrieving stored conversation data.
- Supporting conversation-history access.
- Interacting with the SQLite database.

Conversation data is stored locally in SQLite when the persistence functionality is configured and running.

### 3. LLM Service

**File:** `backend/app/services/llm_service.py`

Integrates the backend with the configured Groq language model.

Its responsibilities include:

- Sending user messages to the language model.
- Processing classification requests.
- Obtaining structured model output.
- Handling LLM request failures.

The classification output is validated against the application's expected schema before it is used by downstream components.

### 4. Response Service

**File:** `backend/app/services/response_service.py`

Handles the response-generation functionality.

Its responsibilities include:

- Preparing the information required for response generation.
- Integrating with the configured LLM response workflow.
- Generating user-facing answers.
- Formatting responses for the API.

The response-generation workflow is intended to use the classified message information to produce a helpful, readable answer.

### 5. Schemas

**Directory:** `backend/app/schemas/`

Contains Pydantic models that define the expected structure of requests and responses.

Schema validation helps ensure that data follows the application's defined format before it is processed.

Examples of schema responsibilities include:

- Validating incoming messages.
- Defining allowed intent categories.
- Validating structured classification results.
- Defining the expected response fields.

### 6. Utilities

**Directory:** `backend/app/utils/`

Contains reusable utility functions.

For example, `token_counter.py` estimates the number of tokens in a message.

Token estimates can help monitor prompt size, but they are not necessarily identical to the provider's final billing calculations.

### 7. SQL Resources

**Directory:** `backend/sql/`

Contains SQL-related resources used by the application.

The `schema.sql` file documents the database table structure.

### 8. Tests

**Directory:** `backend/tests/`

Contains automated tests for application functionality.

The test suite includes API and service-level tests where implemented.

Tests can be executed using pytest.

## Project Structure

```text
Enterprise_Ingestion_Firewall/
│
├── backend/
│   ├── app/
│   │   ├── schemas/
│   │   │   ├── ingestion.py
│   │   │   └── assistant.py
│   │   │
│   │   ├── services/
│   │   │   ├── __init__.py
│   │   │   ├── conversation_service.py
│   │   │   ├── database_service.py
│   │   │   ├── llm_service.py
│   │   │   └── response_service.py
│   │   │
│   │   ├── utils/
│   │   │   └── token_counter.py
│   │   │
│   │   ├── sql/
│   │   │   └── schema.sql
│   │   │
│   │   ├── tests/
│   │   │   ├── test_api.py
│   │   │   └── test_intent_service.py
│   │   │
│   │   ├── config.py
│   │   └── main.py
│   │
│   ├── .env.example
│   ├── .gitignore
│   ├── requirements.txt
│   └── README.md
│
├── frontend-react/
│   ├── src/
│   ├── public/
│   ├── package.json
│   └── README.md
│
├── weekly_wise_tasks/
│   ├── week1/
│   ├── week2/
│   └── ...
│
├── .gitignore
└── README.md
```

*Note: This tree summarizes the known project structure. Some nested files and folders may differ in your current repository. Keep the README aligned with the actual files on disk.*

## Prerequisites

Install the following before running the application:

- Python 3.10 or a compatible version supported by the project dependencies.
- Node.js 18 or newer.
- npm.
- A Groq API key.
- Git.

Official resources:

- [Python](https://www.python.org/downloads/)
- [Node.js](https://nodejs.org/)
- [Groq API Keys](https://console.groq.com/keys)
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [React Documentation](https://react.dev/)

## Installation and Setup

The following commands are for Windows PowerShell.

### Step 1: Clone the Repository

```powershell
git clone https://github.com/Alladurgamshivani/Enterprise_Ingestion_Firewall.git
cd Enterprise_Ingestion_Firewall
```

### Step 2: Set Up the Backend Environment

Navigate to the backend directory:

```powershell
cd backend
```

Create a Python virtual environment:

```powershell
python -m venv .venv
```

Activate the environment:

```powershell
.\.venv\Scripts\Activate.ps1
```

Install the required dependencies:

```powershell
pip install -r requirements.txt
```

### Step 3: Configure Environment Variables

Create a local `.env` file from the example:

```powershell
Copy-Item .env.example .env
```

Open the environment file:

```powershell
notepad .env
```

Configure the variables required by your application.

Example:

```dotenv
GROQ_API_KEY=your_groq_api_key_here
GROQ_MODEL=openai/gpt-oss-120b
```

Replace the placeholder values with valid configuration values supported by your implementation.

**Security requirements:**

- Never commit your actual `.env` file.
- Never include real API keys in `.env.example`.
- Keep credentials out of source code and documentation.
- Rotate any API key that has been accidentally exposed.

### Step 4: Run the Backend

Make sure you are inside the `backend` directory and that your Python environment is activated.

Start the FastAPI application:

```powershell
uvicorn app.main:app --reload --port 8000
```

The backend should be accessible at:

```text
http://127.0.0.1:8000
```

Interactive API documentation:

```text
http://127.0.0.1:8000/docs
```

Health endpoint, if configured:

```text
http://127.0.0.1:8000/health
```

Keep this terminal open while using the application.

### Step 5: Run the React Frontend

Open a second terminal in the repository root.

Navigate to the frontend directory:

```powershell
cd frontend-react
```

Install frontend dependencies:

```powershell
npm install
```

Start the development server:

```powershell
npm run dev
```

Open the local URL displayed by Vite. In the default configuration, it is:

```text
http://localhost:5173
```

Ensure the frontend API configuration points to the running backend.

## API Documentation

FastAPI provides interactive documentation for inspecting and testing available endpoints.

Open:

```text
http://127.0.0.1:8000/docs
```

The application's documented API may include:

| Endpoint | Purpose |
|---|---|
| `/health` | Checks backend health, if configured. |
| `/api/analyze` | Processes a user message and returns the application's analysis and response. |
| `/api/conversations` | Provides conversation-related information, if implemented. |

Refer to the routes defined in `backend/app/main.py` for the authoritative list of available endpoints, HTTP methods, request fields, and response structures.

### Example Request

An illustrative request to a message-processing endpoint might look like this:

```json
{
  "message": "My payment was deducted twice.",
  "session_id": null
}
```

The actual request schema and endpoint must match the application's implementation.

The response may contain classification details, a generated answer, and a session identifier, depending on the endpoint's response model.

## Session-Based Conversation Management

The application is designed to support multiple conversation sessions.

A session identifier associates messages with a particular conversation, allowing the backend to distinguish between separate discussions.

For example:

**Example 1: New conversation**

A user starts a conversation about a payment problem. The application creates or assigns a session identifier and associates the conversation messages with that session.

**Example 2: Follow-up question**

The user asks a follow-up question within the same session. The application can retrieve the relevant conversation history and use it as context when generating the next response.

Persistent conversation retrieval depends on the database and session-handling implementations being configured correctly.

## Database and Conversation History

The application uses SQLite for local conversation persistence, as described in the project workflow.

The database is expected to be stored at:

```text
backend/data/chat.db
```

The database file is created when the application's database initialization logic runs.

If the database is configured and the relevant endpoints are implemented, conversation records can be inspected using a SQLite database viewer or the application's API.

**Note:** Deleting the database removes its stored conversation data. Stop the backend before manually modifying or deleting database files.

## Testing

Run backend tests from the backend directory with the virtual environment activated.

Install pytest if it is not already included in the dependencies:

```powershell
pip install pytest
```

Run the test suite:

```powershell
python -m pytest
```

To run an individual test file:

```powershell
python -m pytest tests/test_api.py
```

The results depend on the tests currently implemented and the availability of any required environment variables or external services.

## Troubleshooting

| Problem | Possible cause | Suggested solution |
|---|---|---|
| `ModuleNotFoundError` | Missing dependency or incorrect Python environment | Activate the virtual environment and install `requirements.txt`. |
| `GROQ_API_KEY` missing | Environment variable not configured | Create `.env` and configure the required API key. |
| LLM request fails | Invalid credentials, unsupported model, network failure, or provider error | Check the API key, configured model, and application logs. |
| Backend is unavailable | The API server is not running | Start Uvicorn and check the configured port. |
| Frontend cannot connect | Incorrect API URL or backend not running | Verify the frontend API configuration and backend status. |
| `npm` is not recognized | Node.js is missing or not on PATH | Install Node.js and reopen the terminal. |
| PowerShell blocks activation | Execution policy prevents the activation script from running | Use an approved execution-policy setting or activate the environment using another supported method. |
| Port already in use | Another process occupies the port | Stop the existing process or configure a different port. |
| Conversation history is missing | Database persistence or session retrieval is not working as expected | Inspect the database service, database file, session identifier, and relevant API responses. |

## Security Considerations

This project handles user-provided messages and external LLM requests. Follow these practices when developing or deploying it:

- Store API credentials in environment variables.
- Validate requests using the application's schemas.
- Avoid exposing credentials or sensitive information in error messages.
- Do not log private user messages unnecessarily.
- Ensure conversation data is isolated by session and, where applicable, authenticated user.
- Keep database files and local environment files out of public repositories.
- Verify generated responses before relying on them for important decisions.

## Learning Outcomes

This project demonstrates practical experience with:

- Building REST APIs using FastAPI.
- Integrating cloud-hosted language models through Groq.
- Producing structured LLM output with Instructor and Pydantic.
- Organizing application logic into independent service modules.
- Implementing input and response validation.
- Managing conversation sessions and message history.
- Persisting data using SQLite.
- Connecting a React frontend to a Python backend.
- Testing API endpoints and backend services.
- Managing configuration and credentials securely.

## Future Enhancements

Potential improvements include:

- User authentication and access control.
- Improved session naming and conversation search.
- Streaming AI responses.
- More comprehensive error handling and retry logic.
- Expanded test coverage.
- Structured logging and monitoring.
- Deployment using a production-ready ASGI server.
- Additional validation and evaluation of AI-generated responses.

## Author

**Shivani Alladurgam**

GitHub: [Alladurgamshivani](https://github.com/Alladurgamshivani)

## Repository

[Enterprise Structured Ingestion Firewall — GitHub Repository](https://github.com/Alladurgamshivani/Enterprise_Ingestion_Firewall)