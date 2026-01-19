from ai_utils.logger import get_logger

logger = get_logger(__name__)

def normalize_text(text: str) -> str:

    logger.info("Normalizing text", extra = {"length": len(text)})
    return text.lower().strip()
