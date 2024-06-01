# fastapi/Class/connection.pyからimport
from . import (
    FastAPI,
    WebSocket,
    HTMLResponse
)
from .connection import ConnectionManager

app = FastAPI()
# ConnectionManagerクラスを継承
class LocationManager(ConnectionManager):

    def __init__(self, connection_manager: ConnectionManager):
        # 親クラス ConnectionManager の初期化を呼び出す
        super().__init__()
        # ConnectionManager クラスのインスタンスを受け取る
        self.connection_manager = connection_manager
        # self.client_ids はクライアントの ID を格納するリストです。
        self.client_ids = []
        # self.markers はクライアントの位置情報を格納する辞書です
        self.markers = {}

    async def broadcast(self, client_id: int, coordinate: str):
        # クライアントidをclient_idリストに追加する
        self.client_ids.append(client_id)
        # client_idはmarkers辞書のキー
        self.markers[client_id] = {
            # "coordinate" は位置情報を表すキーです。
            "coordinate": coordinate,
            # marker_size" はマーカーのサイズを表すキーです
            "marker_size": self.client_ids.index(client_id) + 40,
        }

        # connection_managerのactive_connectionリストにアクセスしてすべてのアクティブな接続に対してループを行います。
        for connection in self.connection_manager.active_connections:
            # 各接続に対してjsonデータを送ります
            await connection.send_json({
                "message": f"user {client_id}'s location: {coordinate}",
                "markers": self.markers
            })