# models/recipient.py
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from . import Base

class BloodRecipient(Base):
    __tablename__ = "blood_recipients"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    blood_type = Column(String)
    received_units = Column(Integer)
    donations = relationship("BloodBank", back_populates="recipient")
