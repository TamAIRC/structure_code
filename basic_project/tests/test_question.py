# tests/test_question.py
import os
import sys
from controllers.question_controller import QuestionController
# current_dir = os.path.dirname(__file__)
# project_root = os.path.abspath(os.path.join(current_dir, "../"))
# sys.path.append(project_root)
print(sys.path)
# from database.database_access.question_dba import QuestionDBA

if __name__ == "__main__":
    ques_controller = QuestionController()
    result = ques_controller.get_one_question_by_id("66260e94a51b34b732f211dd")
    # result1 = dba.get_100_questions()
    print(result)
