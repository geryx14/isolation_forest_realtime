import asyncio
from controller.collect import MqttController
from config.server import Server
from config import Config
from config.logger import logger_init
import logging
from config.database import db_connector
from config.mqtt import mqtt_connector

logger_init()

server = Server()

log = logging.getLogger("main")
async def main():
    #server.begin()
    await db_connector.connect()
    await mqtt_connector.connect()
    log.info(f"start server at host {Config.MQTT_HOST} port {Config.MQTT_PORT}")

    try:
        #await server.start()
        await mqtt_connector.subscribe("sensor/pzem", MqttController.mqtt_callback)
    except asyncio.CancelledError:
        print("Shutdown requested")
        #await server.stop
        log.warning("stop system")
    finally :
        await db_connector.disconnect()

if __name__ == "__main__":
    asyncio.run(main())
