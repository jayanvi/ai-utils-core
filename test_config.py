from ai_utils.config import get_settings
settings = get_settings()

print("Log Level:", settings.log_level)
print("Max Input Tokens:", settings.max_input_tokens)
print("Model Name:", settings.model_name)
