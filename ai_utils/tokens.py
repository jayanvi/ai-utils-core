import tiktoken
from ai_utils.config import get_settings
from ai_utils.logger import get_logger

logger = get_logger(__name__)
_settings = get_settings()


def count_tokens(text: str) -> int:
    encoding = tiktoken.encoding_for_model(_settings.model_name)
    token_count = len(encoding.encode(text))

    logger.debug(
        "Token count computed",
        extra={
            "tokens": token_count,
            "model": _settings.model_name,
        },
    )

    if token_count > _settings.max_input_tokens:
        raise ValueError(
            f"Input exceeds max token limit ({_settings.max_input_tokens})"
        )

    return token_count
