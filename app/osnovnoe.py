from typing import Union
from fastapi import FastAPI
from typing import List
from pydantic.v1 import BaseModel
from starlette.authentication import BaseUser
from enum import Enum
from datetime import date, datetime

app = FastAPI()

class Role(str, Enum):
    student = 'student'
    teacher = "teacher"
    headman = "headman"

class Vkuser(BaseModel): # вот это тупо полученние от вк
    max_id: int
    name: str
    name_2: str
    rol: Role
    univer: str
    gruppa_prepod: List[int] = []  # по умолчанию пустой список
    grupa_starosta: int
    # дописать инфу касательно остальный полей что бы 422 не вылазила

class Visit(BaseModel):
    id_visit: int
    name_visit: str
    visits: bool

class Lesson(BaseModel):
    id: int
    name_lesson: str
    data_created: date # вот это я прям сам без нейронки чувствую себя бил гейтсом