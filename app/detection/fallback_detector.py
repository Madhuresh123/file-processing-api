from .base import BaseDetector

class FallbackDetector(BaseDetector):

    def detect(self, file_path: str, context: dict) -> dict:
        return {"category": "unknown"}
