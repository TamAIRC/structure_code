import os 
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, '../../'))

from configs import db_config
from logger import logger

# import logging
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


class Connection:
    ''' mo ket noi den database, dong ke noi '''
    def __init__(self):
        self.uri = db_config.CONNECT['URL']
        self.database_name = db_config.CONNECT['DATABASE']
        self.client = None
        self.database = None
        print("Connection init")

    def get_connection(self):
        self.client = MongoClient(self.uri)
        try:
            self.client.admin.command('ping')
            # logging.info('Connected to MongoDB') 
            logger.Logger.log_info('Connected to MongoDB')
            self.database = self.client[self.database_name]
        except ServerSelectionTimeoutError as err:
            # logging.error('MongoDB connection error: %s', err) 
            logger.Logger.log_error('MongoDB connection error', err)
            self.client = None
            self.database = None
    def close_connection(self):
        self.client.close()
        # logging.error('Closing connection to MongoDB') 
        logger.Logger.log_info('Closing connection to MongoDB')

# def main():
#     connection = Connection()
#     connection.get_connection()
#     connection.close_connection()
#     return

# main()