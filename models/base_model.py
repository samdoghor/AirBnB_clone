#!/usr/bin/python3
"""
Defines the BaseModel class.
It defines all common attributes/methods for other classes
"""

from datetime import datetime
import uuid
from models.engine.file_storage import FileStorage


class BaseModel:
    """
    Represents the base model for the Airbnb Clone project
    """

    def __init__(self, **kwargs):
        """
        Initialize a new BaseModel.
        Defines the attributes: id, created_at, updated_at
        :param **kwargs: Key/value pairs of arguements (dict).
        """

        self.id = str(uuid.uuid4())
        self.created_at = datetime.today()
        self.updated_at = datetime.today()

        date_formatter = "%Y-%m-%dT%H:%M:%S.%f"

        if len(kwargs) != 0:
            for k, v in kwargs.items():
                if k in ('created_at', 'updated_at'):
                    self.__dict__[k] = datetime.strptime(v, date_formatter)
                else:
                    self.__dict__[k] = v
        else:
            FileStorage.new(self)

    def __str__(self):
        """print: [<class name>] (<self.id>) <self.__dict__>"""

        return "[{}] ({}) {}".format(self.__class__.__name__,
                                     self.id, self.__dict__)

    def save(self):
        """
        Method to update public instance attribute
        'updated_at' with the current datetime
        """
        self.updated_at = datetime.now()
        FileStorage.save()

    def to_dict(self):
        """
        Method to returns a dictionary containing all
        keys/values of __dict__ of the instance.
        """
        obj_dict = self.__dict__.copy()
        obj_dict["__class__"] = self.__class__.__name__
        obj_dict["created_at"] = self.created_at.isoformat()
        obj_dict["updated_at"] = self.updated_at.isoformat()
        return obj_dict
