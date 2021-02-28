from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

settings = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Змінити ім'я"),
            KeyboardButton(text="Змінити вік")
        ],
        [
            KeyboardButton(text="Змінити гендер")
        ],
        [
            KeyboardButton(text="Назад")
        ],
    ],
    resize_keyboard=True
)
