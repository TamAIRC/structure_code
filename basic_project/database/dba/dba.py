import os
import sys


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from abc import ABC, abstractmethod
from typing import Any, Dict, List, Type
from bson import ObjectId

from database.connect.mongo_connection import MongoConnection as db_connection


class DBA(ABC):
    def __init__(self, collection_name: str):
        self.connection = db_connection()
        self.collection = self.connection.get_collection(collection_name)

    #! Chưa sử dụng hợp ý được
    @staticmethod
    def create_dba(dba_type: str, connection, collection_name: str) -> "DBA":
        dba_classes: Dict[str, str] = {
            "mongo": "database.dba.mongodb_dba.MongoDB_DBA",
            "sql": "database.dba.sql_dba.SQL_DBA",
        }

        if dba_type not in dba_classes:
            raise ValueError(
                f"Unsupported DBA type '{dba_type}'. Supported types are: {', '.join(dba_classes.keys())}"
            )

        module_name, class_name = dba_classes[dba_type].rsplit(".", 1)

        try:
            module = __import__(module_name, fromlist=[class_name])
            dba_class: Type[DBA] = getattr(module, class_name)
            return dba_class(connection, collection_name)
        except (ImportError, AttributeError) as e:
            raise ImportError(f"Error importing '{dba_type}' DBA class: {e}")

    def transaction(self, query):
        """Perform a transaction. Implementation depends on specific use case."""
        pass

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
