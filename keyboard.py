from aiogram.types import ReplyKeyboardMarkup, InlineKeyboardMarkup, KeyboardButton, InlineKeyboardButton
from aiogram.utils.keyboard import ReplyKeyboardBuilder
startMenu = ReplyKeyboardMarkup(
    keyboard= [
        [
            KeyboardButton(text='Назад'),
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

            KeyboardButton(text='Immortal'),
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