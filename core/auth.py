import os
from datetime import timedelta, datetime, timezone

import jwt
from fastapi.security import OAuth2PasswordBearer
from jwt import InvalidTokenError
from passlib.context import CryptContext

# 密鑰
SECRET_KEY = os.getenv("PASSLIB_SECRET_KEY") or "09d25e094faa6ca2556c818166b7a9563b93f7099f6f0f4caa6cf63b88e8d3e7"
# 加密算法
ALGORITHM = os.getenv("PASSLIB_ALGORITHM") or "HS256"
# 令牌過期時間
ACCESS_TOKEN_EXPIRE_MINUTES = int(os.getenv("PASSLIB_ACCESS_TOKEN_EXPIRE_MINUTES")) or 30

# 密碼上下文
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
# 認證方案
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")


def verify_password(plain_password: str, hashed_password: str) -> bool:
    """
    驗證密碼
    :param plain_password: 密碼原文
    :param hashed_password: 密碼密文
    :return: 是否一致
    """
    return pwd_context.verify(plain_password, hashed_password)


def get_password_hash(password: str) -> str:
    """
    獲取密碼密文
    :param password: 密碼原文
    :return: 密碼密文
    """
    return pwd_context.hash(password)


def create_access_token(data: dict, expires_delta: timedelta | None = None) -> str:
    """
    創建認證令牌
    :param data: 待加密數據
    :param expires_delta: 過期時間
    :return: JWT令牌
    """
    # 深拷貝待加密數據
    to_encode = data.copy()
    # 添加過期時間
    if expires_delta:
        expire = datetime.now(timezone.utc) + expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(seconds=ACCESS_TOKEN_EXPIRE_MINUTES)
    # 添加過期時間
    to_encode.update({"exp": expire})
    # 加密數據
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    # 返回JWT令牌
    return encoded_jwt


def parse_access_token(token: str) -> dict | None:
    """
    解析認證令牌
    :param token: JWT令牌
    :return: 解密后的數據
    """
    try:
        # 解密數據
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        return payload
    except InvalidTokenError:
        return None
