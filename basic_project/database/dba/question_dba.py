# database/database_access/question_dba.py
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

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
        except ValueError as e:
            print(e)
            return None

    def find_one(self, condition: Dict[str, Any], session=None) -> Question:
        try:
            validated_condition = validate_condition(condition)
            result = self.collection.find_one(validated_condition, session=session)
            if result:
                return Question(**result)
            return None
        except ValueError as e:
            print(e)
            return None

    def find_many(
        self, n: int, condition: Dict[str, Any], session=None
    ) -> List[Question]:
        try:
            validated_condition = validate_condition(condition)
            cursor = self.collection.find(validated_condition, session=session).limit(n)
            return [Question.from_json_obj(data) for data in cursor]
            # return cursor
        except ValueError as e:
            print(e)
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

if __name__ == "__main__":
    # Example usage
    # Get question
    question_dba = QuestionDBA()
    # data = question_dba.transaction(question_dba.get_questions, n=2)
    # print(data)

    # Update question
    # new_questions_data = [
    #     {
    #         "_id": "66260e94a51b34b732f211dd",
    #         "category": "History",
    #         "subcategory": "Vietnam History",
    #         "content": "What is the capital of Vietnam?",
    #         "answers": ["Hanoi", "Ninh Binh", "Thai Nguyen", "Da Nang"],
    #         "correct_answer": "Hanoi",
    #         "difficulty": 1,
    #         "required_rank": 1,
    #         "language": 1,
    #         "multimedia": "66260e86a51b34b732f21182"
    #     }, 
    #     {
    #         "_id": "66260e94a51b34b732f211de",
    #         "category": "History",
    #         "subcategory": "World History",
    #         "content": "What is the capital of France?",
    #         "answers": ["Paris", "London", "Barcelona", "Madrid"],
    #         "correct_answer": "Paris",
    #         "difficulty": 1,
    #         "required_rank": 1,
    #         "language": 1,
    #         "multimedia": "66260e88a51b34b732f2118e"
    #     }, 
    # ]

    # questions_dbo = [Question.from_json_obj(data) for data in new_questions_data]
    # updated_status = question_dba.transaction(question_dba.update_questions, questions=questions_dbo)
    # data = question_dba.transaction(question_dba.get_questions, n=2)
    # print(data)

    # Delete questions
    # delete_data = ["66260e94a51b34b732f211df", "66260e94a51b34b732f211e0"]
    # delete_data_obj = [normalize_id(data) for data in delete_data]
    # print(delete_data_obj)
    # deleted_status = question_dba.transaction(question_dba.delete_questions, ids=delete_data)
    # print("Deleted status: ", deleted_status)

    # Insert a new question
    # new_question = Question(
    #     id=ObjectId(),
    #     category=1,
    #     subcategory="Math",
    #     content="What is 2+2?",
    #     answers=["2", "3", "4", "5"],
    #     correct_answer="4",
    #     multimedia=ObjectId(),
    # )
    # def sample_transaction(session):
    #     # Insert a new question within the transaction
    #     new_question = Question(
    #         id=ObjectId(),
    #         category=1,
    #         subcategory="Math",
    #         content="What is 2+2?",
    #         answers=["2", "3", "4", "5"],
    #         correct_answer="4",
    #         multimedia=ObjectId(),
    #     )
    #     inserted_id = question_dba.insert(new_question, session=session)
    #     print(f"Inserted question with ID: {inserted_id}")

    # # Execute the transaction
    # transaction_result = QuestionDBA.base_transaction(sample_transaction)
    # if transaction_result:
    #     print("Transaction executed successfully")
    # else:
    #     print("Transaction failed")
    # inserted_id = question_dba.insert(new_question)
    # print(f"Inserted question with ID: {inserted_id}")

    # # Find a question by ID
    # question = question_dba.find_by_id(inserted_id)
    # print(question)

    # # Update a question by ID
    # update_result = question_dba.update_one_by_id(
    #     inserted_id, {"content": "What is 3+3?"}
    # )
    # print(f"Update successful: {update_result}")

    # # Find many questions
    # questions = question_dba.find_many(5, {"category": 1})
    # for q in questions:
    #     print(q)

    # # Delete a question by ID
    # delete_result = question_dba.delete_by_id(inserted_id)
    # print(f"Delete successful: {delete_result}")
