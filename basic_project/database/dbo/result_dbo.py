import os
import sys
from bson import ObjectId
from pydantic import ConfigDict, Field
from typing import Any, Dict, List, Union


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from patterns.base_dbo import BaseDBO
from utils import util

class ResultDBO(BaseDBO):
    player_id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    questions: List[Any]

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def validate(self):
        pass

    @classmethod
    def from_json_obj(cls, json_obj: Dict[str, Any]):
        """Convert JSON object to data format."""
        json_obj["_id"] = ObjectId(json_obj["_id"])
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
        data["_id"] = util.toString(data["_id"])
        data["multimedia"] = util.toString(data["multimedia"])
        return data

    def to_string(self) -> str:
        """Convert the Question object to a string representation."""
        return str(self.model_dump(by_alias=True))


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
