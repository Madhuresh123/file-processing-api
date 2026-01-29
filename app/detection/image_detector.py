from .base import BaseDetector

class ImageDetector(BaseDetector):

    def detect(self, file_path: str, context: dict) -> dict:
        if context.get("mime") in ["image/jpeg", "image/png"]:
            return {"category": context["extension"].replace(".", "")}
        return {"category": "unknown"}
