import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from database.database_connection.connection import Connection
from configs import db_config
from database.database_access.dba import DBA
from database.database_access.question_dba import QuestionDBA
from database.database_access.result_dba import ResultDBA
from bson import ObjectId
from database.database_models.question_model import QuestionDBO
if __name__ == "__main__":
    connection_params = {
        'uri_template': db_config.CONNECT['URL'],
        'database_name': db_config.CONNECT['DATABASE']
    }
    connection = Connection.create_connection(db_config.DB_TYPE, **connection_params)
    connection.connect(db_config.USERNAME, db_config.PASSWORD)
    
    question_dba = QuestionDBA(connection)
    print(question_dba.get_n_questions(100))
    new_data = [{'_id': ObjectId('66260e94a51b34b732f211dd'), 'category': 'Geography', 'subcategory': 'Medieval History', 'content': 'Phone rule we pattern be clear.', 'answers': ['why', 'east', 'nature', 'attention'], 'correct_answer': 'nature', 'difficulty': 5, 'required_rank': 5, 'language': 2, 'multimedia': ObjectId('66260e86a51b34b732f21182')}]
    new_question = [QuestionDBO.from_json_obj(data) for data in new_data]
    question_dba.update_n_questions(new_question)
    # question_dba.dba.update_many_by_id(ids, new_values)
    print()
    print(question_dba.dba.find_by_id(ObjectId('66260e94a51b34b732f211dd')))
    
    result_dba = ResultDBA(connection)
    print(result_dba.get_n_questions("663884b5f6b183dfa7faed6c"))