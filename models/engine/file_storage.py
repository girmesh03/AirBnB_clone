#!/usr/bin/python3

import json
from models.base_model import BaseModel
from models.user import User
from models.state import State

"""
This module defines the `FileStorage` class, which is
responsible for managing the serialization and deserialization
of objects from and to a JSON file.

The `FileStorage` class provides methods to load and save objects
from a JSON file specified by the `__file_path` class attribute.
It stores objects in the `__objects` class attribute, which is a
dictionary whose keys are strings in the format "<class name>.<object id>"
and whose values are instances of classes that inherit from `BaseModel`.

The `FileStorage` class provides the following public methods:

- `all()`: returns a dictionary of all objects stored in the file storage.
- `new(obj)`: adds a new object to the file storage dictionary.
- `save()`: saves all objects from the file storage to the JSON file.
- `reload()`: loads all objects from the JSON file into the file storage.

Instances of the `FileStorage` class are typically used in conjunction with
instances of classes that inherit from `BaseModel` to implement a persistence
layer for a data model.

Example usage:

    from models import storage
    from models.user import User

    # create a new user and store it
    my_user = User()
    my_user.name = "Alice"
    storage.new(my_user)
    storage.save()

    # retrieve all users from the file storage
    all_users = storage.all().values()

Note that this implementation of `FileStorage`
is not thread-safe and is intended for use in
single-threaded applications only.
"""


class FileStorage:
    """
    This class defines a file storage system for serializing and deserializing
    objects to and from JSON format. It uses a dictionary to keep track of
    created objects and saves them to a file for persistent storage.

    Attributes:
        __file_path (str): The path to the file where objects are stored.
        __objects (dict): A dictionary containing all created objects.
    """

    # the path of the JSON file to save the objects to
    __file_path = "file.json"

    # the dictionary that stores all the objects
    __objects = {}

    def all(self):
        """
        Returns the dictionary of objects stored in the file storage.
        The file storage is nothing but a dictionary of objects.
        Which is defined in the `__objects` as a class attribute.
        __objects = {class_name.id: {key: value, key: value, ...}, ...}

        Usage:
            my_dict = storage.all()

        Returns:
            A dictionary of all objects.
        """

        # Return the dictionary of objects
        return FileStorage.__objects

    def new(self, obj):
        """
        Adds a new object to the file storage dictionary,
        using the object's class name and id as the key
        and the object itself as the value.

        Args:
            obj (Class): The object to be added to the file storage.

        Usage:
            storage.new(my_obj)
            my_obj is an instance of a class that inherits from BaseModel.

        Returns:
            None
        """
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Serializes __objects to the JSON file (path: __file_path).

        Notes:
            - Converts each object's attributes to a dictionary
            using the to_dict() method.
            - Creates a dictionary where the keys are <ClassName>.<obj.id>
            and the values are the object dictionaries.
            - Serializes the dictionary to a JSON file.

        Usage:
            storage.save()

        Returns:
            None
        """
        # Create an empty dictionary to store the serialized objects
        obj_dict = {}

        # Loop through all objects in __objects and serialize each one
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        # Serialize the dictionary to a JSON file
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(obj_dict, file, indent=2)

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

        Usage:
            storage.reload()

        Returns:
            None
        """
        try:
            # Open the JSON file and load its contents into a dictionary
            with open(FileStorage.__file_path, 'r') as file:
                obj_dict = json.load(file)
            # Iterate over each object in obj_dict and
            # create an instance of the corresponding class
            for key, obj_attrs in obj_dict.items():
                # Get the name of the class from
                # the key (format: "ClassName.id")
                class_name = key.split('.')[0]
                # Create a new object of the appropriate
                # class using the object attributes from obj_dict
                FileStorage.__objects[key] = globals()[class_name](**obj_attrs)
        except FileNotFoundError:
            # If the file doesn't exist, do nothing
            pass
