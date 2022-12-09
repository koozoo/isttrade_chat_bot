from bot.keyboards.inline import *
from aiogram.types import ParseMode


async def contact(obj, uid, text, url):
    await obj.message.delete()

    msg = f'{text}\n' \
          f'\n<a href="{url}">.</a>'

    await obj.bot.send_message(uid, msg, reply_markup=inline_back_menu("CONTACT"), parse_mode=ParseMode.HTML)
