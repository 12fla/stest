from sqlalchemy import Column, Integer, String, DateTime, Text
from sqlalchemy.sql import func
from app.utils.database import Base

class Topic(Base):
    """热点话题模型"""
    __tablename__ = "topics"
    
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(200), nullable=False)
    source = Column(String(50), nullable=False)  # 来源平台
    heat = Column(Integer, nullable=False)  # 热度值
    summary = Column(Text, nullable=True)  # 话题摘要
    created_at = Column(DateTime(timezone=True), server_default=func.now())
    updated_at = Column(DateTime(timezone=True), onupdate=func.now())