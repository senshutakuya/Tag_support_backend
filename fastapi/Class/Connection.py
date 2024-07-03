# WebSocketをインポート
from fastapi import WebSocket
# Listを戻り値にする際に明示的に使いたいからimportした
from typing import List



# websocketのコネクション管理のクラス
class ConnectionManager:
    # 初期化コンストラクタ
    def __init__(self):
        # active_connections というリストを初期化しています。このリストは、現在アクティブな WebSocket 接続を格納します。
        self.active_connections: List[WebSocket] = []

    # 非同期関数接続許可
    async def connect(self, websocket: WebSocket):
        # websocket.accept(): WebSocket 接続を許可します。
        await websocket.accept()
        # self.active_connections.append(websocket): 接続を active_connections リストに追加します。
        self.active_connections.append(websocket)

    # websocketの切断クラス
    def disconnect(self, websocket: WebSocket):
        # self.active_connections.remove(websocket): 切断された接続を active_connections リストから削除します。
        self.active_connections.remove(websocket)

    