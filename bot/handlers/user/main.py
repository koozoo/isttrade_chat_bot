from aiogram import Dispatcher
from bot.handlers.user.EntryStep import Controller

user = Controller()


def register_user_handlers(dp: Dispatcher):

    # CMD_START
    dp.register_message_handler(user.start_cmd, commands=["start"])
# _________________________________________________________________________________________ #
    # CALL ACTION_BACK
    dp.register_callback_query_handler(user.back_hub, text_contains="BACK")
# _________________________________________________________________________________________ #
    # MSG ACTION_MAIN_MANU
    dp.register_message_handler(user.action_main_menu, lambda msg: not msg.text.isdigit())
# _________________________________________________________________________________________ #
    # CALL ACTION_ABOUT
    dp.register_callback_query_handler(user.action_about, text_contains="about")
# _________________________________________________________________________________________ #
    # CALL ACTION_SERVICE
    dp.register_callback_query_handler(user.action_service, text_contains="service")
# _________________________________________________________________________________________ #
    # CALL ACTION_CONTACT
    dp.register_callback_query_handler(user.action_contact, text_contains="contact")
# _________________________________________________________________________________________ #
    # CALL ACTION_QESTIONS
    dp.register_callback_query_handler(user.question_hub, text_contains="quest")
# _________________________________________________________________________________________ #
    # CALL ACTION_CATALOG
    # category
    dp.register_callback_query_handler(user.action_catalog, text_contains="category")
    # products
    dp.register_callback_query_handler(user.action_catalog_products, text_contains="products")
