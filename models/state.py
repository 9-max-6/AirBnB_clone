#!/usr/bin/python3
"""module - state"""
from models.base_model import BaseModel


class State(BaseModel):
    """class to describe state"""
    name = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super.__init__()
