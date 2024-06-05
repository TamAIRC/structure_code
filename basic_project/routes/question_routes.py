# routes/question_routes.py
from fastapi import APIRouter, Query, HTTPException
from typing import List
import os
import sys
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from controllers.get_question_controller import GetQuestionController
from controllers.update_question_controller import UpdateQuestionController
from utils.util import validate_input, validate_positive_number
router = APIRouter()
@router.get("/questions")
async def get_questions(N: int = Query(description="Number of questions to retrieve")):
    try:
        print("N",N)
        if validate_positive_number(N) == False:
            error_input = {
                "status": False,
                "message": "Input must be a positive number"
            }
            return error_input
        question_controller = GetQuestionController()
        successed, questions = await question_controller.get_n_questions(N) 
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
            "error_code": 404,  
            "error_message": str(err)
        }
        return error_result
    
@router.put("/questions")
async def update_questions(data: dict):
    try:
        questions = validate_input(data)
        question_controller = UpdateQuestionController()
        successed = await question_controller.update_n_questions(questions)
        if successed:
            result = {"status": True}
            return result
        else:
            error_result = {
                "status": False,
                "error_code": 202, 
                "error_message": "Failed to fetch questions from the database."
            }
            return error_result
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))