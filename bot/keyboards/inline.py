from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton


text_btn_back ="⤴️ назад"
btn_close = InlineKeyboardButton(text="❌", callback_data="BACK_CLOSE")


def inline_about():
    kb = InlineKeyboardMarkup(row_width=2)

    btns = [("Кто мы", "about_who"), ("Нам доверяют", "about_trust"), ("Поставщики", "about_suppliers")]

    btn_back = InlineKeyboardButton(text=text_btn_back, callback_data="BACK_ABOUT")

    for btn in btns:
        b = InlineKeyboardButton(text=f"{btn[0]}", callback_data=f"{btn[1]}")
        kb.add(b)

    kb.row(btn_back, btn_close)

    return kb


def inline_back_menu(action):
    kb = InlineKeyboardMarkup(row_width=2)

    back = InlineKeyboardButton(text=text_btn_back, callback_data=f"BACK_{action}")

    kb.row(back, btn_close)

    return kb


def inline_service():
    kb = InlineKeyboardMarkup(row_width=2)

    btns = [("🗺 Карта сервисного обслуживания", "service_map"),
            ("📨 Задать вопрос", "quest_SERVICE")]

    btn_back = InlineKeyboardButton(text=text_btn_back, callback_data="BACK_SERVICE")

    for btn in btns:
        b = InlineKeyboardButton(text=f"{btn[0]}", callback_data=f"{btn[1]}")
        kb.add(b)

    kb.row(btn_back, btn_close)

    return kb


def inline_contact():
    kb = InlineKeyboardMarkup(row_width=2)

    btns = [("МОСКВА", "contact_moskva"), ("САНКТ-ПЕТЕРБУРГ", "contact_spb"),
            ("КРАСНОДАР", "contact_krasnodar"),("САМАРА", "contact_samara")]

    btn_back = InlineKeyboardButton(text=text_btn_back, callback_data="BACK_CONTACT")

    for btn in btns:
        b = InlineKeyboardButton(text=f"🏙 {btn[0]}", callback_data=f"{btn[1]}")
        kb.add(b)

    kb.row(btn_back, btn_close)

    return kb


def inline_catalog_category(category: list):
    kb = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text=text_btn_back, callback_data="BACK_CATALOG")
    for btn in category:
        b = InlineKeyboardButton(text=f"{btn[1]}", callback_data=f"category_{btn[0]}")
        kb.add(b)
    kb.row(btn_back, btn_close)

    return kb


def inline_catalog_products(products: list):
    kb = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text=text_btn_back, callback_data="BACK_CATALOG")
    for btn in products:
        b = InlineKeyboardButton(text=f"{btn[1]}", callback_data=f"products_{btn[0]}")
        kb.add(b)
    kb.row(btn_back, btn_close)

    return kb


def inline_catalog_products_card():
    kb = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text=text_btn_back, callback_data="BACK_CATALOG_CATEGORY")
    btns = [("Купить", "quest_BUY_IN_CARD"),
            ("Задать вопрос", "quest_CONSULTATION_PROD"),
            ]
    for btn in btns:
        b = InlineKeyboardButton(text=f"{btn[0]}", callback_data=f"products_{btn[1]}")
        kb.add(b)
    kb.row(btn_back, btn_close)

    return kb


def inline_catalog_products_card_docs(docs):
    kb = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text=text_btn_back, callback_data="BACK_CATALOG_CARD")

    for btn in docs:
        b = InlineKeyboardButton(text=f"{btn[0]}", callback_data=f"docs_{btn[1]}")
        kb.add(b)
    kb.row(btn_back, btn_close)

    return kb


def inline_quest():
    kb = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text=text_btn_back, callback_data="BACK_QUEST")
    btns = [("Купить машину", "quest_BUY"),
            ("Cервис", "quest_SERVICE"),
            ("Другие вопросы", "quest_ANOTHER"),
            ]

    for btn in btns:
        b = InlineKeyboardButton(text=f"{btn[0]}", callback_data=f"{btn[1]}")
        kb.add(b)
    kb.row(btn_back, btn_close)

    return kb


def inline_buy():
    kb = InlineKeyboardMarkup(row_width=1)
    btn_back = InlineKeyboardButton(text=text_btn_back, callback_data="BACK_BUY")
    btns = [("Оставить заявку", "quest_BUY")
            ]

    for btn in btns:
        b = InlineKeyboardButton(text=f"{btn[0]}", callback_data=f"{btn[1]}")
        kb.add(b)
    kb.row(btn_back, btn_close)

    return kb


