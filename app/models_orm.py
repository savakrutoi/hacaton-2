# работа с базаой данных потому что надо первую инфу по юзеру сохранять куда то фамилия имя
# выбор универа
from sqlalchemy import create_engine, Integer, Column, JSON
from typing import List
from typing import Optional
from sqlalchemy import ForeignKey
from sqlalchemy import String
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
from sqlalchemy.orm import relationship

class Base(DeclarativeBase):
    pass

# class MSUGroup(Base):
#     __tablename__ = "msu_groups"
#
#     id = Column(Integer, primary_key=True)
#     group_numbers = ["1213", "3413", "23142", "342342", "0092"]
#     #номер группы
#     user_ids = Column(JSON, default=[])         # список пользователей (из таблицы User), пока пустой
#
# # Создаем базу данных для МГУ
#
# SessionLocal = sessionmaker(bind=engine)
# Base.metadata.create_all(engine)
#

class User(Base):
    __tablename__ = "user"
    id: Mapped[int] = mapped_column(primary_key=True)
    max_id: Mapped[int] = mapped_column(Integer)
    name: Mapped[str] = mapped_column(String(30))
    name_2: Mapped[str] = mapped_column(String(30))
    rol: Mapped[str] = mapped_column(String(30))
    univer: Mapped[str] = mapped_column(String(30))
    gruppa_prepod: Mapped[list[int]] = mapped_column(JSON, default=[])
    grupa_starosta: Mapped[int] = mapped_column(Integer)

    def __repr__(self):
        return f"User(id={self.id}, name={self.name}, name_2={self.name_2}, rol={self.rol})"

# class UNIVER(Base):
#     __tablename__ = "UNIVER"
#
#
#     # написать связь по универу связку
#
#
#
#     id: Mapped[int] = mapped_column(primary_key=True)
#     user_id: Mapped[int] = mapped_column(ForeignKey("user_account.id"))
#     user: Mapped["User"] = relationship(back_populates="addresses")
#     def __repr__(self) -> str:
#         return f"Address(id={self.id!r}, email_address={self.email_address!r})"