#!/usr/bin/python3
"""city class ORM model."""

from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from model_state import Base

Base = declarative_base()


class City(Base):
    """City class definition."""
    __tablename__ = 'cities'
    id = Column(
            Integer, primary_key=True,
            autoincrement=True,
            nullable=False
        )
    name = Column(
            String(128),
            nullable=False
        )
    state_id = Column(
            Integer,
            ForeignKey('states.id'),
            nullable=False
    )
    parent = relationship("State", back_populates="cities")
