from abc import ABC, abstractmethod
import os
import sys
from pymongo.errors import BulkWriteError

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)
class DBA(ABC):
    def __init__(self, connection, collection_name):
        self.connection = connection
        self.collection_name = collection_name

    @staticmethod
    def create_dba(dba_type, connection, collection_name):
        if dba_type == 'mongo':
            from .mongodb_dba import MongoDB_DBA
            return MongoDB_DBA(connection, collection_name)
        elif dba_type == 'sql':
            from .sql_dba import SQL_DBA
            return SQL_DBA(connection, collection_name)
        else:
            raise ValueError("Unsupported DBA type")

    @abstractmethod
    def find_by_id(self, id):
        pass

    @abstractmethod
    def find_one(self, condition):
        pass

    @abstractmethod
    def find_many(self, n, condition):
        pass

    @abstractmethod
    def update_one_by_id(self, id, new_value):
        pass

    @abstractmethod
    def update_many_by_id(self, ids, new_values):
        pass
