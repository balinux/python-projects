import asyncio
import websockets

async def connect_to_server():
    # uri = "ws://localhost:3000"
    uri = "ws://172.16.211.62:4000"
    async with websockets.connect(uri) as websocket:
        # Menerima pesan dari server
        message_from_server = await websocket.recv()
        print(f"Message from server: {message_from_server}")

        # Mengirim pesan ke server
        message_to_server = "Hello, server!"
        await websocket.send(message_to_server)
        print(f"Message to server sent: {message_to_server}")

asyncio.get_event_loop().run_until_complete(connect_to_server())
