# utils/algorithms.py

from models.recipient import BloodDonor
from models.country import Country

def add_blood_donor(db, donor_name, blood_type, country_name):
    # Check if the country exists, create it if not
    country = db.query(Country).filter(Country.name == country_name).first()
    if not country:
        country = Country(name=country_name)
        db.add(country)
        db.commit()
        db.refresh(country)

    # Create a new blood donor
    new_donor = BloodDonor(name=donor_name, blood_type=blood_type, country_id=country.id)
    
    # Add the donor to the database
    db.add(new_donor)
    db.commit()
    db.refresh(new_donor)

    print(f"Blood donor {donor_name} added successfully!")

# You can define more complex algorithms based on your project requirements
