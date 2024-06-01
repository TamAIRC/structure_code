# utils.py
from bson.objectid import ObjectId

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
