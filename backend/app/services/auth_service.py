from typing import Optional
from sqlalchemy.orm import Session
from app.models.user import User
from app.utils.security import verify_password, get_password_hash

class AuthService:
    """认证服务"""
    
    def register_user(self, db: Session, username: str, email: str, password: str) -> User:
        """注册新用户"""
        # 检查用户名是否已存在
        existing_user = db.query(User).filter(
            (User.username == username) | (User.email == email)
        ).first()
        
        if existing_user:
            raise ValueError("用户名或邮箱已存在")
        
        # 创建新用户
        hashed_password = get_password_hash(password)
        new_user = User(
            username=username,
            email=email,
            password_hash=hashed_password
        )
        
        db.add(new_user)
        db.commit()
        db.refresh(new_user)
        
        return new_user
    
    def authenticate_user(self, db: Session, username: str, password: str) -> Optional[User]:
        """验证用户身份"""
        user = db.query(User).filter(User.username == username).first()
        
        if not user:
            return None
        
        if not verify_password(password, user.password_hash):
            return None
        
        return user
    
    def get_user_by_id(self, db: Session, user_id: int) -> Optional[User]:
        """根据ID获取用户"""
        return db.query(User).filter(User.id == user_id).first()
    
    def get_user_by_username(self, db: Session, username: str) -> Optional[User]:
        """根据用户名获取用户"""
        return db.query(User).filter(User.username == username).first()