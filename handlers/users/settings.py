from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp

from states.Menu import Menu
from states.Settings import Settings

from keyboards.reply import back, gender_change_keyboard, menu, settings

from utils.validators import check_name, check_age, check_gender


@dp.message_handler(state=Settings.Main)
async def answer_settings(message: Message, state: FSMContext):
    answer = message.text
    if answer in "Змінити ім'я":
        await message.answer("Введіть нове значення або натисніть «Назад»", reply_markup=back)
        await Settings.Change_name.set()
    elif answer in "Змінити вік":
        await message.answer("Введіть нове значення або натисніть «Назад»", reply_markup=back)
        await Settings.Change_age.set()
    elif answer in "Змінити гендер":
        await message.answer("Введіть нове значення або натисніть «Назад»", reply_markup=gender_change_keyboard)
        await Settings.Change_gender.set()
    elif answer in "Назад":
        await message.answer("Meню: ", reply_markup=menu)
        await state.reset_state(with_data=False)
        await Menu.first()


@dp.message_handler(state=Settings.Change_name)
async def answer_change_name(message: Message, state: FSMContext):
    answer = message.text
    if answer in "Назад":
        await message.answer("Оберіть параметр, який хочете змінити", reply_markup=settings)
        await Settings.Main.set()
    elif check_name(answer):
        await state.update_data(name=answer)
        await message.answer("Ім'я зменено на " + answer, reply_markup=menu)
        await state.reset_state(with_data=False)
        await Menu.Main_menu.set()
    else:
        await message.answer("Довжина імені повинна бути від 2 до 20 символів, введіть ім'я знову")


@dp.message_handler(state=Settings.Change_age)
async def answer_change_age(message: Message, state: FSMContext):
    answer = message.text
    if answer in "Назад":
        await message.answer("Оберіть параметр, який хочете змінити", reply_markup=settings)
        await Settings.Main.set()
    elif check_age(answer):
        await state.update_data(age=answer)
        await message.answer("Вік зменено на " + answer, reply_markup=menu)
        await state.reset_state(with_data=False)
        await Menu.Main_menu.set()
    else:
        await message.answer("Вік повинен бути цілим числом")


@dp.message_handler(state=Settings.Change_gender)
async def answer_change_gender(message: Message, state: FSMContext):
    answer = message.text
    if answer in "Назад":
        await message.answer("Оберіть параметр, який хочете змінити", reply_markup=settings)
        await Settings.Main.set()
    elif check_gender(answer):
        await state.update_data(gender=answer)
        await message.answer("Гендер зменено на " + answer, reply_markup=menu)
        await state.reset_state(with_data=False)
        await Menu.Main_menu.set()
    else:
        await message.answer("Розробник толерантний але для тестовухи треба, щоб ви обрали один з двох гендерів")
