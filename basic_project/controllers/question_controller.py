# controllers/question_controller.py
from fastapi import HTTPException
from typing import List
from database.database_access.question_dba import QuestionDBA

class QuestionController:
    def __init__(self):
        self.question_dba = QuestionDBA()

    async def get_questions(self, N):
        try:
            questions = self.question_dba.get_questions()
            # thuc hien convert ket qua tu list question sang dang mong muon
            successed = True    
            return successed, questions
        except Exception as e:
            # phan hoi loi voi ket qua rong
            successed = False
            return successed, None
