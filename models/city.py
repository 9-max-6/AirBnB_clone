#!/usr/bin/python3
"""module - city"""
from models.base_model import BaseModel


class City(BaseModel):
    """class to describe city"""
    name = ""
    state_id = ""

    def __init__(self, *args, **kwargs):
        if kwargs:
            super().__init__(**kwargs)
        else:
            super().__init__()
