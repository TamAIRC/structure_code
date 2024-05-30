import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "../../"))
from configs import db_config
from logger import logger

from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure, PyMongoError


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

    def transaction(self, query_func):
        """Perform a transaction. Implementation depends on specific use case."""
        if self.client is None:
            self.logger.log_error("No MongoDB client available for transaction")
            return None

        with self.client.start_session() as session:
            try:
                session.start_transaction()
                query_func(session)
                session.commit_transaction()
                self.logger.log_info("Transaction committed successfully")
            except (
                ConnectionFailure,
                ServerSelectionTimeoutError,
                PyMongoError,
            ) as err:
                self.logger.log_error("Transaction failed", err)
                session.abort_transaction()
                self.logger.log_info("Transaction aborted")
                return None
        return True


if __name__ == "__main__":
    mg_connect = Connection()
    mg_connect.get_connection()
    mg_connect.get_collection(db_config.SCHEMA["QUESTIONS"])
    mg_connect.close_connection()
