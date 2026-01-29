from app.extraction.Extraction_Service import ExtractionService

def test_extract_text_pdf(monkeypatch, tmp_path):
    fake_text = "Hello world"

    def mock_extract(*args, **kwargs):
        return fake_text

    monkeypatch.setattr(
        "app.extraction.pdf_Extraction.PdfExtraction.extract",
        mock_extract
    )

    service = ExtractionService()
    result = service.extract("dummy.pdf", "pdf_text")

    assert result == fake_text
