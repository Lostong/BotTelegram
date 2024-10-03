from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.filters.callback_data import CallbackData

class AchivmetCallbackData(CallbackData, prefix="achivmet", sep=";"):
    id: int
    name: str
Menu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='menu'),

        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)
startMenu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='menu'),
            KeyboardButton(text='Досягнення'),
            KeyboardButton(text='Схожі ігри'),
            KeyboardButton(text='Чому варто пограти'),
            KeyboardButton(text='Фото гри'),
            KeyboardButton(text='Місії'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False
)
ahivka1 = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='menu'),
            KeyboardButton(text='Hardcore'),
            KeyboardButton(text='Martian'),
            KeyboardButton(text='Silent Assassin'),
            KeyboardButton(text='Forest Child'),
            KeyboardButton(text='Dukes Fate'),
            KeyboardButton(text='Full Strength'),
            KeyboardButton(text='Friend of the Crew'),
            KeyboardButton(text='Librarian'),
            KeyboardButton(text='Handyman'),
            KeyboardButton(text='Saboteur'),
            KeyboardButton(text='Gunsmith'),
            KeyboardButton(text='>>>'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False

)
ahivka2 = ReplyKeyboardMarkup(
    keyboard= [
        [

            KeyboardButton(text='menu'),
            KeyboardButton(text='Railwayman'),
            KeyboardButton(text='Long-distance Passenger'),
            KeyboardButton(text='Sword of Damocles'),
            KeyboardButton(text='Antibiotic'),
            KeyboardButton(text='Survivalist'),
            KeyboardButton(text='Guide'),
            KeyboardButton(text='Lower the Bridge'),
            KeyboardButton(text='Firebird'),
            KeyboardButton(text='Brakeman'),
            KeyboardButton(text='Last Breath'),
            KeyboardButton(text='<<<'),
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False

)
how_play = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='menu'),
            KeyboardButton(text='game_info'),
            KeyboardButton(text='setting'),
            KeyboardButton(text='gameplay'),
            KeyboardButton(text='story'),
            KeyboardButton(text='why_play'),

        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False

)
mission = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='menu'),
            KeyboardButton(text='Moscow'),
            KeyboardButton(text='The Volga'),
            KeyboardButton(text='Yamantau'),
            KeyboardButton(text='The Caspian'),
            KeyboardButton(text='The Taiga'),
            KeyboardButton(text='The Dead City'),

        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False

)
any_game1 = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='menu'),
            KeyboardButton(text='S.T.A.L.K.E.R.: Shadow of Chernobyl'),
            KeyboardButton(text='Fallout 4'),
            KeyboardButton(text='The Last of Us Part II'),
            KeyboardButton(text='BioShock'),
            KeyboardButton(text='Mad Max'),
            KeyboardButton(text='Far Cry 5'),
            KeyboardButton(text='Rage 2'),
            KeyboardButton(text='Dying Light'),
            KeyboardButton(text='Metro 2033'),
            KeyboardButton(text='Horizon Zero Dawn'),
            KeyboardButton(text='>>>'),

        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False

)
any_game2 = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='menu'),
            KeyboardButton(text='Days Gone'),
            KeyboardButton(text='Escape from Tarkov'),
            KeyboardButton(text='Resident Evil 2 Remake'),
            KeyboardButton(text='Prey'),
            KeyboardButton(text='Half-Life 2'),
            KeyboardButton(text='The Division 2'),
            KeyboardButton(text='The Forest'),
            KeyboardButton(text='Subnautica'),
            KeyboardButton(text='Chernobylite'),
            KeyboardButton(text='<<<'),

        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=False

)

