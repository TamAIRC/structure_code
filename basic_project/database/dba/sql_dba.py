# database/database_access/question_dba.py
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from database.dba.dba import DBA

class SQL_DBA(DBA):
    def __init__(self, connection, table_name):
        super().__init__(connection, table_name)
        self.table = table_name

    def find_by_id(self, id):
        query = f"SELECT * FROM {self.table} WHERE id = %s"
        result = self.connection.execute(query, (id,))
        return result.fetchone()

    def find_one(self, condition):
        query = f"SELECT * FROM {self.table} WHERE {condition}"
        result = self.connection.execute(query)
        return result.fetchone()

    def find_many(self, n, condition):
        query = f"SELECT * FROM {self.table} WHERE {condition} LIMIT %s"
        result = self.connection.execute(query, (n,))
        return result.fetchall()

    def update_one_by_id(self, id, new_value):
        set_clause = ", ".join(f"{k} = %s" for k in new_value.keys())
        values = list(new_value.values())
        query = f"UPDATE {self.table} SET {set_clause} WHERE id = %s"
        result = self.connection.execute(query, (*values, id))
        return result.rowcount

    def update_many_by_id(self, ids, new_values):
        results = []
        for id, new_value in zip(ids, new_values):
            result = self.update_one_by_id(id, new_value)
            results.append(result)
        return results
