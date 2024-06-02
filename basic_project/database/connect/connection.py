import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from abc import ABC, abstractmethod


class Connection(ABC):
    def __init__(self):
        self.client = None
        self.database = None

    @staticmethod
    def create_connection(connection_type, **kwargs):
        if connection_type == "mongo":
            from database.connect.mongo_connection import MongoConnection

            return MongoConnection(**kwargs)
        elif connection_type == "sql":
            from database.connect.sql_connection import SQLConnection

            return SQLConnection(**kwargs)
        else:
            raise ValueError("Unsupported connection type")

    @abstractmethod
    def _test_connection(self):
        pass

    @abstractmethod
    def get_collection(self, **kwargs):
        pass

    @abstractmethod
    def close_connection(self):
        pass

    # Use main_v2 in mongo_connection
    # @abstractmethod
    # def connect(self, username, password):
    #     pass
