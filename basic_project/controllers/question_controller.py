# controllers/question_controller.py
from fastapi import HTTPException
from typing import List
from database.database_access.question_dba import QuestionDBA
from database.database_models.question_dbo import QuestionDBO

class QuestionController:
    def __init__(self):
        self.question_dba = QuestionDBA()

    async def get_questions(self, N):
        try:
            N = int(N)
            questions = self.question_dba.get_questions(N)
            # thuc hien convert ket qua tu list question sang dang mong muon
            questions_json = [question.to_json() for question in questions]
            succeeded = True    
            return succeeded, questions_json
        except Exception as e:
            # phan hoi loi voi ket qua rong
            succeeded = False
            return succeeded, None 
    
    async def update_one_by_id(self, question: QuestionDBO):
        try:
            # thuc hien update question
            updated_question = self.question_dba.update_question(question)
            succeeded = True
            return succeeded, updated_question
        except Exception as e:
            # phan hoi loi
            succeeded = False
            return succeeded