# configs/db_config.py
CONNECT = {
    'URL': 'mongodb+srv://{username}:{password}@cluster0.jmil5cr.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0',
    'DATABASE': 'dtu',
    'QUESTION_COLLECTION': 'questions',
    'RESULT_COLLECTION': 'answered_questions'
}
USERNAME = 'root'
PASSWORD = 'Vly.19952003'
DB_TYPE = 'mongo'