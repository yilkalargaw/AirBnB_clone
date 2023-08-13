#!/usr/bin/python3

""" module to make an instance of filestorage"""

from models.engine.file_storage import FileStorage


storage = FileStorage()
storage.reload()
