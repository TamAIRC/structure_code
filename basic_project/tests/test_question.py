# tests/test_question.py
import os
import sys

# Setting up the environment to import from the project root
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../"))
sys.path.append(project_root)

from database.dbo.question_dbo import QuestionDBO
from database.dba.question_dba import QuestionDBA
import pytest
from bson import ObjectId
from unittest.mock import patch

# Auto test: https://semaphoreci.com/community/tutorials/testing-python-applications-with-pytest
# Use a Testing Framework: Instead of running tests through manual input, consider using a testing framework like pytest. This allows for better test organization and automated testing.
# Assertions: Use assertions to validate the expected outcomes.
# Mocking Database Calls: When testing QuestionDBA, mock the database calls to avoid dependency on the actual database.
# Remove Print Statements: Instead of printing, use assertions to verify the results.

# sample_data: Dữ liệu mẫu để tạo ra một đối tượng QuestionDBO và sử dụng trong các test case.
sample_data = {
    # "_id": ObjectId("6623acca3a33a2effd010dac"),
    "_id": ObjectId(),
    "category": "Geography",
    "subcategory": "History",
    "content": "Sample Question",
    "answers": ["answer1", "answer2", "answer3", "answer4"],
    "correct_answer": "answer1",
    "difficulty": 3,
    "required_rank": 2,
    "language": 1,
    "multimedia": ObjectId(),
}

# sample_question: Một đối tượng QuestionDBO được khởi tạo từ sample_data để sử dụng trong các assertions.
sample_question = QuestionDBO(
    _id=sample_data["_id"],
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
    assert document_instance.id == sample_data["_id"]
    assert document_instance.category == sample_data["category"]
    assert document_instance.subcategory == sample_data["subcategory"]
    assert document_instance.content == sample_data["content"]
    assert document_instance.answers == sample_data["answers"]
    assert document_instance.correct_answer == sample_data["correct_answer"]
    assert document_instance.difficulty == sample_data["difficulty"]
    assert document_instance.required_rank == sample_data["required_rank"]
    assert document_instance.language == sample_data["language"]
    assert document_instance.multimedia == sample_data["multimedia"]


@patch("database.dba.question_dba.QuestionDBA.find_by_id")
@patch("database.dba.question_dba.QuestionDBA.get_questions")
def test_QuestionDBA(mock_get_100_questions, mock_find_by_id):
    # Setup mock return values
    mock_find_by_id.return_value = sample_question
    mock_get_100_questions.return_value = [sample_question]

    question_dba = QuestionDBA()

    # Test find_by_id
    result = question_dba.transaction(
        question_dba.find_by_id, id=ObjectId("6623acca3a33a2effd010dac")
    )
    action_test = "find_by_id"
    print(action_test.center(10, "*"))
    print(result)
    assert result == sample_question

    # Test get_questions - 100
    result1 = question_dba.transaction(question_dba.get_questions, n=100)
    print("get_questions".center(10, "*"))
    print(result1[0])
    assert result1 == [sample_question]
    id_test = ""
    print("=====================")
    # Test insert
    with patch("database.dba.question_dba.QuestionDBA.insert") as mock_insert:
        mock_insert.return_value = sample_data["_id"]
        id_test = question_dba.transaction(question_dba.insert, obj=sample_question)
        print("insert", id_test)
        assert id_test == sample_data["_id"]

    print("=====================")
    # Test insert_many
    with patch("database.dba.question_dba.QuestionDBA.insert_many") as mock_insert_many:
        mock_insert_many.return_value = [id_test]
        result = question_dba.transaction(
            question_dba.insert_many, objs=[sample_question]
        )
        print("insert_many".center(10, "*"))
        print(result)
        assert result == [id_test]
    print("=====================")

    # Test update_one_by_id
    with patch(
        "database.dba.question_dba.QuestionDBA.update_one_by_id"
    ) as mock_update_one:
        mock_update_one.return_value = True
        result = question_dba.transaction(
            question_dba.update_one_by_id,
            id=id_test,
            new_value={"content": "Updated Question"},
        )
        print("update_one_by_id".center(10, "*"))
        print(result)
        assert result == True
    print("=====================")

    # Test update_many_by_id
    with patch(
        "database.dba.question_dba.QuestionDBA.update_many_by_id"
    ) as mock_update_many:
        mock_update_many.return_value = True
        result = question_dba.transaction(
            question_dba.update_many_by_id,
            ids=id_test,
            new_values=[{"content": "Updated Question"}],
        )
        print("update_many_by_id".center(10, "*"))
        print(result)
        assert result == True
    print("=====================")

    # Test find_one
    with patch("database.dba.question_dba.QuestionDBA.find_one") as mock_find_one:
        mock_find_one.return_value = sample_question
        result = question_dba.transaction(
            question_dba.find_one, condition={"category": "Geography"}
        )
        print(result)
        assert result == sample_question
    print("=====================")

    # Test find_many
    with patch("database.dba.question_dba.QuestionDBA.find_many") as mock_find_many:
        mock_find_many.return_value = [sample_question]
        result = question_dba.transaction(
            question_dba.find_many, n=1, condition={"category": "Geography"}
        )
        print("find_many".center(10, "*"))
        print(result)
        assert result == [sample_question]
    print("=====================")

    # Test delete_by_id
    with patch("database.dba.question_dba.QuestionDBA.delete_by_id") as mock_delete:
        mock_delete.return_value = True
        result = question_dba.transaction(question_dba.delete_by_id, id=id_test)
        print("delete_by_id".center(10, "*"))
        print(result)
        assert result == True


if __name__ == "__main__":

    test_QuestionDBO()
    test_QuestionDBA()

    # Pytest
    # pytest.main()
