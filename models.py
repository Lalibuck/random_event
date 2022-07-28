from sqlalchemy import Column, Integer, String, Date, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()


class City(Base):

    __tablename__ = 'City'

    id = Column('id', Integer, primary_key=True)
    city = Column('name', String(255))

    event = relationship('Event')


    def __repr__(self):
        return self.city


class Category(Base):

    __tablename__ = 'Category'

    id = Column('id', Integer, primary_key=True)
    category = Column('name', String(255))

    event = relationship('Event')


    def __repr__(self):
        return self.category


class Event(Base):

    __tablename__ = 'Event'

    id = Column('id', Integer, primary_key=True)
    event = Column('name', String(255))
    desc = Column('description', String(255))
    date = Column('date', Date)
    city_id = Column('city_id', Integer, ForeignKey('City.id'), nullable=False)
    category_id = Column('category_id', Integer, ForeignKey('Category.id'), nullable=False)

    city = relationship('City')
    category = relationship('Category')


    def __repr__(self):
        return self.event