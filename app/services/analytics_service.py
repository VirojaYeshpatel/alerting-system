from sqlalchemy.orm import Session
from app.models.alert import Alert
from app.models.user_alert_pref import UserAlertPreference

def get_analytics(db: Session):
    total_alerts = db.query(Alert).count()
    delivered_count = db.query(UserAlertPreference).filter(UserAlertPreference.last_reminder_time != None).count()
    read_count = db.query(UserAlertPreference).filter(UserAlertPreference.read == True).count()
    snoozed_count = db.query(UserAlertPreference).filter(UserAlertPreference.snoozed == True).count()
    
    severity_breakdown = {
        "Info": db.query(Alert).filter(Alert.severity=="Info").count(),
        "Warning": db.query(Alert).filter(Alert.severity=="Warning").count(),
        "Critical": db.query(Alert).filter(Alert.severity=="Critical").count()
    }
    
    return {
        "total_alerts": total_alerts,
        "delivered": delivered_count,
        "read": read_count,
        "snoozed": snoozed_count,
        "severity_breakdown": severity_breakdown
    }
