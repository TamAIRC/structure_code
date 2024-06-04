# routes/question_routes.py
from fastapi import APIRouter, Depends, HTTPException, Request
from fastapi.middleware.cors import CORSMiddleware
from starlette.middleware.sessions import SessionMiddleware
from pydantic import BaseModel
import json, os, sys
from typing import List
from bson import ObjectId

from controllers.question_controller import QuestionController
from utils.util import compare_documents
router = APIRouter()
router.add_middleware(SessionMiddleware, secret_key='your_secret_key')

# Allow CORS (optional)
router.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


question_controller = QuestionController()


@router.get("/get_question_by_id/{objectid}")
async def get_questions_by_id(objectid):
    result = question_controller.get_one_question_by_id(objectid)
    print(f'this is the new type',type(result))
    return result


'''
nó sẽ cần có 1 userid để lưu session, vì không còn tìm theo id nữa rồi
chỉ cần userid ở đây thôi vì lưu session ở dây và controller không phải pass userid vào
'''
@router.get("/get_questions/{user_id}")
async def get_questions(user_id):
    questions = question_controller.get_n_questions(user_id)
    
    # lưu questions vào session để về sau so sánh
    question_controller.set_session_data(f"questions_{user_id}", questions)
    # print(f'this is the new type',type(result))
    
    return  questions

@router.get("/update_questions/{user_id}")
async def update_question(user_id: str, request: Request, updated_questions: List[dict]):
    # lấy data từ session
    original_questions = question_controller.get_session_data(f'questions for user {user_id}')
    if not original_questions:
        raise HTTPException(status_code=404, detail="Orginal questions not found in session")
    
    '''
    so sánh kết quả bằng cách gọi function từ bên controller
    pass 2 giá trị vào so sánh
    '''    



    
'''
cần lưu kết quả của get question vào session


### cần cải thiện ###
làm sao để cái session đó làm mới với mỗi 10 câu mới
'''