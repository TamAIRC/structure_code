# database/database_models/question_model.py
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)
from pydantic import BaseModel, ConfigDict, Field, ValidationError, field_validator
from bson import ObjectId
from typing import List, Dict, Any, Union
from utils import util


class QuestionDBO(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    category: Union[int, str]
    subcategory: str
    content: str
    answers: List[str]
    correct_answer: str
    difficulty: int
    required_rank: int
    language: int
    multimedia: ObjectId

    model_config = ConfigDict(arbitrary_types_allowed=True)

    @classmethod
    def from_json_obj(self, json_obj: Dict[str, Any]):
        """Convert JSON object to data format."""
        if isinstance(json_obj.get("_id"), str):
            json_obj["_id"] = ObjectId(json_obj["_id"])
        if isinstance(json_obj.get("multimedia"), str):
            json_obj["multimedia"] = ObjectId(json_obj["multimedia"])
        return self(**json_obj)

    @classmethod
    def form_array(self, array: List[Any]):
        """Convert array to data format."""
        result = QuestionDBO(
            id=array[0],
            category=array[1],
            subcategory=array[2],
            content=array[3],
            answers=array[4],
            correct_answer=array[5],
            multimedia=array[6],
        )
        return result

    def copy_a_to_b(self, a: "QuestionDBO", b: "QuestionDBO"):
        """Copy attributes from a to b, with some modifications."""
        for attr, value in a.model_dump().items():
            if hasattr(b, attr):
                setattr(b, attr, value)
        # Modify any attributes if needed
        # Example: b.some_attribute = new_value

    def to_json(self) -> Dict[str, Any]:
        """Convert the Question object to a JSON-serializable dictionary."""
        data = self.model_dump(by_alias=True)
        data["_id"] = util.toString(data["_id"])
        data["multimedia"] = util.toString(data["multimedia"])
        return data

    def to_string(self) -> str:
        """Convert the Question object to a string representation."""
        return str(self.model_dump(by_alias=True))

    # Tham khảo, trong tương lai có thể sử dụng validate điều kiên đặc biệt
    # @field_validator("difficulty", "required_rank", "language")
    # def validate_integers(cls, value, field):
    #     if not isinstance(value, int):
    #         raise ValueError(f"{field.name} must be an integer")
    #     return value

    # @field_validator("category")
    # def validate_category(cls, value):
    #     if not isinstance(value, (int, str)):
    #         raise ValueError("category must be an integer or string")
    #     return value

    # @field_validator("answers")
    # def validate_answers(cls, value):
    #     if not isinstance(value, list) or not all(isinstance(i, str) for i in value):
    #         raise ValueError("answers must be a list of strings")
    #     return value

    def get_id(self):
        """Return the ID of the question."""
        return self.id

    def set_id(self, new_id: ObjectId):
        """Set a new ID for the question."""
        self.id = new_id

    def get_category(self):
        """Return the Category of the question."""
        return self.category

    def set_category(self, new_category: int):
        """Set a new Category for the question."""
        self.category = new_category

    def get_subcategory(self):
        """Return the Subcategory of the question."""
        return self.subcategory

    def set_category(self, new_subcategory: int):
        """Set a new Subcategory for the question."""
        self.subcategory = new_subcategory

    def get_content(self):
        """Return the content of the question."""
        return self.content

    def set_content(self, new_content: str):
        """Set a new content for the question."""
        self.content = new_content

    def get_answers(self):
        """Return the answers of the question."""
        return self.answers

    def set_answers(self, new_answers: List[str]):
        """Set a new answers for the question."""
        self.answers = new_answers

    def get_correct_answer(self):
        """Return the correct_answer of the question."""
        return self.correct_answer

    def set_correct_answer(self, new_correct_answer: str):
        """Set a new correct_answer for the question."""
        self.correct_answer = new_correct_answer

    def get_multimedia(self):
        """Return the multimedia of the question."""
        return self.multimedia

    def set_multimedia(self, new_multimedia: ObjectId):
        """Set a new multimedia for the question."""
        self.multimedia = new_multimedia


if __name__ == "__main__":
    json_data = {
        "_id": "60d5ec49c2a9b8c486d8a5a8",
        "category": "Math",
        "subcategory": "Math",
        "content": "What is 2 + 2?",
        "answers": ["3", "4", "5", "6"],
        "correct_answer": "4",
        "difficulty": "1",
        "required_rank": "5",
        "language": 2,
        "multimedia": "60d5ec49c2a9b8c486d8a5b0",
    }

    try:
        question = QuestionDBO.from_json_obj(json_data)
        print(question)
    except ValidationError as e:
        print(f"Validation error: {e}")
