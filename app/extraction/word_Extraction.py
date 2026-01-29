from docx import Document
from .Base_Extraction import BaseExtraction

class WordExtraction(BaseExtraction):

    def extract(self, file_path: str) -> str:
        doc = Document(file_path)
        return "\n".join(p.text for p in doc.paragraphs if p.text)
