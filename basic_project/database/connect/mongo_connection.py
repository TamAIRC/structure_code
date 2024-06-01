import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "../../"))
from configs import db_config
from logger.logger import Logger

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure


class MongoConnection:
    # Singleton instance
    _instance = None

    def __new__(cls):
        # Ensure only one instance of MongoConnection exists
        if cls._instance is None:
            cls._instance = super(MongoConnection, cls).__new__(cls)
            # Initialize logger, URI, database name, and collections dictionary
            cls._instance.logger = Logger("MongoDBLogger")
            cls._instance.uri = db_config.CONNECT["URL"]
            cls._instance.database_name = db_config.CONNECT["DATABASE"]
            cls._instance.collections = {}
            cls._instance.client = None
            cls._instance.database = None
            try:
                cls._instance.client = MongoClient(
                    cls._instance.uri,
                    server_api=ServerApi("1"),
                    serverSelectionTimeoutMS=5000,
                )
                # Get the database object
                cls._instance.database = cls._instance.client[
                    cls._instance.database_name
                ]
                # Test the connection
                cls._instance._test_connection()
            except (ServerSelectionTimeoutError, ConnectionFailure) as e:
                cls._instance.logger.log_error("MongoDB connection failure", e)
            except Exception as e:
                cls._instance.logger.log_error(
                    "An error occurred while connecting to MongoDB", e
                )
        return cls._instance

    def _test_connection(self):
        """
        Test the MongoDB connection by pinging the server.
        """
        try:
            # Ping the server to check the connection
            self.client.admin.command("ping")
            self.logger.log_info("Connected to MongoDB")
        except Exception as err:
            self.logger.log_error("Failed to ping MongoDB", err)
            self.client = None
            self.database = None

    def get_collection(self, collection_name: str):
        """
        Get a collection from the MongoDB database. Caches collections for quick access.

        Parameters:
            collection_name (str): The name of the collection to access.

        Returns:
            Collection or None: The MongoDB collection object or None if access fails.
        """
        if self.database is None:
            # Log error if there is no database connection
            self.logger.log_error("No database connection available", "")
            return None

        if collection_name in self.collections:
            # Log info if the collection is already cached
            self.logger.log_info(f"Accessing cached collection: {collection_name}")
            return self.collections[collection_name]

        try:
            # Get the collection from the database
            collection = self.database[collection_name]
            # Cache the collection for future access
            self.collections[collection_name] = collection
            self.logger.log_info(f"Accessing new collection: {collection_name}")
            return collection
        except Exception as err:
            self.logger.log_error(
                f"Failed to access collection: {collection_name}", err
            )
            return None

    def close_connection(self):
        """
        Close the MongoDB connection.
        """
        if self.client:
            try:
                self.client.close()
                self.logger.log_info("Closed MongoDB connection")
            except Exception as e:
                self.logger.log_error(
                    "Error occurred while closing MongoDB connection", e
                )
        else:
            self.logger.log_info("No active MongoDB connection to close")


if __name__ == "__main__":
    # Create a MongoDB connection instance
    mongo_connection = MongoConnection()

    # Access collections
    collection1 = mongo_connection.get_collection(db_config.SCHEMA["QUESTIONS"])
    collection2 = mongo_connection.get_collection(db_config.SCHEMA["USER"])
    collection3 = mongo_connection.get_collection(
        db_config.SCHEMA["ANSWERED_QUESTIONS"]
    )

    # Example operations with collections
    if collection1 is not None:
        print(f"Collection 1: {collection1.name}")
    if collection2 is not None:
        print(f"Collection 2: {collection2.name}")
    if collection3 is not None:
        print(f"Collection 3: {collection3.name}")

    # Close the MongoDB connection
    mongo_connection.close_connection()
