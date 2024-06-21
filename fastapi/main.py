from fastapi import FastAPI, Request, HTTPException, UploadFile, File
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from typing import List
import json

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # すべてのドメインからのリクエストを許可
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


def process_files(files: List[UploadFile]):
    for file in files:
        if file.content_type not in ["image/jpeg", "image/png"]:
            raise HTTPException(
                status_code=400, detail="Only JPEG and PNG files are accepted")

        file_contents = file.read()
        # ファイル内容を必要に応じて処理します。ここでは内容を出力します。
        print(f"Filename: {file.filename}, Content Type: {file.content_type}")
        print(file_contents)
    return {"message": "Files have been processed successfully"}


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/test")
def read_user():
    # 例としてテーブル一覧を取得してみる
    tables = show_tables()
    return {"message": "テーブル一覧を表示しました。", "tables": tables}


@app.post("/login")
async def read_user_data(request: Request):
    content_type = request.headers.get('content-type')
    if content_type is None:
        raise HTTPException(
            status_code=400, detail="Content-Type header is missing")

    if 'application/json' in content_type:
        try:
            request_data = await request.json()
            print(request_data)
            return {"message": "ユーザーの情報は以下の通りです。", "request_data": request_data}
        except json.JSONDecodeError:
            raise HTTPException(status_code=400, detail="Invalid JSON")
    elif 'multipart/form-data' in content_type:
        form = await request.form()
        files = [form[key]
                 for key in form.keys() if isinstance(form[key], UploadFile)]
        response = process_files(files)
        form_data = {field: value for field,
                     value in form.items() if not isinstance(value, UploadFile)}
        print(form_data)
        return {**response, "マルチパートのrequest_data": form_data}
    else:
        request_data = await request.body()
        print(request_data)
        return {"message": "ラストユーザーの情報は以下の通りです。", "request_data": request_data.decode('utf-8', errors='ignore')}

# 起動するファイル
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
