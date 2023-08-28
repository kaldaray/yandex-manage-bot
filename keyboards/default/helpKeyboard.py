from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

helpKeyboard = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text="Compute Cloud 🧑‍💻"),
            KeyboardButton(text="Команды бота 🙋‍♂️"),
        ],
    ],
    resize_keyboard=True
)