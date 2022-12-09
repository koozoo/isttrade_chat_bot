from bot.keyboards.inline import *
from aiogram.types import ParseMode


async def about(obj, uid, text, who_url):
    await obj.message.delete()

    msg = f'{text}...\n' \
          f'\nПодробнее на 🌐 <a href="{who_url}">сайте</a>)'

    await obj.bot.send_message(uid, msg, reply_markup=inline_back_menu("ABOUT"), parse_mode=ParseMode.HTML)
