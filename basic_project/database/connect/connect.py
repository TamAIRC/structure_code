import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "../../"))
from configs import db_config
from logger import logger

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure


class Connection:
    def __init__(self):
        self.uri = db_config.CONNECT["URL"]
        self.database_name = db_config.CONNECT["DATABASE"]
        self.client = None
        self.database = None
        self.logger = logger.Logger()

    def get_connection(self):
        try:
            self.client = MongoClient(self.uri, serverSelectionTimeoutMS=5000)
            # Attempt to connect to the server
            self.client.admin.command("ping")
            self.logger.log_info("Connected to MongoDB")
            self.database = self.client[self.database_name]
        except ServerSelectionTimeoutError as err:
            self.logger.log_error("MongoDB connection timeout", err)
            self.client = None
            self.database = None
        except ConnectionFailure as err:
            self.logger.log_error("MongoDB connection failure", err)
            self.client = None
            self.database = None
        except Exception as err:
            self.logger.log_error("An error occurred while connecting to MongoDB", err)
            self.client = None
            self.database = None

    def get_collection(self, collection_name: str):
        if self.database is not None:  # Explicitly compare with None
            self.logger.log_info("Accessing collection: %s", collection_name)
            return self.database[collection_name]
        else:
            self.logger.log_error("No database connection available")
            return None

    def close_connection(self):
        if self.client:
            try:
                self.client.close()
                self.logger.log_info("Closed MongoDB connection")
            except Exception as err:
                self.logger.log_error(
                    "Error occurred while closing MongoDB connection", err
                )
        else:
            self.logger.log_info("No active MongoDB connection to close")


if __name__ == "__main__":
    mg_connect = Connection()
    mg_connect.get_connection()
    mg_connect.get_collection(db_config.SCHEMA["QUESTIONS"])
    mg_connect.close_connection()
