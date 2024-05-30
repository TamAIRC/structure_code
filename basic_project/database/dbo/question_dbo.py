# database/database_models/question_model.py
from pydantic import BaseModel, Field
from bson import ObjectId
from typing import List, Dict, Any


class QuestionDBO(BaseModel):
    id: ObjectId = Field(default_factory=ObjectId, alias="_id")
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

    def get_id(self):
        """Return the ID of the question."""
        return self.id

    def set_id(self, new_id: ObjectId):
        """Set a new ID for the question."""
        self.id = new_id

    def form_json_obj(self, json_obj: Dict[str, Any]):
        """Convert JSON object to data format."""
        return QuestionDBO(**json_obj)

    def form_array(self, array: List[Any]):
        """Convert array to data format."""
        return QuestionDBO(
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
        return self.model_dump(by_alias=True)

    def to_string(self) -> str:
        """Convert the Question object to a string representation."""
        return str(self.model_dump(by_alias=True))
