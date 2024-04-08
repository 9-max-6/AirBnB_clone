#!/usr/bin/python3
"""
module - a module with the class user
"""
from models import base_model


class User(base_model.BaseModel):
    """
    the user class that inherits from baseModel
    """
    email = ""
    password = ""
    first_name = ""
    last_mame = ""

    def __init__(self):
        super().__init__()
