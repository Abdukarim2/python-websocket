import asyncio
import websockets

async def recive(websocket):
    async for message in websocket:
        await websocket.send(f"your message reversed from server {message}")
        print("message from client", message)

async def server():
    async with websockets.serve(recive, "localhost", 8000):
        await asyncio.Future() 

print("ws server is running on localhost:8000")
asyncio.run(server())
