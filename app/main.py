from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from datetime import datetime
from typing import List, Optional

app = FastAPI(title="Simple Log API")

# Modelo de datos para un log
class LogEntry(BaseModel):
    id: Optional[int] = None
    level: str
    message: str
    timestamp: Optional[str] = None

# Almacenamiento temporal en memoria
logs_db = []
log_counter = 1

@app.get("/")
async def root():
    return {"message": "Welcome to the Simple Log API", "status": "online"}

@app.post("/logs/", response_model=LogEntry)
async def create_log(log: LogEntry):
    global log_counter
    new_log = log.dict()
    new_log["id"] = log_counter
    if not new_log["timestamp"]:
        new_log["timestamp"] = datetime.now().isoformat()
    
    logs_db.append(new_log)
    log_counter += 1
    return new_log

@app.get("/logs/", response_model=List[LogEntry])
async def get_logs(level: Optional[str] = None):
    if level:
        return [log for log in logs_db if log["level"].upper() == level.upper()]
    return logs_db

@app.get("/logs/{log_id}", response_model=LogEntry)
async def get_log(log_id: int):
    for log in logs_db:
        if log["id"] == log_id:
            return log
    raise HTTPException(status_code=404, detail="Log not found")
