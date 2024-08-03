import asyncio
import websockets

async def listen(websocket):
    async for message in websocket:
        print(f"Received: {message}")

async def main():
    uri = "ws://localhost:8765"
    async with websockets.connect(uri) as websocket:
        # Start a task to listen for incoming messages
        asyncio.create_task(listen(websocket))

        while True:
            message = input("Enter message: ")
            await websocket.send(message)

if __name__ == "__main__":
    asyncio.run(main())
