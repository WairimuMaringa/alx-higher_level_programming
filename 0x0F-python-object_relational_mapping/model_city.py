#!/usr/bin/python3
"""
Class:
    a) City.
"""
from sqlalchemy import Column, Integer, String, Foreignkey
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base


class City(Base):
    """ Class:
    contains the class definition of city and base.
    """
    __tablename__ = 'cities'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
