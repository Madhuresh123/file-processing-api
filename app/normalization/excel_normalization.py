from .base_normalization import BaseNormalization

class ExcelNormalization(BaseNormalization):

    def normalize(self, text: str) -> str:
        lines = text.splitlines()
        cleaned = [line for line in lines if line.strip()]
        return "\n".join(cleaned)
