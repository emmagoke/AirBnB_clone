#!/usr/bin/python3
import uuid
from datetime import datetime
import models


class BaseModel:
    """
    """

    def __init__(self, *args, **kwargs):
        if kwargs:
            kwargs['created_at'] = datetime.fromisoformat(kwargs['created_at'])
            kwargs['updated_at'] = datetime.fromisoformat(kwargs['updated_at'])
            del kwargs['__class__']
            self.__dict__ = kwargs
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            models.storage.new(self)

    def save(self):
        """
        This method updates updated_at with the current datetime
        """
        self.updated_at = datetime.now()
        models.storage.save()

    def to_dict(self):
        """
         returns a dictionary containing all keys/values
         of __dict__ of the instance:
        """
        output = {}
        output = self.__dict__.copy()
        output['__class__'] = self.__class__.__name__
        output['created_at'] = self.created_at.isoformat()
        output['updated_at'] = self.updated_at.isoformat()
        return output

    def __str__(self):
        """
        Returns the string representation of the class
        """
        class_name = self.__class__.__name__
        return "[{}] ({}) {}".format(class_name, self.id, self.__dict__)
