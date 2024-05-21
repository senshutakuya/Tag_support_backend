from typing import List
from fastapi import (
    Cookie,
    Depends,
    FastAPI,
    Query,
    WebSocket,
    WebSocketDisconnect
)


# websocketのコネクション管理のクラス
class ConnectionManager:
    # 初期化active_connections(websocketを格納する配列)を定義
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    # 非同期関数接続許可
    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)
