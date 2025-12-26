# fastapi-live-data
FastAPI application for real-time data processing using WebSockets. Provides a lightweight streaming pipeline to ingest, process, and broadcast live data with low latency

## Starting the server
To start the FastAPI server, run the following command:

```bash
uvicorn main:app
```


## WebSocket Endpoints
This project provides two simple WebSocket endpoints implemented in `main.py`:

- `/ws` — accepts plain text messages and echoes them back as text.
- `/ws/json` — accepts JSON payloads and responds with a JSON object containing the received data.


## Testing the WebSocket endpoints from the browser
You can test either endpoint from the browser DevTools console.

Plain text example (original):

```javascript
const ws = new WebSocket("ws://127.0.0.1:8000/ws");
ws.onmessage = e => console.log(e.data);
ws.onopen = () => ws.send("some test message");
```

JSON example (new `/ws/json` endpoint):

```javascript
const ws = new WebSocket("ws://127.0.0.1:8000/ws/json");
const testJson = {
  "event": "trade",
  "data": {
    "symbol": "BTCUSD",
    "price": 43250.12,
    "timestamp": "2025-03-26T12:00:00Z"
  }
};
ws.onmessage = e => console.log("RESPONSE:", e.data);
ws.onopen = () => {
  ws.send(JSON.stringify(testJson));
};
```

## Quick troubleshooting
- If the WebSocket fails to connect, verify the server is running and listening on `127.0.0.1:8000` and that no firewall or proxy is blocking the connection.
- If you see JSON parsing errors, confirm that the client sends valid JSON (use `JSON.stringify`).

