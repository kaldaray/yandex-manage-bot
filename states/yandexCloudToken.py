from aiogram.dispatcher.filters.state import StatesGroup, State


class FolderId(StatesGroup):
    id = State()
    yc_iam_token = State()
    yc_list_instances = State()
