from aiogram.dispatcher.filters.state import StatesGroup, State


class Settings(StatesGroup):
    Main = State()
    Change_name = State()
    Change_age = State()
    Change_gender = State()
