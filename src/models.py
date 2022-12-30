import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er
import enum 
from sqlalchemy import Enum

Base = declarative_base()

# 

class Follower(Base):
    __tablename__ = 'follower' 
    id = Column(Integer, primary_key=True)
    user_from_id = Column(Integer, ForeignKey('user.id'))
    user_to_id = Column(Integer, ForeignKey('user.id'))


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer,primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250))
    email = Column(String(250), unique=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer,primary_key=True)
    comment_text = Column(String(250))
    author_id = Column(Integer,ForeignKey('user.id'))
    post_id = Column(Integer, ForeignKey('post.id'))

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer,primary_key=True)
    user_id = Column(Integer, ForeignKey('user.id'))

class Choices(enum.Enum):
    one = 1
    two = 2
    three = 3

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer,primary_key=True)
    type = Column(Enum(Choices))
    url = COlumn(String(250))
    post_id = Column(Integer, ForeignKey('post.id'))

# enum Favorites {
#     Food=1,
#     Fashion=2,
#     Faith=3,
#     Health=4,
#     Education=5,
#     Other=6,
# };

# int main()
# {

#     for (int myFavorites = Food; myFavorites != Other; myFavorites++) {

#     int userInput;
#     cin >> userInput;

#     Favorites myFavorites;
#     myFavorites = (Favorites)userInput;

#     switch (myFavorites) {
#         case Food: cout << "To live a full life, you have to fill your stomach first. ";  break;
#         case Fashion: cout << ""The joy of dressing is an art." —John Galliano ";  break;
#         case Faith: cout << "Faith is taking the first step, even when you don't see the staircase -MLK Jr." ;  break;   
#         case Health: cout << " Health is the greatest gift, contentment the greatest wealth, faithfulness the best relationship -Buddha " ;  break;
#         case Education: cout << "Education is the passport to the future, for tomorrow belongs to those who prepare for it today. -Malcolm X " ;  break;
#         case Other: cout << " The greatest glory in living lies not in never falling, but in rising every time we fall. -Nelson Mandela " ;  break;
# }
#     cout >> endL << endl;
# }
# cin.get();
# }

# t = Table(
#     'data', MetaData(),
#     Column('value', Favorites(myFavorites))
# )

# connection.execute(t.insert(), {"value": MyEnum.two})
# assert connection.scalar(t.select()) is MyEnum.two


    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
