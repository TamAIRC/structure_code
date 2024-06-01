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

class DBA:
    # cac thong tin chung cua moi va hanh dong chung cua moi lop quan ly, tuong tac co so du lieu
    def __init__(self, collection_name):
        self.connection = db_connection()
        self.connection.connect_to_mongodb()
        # self.collection = self.connection.get_collection(collection_name)
        
    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_one(self, condition):
        pass

    @abstractmethod
    def update_one_by_id(self, id, new_value):
        pass

    @abstractmethod
    def find_many(self, n, condition):
        pass
    
    @abstractmethod
    def insert(self, object):
        pass
