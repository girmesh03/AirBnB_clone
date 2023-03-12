#!/usr/bin/python3
"""
This is '__init__.py' module.
It's used for making the 'models' directory a package.
and it's used for creating an instance of FileStorage
and calling the reload() method on it.
"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
