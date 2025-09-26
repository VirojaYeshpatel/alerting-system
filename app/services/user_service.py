from sqlalchemy.orm import Session
from datetime import datetime, date
from app.models.alert import Alert
from app.models.user_alert_pref import UserAlertPreference

def fetch_user_alerts(db: Session, user_id: int):
    today = date.today()
    alerts = db.query(Alert).filter(Alert.archived == False, Alert.expiry_time >= datetime.now()).all()
    result = []
    for alert in alerts:
        pref = db.query(UserAlertPreference).filter_by(user_id=user_id, alert_id=alert.id).first()
        snoozed = pref.snoozed and pref.snoozed_date == today if pref else False
        read = pref.read if pref else False
        result.append({
            "alert": alert,
            "snoozed": snoozed,
            "read": read
        })
    return result

def snooze_alert(db: Session, user_id: int, alert_id: int):
    pref = db.query(UserAlertPreference).filter_by(user_id=user_id, alert_id=alert_id).first()
    if not pref:
        pref = UserAlertPreference(user_id=user_id, alert_id=alert_id)
        db.add(pref)
    pref.snoozed = True
    pref.snoozed_date = date.today()
    db.commit()
    db.refresh(pref)
    return pref

def mark_alert_read(db: Session, user_id: int, alert_id: int):
    pref = db.query(UserAlertPreference).filter_by(user_id=user_id, alert_id=alert_id).first()
    if not pref:
        pref = UserAlertPreference(user_id=user_id, alert_id=alert_id)
        db.add(pref)
    pref.read = True
    db.commit()
    db.refresh(pref)
    return pref

def mark_alert_unread(db: Session, user_id: int, alert_id: int):
    pref = db.query(UserAlertPreference).filter_by(user_id=user_id, alert_id=alert_id).first()
    if not pref:
        pref = UserAlertPreference(user_id=user_id, alert_id=alert_id)
        db.add(pref)
    pref.read = False
    db.commit()
    db.refresh(pref)
    return pref
