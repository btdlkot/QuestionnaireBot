from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp

from states.Menu import Menu
from states.Settings import Settings

from keyboards.reply import settings


@dp.message_handler(state=Menu.Main_menu)
async def answer_main_menu(message: Message, state: FSMContext):
    answer = message.text
    if answer in "Інфа про мене":
        data = await state.get_data()
        name = data.get("name")
        age = data.get("age")
        gender = data.get("gender")
        await message.answer("Ім'я: " + name +
                             "\nВік: " + age +
                             "\nГендер: " + gender)
    elif answer in "Налаштування":
        await message.answer("Оберіть параметр, який хочете змінити", reply_markup=settings)
        await state.reset_state(with_data=False)
        await Settings.first()
