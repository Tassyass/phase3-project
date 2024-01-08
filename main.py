# main.py

from utils.database import Base, engine, SessionLocal
from models.country import Country
from models.recipient import BloodDonor
from utils.algorithms import add_blood_donor

# This line creates the database tables based on the defined models.
Base.metadata.create_all(bind=engine)

def main():
    # Your CLI application logic here
    db = SessionLocal()

    try:
        # Example: Use the add_blood_donor algorithm
        add_blood_donor(db, donor_name="John Doe", blood_type="O+", country_name="Sample Country")

        # You can call more algorithms or perform other operations here

    finally:
        # Close the database connection in a 'finally' block to ensure it gets closed even if an exception occurs.
        db.close()

if __name__ == "__main__":
    main()
