def test_process_api(client, monkeypatch):
    #mock detection
    monkeypatch.setattr(
        "app.services.document_processing_service.FileDetectionService.detect",
        lambda self, x: {"category": "pdf_text"}
    )

    # mock extraction
    monkeypatch.setattr(
        "app.services.document_processing_service.ExtractionService.extract",
        lambda self, x, y: "mock extracted text"
    )

    # mock DB insert
    monkeypatch.setattr(
        "app.services.document_processing_service.DocumentRepository.create",
        lambda self, **kwargs: type("Doc", (), {"id": 1})()
    )

    response = client.post(
        "/files/process",
        files={"file": ("test.pdf", b"fake pdf content")}
    )

    assert response.status_code == 200
    data = response.json()

    assert data["document_id"] == 1
    assert data["category"] == "pdf_text"
