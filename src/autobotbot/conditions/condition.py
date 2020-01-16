from abc import ABC, abstractmethod


class Condition(ABC):
    @abstractmethod
    def satisfied(self) -> bool:
        pass
