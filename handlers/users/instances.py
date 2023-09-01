import sys

import aiohttp

from io import BytesIO
from aiogram import types
from aiogram.dispatcher import FSMContext
from aiogram.dispatcher.filters import Command
from aiogram.types import ReplyKeyboardRemove, CallbackQuery, ContentTypes
from pyisemail import is_email

from keyboards.default import helpKeyboard
from keyboards.inline import folderIdKeyboard
from keyboards.inline import ycTokenKeyboad
from loader import dp
from loader import bot
# States
from states import UsersQuestion
from states import FolderId
from utils.back import manageYC

listAnswers = []

@dp.message_handler(Command("instances"))
async def bot_start(message: types.Message):
    await message.answer(f'{message.from_user.full_name}. Необходим ваш folderid', reply_markup=ReplyKeyboardRemove())
    await message.answer("Пройдите по ссылке для получения folderid", reply_markup=folderIdKeyboard)
    # Сохраняем первое состояние
    await FolderId.id.set()


@dp.message_handler(text="Compute Cloud 🧑‍💻")
async def bot_start(message: types.Message):
    await message.answer(f'{message.from_user.full_name}. Необходим ваш folderid', reply_markup=ReplyKeyboardRemove())
    await message.answer("Пройдите по ссылке для получения folderid", reply_markup=folderIdKeyboard)
    # Сохраняем первое состояние
    await FolderId.id.set()


# Ответ на первый вопрос и переход в состояние 2
@dp.message_handler(state=FolderId.id)
async def bot_start(message: types.Message, state: FSMContext):
    listAnswers.append(message.text)
    await state.update_data(answer1=message.text)
    await message.answer(f'{message.from_user.full_name}, Необходим YC token $(yc iam create-token)', reply_markup=ycTokenKeyboad)
    await FolderId.yc_iam_token.set()


@dp.message_handler(state=FolderId.yc_iam_token)
async def cancel_request(message: types.Message, state: FSMContext):
    listAnswers.append(message.text)
    await state.update_data(answer2=message.text)
    await message.answer("Получаю список машин")
    manageYC.main_function(listAnswers)
    await FolderId.yc_list_instances.set()


@dp.message_handler(text="Нет", state=FolderId)
async def cancel_request(message: types.Message, state: FSMContext):
    await state.update_data(photo="None")
    await message.answer(f'{message.from_user.full_name}, оставь свое email!', reply_markup=ReplyKeyboardRemove())
    await state.update_data(answer3=message.chat.full_name)
    # Сохраняем состояние
    await UsersQuestion.email_of_the_applicant.set()
