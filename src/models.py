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
   
# class Profile(Base):
#     __tablename__ = 'profile'
#     biografy 

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e