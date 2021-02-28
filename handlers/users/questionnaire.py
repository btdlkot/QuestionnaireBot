from aiogram.dispatcher import FSMContext
from aiogram.types import Message

from loader import dp

from states.Questionnaire import Questions
from states.Menu import Menu

from keyboards.reply import gender_keyboard, menu

from utils.validators import check_name, check_age, check_gender


@dp.message_handler(state=Questions.Name)
async def answer_name(message: Message, state: FSMContext):
    answer = message.text

    if check_name(answer):
        await state.update_data(name=answer)
        await message.answer("Вкажіть Ваш вік")
        await Questions.next()
    else:
        await message.answer("Довжина імені повинна бути від 2 до 20 символів, введіть ім'я знову")


@dp.message_handler(state=Questions.Age)
async def answer_age(message: Message, state: FSMContext):
    answer = message.text
    if check_age(answer):
        await state.update_data(age=answer)
        await message.answer("Вкажіть Ваш гендер", reply_markup=gender_keyboard)
        await Questions.next()
    else:
        await message.answer("Вік повинен бути цілим числом")


@dp.message_handler(state=Questions.Gender)
async def answer_gender(message: Message, state: FSMContext):
    answer = message.text
    await state.update_data(gender=answer)
    if check_gender(answer):
        await message.answer("Ви пройшли анкетування", reply_markup=menu)
        await state.reset_state(with_data=False)
        await Menu.first()
    else:
        await message.answer("Розробник толерантний але для тестовухи треба, щоб ви обрали один з двох гендерів")
