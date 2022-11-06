import datetime

import sqlalchemy
from sqlalchemy import Column, Integer, String, Date, DateTime
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

engine = sqlalchemy.create_engine('postgresql+psycopg2://postgres:hn19921995@localhost:5432/project')
conn = engine.connect()

Base = declarative_base()


class Person(Base):
    __tablename__ = 'person'

    person_id = Column(Integer, primary_key=True)
    first_name = Column(String(32))
    last_name = Column(String(32))
    birth_date = Column(Date)
    reg_date = Column(DateTime)


Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()


farid = Person(first_name='Farid', last_name='Aliev', birth_date=datetime.date(1995, 1, 5),
               reg_date=datetime.datetime.now())


for item in session.query(Person):
    print(item.person_id, item.first_name, item.last_name, item.birth_date, item.reg_date)