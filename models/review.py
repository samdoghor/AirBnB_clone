#!/usr/bin/python3
# Authors: Godsway and Prosper

"""Defines a class Review"""

from models.base_model import BaseModel


class Review(BaseModel):
    """Represent a Review"""

    place_id = ""
    user_id = ""
    text = ""
