from aiogram.types import ReplyKeyboardMarkup, ReplyKeyboardRemove, KeyboardButton


def main_kb():
    btn_service = KeyboardButton(text="🧑🏼‍🔧 Сервис")
    btn_question = KeyboardButton(text="📲 Задать вопрос")
    btn_buy = KeyboardButton(text="💵 Купить кофемашину")
    btn_catalog = KeyboardButton(text="☕️ Каталог")
    btn_contact = KeyboardButton(text="📍 Контакты")
    btn_about = KeyboardButton(text="🏬 О компании")

    m = ReplyKeyboardMarkup(resize_keyboard=True)

    m.row(btn_catalog, btn_buy).row(btn_service).row(btn_question, btn_contact, btn_about)

    return m


def admin_kb():
    btn_stat = KeyboardButton(text="Статистика")
    btn_edit = KeyboardButton(text="Редактировать")
    btn_cat = KeyboardButton(text="Обновить каталог")

    btn_service = KeyboardButton(text="🧑🏼‍🔧 Сервис")
    btn_question = KeyboardButton(text="📲 Задать вопрос")
    btn_buy = KeyboardButton(text="💵 Купить кофемашину")
    btn_catalog = KeyboardButton(text="☕️ Каталог")
    btn_contact = KeyboardButton(text="📍 Контакты")
    btn_about = KeyboardButton(text="🏬 О компании")

    m = ReplyKeyboardMarkup(resize_keyboard=True)

    m.row(btn_cat).row(btn_stat, btn_edit).row(btn_catalog, btn_buy).row(btn_service).row(btn_question, btn_contact, btn_about)

    return m
