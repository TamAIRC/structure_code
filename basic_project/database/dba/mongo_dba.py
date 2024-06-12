import os
import sys
from abc import abstractmethod
from typing import Any, Dict, List
from bson import ObjectId
from pymongo import UpdateOne, DeleteOne


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from utils.util import normalize_id
from configs.db_config import CONNECT
from logger.logger import Logger
from patterns.base_dba import BaseDBA
from database.connection.mongo_connection import MongoConnection

from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure, PyMongoError


class MongoDBA(BaseDBA):
    def __init__(self, collection_name):
        self.collection_name = collection_name
        self.collection = None

    def transaction(self, query_func, **kwargs):
        """Perform a transaction. Implementation depends on specific use case."""
        self.connection = MongoConnection(CONNECT["mongo"]["DATABASE"])
        self.collection = self.connection.get_collection(self.collection_name)
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
    def find_one(self, condition: Dict[str, Any]) -> Any:
        """
        Find a single document in a collection that matches the specified condition.

        Parameters:
            condition (Dict[str, Any]): The condition to match the document.

        Returns:
            Any: The matched document, or None if no document matches the condition.
        """
        pass

    @abstractmethod
    def find_many(self, condition: Dict[str, Any], n: int = None) -> List[Any]:
        """
        Find multiple documents in a collection that match the specified condition.

        Parameters:
            condition (List[Any]): The condition to match the documents.
            n (int, optional): The maximum number of documents to return. If None, returns all matched documents.

        Returns:
            List[Any]: A list of matched documents.
        """
        pass

    @abstractmethod
    def insert_one(self, obj: Any):
        pass

    @abstractmethod
    def insert_many(self, obj: Any):
        pass

    @abstractmethod
    def update_one(self, condition: Dict[str, Any], new_value: List[Any]) -> bool:
        pass

    @abstractmethod
    def update_many(self, condition: Dict[str, Any], new_values: List[Any]) -> bool:
        pass

    @abstractmethod
    def delete_one(self, condition: Dict[str, Any]) -> bool:
        pass

    @abstractmethod
    def delete_many(self, condition: Dict[str, Any]) -> bool:
        pass

    @staticmethod
    def prepare_bulk_updates(ids: List[ObjectId], new_values: List[Dict[str, Any]]):
        """
        #     Prepare a list of bulk update operations.

        #     Parameters:
        #     - ids: list of str or ObjectId
        #     - new_values: list of dict

        #     Returns:
        #     - list of dict
        #"""
        if len(ids) != len(new_values):
            raise ValueError("The length of ids and new_values must match")
        bulk_updates = []
        for _id, values in zip(ids, new_values):
            try:
                normalized_id = normalize_id(_id)
                # Ensure _id is not included in the update part
                update_values = {k: v for k, v in values.items() if k != "_id"}
                bulk_updates.append(
                    UpdateOne({"_id": normalized_id}, {"$set": update_values})
                )
            except ValueError as e:
                raise ValueError(f"Error processing ID {id}: {e}") from e
        return bulk_updates

    @staticmethod
    def prepare_bulk_deletes(ids):
        """
        Prepare a list of bulk delete operations.

        Parameters:
        - ids: list of str or ObjectId

        Returns:
        - list of DeleteOne operations
        """
        bulk_deletes = []
        for id in ids:
            try:
                normalized_id = normalize_id(id)
                bulk_deletes.append(DeleteOne({"_id": normalized_id}))
            except ValueError as e:
                raise ValueError(f"Error processing ID {id}: {e}") from e

        return bulk_deletes