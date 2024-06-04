# utils.py
from bson.objectid import ObjectId
from typing import Any, Dict, Union


def normalize_id(id):
    """Convert a string ID to a BSON ObjectId."""
    try:
        return ObjectId(id)
    except Exception as e:
        raise ValueError(f"Invalid ID format: {id}") from e


def serialize_mongo_document(document: Any) -> Any:
    """Recursively convert MongoDB document ObjectId fields to string."""
    if isinstance(document, dict):
        return {key: serialize_mongo_document(value) for key, value in document.items()}
    elif isinstance(document, list):
        return [serialize_mongo_document(item) for item in document]
    elif isinstance(document, ObjectId):
        return str(document)
    else:
        return document


def compare_documents(doc1, doc2):
    """_summary_

    Args:
        doc1 (dict): document 1
        doc2 (dict): document 2

    Returns:
        boolean: match or not
    """
    if isinstance(doc1, dict) and isinstance(doc2, dict):
        if doc1.keys() != doc2.keys():
            return False
        for key in doc1:
            if not compare_documents(doc1[key], doc2[key]):
                return False
        return True
    elif isinstance(doc1, list) and isinstance(doc2, list):
        if len(doc1) != len(doc2):
            return False
        for item1, item2 in zip(doc1, doc2):
            if not compare_documents(item1, item2):
                return False
        return True
    else:
        return doc1 == doc2


def validate_condition(condition):
    """Ensure the condition is a dictionary suitable for MongoDB queries."""
    if not isinstance(condition, dict):
        raise ValueError("Condition must be a dictionary")
    return condition


def prepare_bulk_updates(ids, new_values):
    """Prepare a list of bulk update operations."""
    if len(ids) != len(new_values):
        raise ValueError("The length of ids and new_values must match")

    bulk_updates = []
    for id, new_value in zip(ids, new_values):
        try:
            bulk_updates.append({
                "updateOne": {
                    "filter": {"_id": normalize_id(id)},
                    "update": {"$set": new_value}
                }
            })
        except ValueError as e:
            raise ValueError(f"Error processing ID {id}: {e}") from e

    return bulk_updates
