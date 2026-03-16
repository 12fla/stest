import os
from pydantic_settings import BaseSettings
from typing import Optional

class Settings(BaseSettings):
    """应用配置"""
    # 应用设置
    APP_NAME: str = "Video Script Generator"
    APP_VERSION: str = "1.0.0"
    
    # 数据库设置
    DATABASE_URL: str = "sqlite:///./video_script.db"
    
    # 安全设置
    SECRET_KEY: str = "your-secret-key-here"
    ALGORITHM: str = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES: int = 30
    
    # API设置
    API_PREFIX: str = "/api"
    
    # 外部API设置
    DEEPSEEK_API_BASE: str = "https://api.deepseek.com/v1"
    DEEPSEEK_MODEL: str = "deepseek-chat"
    
    class Config:
        env_file = ".env"
        case_sensitive = True

# 创建全局配置实例
settings = Settings()