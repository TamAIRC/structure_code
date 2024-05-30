# database/database_connection/mongo_connection.py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from configs.db_config import db_config

class MongoConnection:
    _instance = None
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoConnection, cls).__new__(cls)
            cls._instance.client = MongoClient(db_config.URI, server_api=ServerApi('1'))
        return cls._instance