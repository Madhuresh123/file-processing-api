from pdfminer.high_level import extract_text
from .Base_Extraction import BaseExtraction
from pdf2image import convert_from_path
import pytesseract


class PdfExtraction(BaseExtraction):

    def extract(self, file_path: str) -> str:
        try:
            text = extract_text(file_path)
            return text or ""
        except Exception as e:
            raise RuntimeError(f"PDF extraction failed: {e}")

class PdfScannedExtraction(BaseExtraction):

    def extract(self, file_path: str) -> str:
        text = []
        images = convert_from_path(file_path)

        for img in images:
            page_text = pytesseract.image_to_string(img)
            text.append(page_text)

        return "\n".join(text)
