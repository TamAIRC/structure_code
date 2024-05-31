# controllers/question_controller.py
from fastapi import HTTPException
from typing import List
from database.database_access.question_dba import QuestionDBA
from database.database_models.question_model import QuestionDBO
from controllers.get_questions_controller import GetQuestionController
from database.database_connection.connection import Connection
from configs import db_config
class UpdateQuestionController:
    def __init__(self):
        connection_params = {
            'uri_template': db_config.CONNECT['URL'],
            'database_name': db_config.CONNECT['DATABASE']
        }
        connection = Connection.create_connection(db_config.DB_TYPE, **connection_params)
        connection.connect(db_config.USERNAME, db_config.PASSWORD)
        self.question_dba = QuestionDBA(connection)
        question_controller = GetQuestionController()
        self.question = question_controller.get_questions()

    async def update_n_questions(self, questions: List[dict]):
        print(questions)
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
                self.question_dba.update_n_questions([q.to_json() for q in questions_to_update])
            
            successed = True    
            return successed
        except Exception as e:
            print(e)
            successed = False
            return successed, None