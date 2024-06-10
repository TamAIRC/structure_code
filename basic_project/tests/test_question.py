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
    new_data = QuestionDBO(
        category= 1, 
        subcategory= 'Medieval History', 
        content= 'Phone rule we pattern be clear.',
        answers= ['why', 'east', 'nature', 'attention'], 
        correct_answer= 'nature', 
        difficulty= 5, 
        required_rank= 5,
        language= 2,
        multimedia= ObjectId()
    )
    r = question_dba.transaction(question_dba.insert_many, objs= [new_data])
    print(r)