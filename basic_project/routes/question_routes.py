# routes/question_routes.py
from fastapi import APIRouter, Query, HTTPException
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
        question_controller = QuestionController()
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
            "error_code": 404,  
            "error_message": str(err)
        }
        return error_result
    
@router.put("/questions")
async def update_questions(data: List[dict]):
    try: 
        # Validate input
        # questions = [validate_input(datum) for datum in data]
        question_controller = QuestionController()
        successed = await question_controller.update_questions(data)
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
    
async def delete_questions(data: List[str]):
    try:
        # Validate input
        question_controller = QuestionController()
        successed = await question_controller.delete_questions(data)
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
    
def main():
    # Test get_questions
    print(asyncio.run(get_questions(10)))

    # Test update_question
    # new_question_data = [
    # {
    #     "_id": "66260e94a51b34b732f211e0",
    #     "category": "History",
    #     "subcategory": "VN History",
    #     "content": "What is the capital of Vietnam?",
    #     "answers": ["Hanoi", "Ho Chi Minh City", "Da Nang", "Hue"],
    #     "correct_answer": "Hanoi",
    #     "difficulty": 1,
    #     "required_rank": 1,
    #     "language": 1,
    #     "multimedia": "66260e88a51b34b732f2118e"
    # }, 
    # {
    #     "_id": "66260e94a51b34b732f211e3",
    #     "category": "History",
    #     "subcategory": "World History",
    #     "content": "What is the capital of Cambodia?",
    #     "answers": ["Phnom Penh", "Siem Reap", "Sihanoukville", "Battambang"],
    #     "correct_answer": "Phnom Penh",
    #     "difficulty": 1,
    #     "required_rank": 1,
    #     "language": 1,
    #     "multimedia": "66260e7fa51b34b732f21156"
    # }
    # ]
    # print(asyncio.run(update_questions(new_question_data)))
    # print(asyncio.run(get_questions(10)))
    
    # Test delete_questions
    # delete_data = ["66260e94a51b34b732f211e0"]
    # print(asyncio.run(delete_questions(delete_data)))
    # print(asyncio.run(get_questions(10)))

if __name__ == "__main__":
    main()