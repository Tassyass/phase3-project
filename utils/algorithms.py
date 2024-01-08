# utils/algorithms.py
from sqlalchemy.orm import Session
from models.donor import BloodDonor
from models.recipient import BloodRecipient
from models.blood_bank import BloodBank

def donate_blood(db: Session, donor_name: str, blood_type: str, recipient_name: str, units_donated: int):
    # Example algorithm: Simulate a blood donation

    # Check if the donor already exists, or create a new one
    donor = db.query(BloodDonor).filter_by(name=donor_name).first()
    if not donor:
        donor = BloodDonor(name=donor_name, blood_type=blood_type)
        db.add(donor)
        db.commit()

    # Check if the recipient already exists, or create a new one
    recipient = db.query(BloodRecipient).filter_by(name=recipient_name).first()
    if not recipient:
        recipient = BloodRecipient(name=recipient_name, blood_type=blood_type)
        db.add(recipient)
        db.commit()

    # Create a new blood donation record
    blood_donation = BloodBank(donor=donor, recipient=recipient, units_donated=units_donated)
    
    # Add the blood donation to the database
    db.add(blood_donation)
    db.commit()

    print(f"Blood donation from {donor_name} to {recipient_name} recorded successfully.")
