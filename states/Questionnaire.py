from aiogram.dispatcher.filters.state import StatesGroup, State


class Questions(StatesGroup):
    Name = State()
    Age = State()
    Gender = State()
