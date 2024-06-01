from urllib.parse import quote_plus

# Connection details
CONNECT = {
    "URL": "cluster0.jmil5cr.mongodb.net",
    "DATABASE": "dtu",
    "USER": "admin",
    "PASSWORD": "admin123",
}

# URL encode the username and password
username = quote_plus(CONNECT["USER"])
password = quote_plus(CONNECT["PASSWORD"])

# Creating the connection string
CONNECT["URL"] = f"mongodb+srv://{username}:{password}@{CONNECT['URL']}"

SCHEMA = {
    "QUESTIONS": "questions",
    "USER": "user",
    "ANSWERED_QUESTIONS": "answered_questions",
}
