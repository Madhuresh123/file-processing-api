from app.detection.service import FileDetectionService

def test_detect_pdf_text(tmp_path):
    # create fake file
    file = tmp_path / "test.pdf"
    file.write_text("This is a test PDF")

    service = FileDetectionService()
    result = service.detect(str(file))

    assert "category" in result
