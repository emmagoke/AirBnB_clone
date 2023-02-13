#!/usr/bin/python3
"""
This models contains the user class that
inherits from the BaseModel class
"""
from .base_model import BaseModel


class User(BaseModel):
    """
    User Class
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
