# main.py

from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer
from datetime import datetime, timedelta, timezone
import jwt
import secrets
from pydantic import BaseModel  # 追加：Pydanticのインポート
from token_checker import TokenChecker  # TokenCheckerクラスのインポート

app = FastAPI()

# シークレットキーを適切に設定すること
SECRET_KEY = "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# アルゴリズムの設定
ALGORITHM = "HS256"
# トークンの有効期限
ACCESS_TOKEN_EXPIRE_HOURS = 3

# OAuth2パスワードベアラーを設定
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="token")

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
    expire = datetime.utcnow() + timedelta(hours=ACCESS_TOKEN_EXPIRE_HOURS)
    data.update({"exp": expire.timestamp()})
    # トークンを生成
    token = jwt.encode(data, SECRET_KEY, ALGORITHM)
    return token


# TokenChecker インスタンスの作成
token_checker = TokenChecker(secret_key=SECRET_KEY, algorithm=ALGORITHM)

# トークンの有効期限の確認


def get_token_data(token: str):
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        exp = payload.get('exp')
        if exp:
            remaining_seconds = exp - datetime.utcnow().timestamp()
            return {"remaining_seconds": int(remaining_seconds)}
        else:
            raise HTTPException(status_code=400, detail="トークンの有効期限がありません")
    except jwt.ExpiredSignatureError:
        raise HTTPException(status_code=401, detail="トークンの有効期限が切れています")
    except jwt.InvalidTokenError:
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

# 新たに追加：Pydanticモデルの定義


class TokenData(BaseModel):
    token: str


# アプリを起動
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
