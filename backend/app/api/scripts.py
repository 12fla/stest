from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from app.utils.database import get_db
from app.api.auth import get_current_user
from app.models.user import User
from app.models.script import Script
from app.services.script_generator import ScriptGenerator

router = APIRouter()


@router.post("/generate")
def generate_script(
    subject: str,
    video_length: float = 1.0,
    creativity: float = 0.7,
    api_key: str = None,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """生成视频脚本"""
    if not api_key:
        raise HTTPException(status_code=400, detail="DeepSeek API key is required")
    
    try:
        # 生成脚本
        generator = ScriptGenerator(api_key)
        search_result, title, script_content = generator.generate_script(
            subject=subject,
            video_length=video_length,
            creativity=creativity
        )
        
        # 保存脚本到数据库
        new_script = Script(
            user_id=current_user.id,
            title=title,
            content=script_content,
            subject=subject,
            video_length=int(video_length * 60),  # 转换为秒
            creativity=creativity
        )
        db.add(new_script)
        db.commit()
        db.refresh(new_script)
        
        return {
            "id": new_script.id,
            "title": title,
            "script": script_content,
            "search_result": search_result,
            "created_at": new_script.created_at
        }
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"脚本生成失败: {str(e)}")


@router.get("/my")
def get_my_scripts(
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
) -> List[Script]:
    """获取当前用户的脚本"""
    scripts = db.query(Script).filter(Script.user_id == current_user.id).order_by(Script.created_at.desc()).all()
    return scripts


@router.get("/{script_id}")
def get_script(
    script_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """获取指定脚本"""
    script = db.query(Script).filter(Script.id == script_id, Script.user_id == current_user.id).first()
    
    if not script:
        raise HTTPException(status_code=404, detail="脚本不存在")
    
    return script


@router.delete("/{script_id}")
def delete_script(
    script_id: int,
    current_user = Depends(get_current_user),
    db: Session = Depends(get_db)
):
    """删除脚本"""
    script = db.query(Script).filter(Script.id == script_id, Script.user_id == current_user.id).first()
    
    if not script:
        raise HTTPException(status_code=404, detail="脚本不存在")
    
    db.delete(script)
    db.commit()
    
    return {"message": "脚本删除成功"}