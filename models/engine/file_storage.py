#!/usr/bin/python3
"""This module contains the FileStorage class"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class is responsible for serializing and deserializing
    instances to and from JSON file.
    """

    __file_path = "file.json"
    __objects = {}

    def all(self):
        """returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """serializes __objects to the JSON file"""
        new_dict = {}
        for key, value in FileStorage.__objects.items():
            new_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, "w") as f:
            json.dump(new_dict, f)

    def reload(self):
        """
        deserializes the JSON file to __objects
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
            for key, obj in new_dict.items():
                class_name = key.split(".")
                FileStorage.__objects[key] = globals()[class_name[0]](**obj)
