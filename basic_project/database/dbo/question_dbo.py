import os
import sys
from bson import ObjectId
from pydantic import ConfigDict, Field, field_validator, field_serializer
from typing import Any, Dict, List, Union, Optional


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from patterns.base_dbo import BaseDBO
from utils import util


class QuestionDBO(BaseDBO):
    id: Optional[ObjectId] = Field(default=None, alias="_id")
    category: Union[int, str]
    subcategory: str
    content: str
    answers: List[str]
    correct_answer: str
    difficulty: int
    required_rank: int
    language: int
    multimedia: ObjectId
    
    class Config:
        arbitrary_types_allowed = True
        validate_assignment = True # Cho phép xác thực khi gán giá trị
        json_encoders = {
            ObjectId: str  # Ensures ObjectId fields are serialized as strings
        }
        # json_encoders = {ObjectId: str}
        # populate_by_name = True
    
    # Chuyển đổi thành ObjectId nếu đầu vào là string trước khi validate
    @field_validator("id", "multimedia", mode="before")
    def convert_to_object_id(cls, value):
        if isinstance(value, str):
            return ObjectId(value)
        return value
    
    # @field_serializer('id', 'multimedia')
    # def serialize_id(self, id: ObjectId, _info):
    #     return str(id)

    def validate(self):
        pass

    @classmethod
    def from_json_obj(cls, json_obj: Dict[str, Any]):
        """Convert JSON object to data format."""
        # json_obj["_id"] = ObjectId(json_obj["_id"])
        # json_obj["multimedia"] = ObjectId(json_obj["multimedia"])
        return cls(**json_obj)

    @classmethod
    def from_array(cls, array: List[Any]):
        """Convert array to data format."""
        return cls(
            id=array[0],
            category=array[1],
            subcategory=array[2],
            content=array[3],
            answers=array[4],
            correct_answer=array[5],
            multimedia=array[6],
        )

    def copy_a_to_b(self, a: "QuestionDBO", b: "QuestionDBO"):
        """Copy attributes from a to b, with some modifications."""
        for attr, value in a.model_dump().items():
            if hasattr(b, attr):
                setattr(b, attr, value)

    def to_json(self) -> Dict[str, Any]:
        """Convert the Question object to a JSON object."""
        return self.model_dump_json(by_alias=True)

    # Hàm này bỏ đi nó có sẵn r mà :vvvvv
    # def to_string(self) -> str:
    #     """Convert the Question object to a string representation."""
    #     return str(self.model_dump(by_alias=True))


if __name__ == "__main__":
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
