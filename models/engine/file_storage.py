#!/usr/bin/python3
"""
Defines the FileStorage class.
It serializes instances to a JSON file and
deserializes JSON file to instances
"""
import json
from models.amenity import Amenity
from models.city import City
from models.place import Place
from models.review import Review
from models.state import State
from models.user import User


class FileStorage:
    """
    Represent an abstracted storage engine.

    Private class attributes:
        __file_path (str): path to the JSON file (ex: file.json)
        __objects (dict): empty but will store all objects by <class name>.id
    """
    __file_path = "file.json"
    __objects = {}

    CLASSES = {
        'User': User,
        'State': State,
        'City': City,
        'Amenity': Amenity,
        'Place': Place,
        'Review': Review
    }

    def all(self):
        """Returns the dictionary __objects."""
        return self.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id."""
        obj_class_name = obj.__class__.__name__
        key = "{}.{}".format(obj_class_name, obj.id)
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        serialized_objs = {key: obj.to_dict()
                           for key, obj in self.__objects.items()}
        with open(self.__file_path, 'w', encoding="utf-8") as file:
            json.dump(serialized_objs, file)

    def reload(self):
        """
        Deserializes the JSON file to __objects.
        Only if the JSON file (__file_path) exists; otherwise, do nothing.
        If the file doesn’t exist, no exception should be raised.
        """
        try:
            with open(self.__file_path, 'r', encoding="utf-8") as file:
                data = json.load(file)
                for key, value in data.items():
                    class_name, _ = key.split('.')
                    cls = self.CLASSES[class_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        except FileNotFoundError:
            pass
