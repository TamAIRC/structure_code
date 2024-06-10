# postgresql_connection.py
import psycopg2
from configs.db_config import CONNECT
from basic_project.patterns.base_connection import Connect
from logger.logger import Logger


class PostgreSQLConnection(Connect):
    def __init__(self, database_name):
        super().__init__(database_name)
        self._connect()

    def _connect(self):
        try:
            self.client = psycopg2.connect(
                host=CONNECT["postgresql"]["HOST"],
                database=self.database_name,
                user=CONNECT["postgresql"]["USER"],
                password=CONNECT["postgresql"]["PASSWORD"],
            )
            self._test_connection()
            Logger("PostgreSQLConnection").log_info("Connected to PostgreSQL")
        except psycopg2.OperationalError as e:
            Logger("PostgreSQLConnection").log_error("PostgreSQL connection failure", e)
            self.client = None
        except Exception as e:
            Logger("PostgreSQLConnection").log_error("An error occurred while connecting to PostgreSQL", e)
            self.client = None

    def _test_connection(self):
        try:
            if self.client:
                cursor = self.client.cursor()
                cursor.execute("SELECT 1")
                cursor.close()
                Logger("PostgreSQLConnection").log_info("PostgreSQL connection test passed")
        except psycopg2.OperationalError as e:
            Logger("PostgreSQLConnection").log_error("PostgreSQL connection test failed", e)
            self.client = None

    def get_collection(self, table_name):
        if self.client is None:
            Logger("PostgreSQLConnection").log_error("No database connection available", "")
            return None

        try:
            cursor = self.client.cursor()
            cursor.execute(f"SELECT * FROM {table_name}")
            result = cursor.fetchall()
            cursor.close()
            Logger("PostgreSQLConnection").log_info(f"Accessed table: {table_name}")
            return result
        except psycopg2.OperationalError as e:
            Logger("PostgreSQLConnection").log_error(f"Failed to access table: {table_name}", e)
            return None

    def close_connection(self):
        if self.client:
            try:
                self.client.close()
                Logger("PostgreSQLConnection").log_info("PostgreSQL connection closed")
            except psycopg2.OperationalError as e:
                Logger("PostgreSQLConnection").log_error(
                    "Error occurred while closing PostgreSQL connection", e
                )
        else:
            Logger("PostgreSQLConnection").log_info("No active PostgreSQL connection to close")
