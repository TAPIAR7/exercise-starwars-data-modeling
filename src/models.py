import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Planets(Base):
    __tablename__ = 'planets'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    climate = Column(String(250), nullable=False)
    population = Column(String(250), nullable=False)
    orbital_period = Column(String(250), nullable=False)
    rotation_period = Column(String(250), nullable=False)
    diameter = Column(String(250), nullable=False)

class People(Base):
    __tablename__ = 'people'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    birth_year = Column(String(250), nullable=False)
    gender = Column(String(250), nullable=False)
    height = Column(String(250), nullable=False)
    skin_color = Column(String(250), nullable=False)
    eye_color = Column(String(250), nullable=False)

class Favorites(Base):
    __tablename__ = 'favorites'
    # Here we define columns for the table person
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    person = Column(Boolean, unique=True, default=False)
    planet = Column(Boolean, unique=True, default=False)
    # person = Column(Boolean, unique=False, default=False)
    # planet = Column(Boolean, unique=False, default=False)
    poeple_id = Column(Integer, ForeignKey('people.id'))
    planet_id = Column(Integer, ForeignKey('planets.id'))
    user_id = Column(Integer, ForeignKey('user.id'))

class User(Base):
    __tablename__ = 'user'
    # Here we define columns for the table address.
    # Notice that each column is also a normal Python instance attribute.
    id = Column(Integer, primary_key=True)
    email = Column(String(250))
    password = Column(String(250))
    # post_code = Column(String(250), nullable=False)
    
    # person = relationship(Person)

    # def to_dict(self):
    #     return {}

## Draw from SQLAlchemy base
render_er(Base, 'diagram.png')