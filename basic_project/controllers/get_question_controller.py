# controllers/get_question_controller.py
from fastapi import HTTPException
from typing import List
from database.dba.question_dba import QuestionDBA
from database.dbo.question_dbo import QuestionDBO
from configs import db_config
class GetQuestionController:
    def __init__(self):
        self.dba = QuestionDBA()
        self.questions = None
    def get_questions(self):
        return self.questions
    async def get_n_questions(self, N):
        try:
            questions = self.dba.transaction(self.dba.get_questions, n=5)
            self.questions = questions
            json_questions = [QuestionDBO.to_json(question) for question in questions]
            successed = True    
            return successed, json_questions
        except Exception as e:
            successed = False
            return successed, None
        
   