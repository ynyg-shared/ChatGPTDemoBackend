from pydantic import BaseModel, Field


class AuthItem(BaseModel):
    """認證内容"""
    username: str = Field(..., title="用戶名", min_length=3, max_length=20)
    password: str = Field(..., title="密碼", min_length=6, max_length=20)


class TokenItem(BaseModel):
    access_token: str
    token_type: str
