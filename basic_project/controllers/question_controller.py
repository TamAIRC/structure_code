# controllers/get_question_controller.py
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from database.dba.question_dba import QuestionDBA
from database.dbo.question_dbo import QuestionDBO
from utils.util import normalize_id

from fastapi import HTTPException
from typing import List
class QuestionController:
    def __init__(self):
        self.dba = QuestionDBA()
        self.questions = []
    
    def get_questions(self):
        return self.questions
    
    async def get_questions(self, n):
        try:
            questions = self.dba.transaction(self.dba.get_questions, n=n)
            self.questions = questions
            json_questions = [QuestionDBO.to_json(question) for question in questions]
            successed = True    
            return successed, json_questions
        except Exception as e:
            successed = False
            return successed, None
        
    async def update_questions(self, questions: List[dict]):
        incoming_questions = [QuestionDBO.from_json_obj(question) for question in questions]
        try:
            current_questions = {str(q["_id"]): q for q in self.questions}
            questions_to_update = []

            for incoming_question in incoming_questions:
                current_question = current_questions.get(str(incoming_question.get_id()))
                if current_question and incoming_question != current_question:
                    questions_to_update.append(incoming_question)

            if questions_to_update:
                status = self.dba.transaction(self.dba.update_questions, questions_to_update)
            successed = True    
            return successed
        except Exception as e:
            print(e)
            successed = False
            return successed
    
    async def delete_questions(self, ids: List[str]): 
        try:
            # Convert ids to ObjectId 
            ids = [normalize_id(id) for id in ids]
            status = self.dba.transaction(self.dba.delete_questions, ids=ids)
            successed = True    
            return successed
        except Exception as e:
            successed = False
            return successed
        
   