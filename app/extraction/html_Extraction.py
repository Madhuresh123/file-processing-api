from bs4 import BeautifulSoup
from .Base_Extraction import BaseExtraction

class HtmlExtraction(BaseExtraction):

    def extract(self, file_path: str) -> str:
        try:
            with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                soup = BeautifulSoup(f, "html.parser")
            return soup.get_text(separator=" ")
        except Exception as e:
            raise RuntimeError(f"HTML extraction failed: {e}")
