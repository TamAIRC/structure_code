# controllers/question_controller.py
from fastapi import HTTPException
from typing import List
from database.database_access.question_dba import QuestionDBA
from database.database_models.question_model import QuestionDBO
class QuestionController:
    def __init__(self):
        self.question_dba = QuestionDBA()

    async def get_n_questions(self, N):
        try:
            questions = self.question_dba.get_n_questions(N)
            successed = True    
            return successed, questions
        except Exception as e:
            successed = False
            return successed, None
        
    async def update_n_questions(self, questions):
        questions = [QuestionDBO.from_json_obj(question) for question in questions]
        try:
            self.question_dba.update_n_questions(questions)
            successed = True    
            return successed
        except Exception as e:
            successed = False
            return successed, None