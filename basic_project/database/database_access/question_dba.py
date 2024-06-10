# database/database_access/question_dba.py
from database.database_access.dba import DBA
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from configs import db_config
from utils.json_encoder import convert_objectid_to_str

class QuestionDBA(DBA):
    def __init__(self):
        super().__init__()
        # bo xung cau lenh xac dinh collection o day
        self.connection.database =  db_config.SCHEMA['QUESTION_COLLECTION'] #chu co dinh nghia cho cac schemas

    # dinh nghia lai ham abstract cua lop co so DBA
    def find_by_id(self, id):
        try:
            # open session
            normalized_id = normalize_id(id)
            result = self.collection.find_one({"_id": normalized_id})
            # dong sesion
            # dong connection
            return result
        except ValueError as e:
            print(e)
            return None

    
    def get_questions(self, N):
        questions = self.find_many(N, {})
        if questions is None:
            return []
        questions_serializable = [convert_objectid_to_str(question) for question in questions]
        return questions_serializable
