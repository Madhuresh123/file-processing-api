from pdfminer.high_level import extract_text
from .base import BaseDetector

class PdfDetector(BaseDetector):

    def detect(self, file_path: str, context: dict) -> dict:
        if context.get("mime") != "application/pdf":
            return {"category": "unknown"}

        try:
            text = extract_text(file_path)
            if len(text.strip()) < 50:
                return {"category": "pdf_scanned"}
            return {"category": "pdf_text"}
        except Exception:
            return {"category": "pdf_scanned"}
