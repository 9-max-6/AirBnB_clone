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
    last_name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(*args, **kwargs)
        else:
            super().__init__()
