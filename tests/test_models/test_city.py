#!/usr/bin/python3
"""Unittest module."""


import unittest
from models.city import City
from models.base_model import BaseModel
import os

class TestCity(unittest.TestCase):

    def test_instant(self):
        """Tests instantiation of City class."""

        b = City()
        self.assertEqual(str(type(b)), "<class 'models.city.City'>")
        self.assertIsInstance(b, City)
        self.assertTrue(issubclass(type(b), BaseModel))
