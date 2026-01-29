from app.detection.chain import DetectorChain
from app.detection.factory import DetectorFactory
from pdfminer.high_level import extract_text

class FileDetectionService:

    def __init__(self):
        detectors = DetectorFactory.create_chain()
        self.chain = DetectorChain(detectors)

    def detect(self, file_path: str) -> dict:
        info = self.chain.detect(file_path)

        # 🔑 NORMALIZE PDF
        if info["category"] == "pdf":
            info["category"] = self._detect_pdf_type(file_path)

        return info

    def _detect_pdf_type(self, file_path: str) -> str:
        try:
            text = extract_text(file_path)
            if len(text.strip()) < 50:
                return "pdf_scanned"
            return "pdf_text"
        except Exception:
            return "pdf_scanned"
