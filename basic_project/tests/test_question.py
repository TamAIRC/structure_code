import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from controllers.question_controller import QuestionController

if __name__ == "__main__":
    question_controller = QuestionController()
    questions = question_controller.get_n_question(5)
    print(questions)