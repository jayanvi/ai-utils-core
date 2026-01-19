import logging
from pythonjsonlogger import jsonlogger
from ai_utils.config import get_settings

def get_logger(name: str) -> logging.Logger:
    settings = get_settings()
    """
    Returns a JSON-structured logger.
    """
    logger = logging.getLogger(name)
    logger.setLevel(settings.log_level)

    if logger.handlers:
        return logger  # avoid duplicate logs

    handler = logging.StreamHandler()
    formatter = jsonlogger.JsonFormatter(
        "%(asctime)s %(levelname)s %(name)s %(message)s"
    )
    handler.setFormatter(formatter)

    logger.addHandler(handler)
    return logger
