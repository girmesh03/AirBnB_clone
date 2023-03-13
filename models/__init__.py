#!/usr/bin/python3
"""This __init__ file links the BaseModel to FileStorage"""
from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
