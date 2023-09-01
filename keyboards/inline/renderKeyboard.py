from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


def render_keyboard(list):
    buttons = []
    for each in list:
        # button_list.append(InlineKeyboardButton(each, callback_data=each))
        buttons.append(InlineKeyboardButton(each[0], callback_data=each[0]))
# renderKeyboard = InlineKeyboardMarkup(inline_keyboard=[
#     [
#         InlineKeyboardButton(text="Просмотреть свой folder_id", url="https://console.cloud.yandex.ru/folders/")
#     ]
# ])
