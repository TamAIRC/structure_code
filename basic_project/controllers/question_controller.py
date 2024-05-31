# controllers/question_controller.py
from fastapi import HTTPException
from typing import List
from database.database_access.question_dba import QuestionDBA
from bson import ObjectId


class QuestionController:
    def __init__(self):
        self.question_dba = QuestionDBA()

    def get_one_question_by_id(self, question_id):
        try:
            if not isinstance(question_id, ObjectId):
                question_id = ObjectId(question_id)
                result = self.question_dba.get_one_question(question_id)
                return result
        except Exception as e:
            print(f'An error occured {e}')

    async def get_n_questions(self, n):

        try:
            questions = self.question_dba.get_100_questions()
            if not questions:
                raise HTTPException(
                    status_code=404, detail="No questions found")
            return {'result': questions}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))
