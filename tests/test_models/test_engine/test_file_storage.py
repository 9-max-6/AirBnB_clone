#!/usr/bin/python3
"""
test module - class Filestorage
"""
from models.base_model import BaseModel
import unittest
from models import storage
import json


class TestFileStorage(unittest.TestCase):
    """
    A class to test the storage of files by the storage object
    """
    new = BaseModel()

    def test_File(self):
        """check the presence of a file"""
        self.assertIsNotNone(storage._FileStorage__file_path)

    def test_Objects(self):
        """check the presence of a dictionary"""
        self.assertIsNotNone(storage._FileStorage__objects)

    def test_All(self):
        """ Check if the return value of the all method is dict"""
        self.assertIsInstance(storage.all(), dict)

    def test_CreationOfNewObject(self):
        """check if the newly created object is added to the dict"""
        storage.new(self.new)
        a = self.new.to_dict()["__class__"]
        b = self.new.to_dict()["id"]
        object_key = a + "." + b
        self.assertIn(object_key, storage.all())

    def test_Reload(self):
        """check if the reloaded objects has the last added object"""
        storage.new(self.new)
        a = self.new.to_dict()["__class__"]
        b = self.new.to_dict()["id"]
        object_key = a + "." + b
        storage.save()
        storage.reload()
        self.assertIn(object_key, storage.all())

    def test_Delete(self):
        """check if the deletion function works"""
        storage.new(self.new)
        a = self.new.to_dict()["__class__"]
        b = self.new.to_dict()["id"]
        object_key = a + "." + b
        storage.delete(object_key)
        self.assertNotIn(object_key, storage.all())
