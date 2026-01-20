from ai_utils.preprocess import preprocess_input

raw_text = """
   Hello     world!
   This   is    a     messy    input.
"""

clean = preprocess_input(raw_text)
print(clean)
print(f"Cleaned text length: {len(clean)}")