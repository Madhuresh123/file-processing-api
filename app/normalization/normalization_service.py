from .pdf_normalization import PdfNormalization
from .scannedpdf_normalization import ScannedPdfNormalization
from .word_normalization import WordNormalization
from .excel_normalization import ExcelNormalization
from .html_normalization import HtmlNormalization

class NormalizationService:

    _normalizers = {
        "pdf_text": PdfNormalization(),
        "pdf_scanned": ScannedPdfNormalization(),
        "word": WordNormalization(),
        "excel": ExcelNormalization(),
        "html": HtmlNormalization(),
    }

    def normalize(self, text: str, category: str) -> str:
        normalizer = self._normalizers.get(category)
        if not normalizer:
            return text  # fallback: no normalization

        return normalizer.normalize(text)
