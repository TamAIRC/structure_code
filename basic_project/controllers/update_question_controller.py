# controllers/question_controller.py
from fastapi import HTTPException
from typing import List
from database.dba.question_dba import QuestionDBA
from database.dbo.question_dbo import QuestionDBO
from basic_project.controllers.question_controller import GetQuestionController
from configs import db_config
class UpdateQuestionController:
    def __init__(self):
        self.dba = QuestionDBA()
        question_controller = GetQuestionController()
        self.question = question_controller.get_questions()

    async def update_n_questions(self, questions: List[dict]):
        incoming_questions = [QuestionDBO.from_json_obj(question) for question in questions]
        print(incoming_questions)
        try:
            current_questions = {str(q.id): q for q in self.questions}
            questions_to_update = []

            for incoming_question in incoming_questions:
                current_question = current_questions.get(str(incoming_question.id))
                if current_question and incoming_question != current_question:
                    questions_to_update.append(incoming_question)

            if questions_to_update:
                self.dba.update_questions([q.to_json() for q in questions_to_update])
            
            successed = True    
            return successed
        except Exception as e:
            print(e)
            successed = False
            return successed, None