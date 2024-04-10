#!/usr/bin/python3
"""
module - tests
"""
import unittest
from models.base_model import BaseModel


class TestCases(unittest.TestCase):
    def test_init(self):
        test_base = BaseModel()

        self.assertIsNotNone(test_base.id)
        self.assertIsNotNone(test_base.created_at)
        self.assertIsNotNone(test_base.updated_at)

    def test_save(self):
        test_base = BaseModel()

        dummy = test_base.updated_at
        test_base.save()

        self.assertNotEqual(dummy, test_base.updated_at)

    def test_to_dict(self):
        test_base = BaseModel()

        test_base_dict = test_base.to_dict()
        self.assertIsInstance(test_base_dict, dict)
        self.assertEqual(test_base_dict["__class__"], "BaseModel")
        self.assertEqual(test_base_dict["id"], test_base.id)

    def test_str(self):
        test_base = BaseModel()

        test_base_str = str(test_base)
        self.assertNotNone(test_base_str)
