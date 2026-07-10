import asyncio
import logging

from aiogram import Bot, Dispatcher

from bot.config import BOT_TOKEN
from bot.handlers import start, common
from bot.middlewares.auth import AuthMiddleware

logging.basicConfig(level=logging.INFO)


async def main():
    bot = Bot(token=BOT_TOKEN)
    dp = Dispatcher()

    dp.message.middleware(AuthMiddleware())

    dp.include_router(start.router)
    dp.include_router(common.router)

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
