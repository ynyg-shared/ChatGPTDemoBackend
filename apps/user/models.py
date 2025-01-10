from typing import Annotated, Self

from fastapi.param_functions import Depends
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import Mapped, mapped_column, validates
from sqlalchemy.sql.sqltypes import String, Integer

from core.auth import get_password_hash, verify_password, create_access_token, oauth2_scheme, parse_access_token
from core.db import get_session
from core.model import BaseModel

__all__ = [
    "UserModel",
]


class UserModel(BaseModel):
    """用戶模型"""
    __tablename__ = "user"
    __table_args__ = {"comment": "用戶表"}

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="用戶ID",
    )
    username: Mapped[str] = mapped_column(
        String(50),
        unique=True,
        comment="用戶名",
    )
    password: Mapped[str] = mapped_column(
        String(255),
        comment="密碼",
    )

    @validates("password")
    def preprocess_password(self, _key: str, value: str) -> str:
        """
        預處理密碼：在設置密碼時自動加密。
        :param _key: 字段名
        :param value: 原始密碼
        :return: 加密後的密碼
        """
        return get_password_hash(value)

    def verify_password(self, password: str) -> bool:
        """
        校驗密碼
        :param password: 待校驗的密碼
        :return: 是否匹配
        """
        return verify_password(password, self.password)

    def create_token(self) -> str:
        """
        生成token
        :return: token
        """
        # 這裡的id和username是為了方便後續使用
        return create_access_token(data={"id": self.id, "username": self.username})

    @classmethod
    async def get_user(
            cls,
            token: Annotated[str, Depends(oauth2_scheme)],
            db_session: Annotated[AsyncSession, Depends(get_session)]) -> Self | None:
        """
        獲取用戶
        :param token: token
        :param db_session: 數據庫會話
        :return: 用戶
        """
        # 解析token
        data = parse_access_token(token)
        # 如果解析失敗，返回None
        if data is None:
            return None
        # 獲取用戶
        return await db_session.get(cls, data.get("id"))
