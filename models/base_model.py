#!/usr/bin/python3
'''module for BaseModel class
'''


from datetime import datetime
from uuid import uuid4
from . import storage

ISOFORMAT = "%Y-%m-%dT%H:%M:%S.%f"


class BaseModel:

    def __init__(self, *args, **kwargs):
        if kwargs:
            for k in kwargs:
                if k in ['created_at', 'updated_at']:
                    setattr(self, k, datetime.strptime(kwargs[k], ISOFORMAT))
                elif k != '__class__':
                    setattr(self, k, kwargs[k])

        else:
            self.id = str(uuid4())
            self.created_at = datetime.utcnow()
            self.updated_at = self.created_at.replace()
            storage.new(self)

    def save(self):

        self.updated_at = datetime.utcnow()
        storage.save()

    def to_dict(self):

        dct = self.__dict__.copy()
        dct['__class__'] = self.__class__.__name__
        dct['created_at'] = self.created_at.isoformat()
        dct['updated_at'] = self.updated_at.isoformat()
        return dct

    def __str__(self):
        """Returns a string representation of the instance"""
        cls = (str(type(self)).split('.')[-1]).split('\'')[0]
        return '[{}] ({}) {}'.format(cls, self.id, self.__dict__)
