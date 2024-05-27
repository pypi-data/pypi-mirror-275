import asyncio


class WorldClient:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.reader = None
        self.writer = None

        self.message_data = ""

    async def connect(self):
        self.reader, self.writer = await asyncio.open_connection(self.host, self.port)
        print(f"Connected to server at {self.host}:{self.port}")

    async def send_message(self, message):
        print(f"Sending: {message}")
        self.writer.write(message.encode())
        await self.writer.drain()

    async def listen_server(self):
        while True:
            data = await self.reader.read(100)
            if not data:
                break
            message = data.decode()
            print(f"Received: {message}")

    def handle_input(self):
        self.send_message("This is my measdfsadfssage!")

    async def run(self):
        await self.connect()
        asyncio.create_task(self.listen_server())

        await asyncio.sleep(12)

    def close(self):
        print("Closing connection")
        self.writer.close()
        asyncio.run(self.writer.wait_closed())


if __name__ == "__main__":
    # Example usage
    client = WorldClient('localhost', 8488)
    try:
        asyncio.run(client.run())
    except KeyboardInterrupt:
        client.close()
        print("Client shutdown")
