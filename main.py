import asyncio
import logging
from aiogram.types import BotCommand
from config import dp, bot


async def main():
    await bot.set_my_commands([
        BotCommand(command='start', description='Запустить бота'),
        BotCommand(command='zarplata', description='Зарплата')
    ])

    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
