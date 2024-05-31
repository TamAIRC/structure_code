# database/database_access/result_dba.py
from typing import List
import os
import sys
from pymongo import MongoClient

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from configs import db_config
from database.database_models.question_model import QuestionDBO
from database.database_access.mongodb_dba import MongoDB_DBA

class ResultDBA:
    def __init__(self, connection):
        self.connection = connection
        self.dba = MongoDB_DBA(connection, [db_config.CONNECT['RESULT_COLLECTION'], db_config.CONNECT['QUESTION_COLLECTION']])

    def get_n_questions(self, player_id) -> List[QuestionDBO]:
        result = self.dba.find_by_id(player_id)
        if result is None:
            return []
        return [QuestionDBO.from_json_obj(question) for question in result.get('questions', [])]
