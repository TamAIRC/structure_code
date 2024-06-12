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

    # Private function
    def __find_one(self, condition: Dict[str, Any], session=None) -> Question:
        try:
            validated_condition = validate_condition(condition)
            result = self.collection.find_one(validated_condition, session=session)
            if result:
                return Question(**result)
            return None
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when find one: {err}")
            return None

    def __find_many(
        self, condition: Dict[str, Any], n: int = None, session=None
    ) -> List[Question]:
        try:
            validated_condition = validate_condition(condition)
            cursor = self.collection.find(validated_condition, session=session).limit(n)
            return [Question.from_json_obj(data) for data in cursor]
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when find many: {err}")
            return None

    def __find_by_id(self, id, session=None) -> Question:
        try:
            normalized_id = normalize_id(id)
            result = self.collection.find_one({"_id": normalized_id}, session=session)
            if result:
                return Question(**result)
            return None
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when find by id: {err}")
            return None

    def __find_by_ids(self, ids: List[Any], session=None) -> List[Question]:
        try:
            normalized_ids = [normalize_id(id) for id in ids]
            pipeline = [
                {"$match": {"_id": {"$in": normalized_ids}}}
            ]
            results = self.collection.aggregate(pipeline, session=session)
            questions = [Question(**result) for result in results]
            return questions
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when finding by ids: {err}")
            return []

    def __insert_one(self, obj: Question, session=None) -> ObjectId:
        try:
            Question.validate_multimedia(obj.multimedia)
            data = obj.model_dump(exclude_defaults=True)
            result = self.collection.insert_one(data, session=session)
            return result.inserted_id
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when insert: {err}")
            return None

    def __insert_many(self, objs: List[Question], session=None) -> List[ObjectId]:
        try:
            for obj in objs:
                Question.validate_multimedia(obj.multimedia)
            data = [obj.model_dump(exclude_defaults=True) for obj in objs]
            result = self.collection.insert_many(data, session=session)
            return result.inserted_ids
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when insert many: {err}")
            return None

    def __update_one(
        self, condition: Dict[str, Any], new_value: Dict[str, Any], session=None
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
            print(new_values)
            result = self.collection.update_many(condition, {"$set": new_values}, session=session)
            return result.modified_count > 0
        except ValueError as err:
            print(err)
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
        self, ids: List[Any], new_values: List[Dict[str, Any]], session=None
    ) -> bool:
        try:
            bulk_updates = MongoDBA.prepare_bulk_updates(ids, new_values)
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


    # Public function
    def find_one(self, condition: Dict[str, Any]) -> Question:
        result = self.transaction(self.__find_one, condition=condition)
        return result

    def find_many(self, condition: Dict[str, Any], n: int = None) -> List[Question]:
        result = self.transaction(self.__find_many, condition=condition, n=n)
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

    def insert_many(self, objs: Any) -> List[ObjectId]:
        result = self.transaction(self.__insert_many, objs=objs)
        return result

    def update_one(self, condition: Dict[str, Any], new_value: Dict[str, Any]) -> bool:
        result = self.transaction(
            self.__update_one, condition=condition, new_value=new_value
        )
        return result

    def update_many(self, condition: Dict[str, Any], new_values: List[Any]) -> bool:
        result = self.transaction(
            self.__update_many, condition=condition, new_values=new_values
        )
        return result

    def update_by_id(self, id, new_value: Dict[str, Any]) -> bool:
        result = self.transaction(self.__update_by_id, id=id, new_value=new_value)
        return result

    def update_by_ids(self, ids: List[Any], new_values: List[Dict[str, Any]]) -> bool:
        print("ids:", ids)
        print("values:", new_values)
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

    def update_questions(self, questions: List[Question]):
        ids = [question.get_id() for question in questions]
        new_values = [question.to_json() for question in questions]
        result = self.transaction(self.__update_by_ids, ids= ids, new_values= new_values)
        return result
    