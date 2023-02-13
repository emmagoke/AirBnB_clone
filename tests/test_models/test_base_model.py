#!/usr/bin/python3
"""
This module contains test cases for the BaseModel class
"""
from models.base_model import BaseModel
import unittest
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """
    Testing the BaseModel class
    """

    def test_instance(self):
        """
        Testing if instnces are different
        """
        bm1 = BaseModel()
        bm2 = BaseModel()

        self.assertNotEqual(bm1.id, bm2.id)
        self.assertIsInstance(bm1, BaseModel)

    def test_attributes(self):
        """
        This method test the attributes of BaseModel
        """
        bm3 = BaseModel()

        self.assertTrue(hasattr(bm3, "id"))
        self.assertTrue(hasattr(bm3, "created_at"))
        self.assertTrue(hasattr(bm3, "updated_at"))
        self.assertIsInstance(bm3.id, str)
        self.assertIsInstance(bm3.created_at, datetime)
        self.assertIsInstance(bm3.updated_at, datetime)
