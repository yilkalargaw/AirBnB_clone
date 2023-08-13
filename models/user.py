#!/usr/bin/python3

""" This is the user module"""

from models.base_model import BaseModel


class User(BaseModel):

    """ User class that inherits """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
