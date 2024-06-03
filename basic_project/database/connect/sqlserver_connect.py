# sqlserver_connect.py
import os
import sys


current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from configs.db_config import CONNECT
from patterns.base_connect import Connect
from logger.logger import Logger

import pyodbc


class SQLServerConnect(Connect):
    def __init__(self, database_name):
        super().__init__(database_name)
        self.logger = Logger("SQLServerLogger")
        self._connect()

    def _connect(self):
        try:
            self.client = pyodbc.connect(
                f'DRIVER={{ODBC Driver 17 for SQL Server}};SERVER={CONNECT["sqlserver"]["HOST"]};DATABASE={self.database_name};UID={CONNECT["sqlserver"]["USER"]};PWD={CONNECT["sqlserver"]["PASSWORD"]}'
            )
            self._test_connection()
            self.logger.log_info("Connected to SQL Server")
        except pyodbc.Error as e:
            self.logger.log_error("SQL Server connection failure", e)
            self.client = None
        except Exception as e:
            self.logger.log_error("An error occurred while connecting to SQL Server", e)
            self.client = None

    def _test_connection(self):
        try:
            if self.client:
                cursor = self.client.cursor()
                cursor.execute("SELECT 1")
                cursor.close()
                self.logger.log_info("SQL Server connection test passed")
        except pyodbc.Error as e:
            self.logger.log_error("SQL Server connection test failed", e)
            self.client = None

    def get_collection(self, table_name):
        if self.client is None:
            self.logger.log_error("No database connection available", "")
            return None

        try:
            cursor = self.client.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            result = cursor.fetchall()
            cursor.close()
            self.logger.log_info(f"Accessed table: {table_name}")
            return result
        except pyodbc.Error as e:
            self.logger.log_error(f"Failed to access table: {table_name}", e)
            return None

    def close_connection(self):
        if self.client:
            try:
                self.client.close()
                self.logger.log_info("SQL Server connection closed")
            except pyodbc.Error as e:
                self.logger.log_error(
                    "Error occurred while closing SQL Server connection", e
                )
        else:
            self.logger.log_info("No active SQL Server connection to close")
