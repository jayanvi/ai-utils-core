import re
from ai_utils.logger import get_logger
from ai_utils.tokens import count_tokens

def normalize_text(text: str) -> str:
    text = text.strip()
    text = re.sub(r"\s+", " ", text)
    return text


logger = get_logger(__name__)
def preprocess_input(text: str) -> str:
    if not text or not isinstance(text, str):
        raise ValueError("Input text cannot be empty.")
    logger.info("preprocessing input text")

    cleaned = normalize_text(text)

    #token safety check
    count_tokens(cleaned)
    logger.debug("Input preprocessing complete", extra ={"length": len(cleaned)},)

    return cleaned