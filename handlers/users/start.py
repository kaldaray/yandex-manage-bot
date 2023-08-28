from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from loader import dp
from keyboards.default import helpKeyboard


# Команда /start
@dp.message_handler(CommandStart())
async def bot_start(message: types.Message):
    await message.answer(f'Привет, {message.from_user.full_name}!', reply_markup=helpKeyboard)
    await message.answer('Список доступных комманд ты можешь посмотреть с помощью /help')
    await message.answer('Или используй клавиатуру для отправки запроса')
