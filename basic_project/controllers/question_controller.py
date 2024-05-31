import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from database.dba.question_access import QuestionDBA

class QuestionController():
    def __init__(self):
        self.question_service = QuestionDBA()

    def get_n_question(self, n):
        questions = self.question_service.transaction(self.question_service.get_questions, N=5)
        json_questions = [question.dict() for question in questions]
        return questions