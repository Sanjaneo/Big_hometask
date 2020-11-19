import aiogram
import asyncio
import config
import handler


loop = asyncio.get_event_loop()
bot = aiogram.Bot(config.token, parse_mode="HTML")
dp = aiogram.Dispatcher(bot, loop=loop)

if __name__ == "__main__":
    aiogram.executor.start_polling(handler.dp, on_startup=handler.send_to_admin)
