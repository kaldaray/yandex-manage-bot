import aiohttp

from io import BytesIO
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, CallbackQuery, ContentTypes
from pyisemail import is_email

from keyboards.default import helpKeyboard
from keyboards.inline import folderIdKeyboard
from loader import dp
from loader import bot
from states import UsersQuestion


@dp.message_handler(Command("instances"))
async def bot_start(message: types.Message):
    await message.answer(f'{message.from_user.full_name}. Необходим ваш folderid', reply_markup=ReplyKeyboardRemove())
    await message.answer("Пройдите по ссылке для получения folderid", reply_markup=folderIdKeyboard)
    # Сохраняем первое состояние
    await UsersQuestion.whats_the_problem.set()


@dp.message_handler(text="Запрос в ТП 🧑‍💻")
async def bot_start(message: types.Message):
    await message.answer(f'{message.from_user.full_name}. Необходим ваш folderid', reply_markup=ReplyKeyboardRemove())
    await message.answer("Пройдите по ссылке для получения folderid", reply_markup=folderIdKeyboard)
    # Сохраняем первое состояние
    await UsersQuestion.whats_the_problem.set()


# Ответ на первый вопрос и переход в состояние 2
@dp.message_handler(state=UsersQuestion.whats_the_problem)
async def bot_start(message: types.Message, state: FSMContext):
    wh_th_problem = message.text
    await state.update_data(answer1=wh_th_problem)
    await message.answer(f'{message.from_user.full_name}, опиши свою проблему текстом.')
    await message.answer('Про скриншот спрошу дальше')
    await UsersQuestion.description_problem.set()


@dp.message_handler(text="Есть", state=UsersQuestion)
async def cancel_request(message: types.Message):
    await message.answer("Пришли фото", reply_markup=ReplyKeyboardRemove())
    await UsersQuestion.photo_problem.set()


@dp.message_handler(text="Нет", state=UsersQuestion)
async def cancel_request(message: types.Message, state: FSMContext):
    await state.update_data(photo="None")
    await message.answer(f'{message.from_user.full_name}, оставь свое email!', reply_markup=ReplyKeyboardRemove())
    await state.update_data(answer3=message.chat.full_name)
    # Сохраняем состояние
    await UsersQuestion.email_of_the_applicant.set()
