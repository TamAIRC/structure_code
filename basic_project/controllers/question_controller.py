# controllers/question_controller.py
from fastapi import HTTPException
from fastapi import APIRouter, Depends, HTTPException, Request
from bson import ObjectId
from typing import List
from utils.util import normalize_id, serialize_mongo_document
from database.database_access.question_dba import QuestionDBA


class QuestionController:
    def __init__(self, request: Request):
        self.request = request
        self.question_dba = QuestionDBA()

    def get_one_question_by_id(self, question_id):
        try:
            if not isinstance(question_id, ObjectId):
                question_id = ObjectId(question_id)
                result = self.question_dba.get_one_question(question_id)
                # result = serialize_mongo_document(result)
                return result
            else:
                result = self.question_dba.get_one_question(question_id)
                return result
        except Exception as e:
            print(f'An error occured {e} in question controller')

    def get_n_questions(self, n):
        try:
            questions = self.question_dba.get_n_questions(n)
            if not questions:
                raise HTTPException(
                    status_code=404, detail="No questions found")
            return {'result': questions}
        except Exception as e:
            raise HTTPException(status_code=500, detail=str(e))

    def update_changed_questions(self, userid, updated_questions):
        
        pass

    def set_session_data(self, key, value):
        self.request.session[key] = value

    def get_session_data(self, key):
        return self.request.session.get(key)

    def delete_session_data(self, key):
        if key in self.request.session:
            del self.request.session[key]
