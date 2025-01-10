from typing import Annotated

from fastapi.param_functions import Depends
from fastapi.responses import Response, ORJSONResponse
from fastapi.routing import APIRouter
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.exc import SQLAlchemyError
from sqlalchemy.ext.asyncio.session import AsyncSession
from sqlalchemy.sql import exists, select

from core.db import get_session
from .items import AuthItem, TokenItem
from .models import UserModel

router = APIRouter(prefix="/user", tags=["user"])
# 認證方案
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="user/login")


@router.post("/register")
async def register(
        item: AuthItem,
        db_session: Annotated[AsyncSession, Depends(get_session)]
) -> Response:
    """
    註冊
    :param item: 請求數據
    :param db_session: 數據庫會話
    :return: 響應
    """
    # 判斷用戶是否已經存在
    result = await db_session.execute(exists(UserModel).where(UserModel.username == item.username).select())
    # 如果用戶已經存在就返回錯誤信息
    if result.scalar():
        return ORJSONResponse({"message": "user already exists"}, status_code=400)
    try:
        # 創建用戶
        user = UserModel(username=item.username, password=item.password)
        db_session.add(user)
        await db_session.commit()
    except SQLAlchemyError:
        # 如果出現異常就回滾
        await db_session.rollback()
    return ORJSONResponse({"message": "register"})


@router.post("/login", response_model=TokenItem)
async def login(
        item: AuthItem,
        db_session: Annotated[AsyncSession, Depends(get_session)]
) -> ORJSONResponse | TokenItem:
    """
    登錄
    :param item: 請求數據
    :param db_session: 數據庫會話
    :return: 響應
    """
    # 查詢用戶
    result = await db_session.execute(select(UserModel).where(UserModel.username == item.username))
    user = result.scalar()
    # 如果用戶不存在就返回錯誤信息
    if not user:
        return ORJSONResponse({"message": "user not exists"}, status_code=400)
    # 如果密碼不正確就返回錯誤信息
    if not user.verify_password(item.password):
        return ORJSONResponse({"message": "password error"}, status_code=400)
    # 生成token
    token = user.create_token()
    return TokenItem(access_token=token, token_type="bearer")
