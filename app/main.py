from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
import auth_routes
import managers_routes
import employees_routes

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


