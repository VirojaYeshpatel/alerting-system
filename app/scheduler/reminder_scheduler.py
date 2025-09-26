from apscheduler.schedulers.background import BackgroundScheduler
from app.services.notification_service import send_pending_reminders

def send_pending_reminders():
    print("Reminder Job Running...")  # Later: add real logic

def start_scheduler():
    scheduler = BackgroundScheduler()
    scheduler.add_job(send_pending_reminders, "interval", minutes=2)
    scheduler.start()

