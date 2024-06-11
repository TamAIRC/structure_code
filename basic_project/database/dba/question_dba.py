# database/database_access/question_dba.py
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from logger.logger import Logger
from database.dbo.question_dbo import QuestionDBO as Question
from database.dba.mongo_dba import MongoDBA
from configs import db_config
from utils.util import (
    normalize_id,
    validate_condition,
)

from pymongo.errors import PyMongoError
from bson import ObjectId
from typing import Any, Dict, List


class QuestionDBA(MongoDBA):
    def __init__(self):
        super().__init__(db_config.SCHEMA["QUESTIONS"])

    # Private funtion
    def __find_one(self, condition: Dict[str, Any], session=None) -> Question:
        pass

    def __find_many(
        self, condition: Dict[str, Any], n: int = None, session=None
    ) -> List[Question]:
        pass

    def __find_by_id(self, id, session=None) -> Question:
        pass

    def __find_by_ids(self, ids: List[Any], session=None) -> List[Question]:
        pass

    def __insert_one(self, obj: Any, session=None) -> ObjectId:
        pass

    def __insert_many(self, obj: Any, session=None) -> List[ObjectId]:
        pass

    def __update_one(
        self, condition: Dict[str, Any], new_value: List[Any], session=None
    ) -> bool:
        try:
            result = self.collection.update_one(condition, {"$set": new_value}, session=session)
            return result.modified_count > 0
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when update one: {err}")
            return False

    def __update_many(
        self, condition: Dict[str, Any], new_values: List[Any], session=None
    ) -> bool:
        try:
            result = self.collection.update_many(condition, {"$set": new_values}, session=session)
            return result.modified_count > 0
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when update many: {err}")
            return False

    def __update_by_id(self, id, new_value: List[Any], session=None) -> bool:
        try:
            normalized_id = normalize_id(id)
            result = self.collection.update_one(
                {"_id": normalized_id}, {"$set": new_value}, session=session
            )
            return result.modified_count > 0
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when update by id: {err}")
            return False

    def __update_by_ids(
        self, ids: List[Any], new_values: List[Any], session=None
    ) -> bool:
        try:
            bulk_updates = self.prepare_bulk_updates(ids, new_values)
            result = self.collection.bulk_write(bulk_updates, session=session)
            return result.modified_count > 0
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when update many by id: {err}")
            return False

    def __delete_one(self, condition: Dict[str, Any], session=None) -> bool:
        try:
            result = self.collection.delete_one(condition, session=session)
            return result.deleted_count > 0
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when delete one: {err}")
            return False

    def __delete_many(self, condition: Dict[str, Any], session=None) -> bool:
        try:
            result = self.collection.delete_many(condition, session=session)
            return result.deleted_count > 0
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when delete many: {err}")
            return False

    def __delete_by_id(self, id, session=None) -> bool:
        try:
            normalized_id = normalize_id(id)
            result = self.collection.delete_one({"_id": normalized_id}, session=session)
            return result.deleted_count > 0
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when delete by id: {err}")
            return False

    def __delete_by_ids(self, ids: List[Any], session=None) -> bool:
        try:
            bulk_deletes = self.prepare_bulk_deletes(ids)
            result = self.collection.bulk_write(bulk_deletes, session=session)
            return result.deleted_count > 0
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when delete many by id: {err}")
            return False

    # Public funtion
    def find_one(self, condition: Dict[str, Any]) -> Question:
        result = self.transaction(self.__find_one, condition=condition)
        return result

    def find_many(self, condition: Dict[str, Any], n: int = None) -> List[Question]:
        result = self.transaction(self.__find_many, condition=condition)
        return result

    def find_by_id(self, id) -> Question:
        result = self.transaction(self.__find_by_id, id=id)
        return result

    def find_by_ids(self, ids: List[Any]) -> List[Question]:
        result = self.transaction(self.__find_by_ids, ids=ids)
        return result

    def insert_one(self, obj: Any) -> ObjectId:
        result = self.transaction(self.__insert_one, obj=obj)
        return result

    def insert_many(self, obj: Any) -> List[ObjectId]:
        result = self.transaction(self.__insert_many, obj=obj)
        return result

    def update_one(self, condition: Dict[str, Any], new_value: List[Any]) -> bool:
        result = self.transaction(
            self.__update_one, condition=condition, new_value=new_value
        )
        return result

    def update_many(self, condition: Dict[str, Any], new_values: List[Any]) -> bool:
        result = self.transaction(
            self.__update_many, condition=condition, new_values=new_values
        )
        return result

    def update_by_id(self, id, new_value: List[Any]) -> bool:
        result = self.transaction(self.__update_by_id, id=id, new_value=new_value)
        return result

    def update_by_ids(self, ids: List[Any], new_values: List[Any]) -> bool:
        result = self.transaction(self.__update_by_ids, ids=ids, new_values=new_values)
        return result

    def delete_one(self, condition: Dict[str, Any]) -> bool:
        result = self.transaction(self.__delete_one, condition=condition)
        return result

    def delete_many(self, condition: Dict[str, Any]) -> bool:
        result = self.transaction(self.__delete_many, condition=condition)
        return result

    def delete_by_id(self, id) -> bool:
        result = self.transaction(self.__delete_by_id, id=id)
        return result

    def delete_by_ids(self, ids: List[Any]) -> bool:
        result = self.transaction(self.__delete_by_ids, ids=ids)
        return result
