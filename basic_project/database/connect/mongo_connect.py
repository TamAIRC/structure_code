# mongo_connect.py
import os
import sys


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure
from configs.db_config import CONNECT, SCHEMA
from patterns.base_connect import BaseConnect as Connect
from patterns.singleton_meta import SingletonABCMeta
from logger.logger import Logger


class MongoConnect(Connect):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.url = CONNECT["mongo"]["URL"]
        self._connect()
        self.collections = {}

    def _connect(self):
        try:
            self.client = MongoClient(
                self.url,
                server_api=ServerApi("1"),
                serverSelectionTimeoutMS=5000,
            )
            # Get the database object
            self.database = self.client[self.database_name]
            # Test the connection
            self._test_connection()
            Logger("MongoConnect").log_info("Connected to MongoDB")
        except (ServerSelectionTimeoutError, ConnectionFailure) as e:
            Logger("MongoConnect").log_error(f"MongoDB connection failure:{e}")
        except Exception as e:
            Logger("MongoConnect").log_error(
                f"An error occurred while connecting to MongoDB: {e}"
            )

    def _test_connection(self):
        """
        Test the MongoDB connection by pinging the server.
        """
        try:
            # Ping the server to check the connection
            self.client.admin.command("ping")
            Logger("MongoConnect").log_info("Test connection to MongoDB")
        except Exception as err:
            Logger("MongoConnect").log_error(f"Failed to ping MongoDB: {err}")
            self.client = None
            self.client.database = None

    def get_collection(self, collection_name):
        """
        Get a collection from the MongoDB database. Caches collections for quick access.

        Parameters:
            collection_name (str): The name of the collection to access.

        Returns:
            Collection or None: The MongoDB collection object or None if access fails.
        """
        if self.database is None:
            # Log error if there is no database connection
            Logger("MongoConnect").log_error("No database connection available")
            return None

        if collection_name in self.collections:
            # Log info if the collection is already cached
            Logger("MongoConnect").log_info(
                f"Accessing cached collection: {collection_name}"
            )
            return self.collections[collection_name]
        try:
            # Get the collection from the database
            collection = self.database[collection_name]
            # Cache the collection for future access
            self.collections[collection_name] = collection
            Logger("MongoConnect").log_info(
                f"Accessing new collection: {collection_name}"
            )
            return collection
        except Exception as err:
            Logger("MongoConnect").log_error(
                f"Failed to access collection {collection_name}: {err}"
            )
            return None

    def close_connection(self):
        """
        Close the MongoDB connection.
        """
        if self.client:
            print("self.client", self.client)
            try:
                self.client.close()
                Logger("MongoConnect").log_info("MongoDB connection closed")
                self.collections = {}
                SingletonABCMeta._remove_instance(
                    MongoConnect
                )  # Remove instance from Singleton
            except Exception as err:
                Logger("MongoConnect").log_error(
                    f"Error occurred while closing MongoDB connection: {err}"
                )
        else:
            Logger("MongoConnect").log_info("No active MongoDB connection to close")


def main():
    log_main = Logger("mainLogger")
    # Create a MongoDB connection instance
    mongo_connect_1 = MongoConnect(CONNECT["mongo"]["DATABASE"])
    print(mongo_connect_1)
    log_main.log_info("log_main")
    mongo_connect_2 = MongoConnect(CONNECT["mongo"]["DATABASE"])
    print(mongo_connect_2)
    print(mongo_connect_1 is mongo_connect_2)  # Should print: True
    # # Access collections
    # collection1 = mongo_connect_1.get_collection(SCHEMA["QUESTIONS"])
    # collection2 = mongo_connect_2.get_collection(SCHEMA["USER"])
    # collection3 = mongo_connect_1.get_collection(SCHEMA["ANSWERED_QUESTIONS"])
    # # Example operations with collections
    # if collection1 is not None:
    #     print(f"Collection 1: {collection1.name}")
    # if collection2 is not None:
    #     print(f"Collection 2: {collection2.name}")
    # if collection3 is not None:
    #     print(f"Collection 3: {collection3.name}")
    # Close the MongoDB connection

    mongo_connect_1.close_connection()


if __name__ == "__main__":
    main()
