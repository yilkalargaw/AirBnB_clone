#!/usr/bin/python3
"""Unittest module."""


import unittest
from models.review import Review
from models.base_model import BaseModel
import os

class TestState(unittest.TestCase):

    def test_instant(self):
        """Tests instantiation of state class."""

        review = Review()
        self.assertEqual(str(type(review)), "<class 'models.review.Review'>")
        self.assertIsInstance(review, Review)
        self.assertTrue(issubclass(type(Review), BaseModel))
