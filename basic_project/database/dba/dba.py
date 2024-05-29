# database/database_access/dba.py
from bson import ObjectId
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from database.connect.connect import Connection as db_connection
from utils.util import normalize_id, validate_condition, prepare_bulk_updates

class DBA:
    def __init__(self, collection_name):
        self.connection = db_connection()
        self.connection.connect_to_mongodb()
        self.collection = self.connection.get_collection(collection_name)
    
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
            return self.collection.find(validated_condition).limit(1)
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
        except ValueError as e:
            print(e)
            return None
