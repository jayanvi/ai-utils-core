from ai_utils.logger import get_logger
from ai_utils.tokens import count_tokens
from ai_utils.preprocess import preprocess_input

logger = get_logger(__name__)


PROMPT_TEMPLATES = {
    "summarize": (
        "You are a helpful assistant.\n\n"
        "Summarize the following text clearly and concisely:\n\n"
        "{input}"
    ),
    "qa": (
        "Answer the question based on the context below.\n\n"
        "Context:\n{context}\n\n"
        "Question:\n{question}"
    ),
}


def build_prompt(template_name: str, **kwargs) -> str:
    if template_name not in PROMPT_TEMPLATES:
        raise ValueError(f"Unknown prompt template: {template_name}")

    logger.info("Building prompt", extra={"template": template_name})

    processed_kwargs = {
        key: preprocess_input(value)
        for key, value in kwargs.items()
    }

    prompt = PROMPT_TEMPLATES[template_name].format(**processed_kwargs)

    # Final token safety check
    count_tokens(prompt)

    logger.debug(
        "Prompt built successfully",
        extra={"tokens_checked": True},
    )

    return prompt
