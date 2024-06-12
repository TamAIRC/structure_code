from abc import ABC, abstractmethod
from typing import Any, List


class BaseDBA(ABC):
    def __init__(self, connection) -> None:
        self.connection = connection

    @abstractmethod
    def transaction(self, query_func):
        """Perform a transaction. Implementation depends on specific use case."""
        pass

    @abstractmethod
    def find_by_id(self, id) -> Any:
        pass

    @abstractmethod
    def find_one(self, condition) -> Any:
        pass

    @abstractmethod
    def find_many(self, n: int, condition) -> List[Any]:
        pass

    @abstractmethod
    def update_one_by_id(self, id, new_value) -> bool:
        pass

    @abstractmethod
    def update_many_by_id(self, ids: List[Any], new_values: List[Any]) -> bool:
        pass

    @abstractmethod
    def insert(self, obj: Any):
        pass

    @abstractmethod
    def delete_by_id(self, id) -> bool:
        pass
