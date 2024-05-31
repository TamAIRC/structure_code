# controllers/question_controller.py
from fastapi import HTTPException
from typing import List
from database.database_access.question_dba import QuestionDBA
from database.database_models.question_model import QuestionDBO
from database.database_connection.connection import Connection
from configs import db_config
class GetQuestionController:
    def __init__(self):
        connection_params = {
            'uri_template': db_config.CONNECT['URL'],
            'database_name': db_config.CONNECT['DATABASE']
        }
        connection = Connection.create_connection(db_config.DB_TYPE, **connection_params)
        connection.connect(db_config.USERNAME, db_config.PASSWORD)
        self.question_dba = QuestionDBA(connection)
        self.questions = None
    def get_questions(self):
        return self.questions
    async def get_n_questions(self, N):
        try:
            questions = self.question_dba.get_n_questions(N)
            print(questions)
            self.questions = questions
            json_questions = [QuestionDBO.to_json(question) for question in questions]
            print(json_questions)
            successed = True    
            return successed, json_questions
        except Exception as e:
            successed = False
            return successed, None
        
    # async def update_n_questions(self, questions):
    #     questions = [QuestionDBO.from_json_obj(question) for question in questions]
    #     try:
    #         self.question_dba.update_n_questions(questions)
    #         successed = True    
    #         return successed
    #     except Exception as e:
    #         successed = False
    #         return successed, None