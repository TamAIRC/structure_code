# database/database_access/result_dba.py
from typing import List
import os
import sys
from pymongo import MongoClient
from bson import ObjectId
current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from configs import db_config
from database.database_models.question_model import QuestionDBO
from database.database_access.mongodb_dba import MongoDB_DBA

class ResultDBA:
    def __init__(self, connection):
        self.connection = connection
        self.dba = MongoDB_DBA(connection, [db_config.CONNECT['RESULT_COLLECTION'], db_config.CONNECT['QUESTION_COLLECTION']])

    def get_answered_questions_by_player_id(self, player_id):
        try:
            player_object_id = ObjectId(player_id)
            pipeline = [
                { '$match': { '_id': player_object_id } },
                { '$unwind': '$questions' },
                {
                    '$lookup': {
                        'from': 'questions',
                        'localField': 'questions._id',
                        'foreignField': '_id',
                        'as': 'questionDetails'
                    }
                },
                { '$unwind': '$questionDetails' },
                {
                    '$project': {
                        '_id': 0,
                        'playerId': '_id',
                        'questionId': '$questions._id',
                        'timestamp': '$questions.timestamp',
                        'status': '$questions.status',
                        'timeForAnswer': '$questions.timeForAnswer',
                        'difficulty': '$questions.difficulty',
                        'questionContent': '$questionDetails.content',
                        'questionCategory': '$questionDetails.category',
                        'questionSubcategory': '$questionDetails.subcategory',
                        'questionAnswers': '$questionDetails.answers',
                        'correctAnswer': '$questionDetails.correct_answer',
                        'questionDifficulty': '$questionDetails.difficulty',
                        'requiredRank': '$questionDetails.required_rank',
                        'questionLanguage': '$questionDetails.language',
                        'questionMultimedia': '$questionDetails.multimedia'
                    }
                }
            ]
            answered_question_collection = self.dba.collection[0]
            result = list(answered_question_collection.aggregate(pipeline))
            return result
        except Exception as e:
            print(f"Error fetching answered questions: {e}")
            return None
    
    
