#!/usr/bin/python3
"""This module defines the Amenity class."""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity class that inherits from BaseModel."""
    name = ""

    def __init__(self, *args, **kwargs):
        """Initializes Amenity class."""
        super().__init__(*args, **kwargs)
