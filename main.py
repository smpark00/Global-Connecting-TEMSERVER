# main.py
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import api

app = FastAPI()

# CORS 설정
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 모든 도메인에서의 접근을 허용하려면 ["*"]로 설정
    allow_credentials=True,
    allow_methods=["*"],   # 모든 HTTP 메서드를 허용
    allow_headers=["*"],   # 모든 헤더를 허용
)

# 라우터 추가
app.include_router(api.router)

@app.get("/")
async def root():
    return {"message": "Hello, FastAPI!"}
