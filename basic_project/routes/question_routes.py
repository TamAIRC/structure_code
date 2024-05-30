# routes/question_routes.py
from fastapi import APIRouter, Query
from typing import List
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from controllers.question_controller import QuestionController

router = APIRouter()

@router.get("/questions")
async def get_questions(N: int = Query(100, description="Number of questions to retrieve")):
    try:
        question_controller = QuestionController()
        # Fetch questions from the controller
        successed, questions = await question_controller.get_questions(N) 
        if successed:
            result = {
                "status": True,
                "data": questions
            }
            return result
        else:
            error_result = {
                "status": False,
                "error_code": 202, 
                "error_message": "Failed to fetch questions from the database."
            }
            return error_result
    except Exception as err:
        error_result = {
            "status": False,
            "error_code": 404,  # Web server error
            "error_message": str(err)
        }
        return error_result
    
async def update_questions(questions):
    try:
        question_controller = QuestionController()
        successed = await question_controller.update_n_questions(questions)
        if successed:
            result = {
                "status": True
            }
            return result
        else:
            error_result = {
                "status": False,
                "error_code": 202, 
                "error_message": "Failed to fetch questions from the database."
            }
            return error_result
    except Exception as err:
        error_result = {
            "status": False,
            "error_code": 404,  # Web server error
            "error_message": str(err)
        }
        return error_result
