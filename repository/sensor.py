from config.database import db_connector
from model.sensor import ResultSensor
from datetime import datetime
from typing import List

class DBSensor:
    @staticmethod
    async def get_sensor() -> List[ResultSensor]:
        result = await db_connector.db.query_raw(
            """
            SELECT DISTINCT ON (
                date_trunc('minute', "timestamp") - 
                (EXTRACT(minute FROM "timestamp")::int % 10) * INTERVAL '1 minute'
            ) *
            FROM "sensor"
            ORDER BY
                date_trunc('minute', "timestamp") - 
                (EXTRACT(minute FROM "timestamp")::int % 10) * INTERVAL '1 minute',
                "timestamp" ASC
            """
        )
        return [ResultSensor(**row) for row in result]

    
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

