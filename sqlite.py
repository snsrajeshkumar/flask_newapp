from flask import Flask
import sqlalchemy

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy_utils import database_exists, create_database


engine=create_engine('mysql://root:@127.0.0.1/rajesh_flask', echo=True)
if not database_exists(engine.url):
    create_database(engine.url)
    
base = declarative_base()
ses = sessionmaker()
ses.configure(bind=engine)
ses = ses()



class user(base):
    __tablename__='users'

    id = Column(Integer, primary_key=True)

    name=Column(String(50))
    fullname=Column(String(50))
    password = Column(String(50))

    def __repr__(self):
        return "<user(name='%s', fullname='%s', password='%s')>" %(
            self.name,self.fullname,self.password)

