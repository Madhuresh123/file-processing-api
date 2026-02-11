from app.db.models import Document

class DocumentRepository:

    def create(self, db, filename: str, file_type: str, raw_text: str):
        doc = Document(
            filename=filename,
            file_type=file_type,
            raw_text=raw_text
        )
        db.add(doc)
        db.commit()
        db.refresh(doc)
        return doc

    def get_by_id(self, db, document_id: int):
        return db.query(Document).filter(Document.id == document_id).first()

    def get_all(self, db, limit: int = 20, offset: int = 0):
        return (
            db.query(Document)
            .order_by(Document.created_at.desc())
            .offset(offset)
            .limit(limit)
            .all()
        )
    
    def update_raw_text(self, db, document_id: int, raw_text: str):
        doc = (
            db.query(Document)
            .filter(Document.id == document_id)
            .first()
        )

        if not doc:
            return None

        doc.raw_text = raw_text
        db.commit()
        db.refresh(doc)

        return doc