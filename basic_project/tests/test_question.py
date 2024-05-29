# tests/test_question.py
import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from database.dba.question_dba import QuestionDBA

if __name__ == "__main__":
    dba = QuestionDBA()
    result = dba.find_by_id("6623acca3a33a2effd010dac")
    result1 = dba.get_100_questions()
    print(result1)
