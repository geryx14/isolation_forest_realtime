from pydantic import BaseModel
from datetime import datetime 
from prisma.models import sensor_pzem


class DataSensor(BaseModel):
    id: int
    voltage: float
    current: float
    power: float
    energy: float
    frequency: float
    powerFactor: float
    timestamp: datetime

ResultSensor = sensor_pzem