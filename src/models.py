import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy import render_er

Base = declarative_base()

class Users(Base):
    __tablename__ = 'user'
    id= Column(Integer, primary_key = True)
    user_name = Column(String(30), nullable = False)
    name = Column(String(40), nullable = False)
    lastname= Column(String(40))
    email = Column(String(12), unique = True)
    profile = relationship("Profile", back_populates = "parent")
   
class Profile(Base):
    __tablename__ = 'profile'
    id = Column(Integer, primary_key = True)
    biografy = Column(String(300))
    image = Column(String)
    post = Column(String)
    reel = Column(String)
    story = Column(String)
    followers = Column(Integer)
    following = Column(Integer)
    user_id = Column(Integer, ForeignKey("user.id"))
    user = relationship("Users", back_populates = "children")

class Favorites(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key = True)
    fav = Column(String)
    

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key = True)
    image = Column(String)
    comment = Column(String)
    city_adress = Column(String)
    likes = Column(Integer)
    profile_id = Column(Integer, ForeignKey("profile.id"))
    save_id = Column(Integer, ForeignKey("save.id"))
    save = relationship("child")

class Reel(Base):
    __tablename__ = 'reel'
    id = Column(Integer, primary_key = True)
    image = Column(String)
    comment = Column(String)
    likes = Column(Integer)
    profile_id = Column(Integer, ForeignKey("profile.id"))
    save_id = Column(Integer, ForeignKey("save.id"))
    save = relationship("child")

class Story(Base):
    __tablename__ = 'story'
    id = Column(Integer, primary_key = True)
    views = Column(Integer)
    profile_id = Column(Integer, ForeignKey("profile.id"))

class Save(Base):
    __tablename__ = 'save'  
    id = Column(Integer, primary_key = True)
    post = Column(String)
    reel = Column(String)
    favorites_id = Column(Integer, ForeignKey("favorites.id"))


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e