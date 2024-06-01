from dotenv import load_dotenv
load_dotenv()
# 同じディレクトリ内の websocket.py モジュールから router 変数をインポートしています。
from routers.websocket import router as websocket_router
# 同様に、http.py モジュールから router 変数をインポートしています
from routers.http import router as http_router


# __all__ は、モジュールが import * でインポートされたときにインポートされるべき変数のリストを定義します。
# ここでは、websocket_router と http_router を含むリストを定義しています。つまり、このモジュールが import * でインポートされたときに、これらの変数のみがインポートされます。
__all__ = ["websocket_router", "http_router"]


