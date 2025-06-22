import logging
from service.collect import MqttService, TeltonikasServerServiceStatus

log=logging.getLogger("controller daq")

class MqttController:
    @staticmethod
    async def mqtt_callback(topic: str, payload):
        try:
            status, response = await MqttService.handlermassage(topic, payload)

            if status == TeltonikasServerServiceStatus.SUCCESS:
               log.info("berhasill publish mqtt")
            else:
               log.error("gagal publish mqtt")

        except Exception as e:
            log.error("  Terjadi error:", e)
