#!/usr/bin/python3

# Import necessary modules
import uuid  # For generating unique ids
from datetime import datetime  # For handling timestamps
import models  # For storage functionality


"""
This module defines a base model class for creating
objects with unique ids, timestamps, and storage functionality.
"""


class BaseModel:
    """
    This class defines a base model for creating objects with unique ids,
    timestamps, and storage functionality.

    Attributes:
        id (str): The unique identifier of the instance.
        created_at (datetime): Instance creation time.
        updated_at (datetime): Instance last update time.
    """

    def __init__(self, *args, **kwargs):
        """
        Initializes a new instance of the BaseModel class.

        Args:
            *args: Variable-length argument list.
            **kwargs: Arbitrary keyword arguments.
        """
        # Check for keyword arguments.
        if kwargs:
            # Set id attribute to a UUID if it doesn't exist.
            if 'id' not in kwargs:
                self.id = str(uuid.uuid4())
            else:
                self.id = kwargs['id']
                if not isinstance(self.id, str):
                    self.id = str(self.id)

            # Set created_at and updated_at attributes if they exist.

            # Set all other keyword arguments as object attributes.
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                if key == 'created_at' or key == 'updated_at':
                    value = datetime.strptime(value, '%Y-%m-%dT%H:%M:%S.%f')
                    setattr(self, key, value)
        else:
            # Set id attribute to a UUID and created_at
            # and updated_at to current datetime.
            self.id = str(uuid.uuid4())
            self.created_at = self.updated_at = datetime.now()
            # Save new instance to storage.
            models.storage.new(self)

    def __str__(self):
        """
        Returns a string representation of the instance.

        Usage:
            print(my_instance)

        Returns:
            A string with the format '[ClassName] (id) {attributes}'.
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__, self.id, self.__dict__
        )

    def save(self):
        """
        Updates the instance's `updated_at` attribute with the
        current date and time and saves the changes to the storage.

        Usage:
            my_instance.save()

        Returns:
            None
        """
        # Update the updated_at attribute
        self.updated_at = datetime.now()
        # Save the changes to storage
        models.storage.save()

    def to_dict(self):
        """
        Returns a dictionary representation of the instance's attributes.

        Usage:
        my_dict = my_instance.to_dict()

        Returns:
        A dictionary with the keys 'id', 'created_at', 'updated_at', and
        '__class__' that correspond to the instance's attributes.
        """
        # Create a copy of the instance's dict
        dict_copy = self.__dict__.copy()
        # Add the class name
        dict_copy["__class__"] = self.__class__.__name__
        # Convert created_at to ISO format
        dict_copy["created_at"] = self.created_at.isoformat()
        dict_copy["updated_at"] = self.updated_at.isoformat()
        # Return the dictionary representation of the instance
        return dict_copy
