
from fastapi import FastAPI
from app.routes.users import router as user_router
from app.database import engine
from app.models import Base

Base.metadata.create_all(bind=engine)

app = FastAPI()

@app.get("/")
def home():
    return {"message": "Project 6 with database"}

app.include_router(user_router)
