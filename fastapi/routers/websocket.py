from fastapi import APIRouter, WebSocket, WebSocketDisconnect
# fastapi/Class/connection.pyからconnectionManagerクラスをimport
from Class.connection import ConnectionManager
# fastapi/Class/chat.pyからPostManegerクラスをimport
from Class.chat import PostManager
# fastapi/Class/location.pyからLocationManegerクラスをimport
from Class.location import LocationManager

# fastapiのAPIRouterをインスタンス化
router = APIRouter()
# ConnectionManegerをインスタンス化
conmanager = ConnectionManager()
# PostManegerをインスタンス化
chatmanager = PostManager(conmanager)
# LocationManegerをインスタンス化
mapmanager = LocationManager(conmanager)


@router.websocket("/ws/{client_id}/chat")

async def websocket_endpoint(websocket: WebSocket, client_id: int):
    # ConnectionManagerのconnectメソッドを使用して、新しいWebSocket接続を管理します。
    await conmanager.connect(websocket)
    try:
        # ループ: クライアントが接続されている間、無限ループ内でWebSocketからのデータを受信し、メッセージを処理します。
        while True:
            # クライアントからのテキストデータを非同期で受信します。
            data = await websocket.receive_text()
            # PostManagerのsend_personalメソッド使ってクライアントにパーソナルメッセージを送信します。
            await chatmanager.send_personal_message(f"You wrote: {data}", websocket)
            # PostManagerのbroadcast_messageメソッド使って全ての接続しているクライアントに対してメッセージを送信する。
            # await chatmanager.broadcast_message(f"Client #{client_id} says: {data}")
    #  WebSocket接続が切断された場合、WebSocketDisconnect例外を処理し、クライアントの接続を切断します。
    except WebSocketDisconnect:
        # ConnectionManagerのdisconnectメソッドを使って 切断された接続を active_connections リストから削除します。
        conmanager.disconnect(websocket)
        # PostManagerのbroadcast_messageメソッド使って全ての接続しているクライアントに対してメッセージを送信する。
        # await chatmanager.broadcast_message(f"Client #{client_id} left the chat")


@router.websocket("/ws/{client_id}/location")

async def websocket_endpoint(websocket: WebSocket, client_id: int):
    # Websocket の開始
    await conmanager.connect(websocket)
    try:
        # ループ: クライアントが接続されている間、無限ループ内でWebSocketからのデータを受信し、メッセージを処理します。
        while True:
            # クライアントからのテキストデータを非同期で受信します。
            data = await websocket.receive_text()
            # LocationManagerのbroadcastメソッド使って全ての接続しているクライアントに対してメッセージを送信する。
            await mapmanager.broadcast(client_id, data)

    except WebSocketDisconnect:
        # websocketの切断
        conmanager.disconnect(websocket)
        # locationManagerのmarkersリストからクライアントidを削除
        del mapmanager.markers[client_id]