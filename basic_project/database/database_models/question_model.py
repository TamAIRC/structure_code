# database/database_models/question_model.py
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import List

class QuestionSchema(BaseModel):
    id: ObjectId
    category: int
    subcategory: str
    content: str
    answers: List[str]
    correct_answer: str
    multimedia: ObjectId

    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        populate_by_name = True
