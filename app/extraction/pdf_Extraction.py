from pdfminer.high_level import extract_text
from .Base_Extraction import BaseExtraction

class PdfExtraction(BaseExtraction):

    def extract(self, file_path: str) -> str:
        try:
            text = extract_text(file_path)
            return text or ""
        except Exception as e:
            raise RuntimeError(f"PDF extraction failed: {e}")
