from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime
from .database import Base

class GroupDeal(Base):
    __tablename__ = "group_deals"

    id = Column(Integer, primary_key=True, index=True)
    product_name = Column(String, index=True)
    description = Column(String)
    original_price = Column(Float)
    discount_percentage = Column(Float)
    min_participants = Column(Integer)
    end_time = Column(DateTime)
    created_at = Column(DateTime, default=datetime.utcnow)
    
    participants = relationship("Participant", back_populates="deal")

    @property
    def current_participants(self):
        return len(self.participants)

    @property
    def is_active(self):
        return datetime.utcnow() < self.end_time

    @property
    def discounted_price(self):
        return self.original_price * (1 - self.discount_percentage / 100)

class Participant(Base):
    __tablename__ = "participants"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String)
    deal_id = Column(Integer, ForeignKey("group_deals.id"))
    joined_at = Column(DateTime, default=datetime.utcnow)

    deal = relationship("GroupDeal", back_populates="participants") 