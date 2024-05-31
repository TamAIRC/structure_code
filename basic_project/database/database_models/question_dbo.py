# database/database_models/question_model.py
from pydantic import BaseModel, Field, ConfigDict
from bson import ObjectId

from typing import List, Dict, Any, Union

class QuestionDBO(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
    category: Union[int, str]
    subcategory: str
    content: str
    answers: List[str]
    correct_answer: str
    multimedia: ObjectId

    model_config = ConfigDict(arbitrary_types_allowed=True)

    def get_id(self):
        return self.id

    def set_id(self, new_id: ObjectId):
        self.id = new_id

    @classmethod
    def from_json_obj(cls, json_obj: Dict[str, Any]):
        """Convert JSON object to data format."""
        json_obj['_id'] = ObjectId(json_obj['_id'])
        json_obj['multimedia'] = ObjectId(json_obj['multimedia'])  
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
        # Modify any attributes if needed
        # Example: b.some_attribute = new_value

    def to_json(self) -> Dict[str, Any]:
        """Convert the Question object to a JSON-serializable dictionary."""
        data = self.model_dump(by_alias=True)
        data['_id'] = str(data['_id'])
        data['multimedia'] = str(data['multimedia'])
        return data

    def to_string(self) -> str:
        """Convert the Question object to a string representation."""
        return str(self.model_dump(by_alias=True))