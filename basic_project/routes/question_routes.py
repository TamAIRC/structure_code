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


@router.get("/questions")
async def get_questions():
    # lay N quan sat tu bang cau hoi
    # tham so hoa (N quan sat)
    
    # xu ly authorization
    # lay tham so len?
    # xu ly validate tham so 
    N = 100 # xu ly tu request
    try:
        question_controller = QuestionController()
        # tach qua trinh xuy ly ket qua controller ra khoi ket quar tra ve cua API
        await successed, questions question_controller.get_questions(N) # tham so
        if successed:
            result = {
                "status": True,
                "data": questions
            }
            return result
        else:
            error_result = {
                "status": False,
                "error_code": 202 #loi database server
                "error_message":err
            }
            return error_result
    except Exception as err:
        # ghi log khi co loi
        error_result = {
            "status": False,
            "error_code": 404 #loi web_server
            "error_message":err
        }
        return error_result
