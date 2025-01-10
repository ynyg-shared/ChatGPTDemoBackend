from sqlalchemy.orm.decl_api import DeclarativeBase


class BaseModel(DeclarativeBase):
    """基礎模型"""
    __abstract__ = True  # 設置成抽象基類
