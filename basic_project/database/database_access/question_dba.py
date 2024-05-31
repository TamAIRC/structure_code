# database/database_access/question_dba.py
from typing import List
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from configs import db_config
from utils.json_encoder import convert_objectid_to_str
from database.database_access.dba import DBA
from database.database_models.question_model import QuestionDBO

class QuestionDBA():
    def __init__(self, connection):
        self.dba = DBA.create_dba(db_config.DB_TYPE, connection, [db_config.CONNECT['QUESTION_COLLECTION']])

    def get_n_questions(self, n: int) -> List[QuestionDBO]:
        questions = self.dba.find_many(n, {})
        if questions is None:
            return []
        return [QuestionDBO.from_json_obj(question) for question in questions]
    
    def update_n_questions(self, questions: List[QuestionDBO]):
        questions_json = [question.to_json() for question in questions]
        for question in questions_json:
            print(question)
            self.dba.update_one_by_id(question)
