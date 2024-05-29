import logging
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from .connection import Connection

class MongoConnection(Connection):
    def __init__(self, uri_template, database_name):
        super().__init__()
        self.uri_template = uri_template
        self.database_name = database_name

    def connect(self, username, password):
        uri = self.uri_template.format(username=username, password=password)
        self.client = MongoClient(uri)
        try:
            self.client.admin.command('ping')
            logging.info('Connected to MongoDB')
            self.database = self.client[self.database_name]
            print("Connect successfully!")
        except ServerSelectionTimeoutError as err:
            logging.error('MongoDB connection error: %s', err)
            self.client = None
            self.database = None
