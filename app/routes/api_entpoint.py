from fastapi import APIRouter
from fastapi.params import Depends
from pydantic.fields import Deprecated
from sqlalchemy.orm import Session
from app.crud_func import create_user

from app.osnovnoe import Vkuser
from app.models_orm import User
from app.database import get_db
router = APIRouter()

# надо реализовать историю что сначала добовление имен и айди в бд
# потом вуза роли и группы все в табличку user

# написать добовление в базу данны
@router.post("/vk_register/")
def vk_register(vk_user: Vkuser, db: Session = Depends(get_db)):
    return create_user(db, vk_user)  # без .dict()

# @router.post("/vk_register/")
# def vk_register(vk_user: Vkuser, db: Session = Depends(get_db)):
#     user = User(**vk_user.dict())
#     db.add(user)
#     db.commit()
#     db.refresh(user)
#     return {"message": "User saved", "user_id": user.id}
#



