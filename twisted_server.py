import asyncio
import websockets

connected_clients = set()

async def handler(websocket, path):
    # Register the new client
    connected_clients.add(websocket)
    try:
        async for message in websocket:
            # Broadcast the received message to all clients
            await asyncio.wait([client.send(message) for client in connected_clients if client != websocket])
    except websockets.ConnectionClosed:
        print(f"Client disconnected")
    finally:
        # Unregister the client
        connected_clients.remove(websocket)

async def main():
    async with websockets.serve(handler, "localhost", 8765):
        await asyncio.Future()  # Run forever

if __name__ == "__main__":
    asyncio.run(main())
