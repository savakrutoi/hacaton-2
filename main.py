#код с 1- это просто запуски с документации (тоже разбираюсь просто первый раз с FastApi)
from typing import Union # анатация типов переменная может быть и str и int (для удобства короче)

from fastapi import FastAPI

app = FastAPI() # это сделали приложение

# Теперь переменная app — это основной объект твоего веб-сервера.
# Через него ты:
# 	•	добавляешь маршруты (эндпоинты),
# 	•	обрабатываешь запросы,
# 	•	настраиваешь middleware, события, документацию и т.д.


@app.get("/") # когда переходит по / то мы выводим return {"Hello": "World"}
def read_root():
    return {"Hello": "World"}
    # когда обращаемся к корню сайта выполни эту функцию


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}
    # item_id определяем в модели (основной класс где прописываем что это)
    # но в этом случае мы просто берем item_id и выводим его

# from pydantic import BaseModel
# вот например работа модели и функции вместе с ней
# class Item(BaseModel):
#     name: str
#     price: float
#
# @app.post("/items/")
# def create_item(item: Item):
#     return item

# после fastapi dev main.py в терминале
# http://127.0.0.1:8000/docs
#http://127.0.0.1:8000/ вот эти запросы в браузере прокидуй

