from fastapi import FastAPI, WebSocket, WebSocketDisconnect

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Simple FastAPI WebSocket Example"}

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket connected")

    try:
        while True:
            data = await websocket.receive_text()
            await websocket.send_text(f"Message text was: {data}")
    except WebSocketDisconnect:
        print("WebSocket disconnected")

@app.websocket("/ws/json")
async def websocket_json_endpoint(websocket: WebSocket):
    await websocket.accept()
    print("WebSocket connected for JSON")

    try:
        while True:
            data = await websocket.receive_json()
            response = {"received_data": data}
            await websocket.send_json(response)
    except WebSocketDisconnect:
        print("WebSocket disconnected from JSON endpoint")