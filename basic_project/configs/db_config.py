# configs/db_config.py
from urllib.parse import quote_plus 

CONNECT = {
    'URL': '@cluster0.jmil5cr.mongodb.net',
    'DATABASE': 'dtu',
    'USER': 'admin',
    'PASSWORD': 'admin123'
}

SCHEMA = {
    'QUESTION_COLLECTION': 'questions',
}

username = quote_plus(CONNECT['USER'])
password = quote_plus(CONNECT['PASSWORD'])

CONNECT['URL'] = f'mongodb+srv://{username}:{password}{CONNECT["URL"]}'