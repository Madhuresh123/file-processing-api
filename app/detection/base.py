from abc import ABC, abstractmethod

class BaseDetector(ABC):
    @abstractmethod
    def detect(self, file_path: str, context: dict) -> dict:
        """
        Return detection result or {'category': 'unknown'}
        """
        pass
