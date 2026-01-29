from abc import ABC, abstractmethod

class BaseExtraction(ABC):
    """
    Strategy Interface
    """

    @abstractmethod
    def extract(self, file_path: str) -> str:
        pass
