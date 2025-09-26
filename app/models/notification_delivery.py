from sqlalchemy import Column, Integer, DateTime, String
from app.database import Base

class NotificationDelivery(Base):
    __tablename__ = "notification_deliveries"
    id = Column(Integer, primary_key=True, index=True)
    alert_id = Column(Integer)
    user_id = Column(Integer)
    delivered_at = Column(DateTime)
    status = Column(String(50))  # Delivered, Read, Snoozed
