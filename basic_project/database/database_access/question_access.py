import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from database.database_connection.mongo_connection import MongoConnection
from database.database_access.dba import DBA
from configs.db_config import db_config

def QuestionDBA(DBA):
    def __init__(self):
        super().__init__(MongoConnection()[db_config.QUESTION_COLLECTION])
        
    