from typing import List
from fastapi import FastAPI, WebSocket
app = FastAPI()

# websocketのコネクション管理のクラス


class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)


connection = ConnectionManager()


@app.get("/")
async def root():
    return {"message": "Hello World"}
