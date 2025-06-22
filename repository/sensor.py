from config.database import db_connector
from model.sensor import ResultSensor
from datetime import datetime
from typing import List

class DBSensor:
    @staticmethod
    async def get_sensor(limit: int = 10) -> List[ResultSensor]:
        return await db_connector.db.sensor_pzem.find_many(take=limit)
    
    @staticmethod
    async def get_sensor_data(start_date: datetime, end_date: datetime)  -> List[ResultSensor]:
        return await db_connector.db.sensor_pzem.find_many(  where={
            "timestamp": {
                "gte": start_date,
                "lt": end_date
            }
        },
        order={"timestamp": "asc"}
    )