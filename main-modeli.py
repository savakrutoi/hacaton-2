from typing import Union

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()


class Item(BaseModel): # создали модель usera наследуем от BaseModel это база фрейморков
    name: str
    price: float
    is_offer: Union[bool, None] = None # тут прописываем переменные которые у класса будут
#Это Pydantic-модель, которая используется в FastAPI для валидации и сериализации данных.
# логику тут лучше не писать


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.put("/items/{item_id}")
def update_item(item_id: int, item: Item):
    return {"item_name": item.name, "item_id": item_id}