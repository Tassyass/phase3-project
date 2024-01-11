# blood_donation_system.py
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
 
 # Create the engine and session
engine = create_engine('sqlite:///blood_donation_system.db')
Base.metadata.create_all(engine)
Session = sessionmaker(bind=engine)
session = Session()

def delete_donor(donor_id):
    # Query the donor to delete
    donor_to_delete = session.query(Donor).filter_by(id=donor_id).first()

    if donor_to_delete:
        # Delete the donor
        session.delete(donor_to_delete)
        # Commit the changes to persist the deletion
        session.commit()
        print(f'Donor with ID {donor_id} has been deleted.')
    else:
        print(f'Donor with ID {donor_id} not found.')

# Example: Delete a donor with ID 1
delete_donor(1)


class BloodDonationSystem:
    def __init__(self):
        self.engine = create_engine('sqlite:///blood_donation_system.db')
        Base.metadata.create_all(self.engine)
        Session = sessionmaker(bind=self.engine)
        self.session = Session()


    def run(self):
        while True:
            print('1. Add donor')
            print('2. Exit')
            choice = input('Enter your choice: ')
            if choice == '1':
                name = input('Enter donor name: ')
                blood_type = input('Enter blood type: ')
                blood_type_obj = self.session.query(BloodType).filter_by(blood_type=blood_type).first()
                if blood_type_obj is None:
                    blood_type_obj = BloodType(blood_type=blood_type)
                    self.session.add(blood_type_obj)
                donor = Donor(name=name, blood_type=blood_type_obj)
                self.session.add(donor)
                self.session.commit()
                print('Donor added successfully')
            elif choice == '2':
                break
            else:
                print('Invalid choice')