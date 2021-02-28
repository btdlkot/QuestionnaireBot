from aiogram.types import Message

from utils.db import tg_analytic


async def stat(message: Message):
    tg_analytic.statistics(message.chat.id, message.text)
