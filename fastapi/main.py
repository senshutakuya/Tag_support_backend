# main.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
import jwt
import secrets
# from pydantic import BaseModel  # 追加：Pydanticのインポート
from token_checker import TokenChecker  # TokenCheckerクラスのインポート
from Room import Room

app = FastAPI()

# シークレットキーを適切に設定すること
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# アルゴリズムの設定
ALGORITHM = "HS256"
# トークンの有効期限
ACCESS_TOKEN_EXPIRE_HOURS = 3

# OAuth2パスワードベアラーを設定
# oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

# ルームをインスタンス化
rooms = Room()

# CORSミドルウェアの設定
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 仮にフロント側のサーバーをたてるならここでオリジンを指定
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# トークンの生成


def generate_token(data: dict) -> str:
    # 有効期限を設定
    # トークンの有効期限を現在時刻から指定した時間（ACCESS_TOKEN_EXPIRE_HOURS）だけ加算して設定
    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    # トークンデータに有効期限のタイムスタンプ（秒単位）を追加
    data.update({"exp": expire.timestamp()})
    # JWTトークンの生成:
    # トークンデータをシークレットキーとアルゴリズムを使ってJWTトークンにエンコード
    token = jwt.encode(data, SECRET_KEY, ALGORITHM)
    # エンコードされたトークンを返す
    return token


# TokenChecker インスタンスの作成
token_checker = TokenChecker(secret_key=SECRET_KEY, algorithm=ALGORITHM)

# トークンの有効期限の確認


def get_token_data(token: str):
    try:
        # トークンをデコードしてペイロードを取得
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        # ペイロードから有効期限（exp）を取得
        exp = payload.get('exp')
        # もし有効期限があれば
        if exp:
            # 現在時刻との差を計算して残り秒数を取得
            remaining_seconds = exp - datetime.utcnow().timestamp()
            # JSON形式で残り秒数を返す
            return {"remaining_seconds": int(remaining_seconds)}
        # もし有効期限が無ければ
        else:
            # httpレスポンスのエラーで返す
            raise HTTPException(status_code=400, detail="トークンの有効期限がありません")
    # 期限切れ署名エラー
    except jwt.ExpiredSignatureError:
        # httpレスポンスのエラーで返す
        raise HTTPException(status_code=401, detail="トークンの有効期限が切れています")
    # 無効なトークンエラー
    except jwt.InvalidTokenError:
        # httpレスポンスのエラーで返す
        raise HTTPException(status_code=401, detail="無効なトークンです")

# ログインエンドポイント


@app.post("/login")
async def login():
    # トークンに含めるデータ
    token_data = {
        "unique_id": secrets.token_urlsafe(32),  # ランダムな一意なIDを生成
    }

    # トークンを生成
    access_token = generate_token(token_data)

    # 生成したトークンを返す
    return {"access_token": access_token, "token_type": "bearer"}

# トークンの有効期限を確認するエンドポイント


@app.post("/check-token")
def check_token(token_data: dict):
    token = token_data.get("token")
    return get_token_data(token)


# 部屋検索をするエンドポイント

@app.post("/room/search/{room_name}")
# 第一引数にプレイヤー情報、第二引数にルーム名を入れて送信してもらう
async def room_search(player_info, room_name):
    # プレイヤー情報からトークンを取得してチェック
    check_token(player_info)
    # 部屋を検索して入る処理
    Room.join_room(player_info, room_name)
    # 部屋とそのメンバーを返します。
    for room in Room.rooms:
        return {"Entry_Flag":"TrueかFalse", "chat_message":"プレイヤー '{player}' が '{self.name}' に参加しました。", "room_id":room.id, "room_name": room.name, "member": [player.name for player in room.members]}

# 入れたかどうかをTrueかFalse

# チャットに入出の情報を与えないといけない(websocket対応にして全体通知)

# ルームID

# ルーム名

# その地点でのメンバーの情報


# アプリを起動
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
