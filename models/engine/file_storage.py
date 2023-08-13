#!/usr/bin/python3
"""
A class to deal with serializing and deserializing JSON data
"""
import json
import os
from models.base_model import BaseModel
from models.user import User
from models.city import City
from models.place import Place
from models.state import State
from models.review import Review
from models.amenity import Amenity


class FileStorage:
    """
    A class to save and read  files stored in a serialized JSON format
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """
        returns the dictionary __objects
        """
        return FileStorage.__objects

    def new(self, obj):
        """
        sets in __objects the obj with key <obj class name>.id
        """
        joined_obj_symbol = ''.join([obj.__class__.__name__, ".", obj.id])
        FileStorage.__objects[joined_obj_symbol] = obj

    def save(self):
        """
        serializes __objects to the JSON file (path: __file_path)
        """
        tmp_dict = {}

        for k, v in self.__objects.items():
            tmp_dict[k] = v.to_dict()

        with open(FileStorage.__file_path, "w") as to_file:
            json.dump(tmp_dict, to_file)

    def reload(self):
        """
        deserializes the JSON file to __objects (only if the JSON file
        (__file_path) exists ; otherwise, do nothing. If the file doesn’t
        exist, no exception should be raised)
        """
        hbnb_class_map = {
            'BaseModel': BaseModel,
            'User': User,
            'Place': Place,
            'State': State,
            'City': City,
            'Amenity': Amenity,
            'Review': Review,
        }

        try:
            with open(self.__file_path, "r") as ffile:
                js = json.load(ffile)
                for k, v in js.items():
                    self.__objects[k] = hbnb_class_map[v["__class__"]](**v)
        except Exception:
            pass
