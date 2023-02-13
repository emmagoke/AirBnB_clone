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
    _dict = {"id": "2d91cac9-712c-4358-803f-c08a41d6a777",
             "created_at": "2023-02-12T16:55:15.121756",
             "updated_at": "2023-02-12T16:55:15.121768",
             "name": "My_First_Model", "my_number": 89}

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

    def test_kwargs(self):
        """
        Testing the BaseModel Class when kwargs are pass
        """
        base = BaseModel(**self._dict)
        self._dict['__class__'] = base.__class__.__name__

        self.assertTrue(self._dict['id'], base.id)
        self.assertTrue(self._dict['created_at'], base.created_at.isoformat())
        self.assertTrue(self._dict['updated_at'], base.updated_at.isoformat())
        self.assertTrue(hasattr(base, "name"))
        self.assertEqual(base.name, self._dict['name'])
        self.assertEqual(base.to_dict(), self._dict)
