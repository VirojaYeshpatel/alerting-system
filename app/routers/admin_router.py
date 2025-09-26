from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import SessionLocal
from app.schemas.alert_schema import AlertCreate, AlertResponse
from app.services.alert_service import create_alert, list_alerts
from typing import List

router = APIRouter(prefix="/admin", tags=["Admin"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/alerts", response_model=AlertResponse)
def create_new_alert(alert: AlertCreate, db: Session = Depends(get_db)):
    return create_alert(db, alert)

@router.get("/alerts", response_model=List[AlertResponse])
def get_all_alerts(db: Session = Depends(get_db)):
    return list_alerts(db)


@router.put("/alerts/{alert_id}", response_model=AlertResponse)
def update_existing_alert(alert_id: int, update_data: dict, db: Session = Depends(get_db)):
    updated_alert = update_alert(db, alert_id, update_data)
    if not updated_alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return updated_alert

@router.put("/alerts/{alert_id}/archive", response_model=AlertResponse)
def archive_existing_alert(alert_id: int, db: Session = Depends(get_db)):
    archived_alert = archive_alert(db, alert_id)
    if not archived_alert:
        raise HTTPException(status_code=404, detail="Alert not found")
    return archived_alert