from fastapi import APIRouter,Query
from service.sensor import Sensor
from model.sensor import ResultSensor
from datetime import datetime
from typing import List, Optional


router = APIRouter()

@router.get("/data-sensor", response_model=List[ResultSensor])
async def get_sensor():
    data = await Sensor.get_sensor()
    return data

@router.get("/data-sensor-limit",response_model=List[ResultSensor])
async def get_sensorbytime(start_date: Optional[datetime] = Query(None),
    end_date: Optional[datetime] = Query(None)):
    data = await Sensor.get_sensor_data(start_date=start_date, end_date=end_date)
    return data

router_sensor = router