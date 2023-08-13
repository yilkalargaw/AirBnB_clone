#!/usr/bin/python3
"""Unittest module."""


import unittest
from models.place import Place
from models.base_model import BaseModel
import os

class TestState(unittest.TestCase):

    def test_instant(self):
        """Tests instantiation of Place class."""

        place = Place()
        self.assertEqual(str(type(Place)), "<class 'models.place.Place'>")
        self.assertIsInstance(place, Place)
        self.assertTrue(issubclass(type(Place), BaseModel))
