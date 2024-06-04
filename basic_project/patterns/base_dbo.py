# patterns/base_dbo.py
from pydantic import BaseModel
from abc import ABC, abstractmethod


class BaseDBO(BaseModel, ABC):

    @abstractmethod
    def validate(self):
        pass
