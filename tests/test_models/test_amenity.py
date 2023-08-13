#!/usr/bin/python3
"""Unittest module."""


import unittest
from models.amenity import Amenity
from models.base_model import BaseModel
import os

class TestState(unittest.TestCase):

    def test_instant(self):
        """Tests instantiation of Amenity class."""

        amenity = Amenity()
        self.assertEqual(str(type(amenity)), "<class 'models.amenity.Amenity'>")
        self.assertIsInstance(amenity, Amenity)
        self.assertTrue(issubclass(type(Amenity), BaseModel))
