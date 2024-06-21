from fastapi import FastAPI
from postgres_db import show_tables

app = FastAPI()

@app.get("/")
def read_root():
    return {"Hello": "World"}

@app.get("/test")
def read_user():
    # 例としてテーブル一覧を取得してみる
    tables = show_tables()
    return {"message": "テーブル一覧を表示しました。", "tables": tables}

# 起動するファイル
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
