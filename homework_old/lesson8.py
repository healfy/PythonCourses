from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, sessionmaker

engine = create_engine('sqlite:///mydatabase', echo=False)
Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    def __repr__(self):
        return '{} ({})'.format(self.name, self.age)

    id = Column(Integer, primary_key=True)
    age = Column(Integer)
    name = Column(String(250), nullable=True)


class Address(Base):
    __tablename__ = 'address'

    id = Column(Integer, primary_key=True)
    street = Column(String(250))
    post_code = Column(String(10), default='10000000')
    person_id = Column(Integer, ForeignKey('person.id'))
    person = relationship(Person)


Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
# person = session.query(Person).filter(Person.name == 'Sasha').first()
# address_6 = Address(street='DDD', person=person)
# session.add(address_6)
# session.commit()
for address in session.query(Address).all():
    print('{}: {}'.format(address.street, address.person.name))

# address = session.query(Address).filter(Address.street == 'DDD').first()
# print(address.person)
# person_1 = Person(age=20, name='Sasha')
# person_2 = Person(age=21, name='Dima')
# person_3 = Person(age=30, name='PASHA')
# person_4 = Person(age=40, name='Ivan')
# session.add_all([person_1, person_2, person_3, person_4])
# session.commit()
# address_1 = Address(street='AAA', person=person_1)
# address_2 = Address(street='BBB', person=person_2)
# address_3 = Address(street='CCC', person=person_3)
# session.add_all([address_1, address_2, address_3])
# session.commit()

# for person in (
#     session.query(Person).filter(
#         Person.age > 20
#     ).order_by(
#         -Person.age
#     )
# ):
#     print(person)
obj = Task3('new_file.db')
print(obj.select_data(5).__repr__())