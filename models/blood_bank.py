# models/blood_bank.py
from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from .. import Base

class BloodBank(Base):
    __tablename__ = "blood_bank"

    id = Column(Integer, primary_key=True, index=True)
    donor_id = Column(Integer, ForeignKey("blood_donors.id"))
    recipient_id = Column(Integer, ForeignKey("blood_recipients.id"))
    units_donated = Column(Integer)
    
    donor = relationship("BloodDonor", back_populates="donations")
    recipient = relationship("BloodRecipient", back_populates="donations")
