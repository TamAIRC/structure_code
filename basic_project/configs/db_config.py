# configs/db_config.py
from configs.config import BaseSettings

__all__ = ['db_config']

class DBConfig(BaseSettings):
    URI: str
    # USERNAME: str
    # PASSWORD: str
    DATABASE: str
    QUESTION_COLLECTION: str
    
    class Config(BaseSettings.Config):
        env_prefix = "DB_"
        
db_config = DBConfig()