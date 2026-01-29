import magic
from pathlib import Path
from .base import BaseDetector

class MimeDetector(BaseDetector):

    def detect(self, file_path: str, context: dict) -> dict:
        mime = magic.from_file(file_path, mime=True)
        ext = Path(file_path).suffix.lower()

        context["mime"] = mime
        context["extension"] = ext

        if mime == "application/pdf":
            return {"category": "pdf"}

        if mime == "image/jpeg":
            return {"category": "jpg"}

        if mime == "image/png":
            return {"category": "png"}

        if mime == "word":
            return {"category": "word"}

        if mime == "excel" or mime == "spreadsheet":
            return {"category": "excel"}

        if mime in [
            "application/msword",
            "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
        ]:
            return {"category": "word"}

        return {"category": "unknown"}
