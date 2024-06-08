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
    prepare_bulk_deletes,
    prepare_bulk_updates,
    validate_condition,
)

from pymongo.errors import PyMongoError
from bson import ObjectId
from typing import Any, Dict, List


class QuestionDBA(MongoDBA):
    def __init__(self):
        super().__init__(db_config.SCHEMA["QUESTIONS"])

    def find_by_id(self, id: ObjectId, session=None) -> Question:
        try:
            normalized_id = normalize_id(id)
            result = self.collection.find_one({"_id": normalized_id}, session=session)
            if result:
                return Question(**result)
            return None
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when find by id: {err}")
            return None

    def find_one(self, condition: Dict[str, Any], session=None) -> Question:
        try:
            validated_condition = validate_condition(condition)
            result = self.collection.find_one(validated_condition, session=session)
            if result:
                return Question(**result)
            return None
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when find one: {err}")
            return None

    def find_many(
        self, n: int, condition: Dict[str, Any], session=None
    ) -> List[Question]:
        try:
            validated_condition = validate_condition(condition)
            cursor = self.collection.find(validated_condition, session=session).limit(n)
            return [Question.from_json_obj(data) for data in cursor]
            # return cursor
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when find many: {err}")
            return None

    def insert(self, obj: Question, session=None) -> ObjectId:
        try:
            Question.validate_multimedia(obj.multimedia)
            data = obj.model_dump(exclude_defaults=True)
            print("insert: ", data)
            result = self.collection.insert_one(data, session=session)
            return result.inserted_id
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when insert: {err}")
            return None

    def insert_many(self, objs: List[Question], session=None) -> List[ObjectId]:
        try:
            Question.validate_multimedia([obj.multimedia for obj in objs])
            data = [obj.model_dump(exclude_defaults=True) for obj in objs]
            result = self.collection.insert_many(data, session=session)
            return result.inserted_ids
        except ValueError as err:
            Logger("QuestionDBA").log_error(f"Error when insert many: {err}")
            return None

    def update_one_by_id(
        self, id: ObjectId, new_value: Dict[str, Any], session=None
    ) -> bool:
        try:
            normalized_id = normalize_id(id)
            result = self.collection.update_one(
                {"_id": normalized_id}, {"$set": new_value}, session=session
            )
            return result.modified_count > 0
        except ValueError as e:
            print(e)
            return False

    def update_many_by_id(
        self, ids: List[ObjectId], new_values: List[Dict[str, Any]], session=None
    ) -> bool:
        try:
            bulk_updates = prepare_bulk_updates(ids, new_values)
            result = self.collection.bulk_write(bulk_updates, session=session)
            return result.modified_count > 0
        except ValueError as e:
            print(e)
            return False

    def insert(self, obj: Question, session=None) -> ObjectId:
        try:
            data = obj.to_json()
            result = self.collection.insert_one(data, session=session)
            return result.inserted_id
        except ValueError as e:
            print(e)
            return None

    def delete_by_id(self, id: ObjectId, session=None) -> bool:
        try:
            normalized_id = normalize_id(id)
            result = self.collection.delete_one({"_id": normalized_id}, session=session)
            return result.deleted_count > 0
        except ValueError as e:
            print(e)
            return False

    def get_questions(self, n: int, session=None) -> List[Question]:
        try:
            questions = self.find_many(n, {}, session=session)
            if questions is None:
                return []
            return questions
        except PyMongoError as e:
            print(f"Error getting questions: {e}")
            return []

    def update_questions(self, questions: List[Question], session=None): 
        ids, new_values = zip(*((question.get_id(), question.to_json()) for question in questions))
        updated_question = self.update_many_by_id(list(ids), list(new_values), session=session)
        if updated_question is None:
            return None
        return updated_question
    
    def delete_questions(self, ids: List[ObjectId], session=None):
        try:
            bulk_deletes = prepare_bulk_deletes(ids)
            result = self.collection.bulk_write(bulk_deletes, session=session)
            return result.deleted_count
        except ValueError as e:
            print(e)
            return None