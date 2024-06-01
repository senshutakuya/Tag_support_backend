# APIRouter クラスは、FastAPIアプリケーション内でエンドポイントをグループ化するためのルーターを作成するために使用されます。
from fastapi import APIRouter

# インスタンス化
router = APIRouter()

# 最初にリクエストが来たらここ
@router.get("/")
def index():
    # この場合、JSON形式のデータ {"message": "Hello, HTTP!"} を返します。
    return {"message": "Hello, HTTP!"}
