from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup

class MissionsFrom(StatesGroup):
    name = State()
    description = State()
    how_to_achieve = State()
