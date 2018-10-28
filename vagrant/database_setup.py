import os
#config
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship ## to create foreign key rship
from sqlalchemy import create_engine

Base = declarative_base() # help get set up when writing class code
#config ends

class Restaurant(Base):
    __tablename__ = 'restaurant' #table info

    id = Column(Integer, primary_key=True) #mapper
    name = Column(String(250), nullable=False) #mapper


class MenuItem(Base):
    __tablename__ = 'menu_item' #table info

    name = Column(String(80), nullable=False) #mapper
    id = Column(Integer, primary_key=True) #mapper
    description = Column(String(250)) #mapper
    price = Column(String(8)) #mapper
    course = Column(String(250)) #mapper
    restaurant_id = Column(Integer, ForeignKey('restaurant.id')) #mapper
    restaurant = relationship(Restaurant)  #mapper

#config
engine = create_engine('sqlite:///restaurantmenu.db')


Base.metadata.create_all(engine) # goes to db and create as new tables in db

#config ends