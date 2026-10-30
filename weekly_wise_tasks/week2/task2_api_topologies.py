"""Week 2 / Task 2: LLM API topology concepts — no API call required."""

def main() -> None:
    notes = {
        "Direct client-to-provider": "A client calls an LLM provider directly. It is simple for prototypes, but never put private API keys in browser code.",
        "Backend-mediated": "A frontend calls your backend, and the backend calls the provider. This protects secrets and centralizes validation and limits.",
        "Gateway / proxy": "A shared gateway routes requests to providers and can apply authentication, rate limits, monitoring, and policy.",
    }
    for title, description in notes.items():
        print(f"\n{title}\n{'-' * len(title)}\n{description}")
    print("\nPractice questions:")
    print("1. Why should a React frontend not contain a private provider API key?")
    print("2. Which topology fits a production app with user authentication?")
    print("3. Where should request validation and rate limiting be enforced?")

if __name__ == "__main__":
    main()
