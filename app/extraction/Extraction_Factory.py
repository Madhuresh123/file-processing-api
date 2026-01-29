from .pdf_Extraction import PdfExtraction
from .img_Extraction import ImageExtraction
from .html_Extraction import HtmlExtraction

class ExtractionFactory:
    """
    Factory Pattern – creates extractor based on file category
    """

    _extractors = {
        "pdf_text": PdfExtraction(),
        "pdf_scanned": ImageExtraction(),
        "jpg": ImageExtraction(),
        "png": ImageExtraction(),
        "html": HtmlExtraction(),
    }

    @staticmethod
    def get_extractor(category: str):
        extractor = ExtractionFactory._extractors.get(category)
        if not extractor:
            raise ValueError(f"No extractor found for category: {category}")
        return extractor
