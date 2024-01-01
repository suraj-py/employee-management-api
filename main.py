import os
import uvicorn
from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv

from app import auth_routes
from app import managers_routes
from app import employees_routes

load_dotenv()

# creating FastAPI object
app = FastAPI(
    title = "Employee Management API",
    description = "Helps you manage employee details at your company.",
    version="0.0.1",
    contact={
        "name": "Suraj Mhatre",
        "url": "https://github.com/suraj-py",
        "email": "surajrmhatre99@gmail.com",
    },
    )
origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/", tags=["Root"])
async def home():
    return {"Message":"Welcome Employee Management API"}

app.include_router(auth_routes.router)
app.include_router(managers_routes.router)
app.include_router(employees_routes.router)


if __name__ == "__main__":
    try:
        port = os.getenv("PORT", "5000")
        port = int(port)
    except ValueError:
        port = 5000
    uvicorn.run("main:app", host='0.0.0.0', port=port, log_level="info")
