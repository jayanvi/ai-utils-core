import time
from typing import Optional
from openai import OpenAI

from ai_utils.logger import get_logger
from ai_utils.config import get_settings
from ai_utils.tokens import count_tokens

logger = get_logger(__name__)
settings = get_settings()


class LLMClient:
    def __init__(self):
        self._client: Optional[OpenAI] = None
        self.model = settings.model_name

    def _get_client(self) -> OpenAI:
        if self._client is None:
            logger.info("Initializing OpenAI client")
            self._client = OpenAI()
        return self._client

    def generate(self, prompt: str, retries: int = 3) -> str:
        count_tokens(prompt)

        client = self._get_client()

        for attempt in range(1, retries + 1):
            try:
                logger.info(
                    "Sending prompt to LLM",
                    extra={"attempt": attempt, "model": self.model},
                )

                response = client.chat.completions.create(
                    model=self.model,
                    messages=[{"role": "user", "content": prompt}],
                    temperature=0.2,
                )

                logger.info("LLM response received")
                return response.choices[0].message.content

            except Exception as e:
                logger.error(
                    "LLM request failed",
                    extra={"attempt": attempt, "error": str(e)},
                )

                if attempt == retries:
                    raise

                time.sleep(2)
