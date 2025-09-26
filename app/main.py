from fastapi import FastAPI
from app.database import Base, engine
from app.scheduler.reminder_scheduler import start_scheduler
from app.routers import admin_router, user_router, analytics_router


Base.metadata.create_all(bind=engine)

app = FastAPI(title="Alerting & Notification Platform")

# Routers
app.include_router(admin_router.router)
app.include_router(user_router.router)
app.include_router(analytics_router.router)


# Start scheduler
start_scheduler()
