from enum import StrEnum

from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.sql.schema import ForeignKey
from sqlalchemy.sql.sqltypes import String, Enum, Text

from core.model import BaseModel
from ..user.models import UserModel


class ConversationsModel(BaseModel):
    """會話模型"""
    __tablename__ = "conversations"
    __table_args__ = {"comment": "會話表"}

    title: Mapped[str] = mapped_column(
        String(100),
        nullable=True,
        comment="標題",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(UserModel.id, ondelete="CASCADE"),
        comment="用戶ID",
    )

    def __str__(self) -> str:
        return self.title


class ModelsModel(BaseModel):
    """模型"""
    __tablename__ = "models"
    __table_args__ = {"comment": "模型表"}

    name: Mapped[str] = mapped_column(
        String(100),
        comment="名稱",
    )
    description: Mapped[str] = mapped_column(
        String(100),
        comment="描述",
    )
    model_id: Mapped[str] = mapped_column(
        String(100),
        comment="模型ID",
    )
    system_message_name: Mapped[str] = mapped_column(
        String(20),
        comment="系統消息的名稱",
    )
    system_message: Mapped[str] = mapped_column(
        comment="系統消息",
    )

    def __str__(self) -> str:
        return self.name


class MessagesModel(BaseModel):
    """消息模型"""
    __tablename__ = "messages"
    __table_args__ = {"comment": "消息表"}

    class RoleEnum(StrEnum):
        """角色枚舉"""
        USER = "user"  # 用戶
        ASSISTANT = "assistant"  # 助手

    role: Mapped[RoleEnum] = mapped_column(
        Enum(RoleEnum),
        comment="角色",
    )
    user_id: Mapped[int] = mapped_column(
        ForeignKey(UserModel.id, ondelete="CASCADE"),
        comment="用戶ID",
    )
    conversation_id: Mapped[int] = mapped_column(
        ForeignKey(ConversationsModel.id, ondelete="CASCADE"),
        comment="會話ID",
    )
    content: Mapped[str] = mapped_column(
        Text,
        comment="消息",
    )
    sequence_number: Mapped[int] = mapped_column(
        Integer,
        comment="序列號",
    )
    model_id = mapped_column(
        ForeignKey(ModelsModel.id, ondelete="CASCADE"),
        comment="模型ID",
    )

    def __str__(self) -> str:
        return f"{self.role}: {self.content}"
