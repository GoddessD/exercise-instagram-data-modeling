import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

# 

class Follower(Base):
    __tablename__ = 'follower'
    user_from_id = Column(Integer)
    user_to_id = Column(Integer)

class User(Base):
    id = Column(Integer,primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250)), ForeignKey('follower.id')

class Comment(Base):
    id = Column(Integer,primary_key=True)
    comment-text = Column(String(250))
    author_id = Column(Integer,ForeignKey('user.id')
    post_id = Column(Integer,ForeignKey('post.id')

class Post(Base):
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id')

class Media(Base):
    id = Column(Integer,primary_key=True)
    type = Enum
    url = COlumn(String(250))
    post_id = Column(Integer, ForeignKey('post.id')


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
