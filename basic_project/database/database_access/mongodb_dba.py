# database/database_access/mongodb_dba.py
''' thiet ke lop base (co so) cho he thong truy van co so du lieu'''
# database/database_access/dba.py
from bson import ObjectId
import os
import sys
from abc import ABC, abstractmethod 
from database.database_access.dba import DBA
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from database.connect.connect import Connection as db_connection
from utils.util import normalize_id, validate_condition, prepare_bulk_updates

class MongoDB_DBA(DBA):
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
    '''
    các function sẽ có là
    find_many()
    find_one_by_id()
    delete_one_by_id()
    
    '''
    
    @abstractmethod
    #TODO chưa có tìm theo điều kiện
    def find_one_by_id(self, objectid):
        try:
            question = self.collection.find_one({"_id": objectid})
            return question
        except Exception as e:
            print(f"An error occurred: {e}")
            return []

    @abstractmethod
    #TODO chưa có tìm theo điều kiện
    def find_many(self, num_ques, filter=None):
        """_summary_

        Args:
            num_ques (_type_): number of question to take
            filter (_type_, optional): a dictionary of query to perform. Defaults to None.

        Returns:
            list: list of question ObjectId
        """
        try:
            questions = self.collection.find().limit(num_ques)
            return list(questions)
        except Exception as e:
            print(f"An error occurred: {e}")
            return None
        
    @abstractmethod
    def update_one_by_id(self, objectid, update_value):
        """_summary_

        Args:
            objectid (ObjectId): ObjectId of wanted modify document
            update_value (dict): document or pipeline

        Returns:
            _type_: _description_
        """
        try:
            result = self.collection.find_one_and_update(
                {"_id": ObjectId(objectid)},
                {"$set": update_value}
            )
            return result.modified_count
        except Exception as e:
            print(f"An error occured in mongoDBA: {e}")
            return 0

    def update_many(self, condition, update_fields):
        """_summary_

        Args:
            condition (dict): condition to match multiple documents
            update_fields (dict): field of wanted update value

        Returns:
            _type_: _description_
        """
        try:
            result = self.collection.update_many(
            condition,
            {"$set": update_fields}
        )
            return result.modified_count
        except Exception as e:
            print(f"An error occured: {e}")
            return None

if __name__ == "__main__":
    objetcid = ObjectId('66260e94a51b34b732f211dd')
    conn =  MongoDB_DBA('questions')
    result = conn.find_one_by_id(objetcid)
    print(result)