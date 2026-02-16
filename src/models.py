from sqlalchemy import Column, ForeignKey, Integer, String, Boolean
from sqlalchemy.orm import relationship, declarative_base
from eralchemy2 import render_er

Base = declarative_base()

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(50), unique=True, nullable=False)
    email = Column(String(120), unique=True, nullable=False)
    password = Column(String(255), nullable=False)
    is_active = Column(Boolean, default=True)
    favorites = relationship("Favorite", back_populates="user")

class Character(Base):
    __tablename__ = 'character'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    gender = Column(String(20))
    homeworld = Column(String(100))
    favorites = relationship("Favorite", back_populates="character")

class Planet(Base):
    __tablename__ = 'planet'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    climate = Column(String(100))
    terrain = Column(String(100))
    favorites = relationship("Favorite", back_populates="planet")

class Favorite(Base):
    __tablename__ = 'favorite'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'), nullable=False)
    character_id = Column(Integer, ForeignKey('character.id'), nullable=True)
    planet_id = Column(Integer, ForeignKey('planet.id'), nullable=True)
    user = relationship("User", back_populates="favorites")
    character = relationship("Character", back_populates="favorites")
    planet = relationship("Planet", back_populates="favorites")

try:
    result = render_er(Base, 'diagram.png')
    print("Todo bien")
except Exception as e:
    print("error:")
    print(e)