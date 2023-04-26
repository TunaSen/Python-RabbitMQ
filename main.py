from fastapi import FastAPI
from .model import Message
app = FastAPI()


@app.get("/")
async def root():

    return {"message": "Hello World"}


@app.get("/hello/{name}")
async def say_hello(name: str):
    return {"message": f"Hello {name}"}



@app.get()
async def sendMessage(message: Message):
    return

