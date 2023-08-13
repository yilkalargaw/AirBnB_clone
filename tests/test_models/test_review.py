#!/usr/bin/python3
"""Unittest module."""


import unittest
from models.state import State
from models.base_model import BaseModel
import os

class TestState(unittest.TestCase):

    def test_instant(self):
        """Tests instantiation of state class."""

        state = State()
        self.assertEqual(str(type(state)), "<class 'models.state.State'>")
        self.assertIsInstance(state, State)
        self.assertTrue(issubclass(type(State), BaseModel))
