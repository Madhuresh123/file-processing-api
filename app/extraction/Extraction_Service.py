from .Chain_Factory import ExtractionChain

class ExtractionService:
    """
    Facade – single entry point for extraction
    """

    def extract(self, file_path: str, category: str) -> str:
        chain = ExtractionChain(category)
        return chain.extract(file_path)
