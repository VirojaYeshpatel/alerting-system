from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime

class AlertCreate(BaseModel):
    title: str
    message: str
    severity: str
    delivery_type: str = "IN_APP"
    start_time: datetime
    expiry_time: datetime
    visibility_type: str
    target_ids: List[int]

class AlertResponse(AlertCreate):
    id: int
    archived: bool
    class Config:
        orm_mode = True
