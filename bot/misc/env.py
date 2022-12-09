import os
from typing import Final
from dotenv import load_dotenv

load_dotenv()


class TgKeys:
    TOKEN: Final = os.getenv('TOKEN')


class Stuff:
    Admin: Final = int(os.getenv("ADMIN"))
    Admin2: Final = int(os.getenv("ADMIN2"))
    admin_email = os.getenv("ADMIN_EMAIL")
    admin2_email = os.getenv("ADMIN2_EMAIL")
    ADMINS = [Admin, Admin2]
    ADMINS_EMAIL = [admin_email, admin2_email]


class Email:
    EMAIL_LOGIN: Final = os.getenv("EMAIL_LOGIN")
    EMAIL_PWD: Final = os.getenv("EMAIL_PWD")
