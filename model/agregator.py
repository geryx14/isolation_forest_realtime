from pydantic import BaseModel
from datetime import datetime 
from prisma.models import data_agregator_voltage


class Dataagregator(BaseModel):
    timestamp   : datetime
    voltage     : float
    is_anomaly  : bool


ResultSensor = data_agregator_voltage