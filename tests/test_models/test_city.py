#!/usr/bin/python3
"""Unittest module."""


import unittest
from models.city import City
from models.base_model import BaseModel
import os


class TestCity(unittest.TestCase):

    def test_instant(self):
        """Tests instantiation of City class."""

        city = City()
        self.assertEqual(str(type(city)), "<class 'models.city.City'>")
        self.assertIsInstance(city, City)
        self.assertTrue(issubclass(type(city), BaseModel))
