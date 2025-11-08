# НУЖНО РАЗБИТЬ ВСЕ НА ОТДЕЛЬНЫЕ ПИТОН ФАЙЛЫ 

from typing import Union
from fastapi import FastAPI
from pydantic.v1 import BaseModel
from starlette.authentication import BaseUser
from enum import Enum
from datetime import date, datetime

class Role(str, Enum): # это просто строка с ограниченными значениями
    stutent = 'student'
    teacher = "teacher"
    headman = "headman"
class User(BaseModel):
    id: int
    name: str
    role: Role # поле role должно принимать значение из Role (и когда мы будет кидать запрос мы будет автомато проверять есть ли слово после / в этой строке)

#CЕЙЧАС РАБОТАЮ С НЕЙРОНКОЙ И ДУМАЮ НАД МАШТАБИРУЕМОСТЬЮ В ТЕОРИИ ВНЕСУ ПОЛЯ В User ДЛЯ РЕГЕСТИТРАЦИИ ТАМ ПОЧТА И ТАК ДАЛЕЕ


class Visit(BaseModel):
    id_visit: int
    name_visit: str
    visits: bool

class Lesson(BaseModel):
    id: int
    name_lesson: str
    data_created: date # вот это я прям сам без нейронки чувствую себя бил гейтсом

#УЖЕ НАЧИНАТЬ РАБОАТЬ С БАЗОЙ ДАННЫХ sql alchimy


    created_by: int #кто создал староста или препод


