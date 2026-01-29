from .mime_detector import MimeDetector
from .pdf_detector import PdfDetector
from .image_detector import ImageDetector
from .fallback_detector import FallbackDetector

class DetectorFactory:

    @staticmethod
    def create_chain():
        return [
            MimeDetector(),
            PdfDetector(),
            ImageDetector(),
            FallbackDetector()
        ]
