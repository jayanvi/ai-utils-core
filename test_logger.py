#from ai_utils.text import normalize_text
#result = normalize_text("  Hello AI Engineer  ")
#print("Result:", result)

from ai_utils.logger import get_logger

logger = get_logger("day3 test")
logger.warning("This is a warning")


