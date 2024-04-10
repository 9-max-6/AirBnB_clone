#!/usr/bin/python3
"""test module - class city"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCases(unittest.TestCase):
    """
    test cases for the city class
    """
    new = City()

    def testCreation(self):
        """test the creation of the object"""
        self.assertIsInstance(self.new, City)

    def testCreation2(self):
        """test the creation of the object"""
        self.assertIsInstance(self.new, BaseModel)

    def testName(self):
        """test the attributes of the object"""
        self.assertIsNotNone(self.new.name)

    def testState_Id(self):
        """test the attributes of the object"""
        self.assertIsNotNone(self.new.state_id)

    def updation(self):
        """test change in date after updation"""
        current_date = self.new.created_at
        self.new.save()
        self.assertNotEqual(current_date, self.new.updated_at)

    def dynamicObjectCreation(self):
        """test the creation of dynamic objects"""
        new_dict = self.new.to_dict()
        new_object = City(**new_dict)
        self.assertEqual(self.new, new_object)
