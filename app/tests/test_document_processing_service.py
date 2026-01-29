from app.services.document_processing_service import DocumentProcessingService

class FakeDB:
    def add(self, obj): pass
    def commit(self): pass
    def refresh(self, obj): obj.id = 1
    def close(self): pass

def test_process_document(monkeypatch, tmp_path):
    service = DocumentProcessingService()

    # mock detection
    monkeypatch.setattr(
        service.detector,
        "detect",
        lambda x: {"category": "pdf_text"}
    )

    # mock extraction
    monkeypatch.setattr(
        service.extractor,
        "extract",
        lambda x, y: "extracted text"
    )

    # mock repo
    monkeypatch.setattr(
        service.repo,
        "create",
        lambda **kwargs: type("Doc", (), {"id": 1})()
    )

    result = service.process(
        db=FakeDB(),
        file_path="dummy.pdf",
        filename="test.pdf"
    )

    assert result["document_id"] == 1
