#!/usr/bin/python3
"""
This models contains the City class that
inherits from the BaseModel class
"""
from .base_model import BaseModel


class City(BaseModel):
    """
    The City class
    attributes:
        state_id: string - empty string: it will be the State.id
        name: string - empty string
    """
    state_id = ""
    name = ""
