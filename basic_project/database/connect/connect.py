import logging
from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ServerSelectionTimeoutError
from configs import db_config, logging_config
# from configs.db_config import *
import os
import sys

# current_dir = os.path.dirname(__file__)
# print(f'this joined path', os.path.join(current_dir, "../../"))
# project_root = os.path.abspath(os.path.join(current_dir, "../../"))
# print(project_root)
# sys.path.append(project_root)
# print(sys.path)
# Configure logging
logging.basicConfig(
    filename=logging_config.LOGGER_FILE,
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


class Connection:
    def __init__(self):
        self.uri = db_config.CONNECT['URL']
        self.database_name = db_config.CONNECT['DATABASE']
        self.client = None
        self.database = None

    def connect_to_mongodb(self):
        self.client = MongoClient(self.uri, server_api=ServerApi('1'))

        try:
            self.client.admin.command('ping')
            logging.info('Connected to MongoDB')
            self.database = self.client[self.database_name]
            print('Connected to MongoDB')
        except ServerSelectionTimeoutError as err:
            logging.error('MongoDB connection error: %s', err)
            self.client = None
            self.database = None

    def get_collection(self, collection_name):
        if self.database is not None:
            logging.info('Accessing collection: %s', collection_name)
            return self.database[collection_name]
        else:
            logging.warning(
                'Database not connected. Cannot access collection: %s', collection_name)
            return None


if __name__ == "__main__":
    connect = Connection()
    connect.connect_to_mongodb()
