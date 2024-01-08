import os
from typing import List, Dict, Union
from datetime import datetime
from sqlalchemy import create_engine, Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import sessionmaker, relationship
from sqlalchemy.ext.declarative import declarative_base
from prettytable import PrettyTable

Base = declarative_base()

class Donor(Base):
    __tablename__ = 'donors'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    blood_group = Column(String)
    age = Column(Integer)
    gender = Column(String)
    phone_number = Column(String)
    email = Column(String)
    donations = relationship('Donation', back_populates='donor')

class Donation(Base):
    __tablename__ = 'donations'
    id = Column(Integer, primary_key=True)
    donor_id = Column(Integer, ForeignKey('donors.id'))
    donation_date = Column(DateTime, default=datetime.utcnow)
    location = Column(String)
    donor = relationship('Donor', back_populates='donations')

class BloodBank:
    def __init__(self, db_url: str):
        self.engine = create_engine(db_url)
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()

    def add_donor(self, name: str, blood_group: str, age: int, gender: str, phone_number: str, email: str) -> None:
        donor = Donor(name=name, blood_group=blood_group, age=age, gender=gender, phone_number=phone_number, email=email)
        self.session.add(donor)
        self.session.commit()

    def add_donation(self, donor_id: int, location: str) -> None:
        donation = Donation(donor_id=donor_id, location=location)
        self.session.add(donation)
        self.session.commit()

    def get_donors(self) -> List[Dict[str, Union[int, str]]]:
        donors = self.session.query(Donor).all()
        return [{'id': donor.id, 'name': donor.name, 'blood_group': donor.blood_group, 'age': donor.age, 'gender': donor.gender, 'phone_number': donor.phone_number, 'email': donor.email} for donor in donors]

    def get_donations(self) -> List[Dict[str, Union[int, str]]]:
        donations = self.session.query(Donation).all()
        return [{'id': donation.id, 'donor_id': donation.donor_id, 'donation_date': donation.donation_date, 'location': donation.location} for donation in donations]

if __name__ == '__main__':
    db_url = os.environ.get('DATABASE_URL')
    if not db_url:
        db_url = 'sqlite:///blood_bank.db'
    blood_bank = BloodBank(db_url=db_url)
    blood_bank.add_donor(name='John Doe', blood_group='O+', age=25, gender='Male', phone_number='1234567890', email='johndoe@example.com')
    blood_bank.add_donation(donor_id=1, location='Seattle')
    donors = blood_bank.get_donors()
    donations = blood_bank.get_donations()

    # Display the contents of the donors table in a table format
    table = PrettyTable()
    table.field_names = ['ID', 'Name', 'Blood Group', 'Age', 'Gender', 'Phone Number', 'Email']
    for donor in donors:
        table.add_row([donor['id'], donor['name'], donor['blood_group'], donor['age'], donor['gender'], donor['phone_number'], donor['email']])
    print(table)

    print(donations)
