# database/database_connection/mongo_connection.py
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from configs.db_config import db_config
from logger.logger import Logger

class MongoConnection:
    _instance = None
    logger = Logger()
    
    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(MongoConnection, cls).__new__(cls)
            try:
                cls._instance.client = MongoClient(db_config.URI, server_api=ServerApi('1'))
                cls._instance.database = cls._instance.client[db_config.DATABASE]
            except Exception as e:
                cls.logger.log_error("An error occurred while connecting to MongoDB", e)
        return cls._instance