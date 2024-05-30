from bson.objectid import ObjectId


def normalize_id(id):
    """
    Convert a string ID to a BSON ObjectId.

    Parameters:
    - id: str or ObjectId

    Returns:
    - ObjectId
    """
    if isinstance(id, ObjectId):
        return id
    try:
        return ObjectId(id)
    except Exception as e:
        raise ValueError(f"Invalid ID format: {id}") from e


def validate_condition(condition):
    """
    Ensure the condition is a dictionary suitable for MongoDB queries.

    Parameters:
    - condition: dict

    Returns:
    - dict
    """
    if not isinstance(condition, dict):
        raise ValueError("Condition must be a dictionary")
    return condition


def prepare_bulk_updates(ids, new_values):
    """
    Prepare a list of bulk update operations.

    Parameters:
    - ids: list of str or ObjectId
    - new_values: list of dict

    Returns:
    - list of dict
    """
    if len(ids) != len(new_values):
        raise ValueError("The length of ids and new_values must match")

    bulk_updates = []
    for id, new_value in zip(ids, new_values):
        try:
            normalized_id = normalize_id(id)
            bulk_updates.append(
                {
                    "updateOne": {
                        "filter": {"_id": normalized_id},
                        "update": {"$set": new_value},
                    }
                }
            )
        except ValueError as e:
            raise ValueError(f"Error processing ID {id}: {e}") from e

    return bulk_updates


def serialize_object_id(data):
    """
    Recursively convert ObjectId in a dictionary to string.

    Parameters:
    - data: dict or list

    Returns:
    - dict or list
    """
    if isinstance(data, dict):
        return {
            k: str(v) if isinstance(v, ObjectId) else serialize_object_id(v)
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [
            str(item) if isinstance(item, ObjectId) else serialize_object_id(item)
            for item in data
        ]
    return data


def deserialize_object_id(data):
    """
    Recursively convert string representations of ObjectId in a dictionary back to ObjectId.

    Parameters:
    - data: dict or list

    Returns:
    - dict or list
    """
    if isinstance(data, dict):
        return {
            k: (
                ObjectId(v)
                if isinstance(v, str) and ObjectId.is_valid(v)
                else deserialize_object_id(v)
            )
            for k, v in data.items()
        }
    elif isinstance(data, list):
        return [
            (
                ObjectId(item)
                if isinstance(item, str) and ObjectId.is_valid(item)
                else deserialize_object_id(item)
            )
            for item in data
        ]
    return data


def check_required_fields(data, required_fields):
    """
    Ensure that the dictionary contains the required fields.

    Parameters:
    - data: dict
    - required_fields: list of str

    Returns:
    - bool
    """
    missing_fields = [field for field in required_fields if field not in data]
    if missing_fields:
        raise ValueError(f"Missing required fields: {', '.join(missing_fields)}")
    return True


def build_projection(fields):
    """
    Build a MongoDB projection document from a list of fields.

    Parameters:
    - fields: list of str

    Returns:
    - dict
    """
    return {field: 1 for field in fields}


if __name__ == "__main__":
    # Example usage of the utils functions

    # Normalize ID
    print("Example Normalize ID")
    try:
        normalized_id = normalize_id("60b8d295f1d2d21f3cde30f1")
        print(f"Normalized ID: {normalized_id}")
    except ValueError as e:
        print(e)

    # Validate condition
    print("Example Validate condition")
    try:
        condition = validate_condition({"category": 1})
        print(f"Validated condition: {condition}")
    except ValueError as e:
        print(e)

    # Prepare bulk updates
    print("Prepare bulk updates")
    try:
        bulk_updates = prepare_bulk_updates(
            ["60b8d295f1d2d21f3cde30f1", "60b8d295f1d2d21f3cde30f2"],
            [{"content": "New content 1"}, {"content": "New content 2"}],
        )
        print(f"Bulk updates: {bulk_updates}")
    except ValueError as e:
        print(e)

    # Serialize ObjectId
    print("Serialize ObjectId")
    data = {"_id": ObjectId("60b8d295f1d2d21f3cde30f1")}
    serialized_data = serialize_object_id(data)
    print(f"Serialized data: {serialized_data}")

    # Deserialize ObjectId
    print("Deserialize ObjectId")
    deserialized_data = deserialize_object_id(serialized_data)
    print(f"Deserialized data: {deserialized_data}")

    # Check required fields
    print("Check required fields")
    try:
        check_required_fields(data, ["_id", "content"])
    except ValueError as e:
        print(e)

    # Build projection
    projection = build_projection(["_id", "content"])
    print(f"Projection: {projection}")
