#!/usr/bin/python3
"""state class ORM model."""

from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.orm import registry

Base = declarative_base()


class State(Base):
    """State class definition."""
    __tablename__ = 'states'
    id = Column(
            Integer, primary_key=True,
            autoincrement=True,
            nullable=False
        )
    name = Column(
            String(128),
            nullable=False
        )
    cities = relationship("City", back_populates="parent")
