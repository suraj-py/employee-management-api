from fastapi import FastAPI

# creating FastAPI object
app = FastAPI()


@app.get("/home", tags=["Hello World"])
async def home():
    return {"Message":"Hello World"}
