# WebSocketをインポート
from fastapi import WebSocket

from .Connection import ConnectionManager





# ConnectionManagerクラスを継承
class PostManager(ConnectionManager):
    # 初期化コンストラクタ
    def __init__(self, connection_manager: ConnectionManager):
        # ConnectionManager クラスのインスタンスを受け取る
        self.connection_manager = connection_manager

    # メッセージを送るメソッド
    async def send_personal_message(self, message: str, websocket: WebSocket):
        # websocketクラスのsend_textで引数のデータを送る
        await websocket.send_text(message)

    #全体通知のクラス
    async def broadcast_message(self, message: str):
        # connection_managerのactive_connectionリストにアクセスしてすべてのアクティブな接続に対してループを行います。
        for connection in self.connection_manager.active_connections:
            # await connection.send_text(message): 各接続にメッセージを送信します。
            await connection.send_text(message)

