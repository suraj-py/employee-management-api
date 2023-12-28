
from fastapi import FastAPI, Depends
import auth_routes
import managers_routes
import employees_routes

# creating FastAPI object
app = FastAPI()

app.include_router(auth_routes.router)
app.include_router(managers_routes.router)
app.include_router(employees_routes.router)

@app.get("/home", tags=["Hello World"])
async def home():
    return {"Message":"Hello World"}

