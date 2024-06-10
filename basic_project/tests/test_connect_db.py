# test_connect_db.py
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from database.connection.mongo_connection import MongoConnection
# from database.connection.mysql_connection import MySQLConnection
# from database.connection.sqlserver_connection import SQLServerConnection
# from database.connection.postgresql_connection import PostgreSQLConnection
from configs.db_config import CONNECT


def main():
    # MongoDB
    mongo_db1 = MongoConnection(CONNECT["mongo"]["DATABASE"])
    mongo_db2 = MongoConnection(CONNECT["mongo"]["DATABASE"])
    print(mongo_db1 is mongo_db2)  # Should print: True
    mongo_db1.close_connection()

    # # MySQL
    # mysql_db1 = MySQLConnection(CONNECT["mysql"]["DATABASE"])
    # mysql_db2 = MySQLConnection(CONNECT["mysql"]["DATABASE"])
    # print(mysql_db1 is mysql_db2)  # Should print: True
    # mysql_db1.close_connection()

    # # SQL Server
    # sqlserver_db1 = SQLServerConnection(CONNECT["sqlserver"]["DATABASE"])
    # sqlserver_db2 = SQLServerConnection(CONNECT["sqlserver"]["DATABASE"])
    # print(sqlserver_db1 is sqlserver_db2)  # Should print: True
    # sqlserver_db1.close_connection()

    # # PostgreSQL
    # postgresql_db1 = PostgreSQLConnection(CONNECT["postgresql"]["DATABASE"])
    # postgresql_db2 = PostgreSQLConnection(CONNECT["postgresql"]["DATABASE"])
    # print(postgresql_db1 is postgresql_db2)  # Should print: True
    # postgresql_db1.close_connection()


if __name__ == "__main__":
    main()
