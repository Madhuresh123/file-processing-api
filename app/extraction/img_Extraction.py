import pytesseract
from PIL import Image
from .Base_Extraction import BaseExtraction

class ImageExtraction(BaseExtraction):

    def extract(self, file_path: str) -> str:
        try:
            return pytesseract.image_to_string(Image.open(file_path))
        except Exception as e:
            raise RuntimeError(f"Image OCR failed: {e}")
