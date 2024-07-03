import os
import sys

current_dir = os.path.dirname(__file__)
project_root = os.path.abspath(os.path.join(current_dir, "../../"))
sys.path.append(project_root)

from abc import ABC, abstractmethod
from logger.logger import Logger
from patterns.singleton_meta import SingletonABCMeta


class BaseConnection(ABC, metaclass=SingletonABCMeta):
    def __init__(self, database_name, **kwargs):
        self.client = None
        self.database = None
        self.database_name = database_name

    @abstractmethod
    def _connect(self):
        pass

    @abstractmethod
    def _test_connection(self):
        pass

    @abstractmethod
    def get_collection(self, **kwargs):
        pass

    @abstractmethod
    def close_connection(self):
        pass
