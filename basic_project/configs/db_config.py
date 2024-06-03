# config.py
from urllib.parse import quote_plus

DB_TYPE = "mongo"

# Connection details
CONNECT = {
    "mongo": {
        "URL": "cluster0.jmil5cr.mongodb.net",
        "DATABASE": "dtu",
        "USER": "admin",
        "PASSWORD": "admin123",
    },
    "mysql": {
        "HOST": "localhost",
        "DATABASE": "mydb",
        "USER": "root",
        "PASSWORD": "password",
    },
    "sqlserver": {
        "HOST": "localhost",
        "DATABASE": "mydb",
        "USER": "sa",
        "PASSWORD": "password",
    },
    "postgresql": {
        "HOST": "localhost",
        "DATABASE": "mydb",
        "USER": "postgres",
        "PASSWORD": "password",
    },
}

# URL encode the username and password for MongoDB
username = quote_plus(CONNECT["mongo"]["USER"])
password = quote_plus(CONNECT["mongo"]["PASSWORD"])
CONNECT["mongo"][
    "URL"
] = f"mongodb+srv://{username}:{password}@{CONNECT['mongo']['URL']}"

SCHEMA = {
    "QUESTIONS": "questions",
    "USER": "user",
    "ANSWERED_QUESTIONS": "answered_questions",
}
