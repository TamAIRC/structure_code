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
        self, condition: List[Any], n: int = None, session=None
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
        pass

    def __update_many(
        self, condition: List[Any], new_values: List[Any], session=None
    ) -> bool:
        pass

    def __update_by_id(self, id, new_value: List[Any], session=None) -> bool:
        pass

    def __update_by_ids(
        self, ids: List[Any], new_values: List[Any], session=None
    ) -> bool:
        pass

    def __delete_one(self, condition: Dict[str, Any], session=None) -> bool:
        pass

    def __delete_many(self, condition: List[Any], session=None) -> bool:
        pass

    def __delete_by_id(self, id, session=None) -> bool:
        pass

    def __delete_by_ids(self, ids: List[Any], session=None) -> bool:
        pass

    # Public funtion
    def find_one(self, condition: Dict[str, Any]) -> Question:
        result = self.transaction(self.__find_one, condition=condition)
        return result

    def find_many(self, condition: List[Any], n: int = None) -> List[Question]:
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

    def update_many(self, condition: List[Any], new_values: List[Any]) -> bool:
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

    def delete_many(self, condition: List[Any]) -> bool:
        result = self.transaction(self.__delete_many, condition=condition)
        return result

    def delete_by_id(self, id) -> bool:
        result = self.transaction(self.__delete_by_id, id=id)
        return result

    def delete_by_ids(self, ids: List[Any]) -> bool:
        result = self.transaction(self.__delete_by_ids, ids=ids)
        return result
