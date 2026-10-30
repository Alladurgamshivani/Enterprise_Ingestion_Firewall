# Setup and GitHub submission checklist

1. Compare the practice pack with the trainer's official tasks.
2. Install dependencies and configure `.env` locally.
3. Run Week 1 exercises.
4. Run Week 2 Groq tasks only after adding a valid API key and checking that the selected model is supported by your account.
5. Run the Week 3 backend and test `/health`, `/api/sessions`, and `/api/chat`.
6. Run `pytest week3/tests -q`.
7. Run the React starter and test New Chat and follow-up messages.
8. Run `git status` and verify `.env` is ignored before pushing.
9. Push only to your own repository or the submission location specified by the trainer. Do not push to the trainer's repository without permission.

Week 3 uses in-memory storage; history is lost when the backend restarts, as expected for this practice task.
