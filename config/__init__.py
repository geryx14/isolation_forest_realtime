import os
from dotenv import load_dotenv

load_dotenv(override=True)

class Config:
    SERVER_HOST=os.getenv("SERVER_HOST","0.0.0.0")
    SERVER_PORT=int(os.getenv("SERVER_PORT","51000"))
    
    MQTT_HOST=os.getenv("MQTT_HOST","0.0.0.0")
    MQTT_PORT=int(os.getenv("MQTT_PORT","1880"))

    DB_URL=os.getenv("DB_URL","postgresql://gmh:123@localhost:5432/gmh3sensor")
    MODEL_URL=os.getenv("MODEL_URL","isolation.pkl")

    LOGGING_LEVEL = os.getenv("LOGGING_LEVEL","INFO")
    LOGGING_FORMAT = os.getenv("LOGGING_FORMAT","").replace("\\t","\t")