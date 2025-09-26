from sqlalchemy import Column, Integer, Boolean, Date, DateTime
from app.database import Base

class UserAlertPreference(Base):
    __tablename__ = "user_alert_preferences"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer)
    alert_id = Column(Integer)
    read = Column(Boolean, default=False)
    snoozed = Column(Boolean, default=False)
    snoozed_date = Column(Date)
    last_reminder_time = Column(DateTime)
