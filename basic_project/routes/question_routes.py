# routes/question_routes.py
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)
from controllers.question_controller import QuestionController
from database.database_models.question_dbo import QuestionDBO
from database.database_access.question_dba import QuestionDBA

import asyncio
from fastapi import APIRouter

router = APIRouter()

@router.get("/questions")
async def get_questions(N):
    # Handle authorization 
    # Validate input
    try:
        question_controller = QuestionController()
        succeeded, questions = await question_controller.get_questions(N)
        # tach qua trinh xuy ly ket qua controller ra khoi ket quar tra ve cua API
        if succeeded:
            result = {
                "status": True,
                "data": questions
            }
            print(result)
            return result
        else:
            error_result = {
                "status": False,
                "error_code": 202, #loi database server
                "error_message": "Error when getting questions"
            }
            return error_result
    except Exception as err:
        error_result = {
            "status": False,
            "error_code": 404, #loi web_server
            "error_message": err
        }
        return error_result

async def update_question(json_data):
    # Handle authorization
    # Validate input
    try: 
        question_controller = QuestionController()
        question_dbo = QuestionDBO.from_json_obj(json_data) 
        print("Question DBO", question_dbo)
        succeeded, updated_question = await question_controller.update_one_by_id(question_dbo)
        if succeeded:
            result = {
                "status": True,
                "data": updated_question
            }
            print("updated_question", result)
            return result
        else:
            error_result = {
                "status": False,
                "error_code": 202, #loi database server
                "error_message": "Error when getting questions"
            }
            return error_result
    except Exception as err:
        error_result = {
            "status": False,
            "error_code": 404, #loi web_server
            "error_message": err
        }
        return error_result

def main():
    # Test get_questions
    asyncio.run(get_questions(100)) 

    # Test update_question
    new_question_data = {
        "_id": "66260e94a51b34b732f21233",
        "category": "History",
        "subcategory": "VN History",
        "content": "What is the capital of Vietnam?",
        "answers": ["Hanoi", "Ho Chi Minh City", "Da Nang", "Hue"],
        "correct_answer": "Hanoi",
        "multimedia": "66260e86a51b34b732f21182"
    }
    asyncio.run(update_question(new_question_data))

if __name__ == "__main__":
    main()