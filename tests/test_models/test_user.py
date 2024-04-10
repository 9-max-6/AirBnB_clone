#!/usr/bin/python3
"""
module - tests
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class UserTests(unittest.TestCase):
    """
    A class to test the user test case
    """
    new = User()

    def testCreation(self):
        """test the creation of the object"""
        self.assertIsInstance(self.new, User)

    def testCreation2(self):
        """test the creation of the object"""
        self.assertIsInstance(self.new, BaseModel)

    def testLastName(self):
        """test the attributes of the object"""
        self.assertIsNotNone(self.new.last_name)

    def testEmail(self):
        """test the attributes of the object"""
        self.assertIsNotNone(self.new.email)

    def testLastName(self):
        """test the attributes of the object"""
        self.assertIsNotNone(self.new.last_name)

    def testPassword(self):
        """test the attributes of the object"""
        self.assertIsNotNone(self.new.password)

    def testFirstName(self):
        """test the attributes of the object"""
        self.assertIsNone(self.new.last_name)
