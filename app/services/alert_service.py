from sqlalchemy.orm import Session
from app.models.alert import Alert
from app.schemas.alert_schema import AlertCreate

def create_alert(db: Session, alert: AlertCreate):
    db_alert = Alert(**alert.dict())
    db.add(db_alert)
    db.commit()
    db.refresh(db_alert)
    return db_alert

def list_alerts(db: Session):
    return db.query(Alert).all()

def update_alert(db: Session, alert_id: int, update_data: dict):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        return None
    for key, value in update_data.items():
        setattr(alert, key, value)
    db.commit()
    db.refresh(alert)
    return alert

def archive_alert(db: Session, alert_id: int):
    alert = db.query(Alert).filter(Alert.id == alert_id).first()
    if not alert:
        return None
    alert.archived = True
    db.commit()
    db.refresh(alert)
    return alert
