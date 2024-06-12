# controllers/question_controller.py
import os
import sys
from typing import List, Tuple

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

# controllers/question_controller.py
from database.dba.question_dba import QuestionDBA
from database.dbo.question_dbo import QuestionDBO
from utils.util import normalize_id
from controllers.session_manager import session_manager
from typing import List, Tuple

class QuestionController:
    current_questions = []
    def __init__(self):
        self.dba = QuestionDBA()

    async def get_questions(self, n: int) -> Tuple[bool, List[dict]]:
        try:
            result = self.dba.find_many({}, n)
            # session_manager.store_questions(session_id, result)
            QuestionController.current_questions = result
            json_questions = [question.to_json() for question in result]
            successed = True    
            return successed, json_questions
        except Exception as e:
            successed = False
            print("Exception in get_questions:", e)
            return successed, None

    async def insert_questions(self, questions: List[dict]) -> bool:
        try:
            for question in questions:
                question['multimedia'] = normalize_id(question["multimedia"])
            questions = [QuestionDBO(**question) for question in questions]
            self.dba.insert_many(questions)
            successed = True
            return successed
        except Exception as e:
            print("Exception in insert_questions in controllers:", e)
            successed = False
            return successed
    async def update_questions(self, in_questions: List[dict]) -> bool:
        try:
            in_questions = [QuestionDBO.from_json_obj(question) for question in in_questions]
            current_questions = QuestionController.current_questions
            print("current_questions: ",current_questions)
            current_questions_dict = {q.id: q for q in current_questions}
            questions_to_update = []

            for incoming_question in in_questions:
                current_question = current_questions_dict.get(incoming_question.id)
                print("in: ",incoming_question)
                print("cur:",current_question)
                if current_question and incoming_question != current_question:
                    questions_to_update.append(incoming_question)
            if questions_to_update:
                self.dba.update_questions(questions_to_update)
            successed = True    
            return successed
        except Exception as e:
            print("Exception in update_questions:", e)
            successed = False
            return successed
    
    async def delete_questions(self, ids: List[str], session_id: str) -> bool:
        try:
            ids = [normalize_id(id) for id in ids]
            self.dba.transaction(self.dba.delete_questions, ids=ids)
            successed = True    
            return successed
        except Exception as e:
            print("Exception in delete_questions:", e)
            successed = False
            return successed
        