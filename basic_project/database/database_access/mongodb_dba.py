from bson import ObjectId
from pymongo.errors import BulkWriteError
from .dba import DBA
from utils.util import normalize_id, validate_condition, prepare_bulk_updates
from database.database_models.question_model import QuestionDBO

class MongoDB_DBA(DBA):
    def __init__(self, connection, collection_names):
        super().__init__(connection, collection_names)
        self.collections = [self.connection.database[name] for name in collection_names]
        if len(collection_names) == 1:
            self.collection = self.collections[0]
        else:
            self.collection = self.collections

    def find_by_id(self, id):
        try:
            normalized_id = normalize_id(id)
            return QuestionDBO.from_json_obj(self.collection.find_one({"_id": normalized_id}))
        except ValueError as e:
            print(e)
            return None

    def find_one(self, condition):
        try:
            validated_condition = validate_condition(condition)
            return self.collection.find_one(validated_condition)
        except ValueError as e:
            print(e)
            return None

    def find_many(self, n, condition):
        try:
            validated_condition = validate_condition(condition)
            return list(self.collection.find(validated_condition).limit(n))
        except ValueError as e:
            print(e)
            return None

    def update_one_by_id(self, document):
        try:
            normalized_id = normalize_id(document['_id'])
            new_values_dict = {key: value for key, value in document.items() if key != '_id'}
            return self.collection.update_one({"_id": normalized_id}, {"$set": new_values_dict})
        except ValueError as e:
            print(e)
            return None

    def update_many_by_id(self, ids, new_values):
        try:
            bulk_updates = prepare_bulk_updates(ids, new_values)
            return self.collection.bulk_write(bulk_updates)
        except (ValueError, BulkWriteError) as e:
            print(e)
            return None

    