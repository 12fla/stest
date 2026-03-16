from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.utils.database import get_db
from app.api.auth import get_current_user
from app.models.user import User
from app.services.auth_service import AuthService

router = APIRouter()


@router.get("/profile")
def get_user_profile(
    current_user = Depends(get_current_user)
):
    """获取用户个人资料"""
    return {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email,
        "created_at": current_user.created_at
    }


@router.put("/profile")
def update_user_profile(
    email: str = None,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """更新用户个人资料"""
    if email:
        # 检查邮箱是否已被使用
        existing_user = db.query(User).filter(User.email == email, User.id != current_user.id).first()
        if existing_user:
            raise HTTPException(status_code=400, detail="邮箱已被使用")
        
        current_user.email = email
        db.commit()
        db.refresh(current_user)
    
    return {"message": "个人资料更新成功", "user": {
        "id": current_user.id,
        "username": current_user.username,
        "email": current_user.email
    }}