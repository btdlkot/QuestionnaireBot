from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

gender_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Жінка"),
            KeyboardButton(text="Чоловік")
        ],
    ],
    resize_keyboard=True
)
