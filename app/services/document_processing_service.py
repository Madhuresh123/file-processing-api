from app.detection.service import FileDetectionService
from app.extraction.Extraction_Service import ExtractionService
from app.db.repositories.document_repository import DocumentRepository

class DocumentProcessingService:

    def __init__(self):
        self.detector = FileDetectionService()
        self.extractor = ExtractionService()
        self.repo = DocumentRepository()

    def process(self, db, file_path: str, filename: str):
        # Detect
        detection = self.detector.detect(file_path)
        category = detection["category"]

        # Extract
        text = self.extractor.extract(file_path, category)

        # INSERT INTO DB ✅
        document = self.repo.create(
            db=db,
            filename=filename,
            file_type=category,
            raw_text=text
        )

        return {
            "document_id": document.id,   
            "filename": filename,
            "category": category,
            "text_length": len(text)
        }
