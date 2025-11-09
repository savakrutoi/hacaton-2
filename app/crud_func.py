from sqlalchemy.orm import Session
from app.models_orm import User

# ** распоковка это
# user = User(
#     id=123,
#     name="Иван",
#     name_2="Иванов",   -----> это буквально эквивалентно user = User(**user_data)
#     rol="student",
#     univer="МГУ",
#     grupa_starosta=1213
# )
def create_user(db: Session, user_data: dict):
    user = User(**user_data)
    db.add(user)
    db.commit()
    db.refresh(user)



