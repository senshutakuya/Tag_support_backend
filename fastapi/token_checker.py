# token_checker.py

from datetime import datetime, timezone
import jwt
from fastapi import HTTPException

class TokenChecker:
    def __init__(self, secret_key: str, algorithm: str):
        self.secret_key = secret_key
        self.algorithm = algorithm

    def is_token_expired(self, token: str) -> bool:
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
            exp = payload.get('exp')
            if exp:
                # Convert exp to datetime object in UTC
                exp_datetime = datetime.fromtimestamp(exp, tz=timezone.utc)
                return datetime.now(timezone.utc) > exp_datetime
            return True
        except jwt.ExpiredSignatureError:
            return True
        except jwt.InvalidTokenError:
            return True

    def get_token_data(self, token: str):
        try:
            payload = jwt.decode(token, self.secret_key, algorithms=[self.algorithm])
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
