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
    def __init__(self):
        self.dba = QuestionDBA()

    async def get_questions(self, n: int, session_id: str) -> Tuple[bool, List[dict]]:
        try:
            result = self.dba.transaction(self.dba.get_questions, n=n)
            session_manager.store_questions(session_id, result)
            json_questions = [QuestionDBO.to_json(question) for question in result]
            successed = True    
            return successed, json_questions
        except Exception as e:
            successed = False
            print("Exception in get_questions:", e)
            return successed, None

    async def update_questions(self, in_questions: List[dict], session_id: str) -> bool:
        try:
            in_questions = [QuestionDBO.from_json_obj(question) for question in in_questions]
            current_questions = session_manager.get_questions(session_id)
            current_questions_dict = {q.id: q for q in current_questions}
            questions_to_update = []

            for incoming_question in in_questions:
                current_question = current_questions_dict.get(incoming_question.id)
                print("in: ",incoming_question)
                print("cur:",current_question)
                if current_question and incoming_question != current_question:
                    questions_to_update.append(incoming_question)
            if questions_to_update:
                self.dba.transaction(self.dba.update_questions, questions = questions_to_update)
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
