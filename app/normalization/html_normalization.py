import re
from .base_normalization import BaseNormalization

class HtmlNormalization(BaseNormalization):

    def normalize(self, text: str) -> str:
        # Remove excessive whitespace
        text = re.sub(r"\s+", " ", text)
        return text.strip()
