from bot.keyboards.inline import *
from aiogram.types import ParseMode


async def service(obj, uid, text, who_url):
    try:
        await obj.message.delete()
    except Exception as e:
        print(e)

    msg = f'{text}...\n' \
          f'\nПодробнее на 🌐 <a href="{who_url}">сайте</a>)' \
          f'<a href="https://isttrade.ru/images/pdf/wmf_950_s_09_2022_rub.pdf">.</a>'

    await obj.bot.send_message(uid, msg, reply_markup=inline_back_menu("SERVICE"), parse_mode=ParseMode.HTML)


