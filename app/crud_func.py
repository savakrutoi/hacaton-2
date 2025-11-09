from sqlalchemy.orm import Session
from app.models_orm import User
from app.osnovnoe import Vkuser
# ** распоковка это
# user = User(
#     id=123,
#     name="Иван",
#     name_2="Иванов",   -----> это буквально эквивалентно user = User(**user_data)
#     rol="student",
#     univer="МГУ",
#     grupa_starosta=1213
# )
def create_user(db: Session, vk_user: Vkuser):
    user = User(
        name=vk_user.name,
        name_2=vk_user.name_2,
        rol=vk_user.rol.value,  # если Enum
        univer=vk_user.univer,
        max_id=vk_user.max_id,
        gruppa_prepod=vk_user.gruppa_prepod,
        grupa_starosta=vk_user.grupa_starosta
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user




