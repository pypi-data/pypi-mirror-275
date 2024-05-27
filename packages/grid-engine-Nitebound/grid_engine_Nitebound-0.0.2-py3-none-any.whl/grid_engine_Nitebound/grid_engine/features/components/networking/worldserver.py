import asyncio


class WorldServer:
    def __init__(self):
        self.clients = {}  # Stores client connections

    async def handle_client(self, reader, writer):
        addr = writer.get_extra_info('peername')
        self.clients[addr] = (reader, writer)
        print(f"New client connected: {addr}")
        while True:
            data = await reader.read(100)
            if not data:
                break
            message = data.decode()
            print(f"Received from {addr}: {message}")
            await self.parse_message(message, addr)

        print(f"Client disconnected: {addr}")
        writer.close()
        await writer.wait_closed()
        del self.clients[addr]

    async def parse_message(self, message, addr):
        # Simple message parsing. Expand based on your game's protocol.
        if message.startswith("POS"):  # Position update
            # Update player position
            pass
        elif message.startswith("CHAT"):  # Chat message
            # Broadcast chat message to other clients
            print(f"Broadcasting: {message} to {addr}")
            await self.broadcast_message(message, addr)
        else:  # Other message types
            pass

    async def broadcast_message(self, message, sender_addr):
        for addr, (reader, writer) in self.clients.items():
            if addr != sender_addr:
                writer.write(message.encode())
                await writer.drain()

    async def run_server(self, host, port):
        server = await asyncio.start_server(self.handle_client, host, port)
        addr = server.sockets[0].getsockname()
        print(f'Serving on {addr}')

        async with server:
            await server.serve_forever()


if __name__ == "__main__":
    game_server = WorldServer()
    asyncio.run(game_server.run_server('localhost', 8488))
