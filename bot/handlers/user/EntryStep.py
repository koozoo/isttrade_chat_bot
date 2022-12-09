from aiogram.types import Message, CallbackQuery, ParseMode
from bot.keyboards.reply import *
from bot.keyboards.inline import *
from bot.instance.StaticText import *
from bot.handlers.user.template import about as ab, service as se, contact as ct
from bot.Services import TelegramSendlerService, EmailSendlerService, Parser
from bot.misc.env import Stuff
from bot.database.models import *
from bot.database.methods import *


add_db = InsertDataBase()
get_db = GetDataBase()
update_db = UpdateDataBase()


class Controller:
    __storage = {}

    def get_storage(self):
        return self.__storage

    async def start_cmd(self, message: Message):

        ref_id = message.text[7:]
        uid = message.from_user.id
        name = message.from_user.full_name
        # GET USER DATA
        data = [(item.id, item.is_stuff) for item in await get_db.get_user_where_id(uid)]

        await message.delete()

        if data:
            # RESUME USER
            if uid in Stuff.ADMINS and data[0][1] == 0:
                is_stuff = await update_db.update_user_admin(uid, 1)
            elif uid not in Stuff.ADMINS:
                is_stuff = await update_db.update_user_admin(uid, 0)
            else:
                is_stuff = data[0][1]

            if is_stuff == 1:
                msg = admin_menu_t(name)
                await message.bot.send_message(uid, msg, reply_markup=admin_kb(), parse_mode=ParseMode.HTML)
            else:
                msg = main_menu_t(name)
                await message.bot.send_message(uid, msg, reply_markup=main_kb(), parse_mode=ParseMode.HTML)
        else:
            # NEW USER

            if uid in Stuff.ADMINS:

                if ref_id:
                    item = User(uid, name, ref=ref_id, is_stuff=True)
                else:
                    item = User(uid, name, is_stuff=True)

                await add_db.add_item(item)

                msg = admin_menu_t(name)
                await message.bot.send_message(uid, msg, reply_markup=admin_kb(), parse_mode=ParseMode.HTML)
            else:

                if ref_id:
                    item = User(uid, name, ref=ref_id, is_stuff=False)
                else:
                    item = User(uid, name, is_stuff=False)

                await add_db.add_item(item)

                msg = main_menu_t(name)
                await message.bot.send_message(uid, msg, reply_markup=main_kb(), parse_mode=ParseMode.HTML)

    async def back_hub(self, call: CallbackQuery):
        uid = call.from_user.id
        match call.data:
            case "BACK_ABOUT":
                await call.message.delete()
                msg = about_t
                await call.bot.send_message(uid, msg, reply_markup=inline_about(), parse_mode=ParseMode.HTML)
            case "BACK_SERVICE":
                await call.message.delete()
                msg = f'<a href="{service_cert_url}">.</a>\n'\
                    f'{service_t}\n'
                await call.bot.send_message(uid, msg, reply_markup=inline_service(), parse_mode=ParseMode.HTML)
            case "BACK_CONTACT":
                await call.message.delete()
                msg = f'{contact_t}\n'
                await call.bot.send_message(uid, msg, reply_markup=inline_contact(), parse_mode=ParseMode.HTML)
            case "BACK_QUEST":
                await call.message.delete()
                msg = f'{question_t}\n'
                await call.bot.send_message(uid, msg, reply_markup=inline_quest(), parse_mode=ParseMode.HTML)
            case "BACK_BUY":
                await call.message.delete()
                msg = f'{buy_t}\n'
                await call.bot.send_message(uid, msg, reply_markup=inline_buy(), parse_mode=ParseMode.HTML)
            case "BACK_CATALOG":
                await call.message.delete()
                msg = f'{catalog_t}\n'
                category = [(item.id, item.title) for item in await get_db.get_all_category()]
                await call.bot.send_message(uid, msg, reply_markup=inline_catalog_category(category), parse_mode=ParseMode.HTML)
            case "BACK_CATALOG_CATEGORY":
                await call.message.delete()
                data = [(item.id, item.title) for item in await get_db.get_products_by_cat_id(int(self.__storage["cat_id"]))]
                cat_img = [item.img for item in await get_db.get_category_by_id(int(self.__storage["cat_id"]))]

                msg = f'\n<a href="{cat_img[0]}">.</a>'
                await call.bot.send_message(call.from_user.id, msg, reply_markup=inline_catalog_products(data),
                                            parse_mode=ParseMode.HTML)
            case "BACK_CLOSE":
                await call.message.delete()

    async def action_main_menu(self, message: Message):
        uid = message.from_user.id
        match message.text:
            case "🏬 О компании":
                await message.delete()
                msg = about_t
                await message.bot.send_message(uid, msg, reply_markup=inline_about(), parse_mode=ParseMode.HTML)
            case "🧑🏼‍🔧 Сервис":
                await message.delete()
                msg = f'<a href="{service_cert_url}">.</a>\n'\
                    f'{service_t}\n'
                await message.bot.send_message(uid, msg, reply_markup=inline_service(), parse_mode=ParseMode.HTML)
            case "📍 Контакты":
                await message.delete()
                msg = contact_t
                await message.bot.send_message(uid, msg, reply_markup=inline_contact(), parse_mode=ParseMode.HTML)
            case "📲 Задать вопрос":
                await message.delete()
                msg = question_t
                await message.bot.send_message(uid, msg, reply_markup=inline_quest(), parse_mode=ParseMode.HTML)
            case "💵 Купить кофемашину":
                await message.delete()
                msg = buy_t
                await message.bot.send_message(uid, msg, reply_markup=inline_buy(), parse_mode=ParseMode.HTML)
            case "☕️ Каталог":
                await message.delete()
                msg = catalog_t
                category = [(item.id, item.title, item.img) for item in await get_db.get_all_category()]
                self.__storage[f"{category[0][0]}"] = category[0][2]
                await message.bot.send_message(uid, msg, reply_markup=inline_catalog_category(category), parse_mode=ParseMode.HTML)
            case "Обновить каталог": # перенести в админскую часть
                await message.delete()
                msg = "Товары обновлены..."
                await message.answer("Процес обновления запущен...")
                await Parser.update_catalog()
                await message.bot.send_message(uid, msg, reply_markup=admin_kb(),
                                               parse_mode=ParseMode.HTML)

    async def question_hub(self, call: CallbackQuery):

        uid = call.from_user.id
        quest_category = ("", "")
        msg_for_stuff = f"{call.from_user.full_name}, оставил заявку на обратную связь в телеграм, из раздела "
        msg = f"{call.from_user.full_name}\n" \
              f"В ближайшее время мы с вами свяжемся."
        subject = f"Заявка на обратную связь от {call.from_user.full_name}, тема: "
        sendler_email = EmailSendlerService.EmailSendlerService(call, msg_for_stuff,
                                                                call.from_user.full_name,
                                                                subject)
        sendler_tg = TelegramSendlerService.TelegramSendlerService(call, msg, uid, inline_back_menu, quest_category[0])

        match call.data:
            case "quest_SERVICE":
                quest_category = ("SERVICE", "Сервис")

                await call.message.delete()
                await sendler_tg.set_callback(quest_category[0])

                await sendler_tg.send_for_user()
                await sendler_tg.set_theme("сервесного обслуживания.")
                await sendler_tg.send_for_stuff()

                subject += quest_category[1]
                msg_for_stuff += quest_category[1]

                await sendler_email.set_email_attr(subject, msg_for_stuff)
                await sendler_email.send_for_stuff()

            case "quest_ANOTHER":
                quest_category = ("QUEST", "Другой")

                await call.message.delete()
                await sendler_tg.set_callback(quest_category[0])

                await sendler_tg.send_for_user()
                ###############################################
                await sendler_tg.set_theme("по другому вопросу")
                ###############################################
                await sendler_tg.send_for_stuff()

                subject += quest_category[1]
                msg_for_stuff += quest_category[1]

                await sendler_email.set_email_attr(subject, msg_for_stuff)
                await sendler_email.send_for_stuff()
            case "quest_BUY":
                quest_category = ("BUY", "Покупка")

                await call.message.delete()
                await sendler_tg.set_callback(quest_category[0])

                await sendler_tg.send_for_user()
                await sendler_tg.set_theme("покупки продукции.")
                await sendler_tg.send_for_stuff()

                subject += quest_category[1]
                msg_for_stuff += quest_category[1]

                await sendler_email.set_email_attr(subject, msg_for_stuff)
                await sendler_email.send_for_stuff()

    async def action_about(self, call: CallbackQuery):
        uid = call.from_user.id
        match call.data:
            case "about_who": await ab.about(call, uid, who_t, who_url)
            case "about_trust": await ab.about(call, uid, trus_t, trust_url)
            case "about_suppliers": await ab.about(call, uid, supple_t, supple_url)

    async def action_service(self, call: CallbackQuery):
        uid = call.from_user.id
        match call.data:
            case "service_map": await se.service(call, uid, map_service_t, map_service_url)

    async def action_contact(self, call: CallbackQuery):
        uid = call.from_user.id
        match call.data:
            case "contact_moskva": await ct.contact(call, uid, contact_map_moskva_t, contact_map_moskva_url)
            case "contact_spb": await ct.contact(call, uid, contact_map_spb_t, contact_map_spb_url)
            case "contact_krasnodar": await ct.contact(call, uid, contact_map_krasnodar_t, contact_map_krasnodar_url)
            case "contact_samara": await ct.contact(call, uid, contact_map_samara_t, contact_map_samara_url)

    async def action_catalog(self, call: CallbackQuery):
        cat_id = call.data.split("_")[1]
        self.__storage["cat_id"] = cat_id
        if cat_id:
            await call.message.delete()
            data = [(item.id, item.title) for item in await get_db.get_products_by_cat_id(int(cat_id))]
            cat_img = [item.img for item in await get_db.get_category_by_id(int(cat_id))]

            msg = f'\n<a href="{cat_img[0]}">.</a>'
            await call.bot.send_message(call.from_user.id, msg, reply_markup=inline_catalog_products(data),
                                        parse_mode=ParseMode.HTML)

    async def action_catalog_products(self, call: CallbackQuery):
        uid = call.from_user.id
        prod_id = call.data.split("_")[1]
        if prod_id:
            await call.message.delete()
            data = [(item.id, item.title, item.link_img) for item in await get_db.get_product_by_id(int(prod_id))]
            docs_links = [item.link for item in await get_db.get_docs_link_by_prod_id(int(prod_id))]

            link_msg = f'<a href="{data[0][2]}">.</a>\n'

            for link in docs_links:
                link_msg += f'\n<a href="{link}">Прайс/Инструкция</a>\n'

            msg = f'<b>Модель:</b> {data[0][1]}\n\n{product_t}\n{link_msg}'

            await call.bot.send_message(uid, msg, reply_markup=inline_catalog_products_card(),
                                        parse_mode=ParseMode.HTML)
