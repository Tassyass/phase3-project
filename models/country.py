# models/donor.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class BloodDonor(Base):
    __tablename__ = "blood_donors"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    blood_type = Column(String)
    donations = relationship("BloodBank", back_populates="donor")
