# routes/question_routes.py
from fastapi import APIRouter, Query, HTTPException, Depends
from typing import List
import os
import sys
import asyncio

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from controllers.question_controller import QuestionController
from utils.util import validate_input, validate_positive_number

router = APIRouter()

async def get_session_id():
    # Generate a unique session ID for each request or retrieve from user context
    # For simplicity, using a static ID. In production, use a user-specific or request-specific ID.
    return "default_session"

@router.get("/questions")
async def get_questions(N: int = Query(description="Number of questions to retrieve"), session_id: str = Depends(get_session_id)):
    try:
        if not validate_positive_number(N):
            return {"status": False, "message": "Input must be a positive number"}
        
        question_controller = QuestionController()
        successed, questions = await question_controller.get_questions(N, session_id)
        if successed:
            return {"status": True, "data": questions}
        else:
            return {"status": False, "error_code": 202, "error_message": "Failed to fetch questions from the database."}
    except Exception as err:
        return {"status": False, "error_code": 404, "error_message": str(err)}
    
@router.put("/questions")
async def update_questions(data: List[dict], session_id: str = Depends(get_session_id)):
    try:
        question_controller = QuestionController()
        successed = await question_controller.update_questions(data, session_id)
        if successed:
            return {"status": True}
        else:
            return {"status": False, "error_code": 202, "error_message": "Failed to update questions."}
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))

@router.delete("/questions")
async def delete_questions(data: List[str], session_id: str = Depends(get_session_id)):
    try:
        question_controller = QuestionController()
        successed = await question_controller.delete_questions(data, session_id)
        if successed:
            return {"status": True}
        else:
            return {"status": False, "error_code": 202, "error_message": "Failed to delete questions."}
    except Exception as err:
        raise HTTPException(status_code=404, detail=str(err))