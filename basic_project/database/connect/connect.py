import logging
from pymongo import MongoClient
from pymongo.errors import ServerSelectionTimeoutError
from configs import db_config, logging_config

# Configure logging
logging.basicConfig(
    filename= logging_config.LOGGER_FILE,
    level=logging.DEBUG,                
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',  
    datefmt='%Y-%m-%d %H:%M:%S'      
)

class Connection:
    def __init__(self):
        self.uri = db_config.CONNECT['URL']
        self.database_name = db_config.CONNECT['DATABASE']
        self.client = None
        self.database = None
    
    def connect_to_mongodb(self):
        self.client = MongoClient(self.uri)
        
        try:
            self.client.admin.command('ping')
            logging.info('Connected to MongoDB')
            self.database = self.client[self.database_name]
        except ServerSelectionTimeoutError as err:
            logging.error('MongoDB connection error: %s', err)
            self.client = None
            self.database = None
    
    def get_collection(self, collection_name):
        if self.database is not None: 
            logging.info('Accessing collection: %s', collection_name)
            return self.database[collection_name]
        else:
            logging.warning('Database not connected. Cannot access collection: %s', collection_name)
            return None
