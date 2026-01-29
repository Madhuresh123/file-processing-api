from .base import BaseDetector

class FallbackDetector(BaseDetector):

    def detect(self, file_path: str, context: dict):
        ext = file_path.lower()

        if ext.endswith(".doc") or ext.endswith(".docx"):
            return {"category": "word"}

        if ext.endswith(".xls") or ext.endswith(".xlsx"):
            return {"category": "excel"}

        return {"category": "unknown"}
