import jwt
from datetime import datetime, timedelta, timezone

class JWT_Manager:
    def __init__(self, private_key, public_key, algorithm):
        self.private_key = private_key
        self.public_key = public_key
        self.algorithm = algorithm

    def encode(self, data, expires_in_minutes=15):
        try:
            payload = data.copy()
            payload["exp"] = datetime.now(timezone.utc) + timedelta(minutes=expires_in_minutes)
            encoded = jwt.encode(payload, self.private_key, algorithm=self.algorithm)
            return encoded
        except Exception as e:
            print(f"An error occurred in encode function: {e}")
            return None
    
    def encode_refresh(self, data, days_valid=7):
        try:
            payload = data.copy()
            payload["exp"] = datetime.now(timezone.utc) + timedelta(days=days_valid)
            payload["type"] = "refresh"
            encoded = jwt.encode(payload, self.private_key, algorithm=self.algorithm)
            return encoded
        except Exception as e:
            print(f"An error occurred in encode_refresh function: {e}")
            return None

    def decode(self, token):
        try:
            decoded = jwt.decode(token, self.public_key, algorithms=[self.algorithm])
            return decoded
        except Exception as e:
            print(e)
            return None