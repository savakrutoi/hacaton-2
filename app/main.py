from fastapi import FastAPI
from app.routes import api_entpoint

app = FastAPI()

app.include_router(api_entpoint.router)
