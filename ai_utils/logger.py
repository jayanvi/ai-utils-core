import logging
from pythonjsonlogger import jsonlogger
from ai_utils.config import get_settings

_settings = get_settings()

def get_logger(name: str) -> logging.Logger:
    """
    Returns a JSON-structured logger.
    """
    logger = logging.getLogger(name)

    if logger.handlers:
        return logger  # avoid duplicate logs
    logger.setLevel(_settings.log_level)

    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    logger.propagate = False

    return logger
