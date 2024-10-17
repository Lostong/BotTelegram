from aiogram.types import KeyboardButton, InlineKeyboardMarkup
from aiogram.utils.keyboard import ReplyKeyboardMarkup, InlineKeyboardButton


main = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Чому варто пограти"),KeyboardButton(text="Схожі ігри")],
    [KeyboardButton(text="Місії"), KeyboardButton(text="Досягнення")],
    [KeyboardButton(text="Зворотній звязок"),KeyboardButton(text="Усі кінцівки")],
    [KeyboardButton(text="Меми для IT-шніков😂")]
],
resize_keyboard=True,
)
setting = InlineKeyboardMarkup(inline_keyboard=[
    [InlineKeyboardButton(text="YouTube", url="https://www.youtube.com/@lostong7729")]
    ])


games = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="S.T.A.L.K.E.R."),KeyboardButton(text="Fallout 4")],
    [KeyboardButton(text="Dying Light"), KeyboardButton(text="The Last of Us Part II")],
    [KeyboardButton(text="Horizon Zero Dawn"), KeyboardButton(text="Chernobylite")],
    [KeyboardButton(text="Інші ігри"),KeyboardButton(text="Меню")]
],
resize_keyboard=True
)
misions_detal = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Погана")]
])
mision = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Москва"),KeyboardButton(text="Волга")],
    [KeyboardButton(text="Ямантау"),KeyboardButton(text="Каспій")],
    [KeyboardButton(text="Тайга"),KeyboardButton(text="Мертве місто")],
    [KeyboardButton(text="Меню")]

],
resize_keyboard=True

)
end = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Оптимістичний фінал"),KeyboardButton(text="Фінал з Дімою")],
    [KeyboardButton(text="Песимістичний фінал"),KeyboardButton(text="Фінал з Мілею")],
    [KeyboardButton(text="Меню")],
])
resize_keyboard=True


achivm = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="Паспорт"),KeyboardButton(text="Не забудь про нас"),KeyboardButton(text="Смертельний холод"),KeyboardButton(text="Вирушай у мандри"),KeyboardButton(text="Переможець")],
    [KeyboardButton(text="Спостерігач"),KeyboardButton(text="Грішник"),KeyboardButton(text="Тихий вбивця"),KeyboardButton(text="Секрети"),KeyboardButton(text="Життя за життя")],
    [KeyboardButton(text="Снайпер"), KeyboardButton(text="Найкращий друг"), KeyboardButton(text="Мисливець за скарбами"), KeyboardButton(text="Секрети народу"),KeyboardButton(text="Тотальна війна")],
    [KeyboardButton(text="Меню")],
])
mems = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text="1"),KeyboardButton(text="2"),KeyboardButton(text="3"),KeyboardButton(text="4"),KeyboardButton(text="5")],
    [KeyboardButton(text="6"),KeyboardButton(text="7"),KeyboardButton(text="8"),KeyboardButton(text="9"),KeyboardButton(text="10")],
    [KeyboardButton(text="11"), KeyboardButton(text="12"), KeyboardButton(text="13"), KeyboardButton(text="14"),KeyboardButton(text="15")],
    [KeyboardButton(text="Меню")],

],
    resize_keyboard=True
)


