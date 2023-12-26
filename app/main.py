
from fastapi import FastAPI, Depends
from utils import outh2_scheme
import auth
import app_routes

# creating FastAPI object
app = FastAPI()

app.include_router(auth.router)
app.include_router(app_routes.router)

@app.get("/home", tags=["Hello World"])
async def home(token: str = Depends(outh2_scheme)):
    return {"Message":"Hello World"}

