# routes/question_routes.py
from fastapi import APIRouter
from typing import List
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from controllers.question_controller import QuestionController

router = APIRouter()
question_controller = QuestionController()

@router.get("/questions")
async def get_questions():
    return await question_controller.get_questions()
