# database/database_access/mongodb_dba.py
''' thiet ke lop base (co so) cho he thong truy van co so du lieu'''
# database/database_access/dba.py
from bson import ObjectId
import os
import sys
from abc import ABC, abstractmethod 

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from database.connect.connect import Connection as db_connection
from utils.util import normalize_id, validate_condition, prepare_bulk_updates

class MongoDB_DBA:
    # cac thong tin chung cua moi va hanh dong chung cua moi lop quan ly, tuong tac co so du lieu
    def __init__(self, collection_name):
        self.connection = db_connection()
        self.connection.connect_to_mongodb()
        self.collection = self.connection.get_collection(collection_name)


    '''
    mục đích tạo riêng 1 dba cho mongodb là vì các sub-dba cần kế thừa nhiều
    và nếu không có 1 base thì phải viết lại rất nhiều code
    
    có nên có có một cái base để search theo điều kiện
    '''
    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    #TODO chưa có tìm theo điều kiện
    def find_one(self, objectid, filter=None):
        try:
            if filter == None:
                filter = {"_id": objectid}
                question = self.collection.find_one(filter)
                return list(question)
            else:
                question = self.collection.find_one(filter)
                return list(question)
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    @abstractmethod
    def update_one_by_id(self, objectid, new_value):
        try:
            result = self.collection.find_one_and_update(
                {"_id": ObjectId(objectid)},
                {"$set": new_value}
            )
            print(f'successfully update question with id {objectid}')
            return result.modified_count
        except Exception as e:
            print(f"An error occured: {e}")
            return 0

    @abstractmethod
    #TODO chưa có tìm theo điều kiện
    def find_many(self, objectids, filter=None):
        try:
            if filter == None:
                filter = {"_id": {"$in": objectids}}
                questions = self.collection.find(filter)
                # return list gồm các mảng json à?
                return list(questions)
            else:
                questions = self.collection.find(filter)
                return list(questions)
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    @abstractmethod
    def insert(self, object):
        pass