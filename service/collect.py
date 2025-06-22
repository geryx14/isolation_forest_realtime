from typing import Tuple, Optional, Any, List, Dict
from enum import Enum
from util.parser import parser
from util.calculate import anomaly, calculate_status
from util.parser_status import ParsingStatus
from model.agregator import Dataagregator
from repository.db import SaveSensorDb
from model.mqtt import DataSensor
import logging
from repository.collect import Mqttsensor

log = logging.getLogger("Service daq")

class TeltonikasServerServiceStatus(Enum):
    FAILED = 0
    SUCCESS = 1


class MqttService:
    @staticmethod
    async def handlermassage(topic: str, payload: str) -> Tuple[TeltonikasServerServiceStatus, Any]:
        data_parsing = parser.mqttdata(topic, payload)
        if data_parsing[0] == ParsingStatus.SUCCESS:
            return await MqttService.calculateanomaly(data_parsing)
        
        log.error(f"Gagal parsing")
        return TeltonikasServerServiceStatus.FAILED, None

    @staticmethod
    async def calculateanomaly(data_parsing: Tuple[ParsingStatus, Optional[List[Dict[str, Any]]]]) -> Tuple[TeltonikasServerServiceStatus, Any]:
        result = []

        if data_parsing[0] is not None: 
            for data_mqtt in data_parsing[2]:
                status,response = await anomaly.calculate(data_mqtt)
                log.info(f"hasil kalkulasi anomaly : {response}") 
                if status == calculate_status.FAILED_CALCULATE:
                    log.warning(f"gagal kalkulasi") 
                    return TeltonikasServerServiceStatus.FAILED, None
                    

                await MqttService.mapdata(response)
                await MqttService.savetodb(response)
                    

            return TeltonikasServerServiceStatus.SUCCESS, result

        return TeltonikasServerServiceStatus.FAILED, None
    
    @staticmethod
    async def savetodb(data: Dict[str, Any]) -> Tuple[TeltonikasServerServiceStatus, None]:
        data_agregator = Dataagregator(**data)
        await SaveSensorDb.create(data_agregator)
        return TeltonikasServerServiceStatus.SUCCESS, None
    
     
    @staticmethod
    async def mapdata(data: Dict[str, Any]) -> Tuple[TeltonikasServerServiceStatus, None]:
        data_buffer = DataSensor(**data)
        json_payload = data_buffer.model_dump_json()
        await Mqttsensor.Publish(json_payload)
        log.info(f"sukses publish mqtt : {json_payload}") 
        return TeltonikasServerServiceStatus.SUCCESS, None
