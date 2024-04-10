#!/usr/bin/python3
"""test module - class review"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestCases(unittest.TestCase):
    """
    test cases for the review class
    """
    new = Review()
    attr_list = [new.user_id, new.place_id, new.text]

    def testCreation(self):
        """test the creation of the object"""
        self.assertIsInstance(self.new, Review)

    def testCreation2(self):
        """test the creation of the object"""
        self.assertIsInstance(self.new, BaseModel)

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
        new_object = Review(**new_dict)
        self.assertEqual(self.new, new_object)
