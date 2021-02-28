from aiogram.dispatcher.filters.builtin import CommandStart
from aiogram.types import Message, ReplyKeyboardRemove

from loader import dp

from states.Questionnaire import Questions


@dp.message_handler(CommandStart())
async def bot_start(message: Message):
    await message.answer(f"Привіт!\n"
                         "Для початку напишіть Ваше ім'я", reply_markup=ReplyKeyboardRemove())
    await Questions.first()
