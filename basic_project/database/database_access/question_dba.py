# database/database_access/question_dba.py
from database.database_access.dba import DBA
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from configs import db_config
from utils.json_encoder import convert_objectid_to_str
from utils.util import normalize_id, validate_condition, prepare_bulk_updates
from database.database_models.question_dbo import QuestionDBO

class QuestionDBA(DBA):
    def __init__(self):
        collection_name = db_config.SCHEMA['QUESTION_COLLECTION']
        super().__init__(collection_name)
        print("QuestionDBA init")
    
    def find_by_id(self, id):
        try:
            # open session
            normalized_id = normalize_id(id)
            # dong sesion
            # dong connection
            return QuestionDBO.from_json_obj(self.collection.find_one({"_id": normalized_id}))
        except ValueError as e:
            print(e)
            return None
    
    def find_one(self, condition):
        try:
            validated_condition = validate_condition(condition)
            return self.collection.find(validated_condition).limit(1)
        except ValueError as e:
            print(e)
            return None

    def find_many(self, n, condition):
        try:
            validated_condition = validate_condition(condition)
            return list(self.collection.find(validated_condition).limit(n))
        except ValueError as e:
            print(e)
            return None
    
    def update_one_by_id(self, id, new_value):
        try:
            normalized_id = normalize_id(id)
            return self.collection.update_one({"_id": normalized_id}, {"$set": new_value})
        except ValueError as e:
            print(e)
            return None
    
    def update_many_by_id(self, ids, new_values):
        try:
            bulk_updates = prepare_bulk_updates(ids, new_values)
            return self.collection.bulk_write(bulk_updates)
        except ValueError as e:
            print(e)
            return None

    def get_questions(self, N):
        questions = self.find_many(N, {})
        if questions is None:
            return []
        question_dbo = [QuestionDBO.from_json_obj(question) for question in questions]
        return question_dbo
    
    def update_question(self, question_dbo):
        updated_question = self.update_one_by_id(question_dbo.get_id(), question_dbo.to_json())
        if updated_question is None:
            return None
        return updated_question