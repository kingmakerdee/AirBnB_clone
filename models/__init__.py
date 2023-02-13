#!/usr/binpython3
"""initializes the package"""
from models.engine.file_storage import FileStorage
storage = FileStorage()
storage.reload()
