from abc import ABC, abstractmethod

class BaseNormalization(ABC):

    @abstractmethod
    def normalize(self, text: str) -> str:
        pass
