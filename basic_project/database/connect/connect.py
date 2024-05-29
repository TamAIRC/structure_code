import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "..\\..\\"))
from configs import db_config
from logger import logger

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError


class Connection:
    def __init__(self):
        self.uri = db_config.CONNECT["URL"]
        self.database_name = db_config.CONNECT["DATABASE"]
        self.client = None
        self.database = None
        self.logger = logger.Logger()

    def get_connection(self):
        self.client = MongoClient(self.uri)

        try:
            self.client.admin.command("ping")
            self.logger.log_info("Connected to MongoDB")
            self.database = self.client[self.database_name]
        except ServerSelectionTimeoutError as err:
            self.logger.log_error("MongoDB connection error", err)
            self.client = None
            self.database = None

    def close_connection(self):
        self.client.close()
        self.logger.log_info("Close connect MongoDB")


if __name__ == "__main__":
    mg_connect = Connection()
    mg_connect.get_connection()
    mg_connect.close_connection()
