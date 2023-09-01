from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

ycTokenKeyboad = InlineKeyboardMarkup(inline_keyboard=[
    [
        InlineKeyboardButton(text="Получить token", url="https://oauth.yandex.com/authorize?response_type=token&client_id=1a6990aa636648e9b2ef855fa7bec2fb")
    ]
])
