# Class/__init__.pyでimportするものです。

# Listを戻り値にする際に明示的に使いたいからimportした
from typing import List
# 今回使うFastAPIをimport
from fastapi import (
    # Cookie: クッキーを操作するためのクラスです。エンドポイントでクッキーを取得する際に使用します。
    Cookie,
    # Depends: 依存関係を注入するための関数です。リクエストハンドラに共通のロジック（例：認証やデータベース接続）を注入する際に使用します。
    Depends,
    # FastAPI クラス: FastAPI アプリケーションを作成するためのクラスです。このクラスを使って新しい FastAPI アプリケーションのインスタンスを生成します。
    FastAPI,
    # Query: クエリパラメータを操作するためのクラスです。エンドポイントでクエリパラメータを取得する際に使用します。
    Query,
    # WebSocket: WebSocket 接続を扱うためのクラスです。これを使ってリアルタイム通信を実装します。
    WebSocket,
    # WebSocketDisconnect: WebSocket 接続が切断されたときに発生する例外クラスです。これをキャッチして、接続のクリーンアップ処理などを行います。
    WebSocketDisconnect
)

# レスポンスでHTMLをレスポンスする
from fastapi.responses import HTMLResponse

# ここでインポートしたモジュールを他のファイルで利用する
