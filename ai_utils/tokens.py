import tiktoken
from ai_utils.config import get_settings
from ai_utils.logger import get_logger

logger = get_logger(__name__)

def count_tokens(text:str)-> int:
    """
    Counts the number of tokens in the given text using the tokenizer
    for the specified model from settings.
    """
    settings = get_settings()
    encoding = tiktoken.encoding_for_model(settings.model_name)
    tokens = len(encoding.encode(text))

    logger.info(
        "Token count calculated",
        extra={"tokens": tokens, "model": settings.model_name}
    )

    return tokens
    