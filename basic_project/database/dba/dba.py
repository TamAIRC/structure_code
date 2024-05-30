import os
import sys


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from abc import ABC, abstractmethod
from typing import Any, Dict, List
from bson import ObjectId
from database.connect.connect import Connection as db_connection


class DBA(ABC):
    def __init__(self, collection_name: str):
        self.connection = db_connection()
        self.connection.get_connection()
        self.collection = self.connection.get_collection(collection_name)

    @abstractmethod
    def find_by_id(self, id: ObjectId) -> Any:
        pass

    @abstractmethod
    def find_one(self, condition: Dict[str, Any]) -> Any:
        pass

    @abstractmethod
    def find_many(self, n: int, condition: Dict[str, Any]) -> List[Any]:
        pass

    @abstractmethod
    def update_one_by_id(self, id: ObjectId, new_value: Dict[str, Any]) -> bool:
        pass

    @abstractmethod
    def update_many_by_id(
        self, ids: List[ObjectId], new_values: List[Dict[str, Any]]
    ) -> bool:
        pass

    @abstractmethod
    def insert(self, obj: Any) -> ObjectId:
        pass

    @abstractmethod
    def delete_by_id(self, id: ObjectId) -> bool:
        pass
