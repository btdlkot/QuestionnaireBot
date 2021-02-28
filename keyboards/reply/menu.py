from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

menu = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Інфа про мене"),
        ],
        [
            KeyboardButton(text="Налаштування")
        ],
    ],
    resize_keyboard=True
)
