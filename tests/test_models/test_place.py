#!/usr/bin/python3
"""test module - class place"""
import unittest
from models.place import Place
from models.base_model import BaseModel


class TestCases(unittest.TestCase):
    """
    test cases for the place class
    """
    new = Place()
    attr_list = [new.user_id, new.name, new.description, new.number_bathrooms,
                 new.latitude, new.price_by_night, new.longitude]

    def testCreation(self):
        """test the creation of the object"""
        self.assertIsInstance(self.new, Place)

    def testCreation2(self):
        """test the creation of the object"""
        self.assertIsInstance(self.new, BaseModel)

    def testName(self):
        """test the attributes of the object"""
        self.assertIsNotNone(self.new.name)

    def testUserId(self):
        """test the attributes of the object"""
        self.assertIsNotNone(self.new.user_id)

    def testAttrs(self):
        """test attributes in a list"""
        for item in self.attr_list:
            self.assertIsNotNone(item)

    def updation(self):
        """test change in date after updation"""
        current_date = self.new.created_at
        self.new.save()
        self.assertNotEqual(current_date, self.new.updated_at)

    def dynamicObjectCreation(self):
        """test the creation of dynamic objects"""
        new_dict = self.new.to_dict()
        new_object = Place(**new_dict)
        self.assertEqual(self.new, new_object)
