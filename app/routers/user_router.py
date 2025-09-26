from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.services.user_service import fetch_user_alerts, snooze_alert, mark_alert_read, mark_alert_unread

router = APIRouter(prefix="/user", tags=["User"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/alerts")
def get_user_alerts(user_id: int, db: Session = Depends(get_db)):
    return fetch_user_alerts(db, user_id)

@router.post("/alerts/{alert_id}/snooze")
def snooze_user_alert(alert_id: int, user_id: int, db: Session = Depends(get_db)):
    return snooze_alert(db, user_id, alert_id)

@router.post("/alerts/{alert_id}/read")
def mark_read(alert_id: int, user_id: int, db: Session = Depends(get_db)):
    return mark_alert_read(db, user_id, alert_id)

@router.post("/alerts/{alert_id}/unread")
def mark_unread(alert_id: int, user_id: int, db: Session = Depends(get_db)):
    return mark_alert_unread(db, user_id, alert_id)
