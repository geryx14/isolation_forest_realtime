import numpy as np
import joblib
from datetime import datetime
from typing import Dict, Any, Tuple, Optional
from util.parser_status import ResultField
from enum import Enum
from config import Config

iso_forest = joblib.load(Config.MODEL_URL)

class calculate_status(Enum):
    SUCCESS_CALCULATE, FAILED_CALCULATE = range(2)

class anomaly:
    @staticmethod
    async def calculate(data_parsing: Dict[str, Any]) -> Tuple[calculate_status, Optional[Dict[Any, Any]]]:
        try:
            timestamp = data_parsing.get(ResultField.TIMESTAMP)
            voltage = data_parsing.get(ResultField.VOLTAGE)

            if timestamp is None or voltage is None:
                return calculate_status.FAILED_CALCULATE, None
            
            input_voltage = np.array([[voltage]]) 
            is_anomaly = bool(iso_forest.predict(input_voltage)[0] == -1)


            result ={
                 "timestamp": timestamp,
                 "voltage": voltage,
                 "is_anomaly": is_anomaly
            }

            print(result)

            return calculate_status.SUCCESS_CALCULATE,result

        except Exception as e:
            return calculate_status.FAILED_CALCULATE, {"error": str(e)}
