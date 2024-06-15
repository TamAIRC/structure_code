import os
import sys
from bson import ObjectId
from pydantic import BaseModel, Field
from typing import Any, Dict, List
from datetime import datetime as Date

# Assuming current_dir, project_root, and sys.path setup are correct
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from patterns.base_dbo import BaseDBO
from utils import util

class Interaction(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    outcome: int
    timestamp: Date
    timeForAnswer: int

    class Config:
        arbitrary_types_allowed = True

class ResultDBO(BaseDBO):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    questions: List[Interaction]
    
    class Config:
        arbitrary_types_allowed = True

    def validate(self):
        pass

    @classmethod
    def from_json_obj(cls, json_obj: Dict[str, Any]):
        """Convert JSON object to data format."""
        player_id = json_obj['player_id']
        questions = json_obj['questions']
        question = [Interaction(**question) for question in questions]
        return ResultDBO(id=player_id, questions=questions)

    @classmethod
    def from_array(cls, array: List[Any]):
        """Convert array to data format."""
        player_id = ObjectId(array[0])
        questions = [
            Interaction(
                id=ObjectId(question[0]),
                outcome=question[1],
                timestamp=Date.fromisoformat(question[2]),
                timeForAnswer=question[3]
            ) for question in array[1]
        ]
        return cls(id=player_id, questions=questions)

    def copy_a_to_b(self, a: "ResultDBO", b: "ResultDBO"):
        """Copy attributes from a to b, with some modifications."""
        for attr, value in a.dict().items():
            if hasattr(b, attr):
                setattr(b, attr, value)

    def to_json(self) -> Dict[str, Any]:
        data = self.dict(by_alias=True)
        data["_id"] = util.toString(data["_id"])
        return data

    def to_string(self) -> str:
        """Convert the ResultDBO object to a string representation."""
        return str(self.dict(by_alias=True))

