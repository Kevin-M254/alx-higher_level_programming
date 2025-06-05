#!/usr/bin/python3
"""
    Defines a state model that contain the class definition
    of a state and an instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class State(Base):
    """
        Inherits from Base and links to MySQL table states
        class attribute id that is an integer column
        class attribute name that is a string column
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True, nullable=False, autoincrement=True)
    name = Column(String(128), nullable=False)
