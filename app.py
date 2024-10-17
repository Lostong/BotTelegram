import asyncio
import logging
import sys

from aiogram import Bot, Dispatcher
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.client.session.aiohttp import AiohttpSession

from config import BOT_TOKEN as TOKEN
from hendlers import router


dp = Dispatcher()


# Ініціалізація проксі-сервера
session = AiohttpSession(proxy='http://proxy.server:3128')


async def main() -> None:
    dp.include_router(router)
    bot = Bot(token=TOKEN,
              session=session,
              default=DefaultBotProperties(parse_mode=ParseMode.HTML))


    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())