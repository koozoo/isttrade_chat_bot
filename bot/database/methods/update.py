import datetime
import logging
from bot.database.main import engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import update
from bot.database.models import *

session = sessionmaker(bind=engine)


class UpdateDataBase:

    async def update_user_admin(self, uid, status):
        with session() as s:
            s.execute(
                update(User).where(User.id == uid)
                .values(is_stuff=status)
            )

            s.commit()
        return status

