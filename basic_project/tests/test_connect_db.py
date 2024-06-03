# test_connect_db.py
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from database.connect.mongo_connect import MongoConnect
from database.connect.mysql_connect import MySQLConnect
from database.connect.sqlserver_connect import SQLServerConnect
from database.connect.postgresql_connect import PostgreSQLConnect
from configs.db_config import CONNECT


def main():
    # MongoDB
    mongo_db1 = MongoConnect(CONNECT["mongo"]["DATABASE"])
    mongo_db2 = MongoConnect(CONNECT["mongo"]["DATABASE"])
    print(mongo_db1 is mongo_db2)  # Should print: True
    mongo_db1.close_connection()

    # MySQL
    mysql_db1 = MySQLConnect(CONNECT["mysql"]["DATABASE"])
    mysql_db2 = MySQLConnect(CONNECT["mysql"]["DATABASE"])
    print(mysql_db1 is mysql_db2)  # Should print: True
    mysql_db1.close_connection()

    # SQL Server
    sqlserver_db1 = SQLServerConnect(CONNECT["sqlserver"]["DATABASE"])
    sqlserver_db2 = SQLServerConnect(CONNECT["sqlserver"]["DATABASE"])
    print(sqlserver_db1 is sqlserver_db2)  # Should print: True
    sqlserver_db1.close_connection()

    # PostgreSQL
    postgresql_db1 = PostgreSQLConnect(CONNECT["postgresql"]["DATABASE"])
    postgresql_db2 = PostgreSQLConnect(CONNECT["postgresql"]["DATABASE"])
    print(postgresql_db1 is postgresql_db2)  # Should print: True
    postgresql_db1.close_connection()


if __name__ == "__main__":
    main()
