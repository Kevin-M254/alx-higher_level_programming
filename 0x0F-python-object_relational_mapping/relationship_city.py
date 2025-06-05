#!/usr/bin/python3
"""
  Defines a City model that contains class definition of a City
  and an instance Base
"""
from sqlalchemy import Column, Integer, String, ForeignKey, null
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):
    """
      Inherits form model_state Base
      class attributes id, name, state_id which is foreign key
      to states.id
    """

    __tablename__ = "cities"
    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
