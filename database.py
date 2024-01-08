# database.py
from sqlalchemy import create_engine, Column, Integer, String, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class Donor(Base):
    __tablename__ = 'donors'
    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    blood_type_id = Column(Integer, ForeignKey('blood_types.id'))
    blood_type = relationship('BloodType', back_populates='donors')

class BloodType(Base):
    __tablename__ = 'blood_types'
    id = Column(Integer, primary_key=True)
    blood_type = Column(String(10))
    donors = relationship('Donor', back_populates='blood_type')

engine = create_engine('sqlite:///blood_donation_system.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()
