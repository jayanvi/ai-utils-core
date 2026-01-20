from ai_utils.prompts import build_prompt

text = """
Artificial intelligence is transforming industries by automating tasks
and enabling data-driven decisions.
"""

prompt = build_prompt("summarize", input=text)
print(prompt)
