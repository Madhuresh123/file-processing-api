from .pdf_Extraction import PdfExtraction, PdfScannedExtraction
from .img_Extraction import ImageExtraction
from .html_Extraction import HtmlExtraction
from .word_Extraction import WordExtraction
from .excel_Extraction import ExcelExtraction

class ExtractionFactory:
    """
    Factory Pattern – creates extractor based on file category
    """

    _extractors = {
        "pdf_text": PdfExtraction(),
        "pdf_scanned": PdfScannedExtraction(),
        "jpg": ImageExtraction(),
        "png": ImageExtraction(),
        "html": HtmlExtraction(),
        "word": WordExtraction(),
        "excel": ExcelExtraction(), 
    }

    @staticmethod
    def get_extractor(category: str):
        extractor = ExtractionFactory._extractors.get(category)
        if not extractor:
            raise ValueError(f"No extractor found for category: {category}")
        return extractor
