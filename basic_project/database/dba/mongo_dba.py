import os
import sys
from abc import ABC, abstractmethod
from typing import Any, Dict, List
from bson import ObjectId


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from configs.db_config import CONNECT
from logger.logger import Logger
from patterns.base_dba import BaseDBA
from database.connection.mongo_connection import MongoConnection

from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure, PyMongoError


class MongoDBA(BaseDBA):
    def __init__(self, collection_name):
        self.connection = MongoConnection(CONNECT["mongo"]["DATABASE"])
        self.collection = self.connection.get_collection(collection_name)

    def transaction(self, query_func, **kwargs):
        """Perform a transaction. Implementation depends on specific use case."""
        if self.connection is None:
            Logger("MongoDBA").log_error("No MongoDB client available for transaction")
            return None

        with self.connection.client.start_session() as session:
            try:
                session.start_transaction()
                result = query_func(session=session, **kwargs)
                session.commit_transaction()
                Logger("MongoDBA").log_info("Transaction committed successfully")
            except (
                ConnectionFailure,
                ServerSelectionTimeoutError,
                PyMongoError,
            ) as err:
                Logger("MongoDBA").log_error("Transaction failed", err)
                session.abort_transaction()
                Logger("MongoDBA").log_info("Transaction aborted")
                result = None
        self.connection.close_connection()
        return result

    @abstractmethod
    def find_by_id(self, id) -> Any:
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
