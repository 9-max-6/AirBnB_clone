#!/usr/bin/python3
"""module - amenity"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """class to describe State"""
    name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super.__init__()
