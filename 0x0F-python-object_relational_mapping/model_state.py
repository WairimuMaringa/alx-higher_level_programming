#!/usr/bin/python3
"""
Class:
    a) State.
"""
from sqlachemy import Column, Integer, String, MetaData
from sqlachemy.ext.declarative import declarative_base

mymetadata = MetaData()
Base = declarative_base(metadata=mymetadata)


class State(Base):
    """ Class:
    contains the class definition of state and base.
    """
    __tablename__ = 'states'
    id = Column(Integer, unique=True, nullable=False, primary_key=True)
    name = Column(String(128), nullable=False)
