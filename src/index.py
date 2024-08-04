from typing import Union

from fastapi import FastAPI, WebSocket

app = FastAPI()

@app.get("/")
async def talk_with_groq():
    return {"Hello": "World"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = await websocket.receive_text()
        await websocket.send_text(f"Message received: {data}")