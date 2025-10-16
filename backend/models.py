from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
import datetime

Base = declarative_base()

class Tender(Base):
    __tablename__ = 'tenders'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    department = Column(String)
    province = Column(String)
    description = Column(Text)
    posted_at = Column(DateTime, default=datetime.datetime.utcnow)
    document_hash = Column(String)
    status = Column(String, default="open")
    bids = relationship("Bid", back_populates="tender")
    awards = relationship("Award", back_populates="tender")

class Bid(Base):
    __tablename__ = 'bids'
    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(Integer, ForeignKey('tenders.id'))
    vendor = Column(String)
    amount = Column(Float)
    submitted_at = Column(DateTime, default=datetime.datetime.utcnow)
    bid_hash = Column(String)
    tender = relationship("Tender", back_populates="bids")

class Award(Base):
    __tablename__ = 'awards'
    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(Integer, ForeignKey('tenders.id'))
    vendor = Column(String)
    awarded_at = Column(DateTime, default=datetime.datetime.utcnow)
    award_hash = Column(String)
    tender = relationship("Tender", back_populates="awards")

class Report(Base):
    __tablename__ = 'reports'
    id = Column(Integer, primary_key=True, index=True)
    tender_id = Column(Integer, ForeignKey('tenders.id'), nullable=True)
    description = Column(Text)
    submitted_at = Column(DateTime, default=datetime.datetime.utcnow)
    encrypted = Column(String)