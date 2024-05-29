from abc import ABC, abstractmethod

class Connection(ABC):
    def __init__(self):
        self.client = None
        self.database = None

    @staticmethod
    def create_connection(connection_type, **kwargs):
        if connection_type == 'mongo':
            from .mongo_connection import MongoConnection
            return MongoConnection(**kwargs)
        elif connection_type == 'sql':
            from .sql_connection import SQLConnection
            return SQLConnection(**kwargs)
        else:
            raise ValueError("Unsupported connection type")

    @abstractmethod
    def connect(self, username, password):
        pass
