from sqlalchemy import Column, Integer, String, Boolean, DateTime, JSON
from app.database import Base

class Alert(Base):
    __tablename__ = "alerts"
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255))
    message = Column(String(500))
    severity = Column(String(20))  # Info, Warning, Critical
    delivery_type = Column(String(20), default="IN_APP")
    start_time = Column(DateTime)
    expiry_time = Column(DateTime)
    reminder_frequency = Column(Integer, default=120)  # minutes
    reminders_enabled = Column(Boolean, default=True)
    visibility_type = Column(String(20))  # ORG, TEAM, USER
    target_ids = Column(JSON)  # list of ids
    archived = Column(Boolean, default=False)
