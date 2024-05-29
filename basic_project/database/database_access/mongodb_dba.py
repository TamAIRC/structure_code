from bson import ObjectId
from pymongo.errors import BulkWriteError
from .dba import DBA
from utils.util import normalize_id, validate_condition, prepare_bulk_updates

class MongoDB_DBA(DBA):
    def __init__(self, connection, collection_name):
        super().__init__(connection, collection_name)
        self.collection = self.connection.database[collection_name]

    def find_by_id(self, id):
        try:
            normalized_id = normalize_id(id)
            return self.collection.find_one({"_id": normalized_id})
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

    def update_one_by_id(self, id, new_value):
        try:
            normalized_id = normalize_id(id)
            return self.collection.update_one({"_id": normalized_id}, {"$set": new_value})
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
    def get_n(self, n):
        try:
            return list(self.collection.find().limit(n))
        except Exception as e:
            print(e)
            return None