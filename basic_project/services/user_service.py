# services/user_service.py
from pymongo import MongoClient
from bson import ObjectId
from typing import List, Dict
from database.database_access.question_dba import QuestionDBA

class UserService:
    def __init__(self):
        self.question_dba = QuestionDBA()
        
    def get_one_question_by_id(self, question_id):
        try:
            result = self.question_dba.get_one_question(question_id)
            if result is None:
                print(f'No question found with id {question_id}')
        except Exception as e:
            raise e
            
    def get_n_questions(self, n: int) -> List[dict]:
        try:
            return self.question_dba.get_n_questions(n)
        except Exception as e:
            raise e
        
    # update_questions phải được đưa về chung 1 dạng
    def update_questions(self, update_questions: List[dict]) -> int:
        try:
            update_count = 0
            for question in update_questions:
                
        except Exception as e:
            raise e