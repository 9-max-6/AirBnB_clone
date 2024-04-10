#!/usr/bin/python3
"""test module - class amenity"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestCases(unittest.TestCase):
    """
    test cases for the amenity class
    """
    new = Amenity()

    def testCreation(self):
        """test the creation of the object"""
        self.assertIsInstance(self.new, Amenity)

    def testCreation2(self):
        """test the creation of the object"""
        self.assertIsInstance(self.new, BaseModel)

    def testName(self):
        """test the attributes of the object"""
        self.assertIsNotNone(self.new.name)

    def updation(self):
        """test change in date after updation"""
        current_date = self.new.created_at
        self.new.save()
        self.assertNotEqual(current_date, self.new.updated_at)
