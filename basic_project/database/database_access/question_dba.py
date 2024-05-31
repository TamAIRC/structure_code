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
        question = self.find_one_by_id(id)
        if question is None:
            print('No questions found')
            return []
        # questions_serializable = convert_objectid_to_str(question)
        # return questions_serializable
        return question
    
    def get_n_questions(self, num_ques):
        """_summary_

        Args:
            num_ques (_type_): number of questions wanted to take

        Returns:
            list: list of question ID
        """
        questions = self.find_many(num_ques)
        #TODO save to log
        if questions is None:
            print('No questions found')
            return []
        else:
            questions_serializable = [convert_objectid_to_str(question) for question in questions]
            return questions_serializable
    
    # viết để handle được cả update 1 và many
    def update_one_question(self, question_id, update_data):
        '''
        được update hết tất cả giá trị thay đổi à?
        có cần check quyền không
        check định dạng dữ liệu
        '''
        try:
            # check định dạng dữ liệu
            update_user_data = QuestionSchema(**update_data)
            result = self.update_one_by_id(question_id, 
                                           update_user_data.model_dump_json())
            print(f'successfully update question with id {question_id}')
            return result.modified_count
        except ValidationError as e:
            print(f"Validation error: {e}")
            return None
    
    def update_many_question(self, condition, update_value):
        try:
            # cái này đang không đúng vì update value là một tập dict
            update_value = QuestionSchema(**update_value)
            results = self.update_many(condition=condition,
                                       update_fields=update_value)
        except ValidationError as e:
            print(f"Validation error: {e}")
            return None