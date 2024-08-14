#!/usr/bin/env python3

""" Defining a model module """
from sqlalchemy import Column, String, Integer


class User(Base):
    """ Base model """
    __tablename__ = "users"
    
    id = Column(integer, primary_key=True),
    email = Column(String(250), nullable=False),
    hash_password = Column(String(250), nullable=False),
    session_id = Column(String(250)),
    reset_token = Column(string(250))
