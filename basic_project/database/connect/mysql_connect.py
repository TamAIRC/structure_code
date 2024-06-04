# mysql_connect.py
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from configs.db_config import CONNECT
from patterns.base_connect import Connect
from logger.logger import Logger

import mysql.connector
from mysql.connector import Error


class MySQLConnect(Connect):
    def __init__(self, database_name):
        super().__init__(database_name)
        self._connect()

    def _connect(self):
        try:
            self.client = mysql.connector.connect(
                host=CONNECT["mysql"]["HOST"],
                database=self.database_name,
                user=CONNECT["mysql"]["USER"],
                password=CONNECT["mysql"]["PASSWORD"],
            )
            self._test_connection()
            Logger("MySQLConnect").log_info("Connected to MySQL")
        except Error as e:
            Logger("MySQLConnect").log_error("MySQL connection failure", e)
            self.client = None
        except Exception as e:
            Logger("MySQLConnect").log_error("An error occurred while connecting to MySQL", e)
            self.client = None

    def _test_connection(self):
        try:
            if self.client:
                cursor = self.client.cursor()
                cursor.execute("SELECT 1")
                cursor.close()
                Logger("MySQLConnect").log_info("MySQL connection test passed")
        except Error as e:
            Logger("MySQLConnect").log_error("MySQL connection test failed", e)
            self.client = None

    def get_collection(self, table_name):
        if self.client is None:
            Logger("MySQLConnect").log_error("No database connection available", "")
            return None

        try:
            cursor = self.client.cursor(dictionary=True)
            cursor.execute(f"SELECT * FROM {table_name}")
            result = cursor.fetchall()
            cursor.close()
            Logger("MySQLConnect").log_info(f"Accessed table: {table_name}")
            return result
        except Error as e:
            Logger("MySQLConnect").log_error(f"Failed to access table: {table_name}", e)
            return None

    def close_connection(self):
        if self.client:
            try:
                self.client.close()
                Logger("MySQLConnect").log_info("MySQL connection closed")
            except Error as e:
                Logger("MySQLConnect").log_error(
                    "Error occurred while closing MySQL connection", e
                )
        else:
            Logger("MySQLConnect").log_info("No active MySQL connection to close")
