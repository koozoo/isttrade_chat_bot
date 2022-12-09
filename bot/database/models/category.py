from sqlalchemy import Column, Integer, String, Text
from bot.database.main import Base


class Category(Base):
    __tablename__ = "categorys"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    img = Column(String)
    sub_category = Column(String)

    def __init__(self, title):
        self.title = title

    def __str__(self):
        return self.title

    def set_sub_category(self, parent):
        self.sub_category = parent
