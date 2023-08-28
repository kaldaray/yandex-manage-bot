from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

cancelKeyboard = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Отменить", callback_data="cancel")
    ]
])
