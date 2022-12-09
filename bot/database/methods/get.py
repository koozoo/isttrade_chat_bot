import datetime
import logging
from bot.database.main import engine
from sqlalchemy.orm import sessionmaker
from bot.database.models import *

session = sessionmaker(bind=engine)


class GetDataBase:
    async def get_user_where_id(self, uid):
        with session() as s:
            data = s.query(User).where(User.id == uid)
        return data

    async def get_products(self):
        with session() as s:
            data = s.query(Products)
        return data

    async def get_links_where_id(self, prod_id):
        with session() as s:
            data = s.query(Links).where(Links.product_id == prod_id)
        return data

    async def get_product_wher_title(self, title):
        with session() as s:
            data = s.query(Products).where(Products.title == title)

        return data

    async def get_product_by_id(self, prod_id):
        with session() as s:
            data = s.query(Products).where(Products.id == prod_id)

        return data

    async def get_category_where_title(self, title):
        with session() as s:
            data = s.query(Category).where(Category.title == title)
        return data

    async def get_all_category(self):
        with session() as s:
            data = s.query(Category).where(Category.sub_category == 0)
        return data

    async def get_products_by_cat_id(self, cat_id):
        with session() as s:
            data = s.query(Products).where(Products.category_id == cat_id)
        return data

    async def get_docs_link_by_prod_id(self, prod_id):
        with session() as s:
            data = s.query(Links).where(Links.product_id == prod_id)
        return data

    async def get_category_by_id(self, cat_id):
        with session() as s:
            data = s.query(Category).where(Category.id == cat_id)
        return data