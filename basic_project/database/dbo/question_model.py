import os
import sys
from bson import ObjectId
from pydantic import Field
from typing import List

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from database.dbo.dbo import DBO
from database.dbo.fields import PyObjectId


class QuestionDBO(DBO):
    id: PyObjectId = Field(alias="_id")
    category: str
    subcategory: str
    content: str
    answers: List[str]
    correct_answer: str
    difficulty: int
    required_rank: int
    language: int
    multimedia: PyObjectId
        
    def do_something(self):
        print("I am a QuestionDBO instance")

if __name__ == '__main__':
    # Example data
    example_data = {
        "_id": ObjectId("66260e86a51b34b732f21182"),
        "category": "Geography",
        "subcategory": "Medieval History",
        "content": "Phone rule we pattern be clear.",
        "answers": ["answer1", "answer2", "answer3", "answer4"],
        "correct_answer": "nature",
        "difficulty": 5,
        "required_rank": 5,
        "language": 2,
        "multimedia": ObjectId("66260e86a51b34b732f21182"),
    }

    # Create an instance of the Document model
    document_instance = QuestionDBO(**example_data)
    print(document_instance)
