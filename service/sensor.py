from repository.sensor import DBSensor
from model.sensor import ResultSensor
from datetime import datetime, timedelta
from typing import List, Optional
from fastapi import Query

class Sensor:
    @staticmethod
    async def get_sensor() -> List[ResultSensor]:
        return await DBSensor.get_sensor()
    
    @staticmethod
    async def get_sensor_data(start_date: Optional[datetime] = Query(None),
        end_date: Optional[datetime] = Query(None)) -> List[ResultSensor]:
        
        if not start_date or not end_date:
            end_date = datetime.utcnow()
            start_date = end_date - timedelta(days=1)
        
        return await DBSensor.get_sensor_data(start_date=start_date, end_date=end_date)

    




