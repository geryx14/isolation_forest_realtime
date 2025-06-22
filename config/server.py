import uvicorn
from fastapi import FastAPI
from config import Config
from controller.sensor import router_sensor


app = FastAPI()


class Server:
    def begin(self):
        app.include_router(router_sensor, prefix="/api/data", tags=["Data energy seluruh"])
        config = uvicorn.Config(app,Config.SERVER_HOST,Config.SERVER_PORT)
        self.__server = uvicorn.Server(config)

    async def start(self):
        await self.__server.serve()

    async def stop(self):
        await self.__server.shutdown()