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
