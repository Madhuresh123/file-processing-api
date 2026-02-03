from .base_normalization import BaseNormalization

class WordNormalization(BaseNormalization):

    def normalize(self, text: str) -> str:
        paragraphs = [p.strip() for p in text.split("\n") if p.strip()]
        return "\n".join(paragraphs)
