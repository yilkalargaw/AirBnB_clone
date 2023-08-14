#!/usr/bin/python3
"""Module for Base class"""


import uuid
from datetime import datetime

class BaseModel:
    """Base class that will be inherited later"""

    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
                date_format = "%Y-%m-%dT%H:%M:%S.%f"
                if key == 'created_at' or key == 'updated at':
                    value = datetime.strptime(value, date_format)
                    setattr(self, key, value)
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            from models import storage
            storage.new(self)

    def __str__(self):
        """Returns a human-readable string representation"""
        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """Updates current datetime."""
        self.updated_at = datetime.now()
        from models import storage
        storage.save()


    def to_dict(self):
        """Returns a dictionary representation of an instance."""
        dic = self.__dict__.copy()
        dic['__class__'] = self.__class__.__name__
        dic['created_at'] = self.created_at.isoformat()
        dic['updated_at'] = self.updated_at.isoformat()
        return dic
