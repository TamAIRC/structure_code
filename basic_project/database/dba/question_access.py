import os
import sys
from bson import ObjectId
from typing import Any, Dict, List
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure, PyMongoError

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from database.database_connection.mongo_connection import MongoConnection
from database.dba.dba import DBA
from database.dbo.question_model import QuestionDBO as Question
from configs.db_config import db_config
from utils.util import (
    normalize_id,
    prepare_bulk_updates,
    validate_condition,
)


class QuestionDBA(DBA):
    def __init__(self):
        super().__init__(MongoConnection().database[db_config.QUESTION_COLLECTION])
    
    def transaction(self, query_func, **kwargs):
        """Perform a transaction. Implementation depends on specific use case."""
        if MongoConnection() is None:
            MongoConnection.logger.log_error("No MongoDB client available for transaction")
            return None

        with MongoConnection().client.start_session() as session:
            try:
                session.start_transaction()
                result = query_func(session=session, **kwargs)
                session.commit_transaction()
                MongoConnection.logger.log_info("Transaction committed successfully")
            except (
                ConnectionFailure,
                ServerSelectionTimeoutError,
                PyMongoError,
            ) as err:
                MongoConnection.logger.log_error("Transaction failed", err)
                session.abort_transaction()
                MongoConnection.logger.log_info("Transaction aborted")
                return None
        return result

    def find_by_id(self, id: ObjectId, session=None) -> Question:
        try:
            normalized_id = normalize_id(id)
            result = self.connection.find_one({"_id": normalized_id}, session=session)
            if result:
                return Question(**result)
            return None
        except ValueError as e:
            print(e)
            return None

    def find_one(self, condition: Dict[str, Any], session=None) -> Question:
        try:
            validated_condition = validate_condition(condition)
            result = self.connection.find_one(validated_condition, session=session)
            if result:
                return Question(**result)
            return None
        except ValueError as e:
            print(e)
            return None

    def find_many(
        self, n: int, condition: Dict[str, Any], session=None
    ) -> List[Question]:
        try:
            validated_condition = validate_condition(condition)
            cursor = self.connection.find(validated_condition, session=session).limit(n)
            return [Question(**data) for data in cursor]
        except ValueError as e:
            print(e)
            return None

    def update_one_by_id(
        self, id: ObjectId, new_value: Dict[str, Any], session=None
    ) -> bool:
        try:
            normalized_id = normalize_id(id)
            result = self.connection.update_one(
                {"_id": normalized_id}, {"$set": new_value}, session=session
            )
            return result.modified_count > 0
        except ValueError as e:
            print(e)
            return False

    def update_many_by_id(
        self, ids: List[ObjectId], new_values: List[Dict[str, Any]], session=None
    ) -> bool:
        try:
            bulk_updates = prepare_bulk_updates(ids, new_values)
            result = self.connection.bulk_write(bulk_updates, session=session)
            return result.modified_count > 0
        except ValueError as e:
            print(e)
            return False

    def insert(self, obj: Question, session=None) -> ObjectId:
        try:
            data = obj.to_json()
            result = self.connection.insert_one(data, session=session)
            return result.inserted_id
        except ValueError as e:
            print(e)
            return None

    def delete_by_id(self, id: ObjectId, session=None) -> bool:
        try:
            normalized_id = normalize_id(id)
            result = self.connection.delete_one({"_id": normalized_id}, session=session)
            return result.deleted_count > 0
        except ValueError as e:
            print(e)
            return False

    def get_questions(self, N, session=None):
        questions = self.find_many(N, {}, session=session)
        if questions is None:
            return []
        return questions
    
if __name__ == "__main__":
    question_dba = QuestionDBA()
    data = question_dba.transaction(question_dba.get_questions, N=5)
    print(data)