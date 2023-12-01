import asyncio
import logging
from aiogram import F, types
from aiogram.filters import Command
from config import dp, bot
from pprint import pprint


async def on_startup(dispatcher):
    pprint("Bot started")


@dp.message(Command("start"))
async def cmd_start(message: types.Message):
    kb = types.ReplyKeyboardMarkup(
        keyboard=[[
            types.KeyboardButton(
                text="Отправить мой номер",
                request_contact=True)
        ]],
        resize_keyboard=True,
    )
    await message.answer(
        f"Привет, {message.from_user.full_name}! Для начала, отправьте нам ваш номер",
        reply_markup=kb,
    )


@dp.message(Command("zarplata"))
async def cmd_zarplata(message: types.Message):
    # get zp from DB by message.from_user.id
    await message.answer("Зарплата")


@dp.message(F.contact)
async def echo(message: types.Message):
    # if message.contact is not None:
    kb = types.ReplyKeyboardRemove()
    pprint(message.contact)
    # save to DB message.contact.phone_number and message.contact.user_id
    await message.answer("Спасибо за заявку! Мы Вам ответим после проверки данных", reply_markup=kb)


async def main():
    await bot.set_my_commands(
        [
            types.BotCommand(command="start", description="Старт, отправка номера"),
            types.BotCommand(command="zarplata", description="Зарплата"),
        ]
    )
    dp.startup.register(on_startup)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
