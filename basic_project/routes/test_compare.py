doc1 = {
    "_id": {
        "$oid": "66260e94a51b34b732f211dd"
    },
    "category": "Geography",
    "subcategory": "Medieval History",
    "content": "Phone rule we pattern be clear.",
    "answers": [
        "why",
        "east",
        "nature",
        "attention"
    ],
    "correct_answer": "nature",
    "difficulty": 5,
    "required_rank": 5,
    "language": 2,
    "multimedia": "66260e86a51b34b732f21182"
}

doc2 = {
    "_id": {
        "$oid": "66260e94a51b34b732f211dd"
    },
    "category": "Geography",
    "subcategory": "Medieval History",
    "content": "Phone rule we pattern be clear.",
    "answers": [
        "why",
        "east",
        "nature",
        "attention"
    ],
    "correct_answer": "nature",
    "difficulty": 5,
    "required_rank": 5,
    "language": 2,
    "multimedia": "66260e86a51b34b732f21182"
}


def compare_documents(doc1, doc2):
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


if __name__ == "__main__":
    print(doc1.values())
    # if not compare_documents(doc1, doc2):
    #     print(False)
    # else:
    #     print(True)
