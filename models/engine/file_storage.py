#!/usr/bin/python3
"""
"""
from models.base_model import BaseModel
import json


class FileStorage:
    """
    """
    __file_path = 'file.json'
    __objects = {}

    def all(self):
        """
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        """
        obj_name = obj.__class__.__name__
        obj_id = obj_name + '.' + obj.id
        FileStorage.__objects[obj_id] = obj

    def save(self):
        """
        """
        output = {}
        for key, value in FileStorage.__objects.items():
            output[key] = FileStorage.__objects[key].to_dict()
        with open(self.__file_path, 'w', encoding="utf-8") as f:
            f.write(json.dumps(output))

    def reload(self):
        """
        """
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                output = json.load(f)
                for key, value in output.items():
                    class_name = value.get('__class__')
                    obj = BaseModel(**value)
                    FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
