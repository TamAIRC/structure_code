import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "../../"))
from configs import db_config
from logger.logger import Logger
from database.connect.connection import Connection

from pymongo import MongoClient
from pymongo.server_api import ServerApi
from pymongo.errors import ServerSelectionTimeoutError, ConnectionFailure

# main_v1
class MongoConnection():
# main_v2
# class MongoConnection(Connection):
    # Singleton instance
    _instance = None

    def __new__(
        self, uri=db_config.CONNECT["URL"], database_name=db_config.CONNECT["DATABASE"]
    ):
        # Ensure only one instance of MongoConnection exists
        if self._instance is None:
            self._instance = super(MongoConnection, self).__new__(self)
            # Initialize logger, URI, database name, and collections dictionary
            self._instance.logger = Logger("MongoDBLogger")
            self._instance.uri = uri
            self._instance.database_name = database_name
            self._instance.collections = {}
            self._instance.client = None
            self._instance.database = None
            try:
                self._instance.client = MongoClient(
                    self._instance.uri,
                    server_api=ServerApi("1"),
                    serverSelectionTimeoutMS=5000,
                )
                # Get the database object
                self._instance.database = self._instance.client[
                    self._instance.database_name
                ]
                # Test the connection
                self._instance._test_connection()
            except (ServerSelectionTimeoutError, ConnectionFailure) as e:
                self._instance.logger.log_error("MongoDB connection failure", e)
            except Exception as e:
                self._instance.logger.log_error(
                    "An error occurred while connecting to MongoDB", e
                )
        return self._instance

    def _test_connection(self):
        """
        Test the MongoDB connection by pinging the server.
        """
        try:
            # Ping the server to check the connection
            self._instance.client.admin.command("ping")
            self._instance.logger.log_info("Connected to MongoDB")
        except Exception as err:
            self._instance.logger.log_error("Failed to ping MongoDB", err)
            self._instance.client = None
            self._instance.database = None

    def get_collection(self, collection_name: str):
        """
        Get a collection from the MongoDB database. Caches collections for quick access.

        Parameters:
            collection_name (str): The name of the collection to access.

        Returns:
            Collection or None: The MongoDB collection object or None if access fails.
        """
        # print("self._instance.database", self._instance.database)
        if self._instance.database is None:
            # Log error if there is no database connection
            self._instance.logger.log_error("No database connection available", "")
            return None

        if collection_name in self.collections:
            # Log info if the collection is already cached
            self._instance.logger.log_info(
                f"Accessing cached collection: {collection_name}"
            )
            return self.collections[collection_name]

        try:
            # Get the collection from the database
            collection = self._instance.database[collection_name]
            # Cache the collection for future access
            self.collections[collection_name] = collection
            self._instance.logger.log_info(
                f"Accessing new collection: {collection_name}"
            )
            return collection
        except Exception as err:
            self._instance.logger.log_error(
                f"Failed to access collection: {collection_name}", err
            )
            return None

    def close_connection(self):
        """
        Close the MongoDB connection.
        """
        if self._instance.client:
            try:
                self._instance.client.close()
                self._instance.logger.log_info("Closed MongoDB connection")
            except Exception as e:
                self._instance.logger.log_error(
                    "Error occurred while closing MongoDB connection", e
                )
        else:
            self._instance.logger.log_info("No active MongoDB connection to close")

    def connect(self, username, password):
        uri = self.uri_template.format(username=username, password=password)
        self._instance.client = MongoClient(uri)
        try:
            self._instance.client.admin.command('ping')
            self._instance.logger.info('Connected to MongoDB')
            self.database = self._instance.client[self.database_name]
            print("Connect successfully!")
        except ServerSelectionTimeoutError as err:
            self._instance.logger.error('MongoDB connection error: %s', err)
            self._instance.client = None
            self.database = None

def main_v1():
    # Edit MongoConnection(Connection) to MongoConnection() - Maybe line 15
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

# Hướng chọn db khác nhau chưa thể xử lý - Co chưa tương thích được
def main_v2():
    # Create a MongoDB connection instance
    connection = Connection.create_connection(db_config.DB_TYPE)
    print(connection)
    # Access collections
    collection1 = connection.get_collection(db_config.SCHEMA["QUESTIONS"])
    collection2 = connection.get_collection(db_config.SCHEMA["USER"])
    collection3 = connection.get_collection(db_config.SCHEMA["ANSWERED_QUESTIONS"])

    # Example operations with collections
    if collection1 is not None:
        print(f"Collection 1: {collection1.name}")
    if collection2 is not None:
        print(f"Collection 2: {collection2.name}")
    if collection3 is not None:
        print(f"Collection 3: {collection3.name}")

    # Close the MongoDB connection
    connection.close_connection()


if __name__ == "__main__":
    main_v1()
    # main_v2()
