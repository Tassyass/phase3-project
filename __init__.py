# main.py
from models.donor import BloodDonor
from models.recipient import BloodRecipient
from models.blood_bank import BloodBank
from utils.algorithms import donate_blood, get_blood_inventory
from __init__ import Base, engine, SessionLocal  # Update this line

# This line creates the database tables based on the defined models.
Base.metadata.create_all(bind=engine)

def main():
    # Your CLI application logic here
    db = SessionLocal()

    try:
        # Example: Use the donate_blood algorithm
        donate_blood(db, donor_name="John Doe", blood_type="O+", recipient_name="Jane Doe", units_donated=2)

        # Example: Use the get_blood_inventory algorithm
        blood_inventory = get_blood_inventory(db)
        print("Current Blood Inventory:")
        for blood_record in blood_inventory:
            print(f"{blood_record.donor.name} donated {blood_record.units_donated} units to {blood_record.recipient.name}")

        # You can call more algorithms or perform other operations here

    finally:
        # Close the database connection in a 'finally' block to ensure it gets closed even if an exception occurs.
        db.close()

if __name__ == "__main__":
    main()
