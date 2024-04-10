#!/usr/bin/python3
"""
test module - class Filestorage
"""
from models.base_model import BaseModel
import unittest
from models import storage


class TestFileStorage(unittest.TestCase):
    """
    A class to test the storage of files by the storage object
    """
    new = BaseModel()

    def checkFile(self):
        """check the presence of a file"""
        self.assertIsNotNone(storage._FileStorage__file_path)

    def checkObjects(self):
        """check the presence of a dictionary"""
        self.assertIsNone(storage._FileStorage__objects)

    def checkAll(self):
        """ Check if the return value of the all method is dict"""
        self.assertIsInstance(storage.all(), dict)

    def checkCreationOfNewObject(self):
        """check if the newly created object is added to the dict"""
        storage.new(self.new)
        a = self.new.to_dict()["__class__"]
        b = self.new.to_dict()["id"]
        object_key = key = a + "." + b
        self.assertIn(object_key, storage.all)

    def checkReload(self):
        """check if the reloaded objects has the last added object"""
        storage.new(self.new)
        a = self.new.to_dict()["__class__"]
        b = self.new.to_dict()["id"]
        object_key = key = a + "." + b
        storage.save()
        storage.reload()
        self.assertIn(object_key, storage.all)

    def checkDelete(self):
        """check if the deletion function works"""
        storage.new(self.new)
        a = self.new.to_dict()["__class__"]
        b = self.new.to_dict()["id"]
        object_key = key = a + "." + b
        storage.delete(self.new)
        self.assertNotIn(object, storage.all)
