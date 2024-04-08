#!/usr/bin/python3
"""module - Review"""
from models.base_model import BaseModel


class City(BaseModel):
    """class to describe Review"""
    user_id = ""
    place_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super.__init__()
