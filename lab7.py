import asyncio
import websockets
import logging

# Налаштування логування для відстеження стану з'єднання
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger("WebSocketClient")


class WebSocketClient:
    def __init__(self):
        self.connection = None

    async def connect(self, url):
        """Встановлює WebSocket-з'єднання за вказаною адресою [cite: 41]"""
        try:
            self.connection = await websockets.connect(url)
            logger.info(f"Підключено до {url}")
        except Exception as e:
            logger.error(f"Помилка підключення: {e}")
            self.connection = None

    async def send_message(self, message):
        """Надсилає повідомлення серверу [cite: 42]"""
        if self.connection:
            try:
                await self.connection.send(message)
                logger.info(f"Надіслано: {message}")
            except websockets.exceptions.ConnectionClosed:
                logger.error("Помилка: З'єднання розірвано сервером.")
        else:
            logger.warning("Помилка: З'єднання не встановлено.")

    async def receive_message(self):
        """Отримує повідомлення від сервера [cite: 43]"""
        if self.connection:
            try:
                response = await self.connection.recv()
                logger.info(f"Отримано: {response}")
                return response
            except websockets.exceptions.ConnectionClosed:
                logger.error("Помилка: З'єднання закрито.")
                return None
        return None

    async def close_connection(self):
        """Закриває WebSocket-з'єднання [cite: 44]"""
        if self.connection:
            await self.connection.close()
            logger.info("З'єднання закрито.")


# Приклад використання класу [cite: 47]
async def main():
    client = WebSocketClient()
    # Використовуємо тестовий сервер з методички [cite: 34]
    uri = "wss://ws.postman-echo.com/raw"

    await client.connect(uri)

    if client.connection:
        await client.send_message("Привіт! Це Назар тестує WebSocket.")
        response = await client.receive_message()
        print(f"\n--- Фінальна відповідь сервера: {response} ---\n")

        await client.close_connection()


if __name__ == "__main__":
    asyncio.run(main())