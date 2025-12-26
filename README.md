# fastapi-live-data
FastAPI application for real-time data processing using WebSockets. Provides a lightweight streaming pipeline to ingest, process, and broadcast live data with low latency

## Starting the server
To start the FastAPI server, run the following command:

```bash
uvicorn main:app
```
## WebSocket Endpoint
The WebSocket endpoint is available at `/ws`. Clients can connect to this endpoint to send and receive real-time data.

## DevTools testing
You can test the WebSocket connection using browser DevTools. Open the console and run the following JavaScript code:
```javascript
const ws = new WebSocket("ws://127.0.0.1:8000/ws");
ws.onmessage = e => console.log(e.data);
ws.onopen = () => ws.send("some test message");
```

