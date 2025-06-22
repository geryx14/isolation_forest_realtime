from enum import Enum
from typing import Tuple, Any, Optional, Dict

class ParsingStatus(Enum):
    SUCCESS, FAILED, INVALID_JSON= range(3)

class MQTT(str,Enum):
    TOPIC = "sensor/pzem"
    VOLTAGE = "v"

class ResultField(str, Enum):
    VOLTAGE = "voltage"
    TIMESTAMP = "timestamp"