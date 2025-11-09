from fastapi import FastAPI
from app.routes import api_entpoint
from sqlalchemy.orm import Session
from .database import SessionLocal
from app.models_orm import Base
from app.database import engine

app = FastAPI() # объявили наше приложение

app.include_router(api_entpoint.router) # тут установии роутеры

Base.metadata.create_all(bind=engine)



