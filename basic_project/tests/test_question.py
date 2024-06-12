# tests/test_question.py
import os
import sys

from bson import ObjectId

# Setting up the environment to import from the project root
# Setting up the environment to import from the project root
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from database.dbo.question_dbo import QuestionDBO
from database.dba.question_dba import QuestionDBA

from bson import ObjectId

# Auto test: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
# Use a Testing Framework: Instead of running tests through manual input, consider using a testing framework like pytest. This allows for better test organization and automated testing.
# Assertions: Use assertions to validate the expected outcomes.
# Mocking Database Calls: When testing QuestionDBA, mock the database calls to avoid dependency on the actual database.
# Remove Print Statements: Instead of printing, use assertions to verify the results.

# sample_data: Dữ liệu mẫu để tạo ra một đối tượng QuestionDBO và sử dụng trong các test case.
sample_data = {
    # "_id": ObjectId("6623acca3a33a2effd010dac"),
    "category": "CMath",
    "subcategory": "Math",
    "content": "1 + 1 bằng mấy?",
    "answers": ["answer1", "answer2", "answer3", "answer4"],
    "correct_answer": "answer1",
    "difficulty": 3,
    "required_rank": 2,
    "language": 1,
    "multimedia": ObjectId(),
}

# sample_question: Một đối tượng QuestionDBO được khởi tạo từ sample_data để sử dụng trong các assertions.
sample_question = QuestionDBO(
    category=sample_data["category"],
    subcategory=sample_data["subcategory"],
    content=sample_data["content"],
    answers=sample_data["answers"],
    correct_answer=sample_data["correct_answer"],
    difficulty=sample_data["difficulty"],
    required_rank=sample_data["required_rank"],
    language=sample_data["language"],
    multimedia=sample_data["multimedia"],
)


def test_QuestionDBO():
    # Create an instance of the Document model
    document_instance = QuestionDBO(**sample_data)

    # Assertions to validate the instance
    assert document_instance.category == sample_data["category"]
    assert document_instance.subcategory == sample_data["subcategory"]
    assert document_instance.content == sample_data["content"]
    assert document_instance.answers == sample_data["answers"]
    assert document_instance.correct_answer == sample_data["correct_answer"]
    assert document_instance.difficulty == sample_data["difficulty"]
    assert document_instance.required_rank == sample_data["required_rank"]
    assert document_instance.language == sample_data["language"]
    assert document_instance.multimedia == sample_data["multimedia"]


def test_QuestionDBA():
    question_dba = QuestionDBA()
    print("sample_question", sample_question)
    print("=====================")

    # # Test get_questions - 100
    # result1 = question_dba.transaction(question_dba.get_questions, n=10)
    # print("get_questions")
    # # Sử dụng to_json để đảm bảo ObjectId được tuần tự hóa đúng cách
    # new_values = [question.to_json() for question in result1]
    # print(new_values)

    # print("=====================")

    id_test = ObjectId("66260e94a51b34b732f211ee")

    # Test insert
    # id_test = question_dba.insert_one(obj=sample_question)
    # print("insert", id_test)

    # print("=====================")

    # # Test find_by_id
    # result = question_dba.find_by_id(
    #     ObjectId(id_test)
    # )
    # print("find_by_id")
    # print(result)
    # print("=====================")

    # # Test insert_many
    # result = question_dba.insert_many(objs=[sample_question])
    # print("insert_many")
    # print(result)
    # print("=====================")

    # # Test update_one_by_id
    # result = question_dba.update_by_id(
    #     id=id_test,
    #     new_value={"content": "Updated Question"},
    # )
    # print("update_one_by_id")
    # print(result)
    # print("=====================")

    # Test update_many_by_id
    # result = question_dba.update_by_ids(
    #     ids=[id_test],
    #     new_values=[{"content": "Updated Question"}],
    # )
    # print("update_many_by_id")
    # print(result)
    # print("=====================")
    result = question_dba.update_many(
        {"_id": id_test},
        new_values={"content": "Updated Question"}
    )
    print("update_many")
    print(result)
    print("=====================")
    # Test find_one
    print("find_one")
    result = question_dba.find_one(
        condition={"category": "Geography"}
    )
    print(result)
    print("=====================")

    # Test find_many
    print("find_many")
    result = question_dba.find_many(
        condition={"category": "Geography"}, n=1
    )
    print(result)
    print("=====================")

    # # Test delete_by_id
    # print("delete_by_id")
    # result = question_dba.delete_by_id(id=id_test)
    # print(result)
    
    # Delete questions
    # delete_data = ["66260e94a51b34b732f211df", "66260e94a51b34b732f211e0"]
    # delete_data_obj = [normalize_id(data) for data in delete_data]
    # print(delete_data_obj)
    # deleted_status = question_dba.transaction(
    #     question_dba.delete_questions, ids=delete_data
    # )
    # print("Deleted status: ", deleted_status)


if __name__ == "__main__":

    # test_QuestionDBO()
    test_QuestionDBA()
