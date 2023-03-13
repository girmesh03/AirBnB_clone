#!/usr/bin/python3
"""This module contains the FileStorage class"""

import json
import os
from models.base_model import BaseModel


class FileStorage:
    """FileStorage class is responsible for serializing and deserializing
    instances to and from JSON file. It has the following public instance
    attributes:
        __file_path: path to the JSON file
        __objects: empty dictionary
    And the following public instance methods:
        all(): returns the dictionary __objects
        new(obj): sets in __objects the obj with key <obj class name>.id
        save(): serializes __objects to the JSON file
        reload(): deserializes the JSON file to __objects
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
        Loads all objects from the file storage.
        This method reads the contents of the JSON file
        specified in the `__file_path` attribute and creates
        instances of the corresponding classes for each
        object found in the file. Each object is then added to
        the dictionary of objects stored in the `__objects`
        attribute, with the object's ID and class name used
        as the dictionary key.

        If the file specified in the `__file_path`
        attribute does not exist or cannot be read,
        this method does nothing.
        """
        if os.path.exists(FileStorage.__file_path):
            with open(FileStorage.__file_path, "r") as f:
                new_dict = json.load(f)
            for key, obj in new_dict.items():
                class_name = key.split(".")
                FileStorage.__objects[key] = globals()[class_name[0]](**obj)
