from config.mqtt import mqtt_connector

class Mqttsensor:
    @staticmethod
    async def Publish(data: str): 
        await mqtt_connector.publish("anomaly/data", data)
