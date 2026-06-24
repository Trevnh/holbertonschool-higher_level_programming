#!/usr/bin/python3
"""Module for City Class/Table"""

from sqlalchemy import Column, Integer, String, ForeignKey
from model_state import Base


class City(Base):
    """Class for State table"""
    __tablename__ = 'cities'

    id = Column(
        "id",
        Integer,
        primary_key=True,
        nullable=False,
        autoincrement=True
    )
    name = Column("name", String(128), nullable=False)
    state_id = Column(
        "state_id",
        Integer,
        ForeignKey("states.id"),
        nullable=False
    )
