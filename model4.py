from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///new_file', echo=False)
Base = declarative_base()


class Shops(Base):
    __tablename__ = 'Shops'
    id = Column(Integer, primary_key=True)
    name = Column(String(250), nullable=False)
    address = Column(String(250), nullable=True)
    staff_amount = Column(Integer)


class Departments(Base):
    __tablename__ = 'Departments'
    id = Column(Integer, primary_key=True)
    sphere = Column(String(250))
    staff_amount = Column(Integer)
    shop_id = Column(String(250), ForeignKey('Shops.id'))
    shop = relationship(Shops)


class Items(Base):
    __tablename__ = 'Items'
    id = Column(Integer, primary_key=True)
    name = Column(String(250))
    description = Column(String(250), nullable=True)
    price = Column(Integer)
    department_id = Column(Integer, ForeignKey('Departments.id'))
    department = relationship(Departments)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
