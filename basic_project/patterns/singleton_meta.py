# singleton_meta.py
from abc import ABCMeta


class SingletonMeta(type):
    """
    A Singleton metaclass. All classes that use this metaclass will follow the Singleton pattern.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance
        return cls._instances[cls]

    def _remove_instance(cls):
        if cls in cls._instances:
            del cls._instances[cls]


class SingletonABCMeta(SingletonMeta, ABCMeta):
    """
    A metaclass that combines SingletonMeta and ABCMeta.
    """

    pass
