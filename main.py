from dotenv import load_dotenv, find_dotenv

# 加載 .env 文件
load_dotenv(find_dotenv(raise_error_if_not_found=True))

from fastapi import FastAPI
from fastapi.responses import ORJSONResponse

from apps.chat import router as chat_router
from apps.user import router as user_router

# 創建 FastAPI 應用
app = FastAPI()


@app.get("/")
async def root():
    """根路由"""
    return ORJSONResponse({"message": "Hello World"})


# 導入路由
app.include_router(chat_router)
app.include_router(user_router)
