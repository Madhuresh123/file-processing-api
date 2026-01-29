from app.db.repositories.document_repository import DocumentRepository

class DocumentQueryService:

    def __init__(self):
        self.repo = DocumentRepository()

    def get_document(self, db, document_id: int):
        doc = self.repo.get_by_id(db, document_id)
        if not doc:
            raise ValueError("Document not found")
        return doc

    def list_documents(self, db, limit: int, offset: int):
        return self.repo.get_all(db, limit, offset)
