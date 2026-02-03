from app.detection.service import FileDetectionService
from app.extraction.Extraction_Service import ExtractionService
from app.db.repositories.document_repository import DocumentRepository
from app.normalization.normalization_service import NormalizationService

class DocumentProcessingService:

    def __init__(self):
        self.detector = FileDetectionService()
        self.extractor = ExtractionService()
        self.normalizer = NormalizationService()
        self.repo = DocumentRepository()

    def process(self, db, file_path: str, filename: str):
        # Detect
        detection = self.detector.detect(file_path)
        category = detection["category"]

        if category == "unknown":
            raise ValueError(
                "Unsupported file type. Allowed: PDF, Word, Excel, Image, HTML"
            )

        # Extract
        text = self.extractor.extract(file_path, category)

        # normalization
        normalized_text = self.normalizer.normalize(text, category)

        # INSERT INTO DB 
        document = self.repo.create(
            db=db,
            filename=filename,
            file_type=category,
            raw_text=normalized_text    
        )


        # redirectApi
        # localhost:8000/file/process -> localhost:8000/documents/{id}

        # showExtraction

        # editExtraction

        # saveExtraction

        return {
            "document_id": document.id,   
            "filename": filename,
            "category": category,
            "text_length": len(normalized_text)
        }
