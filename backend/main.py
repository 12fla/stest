from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from app.api import auth, scripts, topics, users
from app.utils.database import engine, Base

# 创建数据库表
Base.metadata.create_all(bind=engine)

app = FastAPI(title="Video Script Generator API")

# 配置CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # 生产环境中应该设置具体的前端域名
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# 注册路由
app.include_router(auth.router, prefix="/api/auth", tags=["auth"])
app.include_router(scripts.router, prefix="/api/scripts", tags=["scripts"])
app.include_router(topics.router, prefix="/api/topics", tags=["topics"])
app.include_router(users.router, prefix="/api/users", tags=["users"])

# 根路径
@app.get("/")
def read_root():
    return {"message": "Welcome to Video Script Generator API"}

# 健康检查
@app.get("/health")
def health_check():
    return {"status": "healthy"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)