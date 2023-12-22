
from fastapi import FastAPI
import auth

# creating FastAPI object
app = FastAPI()

app.include_router(auth.router)

@app.get("/home", tags=["Hello World"])
async def home():
    return {"Message":"Hello World"}

