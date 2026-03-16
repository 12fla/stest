from fastapi import APIRouter, Depends, HTTPException
from typing import List, Dict

from app.api.auth import get_current_user
from app.services.topic_analyzer import TopicAnalyzer

router = APIRouter()


@router.get("/hot")
def get_hot_topics(
    platform: str = "all",
    current_user = Depends(get_current_user)
) -> List[Dict]:
    """获取热点话题"""
    analyzer = TopicAnalyzer()
    topics = analyzer.get_hot_topics(platform)
    return topics


@router.get("/trend/{topic}")
def analyze_topic_trend(
    topic: str,
    current_user = Depends(get_current_user)
) -> Dict:
    """分析话题趋势"""
    analyzer = TopicAnalyzer()
    trend = analyzer.analyze_topic_trend(topic)
    return trend