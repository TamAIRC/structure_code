from bson import ObjectId
from pymongo.errors import BulkWriteError
from .dba import DBA
from utils.util import normalize_id, validate_condition, prepare_bulk_updates
from database.database_models.question_model import QuestionDBO

class MongoDB_DBA(DBA):
    def __init__(self, connection, collection_names):
        super().__init__(connection, collection_names)
        self.collections = {name: self.connection.database[name] for name in collection_names}
        if len(collection_names) == 1:
            self.collection = self.collections[collection_names[0]]
        else:
            self.collection = self.join_collections(collection_names)

    def find_by_id(self, id):
        try:
            normalized_id = normalize_id(id)
            return QuestionDBO.from_json_obj(self.collection.find_one({"_id": normalized_id}))
        except ValueError as e:
            print(e)
            return None

    def find_one(self, condition):
        try:
            validated_condition = validate_condition(condition)
            return self.collection.find_one(validated_condition)
        except ValueError as e:
            print(e)
            return None

    def find_many(self, n, condition):
        try:
            validated_condition = validate_condition(condition)
            return list(self.collection.find(validated_condition).limit(n))
        except ValueError as e:
            print(e)
            return None

    def update_one_by_id(self, document):
        try:
            normalized_id = normalize_id(document['_id'])
            new_values_dict = {key: value for key, value in document.items() if key != '_id'}
            return self.collection.update_one({"_id": normalized_id}, {"$set": new_values_dict})
        except ValueError as e:
            print(e)
            return None

    def update_many_by_id(self, ids, new_values):
        try:
            bulk_updates = prepare_bulk_updates(ids, new_values)
            return self.collection.bulk_write(bulk_updates)
        except (ValueError, BulkWriteError) as e:
            print(e)
            return None

    def join_collections(self, collection_names):
        try:
            pipeline = [
                {
                    "$lookup": {
                        "from": collection_names[1],
                        "localField": "questions._id",
                        "foreignField": "_id",
                        "as": "questions_detail"
                    }
                },
                {
                    "$unwind": "$questions_detail"
                },
                {
                    "$replaceRoot": {
                        "newRoot": {
                            "$mergeObjects": ["$$ROOT", "$questions_detail"]
                        }
                    }
                }
            ]

            local_collection_name = collection_names[0]
            joined_data = list(self.collections[local_collection_name].aggregate(pipeline))

            # Use a temporary collection to store the joined data
            self.collection = self.connection.database['joined_collection']
            self.collection.drop()  # Clear the collection if it exists
            if joined_data:
                self.collection.insert_many(joined_data)
            return self.collection
        except Exception as e:
            print(e)
            return None
