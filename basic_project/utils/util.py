# utils.py
from bson.objectid import ObjectId
import json

def validate_input(data):
    """Validate that the input is a JSON object with an 'input' key."""
    try:
        # Ensure data is a dictionary and has an 'input' key
        if not isinstance(data, dict):
            data = json.loads(data)
        if "input" not in data:
            raise ValueError("The JSON object must contain an 'input' key")
        return data["input"]
    except (ValueError, json.JSONDecodeError) as e:
        raise ValueError(f"Error validating input: {data}") from e
def toString(id):
    """Convert an ObjectId to  a string"""
    try:
        return str(id)
    except Exception as e:
        raise ValueError(f"Invalid ID format: {id}") from e
def normalize_id(id):
    """Convert a string ID to a BSON ObjectId."""
    try:
        return ObjectId(id)
    except Exception as e:
        raise ValueError(f"Invalid ID format: {id}") from e

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
