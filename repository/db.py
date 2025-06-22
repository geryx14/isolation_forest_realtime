from config.database import db_connector
import logging 
from model.agregator import (
    Dataagregator,
    data_agregator_voltage,
)
log = logging.getLogger(f"db")

class SaveSensorDb:
    @staticmethod
    async def create(data: Dataagregator) -> data_agregator_voltage:
        try:
            result = await db_connector.db.data_agregator_voltage.create(data=data.model_dump())
            logging.info(f"[DB] Data berhasil disimpan: {result}")
            return result
        except Exception as e:
            logging.error(f"[DB] Gagal menyimpan data: {e}")
            raise

