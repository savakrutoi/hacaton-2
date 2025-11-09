from typing import Union
from fastapi import FastAPI
from pydantic.v1 import BaseModel
from starlette.authentication import BaseUser
from enum import Enum
from datetime import date, datetime

app = FastAPI()

class Vkuser(BaseModel): # вот это тупо полученние от вк
    vk_id: int
    first_name: str
    last_name: str
    #


class Role(str, Enum):
    stutent = 'student'
    teacher = "teacher"
    headman = "headman"

class Visit(BaseModel):
    id_visit: int
    name_visit: str
    visits: bool

class Lesson(BaseModel):
    id: int
    name_lesson: str
    data_created: date # вот это я прям сам без нейронки чувствую себя бил гейтсом



