import uvicorn
from fastapi import FastAPI
from app.routes.router import router


app = FastAPI()
app.include_router(router)

# @app.get("/", tags=["test"])
# def greet():
#     return {"hello": "world"}
