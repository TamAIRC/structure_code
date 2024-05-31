# database/database_access/dba.py
from bson import ObjectId
import os
import sys
from abc import ABC, abstractmethod
from typing import Any, Dict, List
from bson import ObjectId

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from database.connect.connect import Connection as db_connection
from utils.util import normalize_id, validate_condition, prepare_bulk_updates

class DBA(ABC):
    # cac thong tin chung cua moi va hanh dong chung cua moi lop quan ly, tuong tac co so du lieu
    def __init__(self, collection):
        self.connection = db_connection()
        self.connection.get_connection()
        self.collection = self.connection.database[collection]
        print("DBA init")
    
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