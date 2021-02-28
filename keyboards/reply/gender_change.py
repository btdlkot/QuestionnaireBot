from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

gender_change_keyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Жінка"),
            KeyboardButton(text="Чоловік")
        ],
        [
            KeyboardButton(text="Назад"),
        ]
    ],
    resize_keyboard=True
)
