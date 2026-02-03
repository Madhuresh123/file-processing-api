import re
from .base_normalization import BaseNormalization

class PdfNormalization(BaseNormalization):

    def normalize(self, text: str) -> str:
        # Remove page numbers
        text = re.sub(r"\n\d+\n", "\n", text)

        # Remove multiple newlines
        text = re.sub(r"\n{2,}", "\n", text)

        # Remove excessive spaces
        text = re.sub(r"[ \t]{2,}", " ", text)

        return text.strip()
