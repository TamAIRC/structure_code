# routes/question_routes.py
from fastapi import APIRouter
from typing import List
from bson import ObjectId
import os
import sys

from controllers.question_controller import QuestionController

router = APIRouter()
question_controller = QuestionController()


@router.get("/questions/{objectid}")
async def get_questions(objectid):
    result = question_controller.get_one_question_by_id(objectid)
    print(f'this is the new type',type(result))
    return result
