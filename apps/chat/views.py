from typing import Annotated

from fastapi.param_functions import Depends
from fastapi.params import Query
from fastapi.responses import ORJSONResponse
from fastapi.routing import APIRouter
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.sql import select, and_, delete

from core.db import get_session
from .models import ConversationsModel
from ..user.models import UserModel

# 創建路由器
router = APIRouter(prefix="/chat", tags=["chat"])


@router.get("/conversations")
async def get_conversations(
        user: Annotated[UserModel, Depends(UserModel.get_user)],
        db_session: Annotated[AsyncSession, Depends(get_session)],
        limit: int = Query(10, title="每頁條數", description="每頁條數", ge=1, le=100),
        offset: int = Query(0, title="偏移量", description="偏移量", ge=0),
):
    """獲取對話列表"""
    # 創建查詢語句
    query = select(ConversationsModel).where(and_(
        ConversationsModel.user_id == user.id,
        ConversationsModel.title.isnot(None),
    )).offset(offset).limit(limit)
    # 查詢數據
    result = await db_session.execute(query)
    conversations = result.scalars().all()
    # 拼接返回數據
    data = [{"id": conversation.id, "title": conversation.title} for conversation in conversations]
    return ORJSONResponse(data)


@router.post("/conversations")
async def create_conversation(
        user: Annotated[UserModel, Depends(UserModel.get_user)],
        db_session: Annotated[AsyncSession, Depends(get_session)]
):
    """創建對話"""
    conversation = ConversationsModel(user_id=user.id)
    db_session.add(conversation)
    await db_session.commit()
    return ORJSONResponse({"id": conversation.id, "title": conversation.title})


@router.delete("/conversations/{conversation_id}")
async def delete_conversation(
        user: Annotated[UserModel, Depends(UserModel.get_user)],
        db_session: Annotated[AsyncSession, Depends(get_session)],
        conversation_id: int = Query(..., title="對話ID", description="對話ID"),
):
    """刪除對話"""
    query = delete(ConversationsModel).where(and_(
        ConversationsModel.user_id == user.id,
        ConversationsModel.id == conversation_id,
    ))
    await db_session.execute(query)
    await db_session.commit()
    return ORJSONResponse({"message": "刪除成功"})
