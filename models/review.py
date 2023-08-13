#!/usr/bin/python3
"""Module for State class."""

from models.base_model import BaseModel


class Review(BaseModel):
    """Class representing a State. and inherits from basemodel"""
    text = ""
    user_id = ""
    place_id = ""
