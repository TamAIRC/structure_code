import pydantic_settings
import os
BASE_PATH = os.path.dirname(__file__)


class BaseSettings(pydantic_settings.BaseSettings):
    class Config:
        env_file = os.path.abspath(os.path.join(BASE_PATH, "../.env"))
