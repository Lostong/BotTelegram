import asyncio
from telegram import Update
from  telegram.ext import Updater, CommandHandler, CallbackContext
from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode
import logging
import sys
from aiogram.utils.keyboard import ReplyKeyboardBuilder
import json
from jsons import get_missions, get_achievment, get_description,get_csimilyaryty,get_photo
from aiogram import Bot, Dispatcher, types, F
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message, ReplyKeyboardMarkup, KeyboardButton
from config import BOT_TOKEN as TOKEN
import keyboard as kb
import state
import models
from command import (
    ACHIVMENTS,
    PHOTO_FOR_GAME,
    DESCTIPRION,
    MISSIONS,
    MISSIONS_BOT,
    PHOTO_FOR_GAME_BOT,
    ACHIVMENTS_BOT,
    DESCTIPRION_BOT,
    ANY_GAME_BOT,
    ANY_GAME,
)


dp = Dispatcher()

@dp.message(CommandStart())
async def start(message: Message) -> None:
        await message.answer(
        f"Привіт, я Назар (розробник цього бота).\n"
        f"Коли я проходив Metro Exodus я багато чого не знав і через це проходження затягнулося на довго\n"
        f"Тож, щоб не повторювати мої похибки, пропоную вам ознайомитись з моїм ботом-посібником по цій чудовій грі",
        reply_markup=kb.startMenu
    )


@dp.message()
async def echo_handler(message: Message) -> None:
    text = message.text
    if message.text == "Досягнення":
        await message.answer("Ви обрали Досягнення.",

        reply_markup= kb.ahivka1)

        async def reply_builder(message: types.Message):
            await message.answer(
            "Оберіть досягнення що вас цікавить:",
        )
    elif message.text == ">>>":
                await message.answer("Друга сторінка місій",
                reply_markup=kb.ahivka2)
    elif message.text == "<<<":
                await message.answer("Перша сторінка місій",
                reply_markup=kb.ahivka1)





    elif message.text == "Чому варто пограти":
        text = message.text
        await message.answer("Що саме ви хочете дізнатись",
            reply_markup=kb.how_play)
        if message.text == "game_info":
            pass
        elif message.text == "setting":
            pass
        elif message.text == "gameplay":
            pass
        elif message.text == "story":
            pass
        elif message.text == "why_play":
            pass







    elif message.text == "Фото гри":
        await message.answer("Ви обрали Фото гри. Ось фото з гри...")
        text = message.text



    elif message.text == "Місії":
        await message.answer("Ви обрали Місії. Ось список місій...",
            reply_markup=kb.mission)
        text = message.text
        if message.text == "Moscow":
            pass
        elif message.text == "The Volga":
            pass
        elif message.text == "Yamantau":
            pass
        elif message.text == "The Caspian":
            pass
        elif message.text == "The Taiga":
            pass
        elif message.text == "The Dead City":
            pass



    elif message.text == "Схожі ігри":
        await message.answer("Ви обрали Схожі ігри. Ось список схожих ігор...",
        reply_markup = kb.any_game1)
        text = message.text

        async def reply_builder(message: types.Message):
            await message.answer(
                "Оберіть досягнення що вас цікавить:",
            )
        if message.text == "":
            pass
        elif message.text == ">>>":
            await message.answer("Друга сторінка місій",
                             reply_markup=kb.any_game2)
        elif message.text == "<<<":
            await message.answer("Перша сторінка місій",
                             reply_markup=kb.any_game1)
    elif message.text == "menu":
        text = message.text
        await message.answer("Ви обрали головне меню",
            reply_markup=kb.startMenu)

    else:
        await message.answer('Ви попали в аномалію')

# @dp.message(lambda message: message.text == "MISSIONS")
# async def missions_handler(message: Message) -> None:
#     missions = get_missions()
#
#     if not missions:
#         await message.answer("Немає доступних місій.")
#         return
#
#
#     keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
#     for mission in missions:
#         keyboard.add(KeyboardButton(text=mission["name"]))
#
#
#     await message.answer("Оберіть місію:", reply_markup=keyboard)

# @dp.message(lambda message: message.text in [mission["name"] for mission in get_missions()])
# async def mission_detail(message: Message) -> None:
#     mission_name = message.text
#     missions = get_missions()
#
#
#     selected_mission = next((mission for mission in missions if mission["name"] == mission_name), None)
#
#     if selected_mission:
#
#         response_text = (
#             f"Місія: {selected_mission['name']}\n"
#             f"Опис: {selected_mission['description']}\n"
#             f"Нюанси: {selected_mission['nuances']}\n"
#             f"Лайфхаки: {selected_mission['lifehacks']}\n"
#         )
#         await message.answer(response_text)
#     else:
#         await message.answer("Місія не знайдена.")




async def main() -> None:
    bot = Bot(token=TOKEN, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    await bot.set_my_commands([
        ACHIVMENTS_BOT,
        # DESCTIPRION_BOT,
        # PHOTO_FOR_GAME_BOT,
        # MISSIONS_BOT,
        # ANY_GAME_BOT,
    ])

    await dp.start_polling(bot)

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
