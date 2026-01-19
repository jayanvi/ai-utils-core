from ai_utils.tokens import count_tokens
t = []
text = "Hello AI Engineers!"
for i in text:
    t.append(i)

tokens = count_tokens(text)
print(text)

print(f"Number of tokens in the text: {tokens}")