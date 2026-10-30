
import tiktoken

text = "I am learning Python."

# Select a tokenizer
encoding = tiktoken.get_encoding("o200k_base")

# Convert text into tokens
tokens = encoding.encode(text)

print("Text:", text)
print("Token IDs:", tokens)
print("Number of tokens:", len(tokens))
