# tests/test_question.py
import os
import sys
from bson import ObjectId

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from database.dba.question_dba import QuestionDBA
from database.dbo.question_dbo import QuestionDBO
if __name__ == "__main__":
    # result = dba.find_by_id("6623acca3a33a2effd010dac")
    # result1 = dba.get_100_questions()
    # print(result1)
    question_dba = QuestionDBA()
    # print(question_dba.get_n_questions(100))
    new_data = [{'_id': ObjectId("66260e94a51b34b732f211dd"), 'category': 'Geography', 'subcategory': 'Medieval History', 'content': 'Phone rule we pattern be clear.', 'answers': ['why', 'east', 'nature', 'attention'], 'correct_answer': 'nature', 'difficulty': 5, 'required_rank': 5, 'language': 2, 'multimedia': ObjectId('66260e86a51b34b732f21182')}]
    new_question = [QuestionDBO.from_json_obj(data) for data in new_data]
    # question_dba.update_n_questions(new_question)
    question_dba.update_many_by_id([ObjectId("66260e94a51b34b732f211dd")], new_data)
    print()
    print(question_dba.find_by_id(ObjectId('66260e94a51b34b732f211dd')))