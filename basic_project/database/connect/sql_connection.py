# database/database_connection/sql_connection.py
import os
import sys

__dir__ = os.path.dirname(__file__)
sys.path.append(os.path.join(__dir__, "../../"))
from configs import db_config
from logger.logger import Logger
from database.connect.connection import Connection


class SQLConnection(Connection):
    # Singleton instance
    _instance = None

    def __new__(cls):
        # Ensure only one instance of SQLConnection exists
        pass

    def _test_connection(self):
        """
        Test the SQLDB connection by pinging the server.
        """
        pass

    def get_collection(self):
        """
        Get a table from the SQLDB database. Caches tables for quick access.
        """
        pass

    def close_connection(self):
        """
        Close the SQLDB connection.
        """
        pass


if __name__ == "__main__":
    # Create a SQLDB connection instance
    sql_connection = SQLConnection()

    # Access collections
    collection1 = sql_connection.get_collection()
    # Close the SQLDB connection
    sql_connection.close_connection()
