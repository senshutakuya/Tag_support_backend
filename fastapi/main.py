# .envファイルを読みこんで環境変数を読み込む
from dotenv import load_dotenv
# import os
import sys
# sys.path.append('../')

load_dotenv()

from fastapi import FastAPI



print(__file__)  # main.py ファイルのパスを表示

from routers import websocket_router

from routers import http_router



print(websocket_router)  # websocket_router のパスを表示
print(http_router)  # http_router のパスを表示


app = FastAPI()

# ルーターをアプリケーションに追加する
app.include_router(websocket_router)
app.include_router(http_router)

# 起動するファイル
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)


# print(os.getenv("PYTHONPATH"))

