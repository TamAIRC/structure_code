import os
import sys
from bson import ObjectId
from pydantic import ConfigDict, Field, field_validator
from typing import Any, Dict, List, Union, Optional


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from patterns.base_dbo import BaseDBO


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
    multimedia: Optional[ObjectId] = Field(default=None)

    model_config = ConfigDict(
        arbitrary_types_allowed=True,
        validate_assignment=True,
        json_encoders={ObjectId: str},
    )

    # Chuyển đổi thành ObjectId nếu đầu vào là string trước khi validate
    @field_validator("id", "multimedia", mode="before")
    def convert_to_object_id(cls, value):
        if isinstance(value, str):
            return ObjectId(value)
        return value

    # Chuyển đổi thành ObjectId nếu đầu vào là string trước khi validate
    @field_validator("id", "multimedia", mode="before")
    def convert_to_object_id(cls, value):
        if isinstance(value, str):
            return ObjectId(value)
        return value

    def validate(self):
        pass

    def get_id(self):
        return self.id

    def set_id(self, new_id: ObjectId):
        self.id = new_id

    @classmethod
    def from_json_obj(cls, json_obj: Dict[str, Any]):
        """Convert JSON object to data format."""
        if json_obj["_id"]:
            json_obj["_id"] = ObjectId(json_obj["_id"])
        if json_obj["multimedia"]:
            json_obj["multimedia"] = ObjectId(json_obj["multimedia"])
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
        data = self.model_dump(by_alias=True)
        data["_id"] = str(data["_id"]) if data["_id"] else None
        data["multimedia"] = str(data["multimedia"]) if data["multimedia"] else None
        return data

    def to_string(self) -> str:
        """Convert the Question object to a string representation."""
        return str(self.model_dump(by_alias=True))

    def validate_multimedia(id):
        # TODO: Ensure the multimedia ID exists in the database.
        return True
