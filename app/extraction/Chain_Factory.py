from .Extraction_Factory import ExtractionFactory

class ExtractionChain:

    def __init__(self, category: str):
        self.extractor = ExtractionFactory.get_extractor(category)

    def extract(self, file_path: str) -> str:
        return self.extractor.extract(file_path)
