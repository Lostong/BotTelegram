from aiogram.filters import Command
from aiogram.types.bot_command import BotCommand


ACHIVMENTS = Command("achievement")
MISSIONS = Command("missions")
DESCTIPRION = Command("metro_exodus?")
PHOTO_FOR_GAME = Command("photo")
ANY_GAME = Command("similarygame")

ACHIVMENTS_BOT = BotCommand(command="achievement", description="досягнення")
MISSIONS_BOT = BotCommand(command="missions", description="місії")
DESCTIPRION_BOT = BotCommand(command="metro_exodus?", description="опис гри")
PHOTO_FOR_GAME_BOT = BotCommand(command="photo", description="фото гри")
ANY_GAME_BOT = BotCommand(command="similarygame", description="ігри по типу")


