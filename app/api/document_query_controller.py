from fastapi import APIRouter, Depends, HTTPException, Query
from app.db.dependencies import get_db
from app.services.document_query_service import DocumentQueryService
from app.schemas.document import (
    DocumentResponse,
    DocumentDetailResponse
)

class DocumentQueryController:

    def __init__(self):
        self.router = APIRouter(
            prefix="/documents",
            tags=["Documents"]
        )
        self.service = DocumentQueryService()
        self._register_routes()

    def _register_routes(self):
        self.router.get("/", response_model=list[DocumentResponse])(self.get_all)
        self.router.get("/{document_id}", response_model=DocumentDetailResponse)(
            self.get_by_id
        )

    def get_all(
        self,
        limit: int = Query(20, le=100),
        offset: int = Query(0),
        db = Depends(get_db)
    ):
        return self.service.list_documents(db, limit, offset)

    def get_by_id(
        self,
        document_id: int,
        db = Depends(get_db)
    ):
        try:
            return self.service.get_document(db, document_id)
        except ValueError:
            raise HTTPException(status_code=404, detail="Document not found")
