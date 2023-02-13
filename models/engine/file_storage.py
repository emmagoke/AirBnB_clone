#!/usr/bin/python3
"""
This module contains the FileStorage class.
"""
from models.base_model import BaseModel
from models.user import User
import json


class_dict = {
        "BaseModel": BaseModel,
        "User": User
        }


class FileStorage:
    """
    This class serializes instances to a JSON file and deserializes
    JSON file to instances.
    Attributes:
        __file_path: string - path to the JSON file.
        __objects: dictionary - empty but will store all objects by
        <class name>.id
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects.
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        ets in __objects the obj with key <obj class name>.id
        """
        obj_name = obj.__class__.__name__
        obj_id = obj_name + '.' + obj.id
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        output = {}
        for key, value in FileStorage.__objects.items():
            output[key] = FileStorage.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(output))

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                output = json.load(f)
                for key, value in output.items():
                    class_name = value.get('__class__')
                    obj = class_dict[class_name](**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
