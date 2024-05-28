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
            #if not questions:
                # raise HTTPException(status_code=404, detail="No questions found") Khong bao loi len giao dien tu controller
            successed = True    
            return successed, questions
        except Exception as e:
            # raise HTTPException(status_code=500, detail=str(e))
            successed = False
            return successed, None
