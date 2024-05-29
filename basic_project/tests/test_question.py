import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from database.database_connection.connection import Connection
from configs import db_config
from database.database_access.dba import DBA
from bson import ObjectId
if __name__ == "__main__":
    connection_params = {
        'uri_template': db_config.CONNECT['URL'],
        'database_name': db_config.CONNECT['DATABASE']
    }
    connection = Connection.create_connection(db_config.DB_TYPE, **connection_params)
    connection.connect(db_config.USERNAME, db_config.PASSWORD)
    dba = DBA.create_dba(db_config.DB_TYPE, connection, db_config.CONNECT['QUESTION_COLLECTION'])
    print(dba.get_n(100))
    
    ids = [ObjectId('66260e94a51b34b732f211dd'), ObjectId('66260e94a51b34b732f211e1'), ObjectId('66260e94a51b34b732f211e0')]
    new_values = [{"category": "Geography"}, {"language": "2"}, {"category": "2"}]
    dba.update_one_by_id(ObjectId('66260e94a51b34b732f211dd'), {"category": "Geography"})
    dba.update_many_by_id(ids, new_values)
    print(dba.find_by_id(ObjectId('66260e94a51b34b732f211dd')))