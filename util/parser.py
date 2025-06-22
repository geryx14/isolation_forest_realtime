from typing import Dict, Any, Tuple, Optional, List
from enum import Enum
from datetime import datetime
from zoneinfo import ZoneInfo
import json
import logging
from util.parser_status import ParsingStatus, MQTT, ResultField


log = logging.getLogger(f"Parser Data")

class parser:
    @staticmethod
    def mqttdata(topic: str, payload: str) -> Tuple[ParsingStatus, Optional[Enum], Optional[List[Dict[str, Any]]]]:
        if str(topic) == MQTT.TOPIC.value:
            try:
                data = json.loads(payload)

                if MQTT.VOLTAGE not in data:
                    return ParsingStatus.FAILED, None, None
                log.info(f"Gagal parsing tidak ada data VOLTAGE ")

                result = [{
                    ResultField.VOLTAGE.value: float(data[MQTT.VOLTAGE]),
                    ResultField.TIMESTAMP.value: datetime.now(ZoneInfo("Asia/Jakarta")).isoformat()
                }]
                log.info(f"Parsed data: {result}")

                return ParsingStatus.SUCCESS, None, result
               

            except json.JSONDecodeError:
                return ParsingStatus.INVALID_JSON, None, None
        log.warning(f"Tidak ada topic yang sama")
        return ParsingStatus.FAILED, None, None
