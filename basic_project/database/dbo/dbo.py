import os
import sys
from pydantic import BaseModel
from abc import ABC, abstractmethod

class DBO(BaseModel, ABC):

    @abstractmethod
    def do_something(self):
        pass