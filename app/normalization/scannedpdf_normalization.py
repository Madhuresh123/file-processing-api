import re
from .base_normalization import BaseNormalization

class ScannedPdfNormalization(BaseNormalization):

    def normalize(self, text: str) -> str:
        # Fix broken words
        text = re.sub(r"-\n", "", text)

        # Remove OCR junk
        text = re.sub(r"[^\x00-\x7F]+", " ", text)

        # Normalize whitespace
        text = re.sub(r"\s+", " ", text)

        return text.strip()
