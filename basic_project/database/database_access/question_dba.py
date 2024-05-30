# database/database_access/question_dba.py
'''
cái này là dành cho Reviewer
chỉ họ có quyền thay đổi thông tin câu hỏi
'''

from database.database_access.mongodb_dba import MongoDB_DBA
from database.database_models.question_model import QuestionSchema
from bson.objectid import ObjectId
from pydantic import ValidationError
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from configs import db_config
from utils.json_encoder import convert_objectid_to_str
from utils.util import normalize_id


class QuestionDBA(MongoDB_DBA):
    def __init__(self):
        super().__init__(db_config.CONNECT['QUESTION_COLLECTION'])
    
    def get_one_question(self, id):
        question = self.find_one(id)
        if question is None:
            print('No questions found')
            return []
        pass
    
    def get_questions(self, object_ids):
        object_ids = [normalize_id(id) for id in object_ids]
        questions = self.find_many(object_ids)
        #TODO save to log
        if questions is None:
            print('No questions found')
            return []
        else:
            questions_serializable = [convert_objectid_to_str(question) for question in questions]
            return questions_serializable
    
    # viết để handle được cả update 1 và many
    def update_question_by_id(self, question_ids, update_data):
        '''
        được update hết tất cả giá trị thay đổi à?
        có cần check quyền không
        check định dạng dữ liệu
        '''
        try:
            # check định dạng dữ liệu
            update_user_data = QuestionSchema(**update_data)
            result = self.collection.find_one_and_update(
                {"_id": ObjectId(question_ids)},
                {"$set": update_user_data.model_dump_json()}
            )
            print(f'successfully update question with id {question_ids}')
            return result.modified_count
        except ValidationError as e:
            print(f"Validation error: {e}")
            return 0
        
    
        
    # def get_100_questions(self, objectList):
    #     questions = self.find_many(objectList, {})
        
    #     if questions is None:
    #         return []
        
    #     questions_serializable = [convert_objectid_to_str(question) for question in questions]
    #     return questions_serializable
    
    def update_question(self, question_data):
        '''
        phải có check định dạng của dữ liệu muốn update
        -> cần có DBO <=> questionSchema
        '''
        try:
            question = QuestionSchema(**question_data)
            result  = self.update_one_by_id(question.model_dump_json())
            return str(result.inserted_id) # vì muốn in nên vì thế ép kiểu str à???
        except ValidationError as e:
            print(f"Validation error:", e)
            return None