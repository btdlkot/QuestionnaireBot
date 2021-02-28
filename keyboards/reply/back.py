from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

back = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True
)