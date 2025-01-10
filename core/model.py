from datetime import datetime, timezone
from functools import partial

from sqlalchemy.orm import mapped_column, Mapped
from sqlalchemy.orm.decl_api import DeclarativeBase
from sqlalchemy.sql.sqltypes import Integer, DateTime

# 創建獲取utc時間的函數
utc_now = partial(datetime.now, timezone.utc)


class BaseModel(DeclarativeBase):
    """基礎模型"""
    __abstract__ = True  # 設置成抽象基類

    id: Mapped[int] = mapped_column(
        Integer,
        primary_key=True,
        autoincrement=True,
        comment="會話ID",
    )
    # 創建時間
    create_time: Mapped[datetime] = mapped_column(
        DateTime,
        default=utc_now,
        comment='創建時間'
    )
    # 更新時間
    update_time: Mapped[datetime] = mapped_column(
        DateTime,
        default=utc_now,
        onupdate=utc_now,
        comment='更新時間'
    )
