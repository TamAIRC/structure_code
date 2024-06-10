from abc import ABC, abstractmethod
from typing import Any, List


class BaseDBA(ABC):
    def __init__(self) -> None:
        pass

    @abstractmethod
    def transaction(self, query_func):
        """Perform a transaction. Implementation depends on specific use case."""
        pass

    @abstractmethod
    def find_one(self, condition) -> Any:
        pass

    @abstractmethod
    def find_many(self, n: int, condition) -> List[Any]:
        pass

    @abstractmethod
    def insert_one(self, obj: Any):
        pass

    @abstractmethod
    def insert_many(self, obj: Any):
        pass

    @abstractmethod
    def update_one(self, condition, new_value: List[Any]) -> bool:
        pass

    @abstractmethod
    def update_many(self, condition: List[Any], new_values: List[Any]) -> bool:
        pass

    @abstractmethod
    def delete_one(self, condition) -> bool:
        pass

    @abstractmethod
    def delete_many(self, condition) -> bool:
        pass
