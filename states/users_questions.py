from aiogram.dispatcher.filters.state import StatesGroup, State


class UsersQuestion(StatesGroup):
    # С чем связана проблема
    whats_the_problem = State()
    # Описание проблемы
    description_problem = State()
    # Фото проблемы (при наличии)
    photo_problem = State()
    # Имя обратившегося
    email_without_photo = State()
    # Почта обратившегося
    email_of_the_applicant = State()
    # Номер телефона обратившегося
    number_of_the_applicant = State()
