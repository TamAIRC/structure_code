import os
import sys


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)
from logger.logger import Logger
from database.connect.mongo_connection import MongoConnection
from database.dbo.question_dbo import QuestionDBO
from database.dba.dba import DBA
from utils.util import normalize_id, validate_condition, prepare_bulk_updates

from bson import ObjectId
from typing import Any, Dict, List
from pymongo.errors import BulkWriteError, PyMongoError


class MongoDB_DBA(DBA):
    dbo_classes = {}

    def __init__(self, connection, collection_names):
        super().__init__(connection, collection_names)
        self.client = MongoConnection()
        self.logger = Logger("MongoDB_DBA")
        self.collections = {
            name: self.connection.database[name] for name in collection_names
        }
        self.dbo_classes = {
            "questions": QuestionDBO
            # Add other collection to DBO class mappings here
        }
        if len(collection_names) == 1:
            self.collection = self.collections[collection_names[0]]
            self.dbo_class = self.dbo_classes.get(collection_names[0])
        else:
            self.collection = self.join_collections(collection_names)
            self.dbo_class = None  # Handle multi-collection cases appropriately

    def find_by_id(self, id: ObjectId) -> Any:
        results = []
        try:
            normalized_id = normalize_id(id)
            for name, collection in self.collections.items():
                result = collection.find_one({"_id": normalized_id})
                if result:
                    dbo_class = self.dbo_classes.get(name)
                    if dbo_class:
                        results.append(dbo_class.from_json_obj(result))
                    else:
                        results.append(result)
            return results if results else None
        except ValueError as e:
            self.logger.log_error("ValueError", e)
            return None
        except PyMongoError as e:
            self.logger.log_error("PyMongoError", e)
            return None

    def find_one(self, condition: Dict[str, Any]) -> Any:
        results = []
        try:
            validated_condition = validate_condition(condition)
            for name, collection in self.collections.items():
                result = collection.find_one(validated_condition)
                if result:
                    dbo_class = self.dbo_classes.get(name)
                    if dbo_class:
                        results.append(dbo_class.from_json_obj(result))
                    else:
                        results.append(result)
            return results if results else None
        except ValueError as e:
            self.logger.log_error("ValueError:", e)
            return None
        except PyMongoError as e:
            self.logger.log_error("PyMongoError:", e)
            return None

    def find_many(self, n: int, condition: Dict[str, Any]) -> List[Any]:
        all_results = []
        try:
            validated_condition = validate_condition(condition)
            for name, collection in self.collections.items():
                results = collection.find(validated_condition).limit(n)
                dbo_class = self.dbo_classes.get(name)
                for result in results:
                    if dbo_class:
                        all_results.append(dbo_class.from_json_obj(result))
                    else:
                        all_results.append(result)
            return all_results
        except ValueError as e:
            self.logger.log_error("ValueError:", e)
            return None
        except PyMongoError as e:
            self.logger.log_error("PyMongoError:", e)
            return None

    def update_one_by_id(self, id: ObjectId, new_value: Dict[str, Any]) -> bool:
        try:
            normalized_id = normalize_id(id)
            new_values_dict = {
                key: value for key, value in new_value.items() if key != "_id"
            }
            result = self.collection.update_one(
                {"_id": normalized_id}, {"$set": new_values_dict}
            )
            return result
        except ValueError as e:
            self.logger.log_error("ValueError:", e)
            return None
        except PyMongoError as e:
            self.logger.log_error("PyMongoError:", e)
            return None

    def update_many_by_id(
        self, ids: List[ObjectId], new_values: List[Dict[str, Any]]
    ) -> bool:
        try:
            bulk_updates = prepare_bulk_updates(ids, new_values)
            result = self.collection.bulk_write(bulk_updates)
            return result
        except ValueError as e:
            self.logger.log_error("ValueError:", e)
            return None
        except BulkWriteError as e:
            self.logger.log_error("BulkWriteError:", e)
            return None
        except PyMongoError as e:
            self.logger.log_error("PyMongoError:", e)
            return None

    def insert(self, obj: Any) -> ObjectId:
        try:
            if self.dbo_class:
                obj = self.dbo_class.to_json_obj(obj)
            result = self.collection.insert_one(obj)
            return result.inserted_id
        except PyMongoError as e:
            self.logger.log_error("PyMongoError:", e)
            return None

    def delete_by_id(self, id: ObjectId) -> bool:
        try:
            normalized_id = normalize_id(id)
            result = self.collection.delete_one({"_id": normalized_id})
            return result.deleted_count > 0
        except ValueError as e:
            self.logger.log_error("ValueError:", e)
            return False
        except PyMongoError as e:
            self.logger.log_error("PyMongoError:", e)
            return False

    def join_collections(self, collection_names):
        pass


if __name__ == "__main__":
    from database.dbo.question_dbo import QuestionDBO

    # Add other collection to DBO class mappings
    MongoDB_DBA.dbo_classes.update(
        {
            "questions": QuestionDBO,
            # Add other mappings as needed
        }
    )
    # Example usage
    connection = MongoConnection()
    dba = MongoDB_DBA(connection, ["questions"])

    # Test the methods
    result_one = dba.find_one({"difficulty": 5})
    print("Find one: difficulty = 5 :", result_one,"\n------------------")
    result_by_id = dba.find_by_id("66260e94a51b34b732f211dd")
    print("Find by id: id = 66260e94a51b34b732f211dd :", result_by_id,"\n------------------")
    result_many = dba.find_many(10, {"category": "Geography"})
    print("Find many: category = Geography :", result_many,"\n------------------")
    # Có thực hiện validate định dạng trước find trong db
    result_many = dba.find_many(10, {"difficulty": "5"})
    print("Find many: difficulty = 5 :", result_many, "\n------------------")

