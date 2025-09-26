from datetime import datetime, timedelta
from sqlalchemy.orm import Session
from app.models.alert import Alert
from app.models.user_alert_pref import UserAlertPreference
from app.models.user import User

def send_pending_reminders():
    db = SessionLocal()
    try:
        now = datetime.now()
        alerts = db.query(Alert).filter(Alert.archived == False, Alert.expiry_time >= now, Alert.reminders_enabled == True).all()
        for alert in alerts:
            users = db.query(User).all()  # Fetch all users for demo
            for user in users:
                pref = db.query(UserAlertPreference).filter_by(user_id=user.id, alert_id=alert.id).first()
                if pref and pref.snoozed and pref.snoozed_date == datetime.today().date():
                    continue  # Skip snoozed alerts
                # Check last reminder
                last_time = pref.last_reminder_time if pref else None
                if not last_time or (now - last_time) >= timedelta(minutes=alert.reminder_frequency):
                    print(f"Reminder sent to {user.name}: {alert.title}")
                    if not pref:
                        pref = UserAlertPreference(user_id=user.id, alert_id=alert.id)
                        db.add(pref)
                    pref.last_reminder_time = now
        db.commit()
    finally:
        db.close()
