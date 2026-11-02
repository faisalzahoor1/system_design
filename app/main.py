from fastapi import FastAPI
from app.databases.mongo_connection import lifespan


app = FastAPI(
    title = "Student Management API",
    version = "1.0.0",
    lifespan = lifespan
)


@app.get('/')
async def home_api():
    return {"message":"Student Management API is running"}