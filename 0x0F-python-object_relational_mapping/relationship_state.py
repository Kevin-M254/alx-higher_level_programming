#!/usr/bin/python3
"""
    Defines a state model that contain the class definition
    of a state and an instance Base
"""

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from relationship_city import Base, City


class State(Base):
    """
      Attributes:
        __tablename__ (str):  Name of the MySQL table
        id (Integer): The state's id.
        name (String): The state's name.
        cities (relationship): The State-City relationship.
    """
    __tablename__ = "states"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)

    cities = relationship("City", backref="state", cascade="all, delete")
