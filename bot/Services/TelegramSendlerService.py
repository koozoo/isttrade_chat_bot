from bot.Services.SendlerService import SendlerService
from bot.misc.env import Stuff


class TelegramSendlerService(SendlerService):
    __slots__ = ["obj", "text", "method", "uid", "keyboard", "call_back", "theme"]

    def __init__(self, obj, text, uid, keyboard, call_back, theme="none", method="none"):
        super().__init__(obj, text, method)
        self.uid = uid
        self.keyboard = keyboard
        self.call_back = call_back
        self.theme = theme

    async def send_for_user(self):
        await self.obj.bot.send_message(self.uid, self.text, reply_markup=self.keyboard(self.call_back))

    async def send_for_stuff(self):
        msg = f"Клиент: {self.obj.from_user.full_name}\n" \
              f"Ссылка для связи в телеграмм: {self.obj.from_user.url}\n" \
              f"Тема: По вопросу {self.theme}."

        stuff = Stuff()
        for admin in stuff.ADMINS:
            await self.obj.bot.send_message(admin, msg)

    async def set_callback(self, callback):
        self.call_back = callback

    async def set_theme(self, theme):
        self.theme = theme



