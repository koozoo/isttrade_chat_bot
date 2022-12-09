import datetime
import logging
from bot.database.main import engine
from sqlalchemy.orm import sessionmaker

session = sessionmaker(bind=engine)


class InsertDataBase:
    async def add_item(self, obj):
        with session() as s:
            s.add(obj)
            s.commit()
            logging.info(f"item add in data base {datetime.datetime.now()}")

    async def add_item_autoincrement(self, obj):
        with session() as s:
            s.add(obj)
            s.flush()
            s.commit()
            logging.info(f"item add in data base {datetime.datetime.now()}")
