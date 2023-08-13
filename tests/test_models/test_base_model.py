#!/usr/bin/env python3
"""
Unit Tests for Base Model
"""
import unittest
from models.base_model import BaseModel
import os


class TestBaseModel(unittest.TestCase):
    """
    Unit Test for Base model
    """

    def test_create(self):
        """Test if an instance can be created with proper type"""
        self.assertIsInstance(TestBaseModel.BaseModel(),
                              TestBaseModel.BaseModel)

    def test_id(self):
        """Tests if id is string."""
        tmp = TestBaseModel.BaseModel()
        self.assertEqual(str, type(tmp.id))
