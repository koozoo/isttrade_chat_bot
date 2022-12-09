from sqlalchemy import Column, Integer, String, Boolean
from bot.database.main import Base


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    phone = Column(String(20))
    email = Column(String(100))
    referer = Column(String)
    is_stuff = Column(Boolean)

    def __init__(self, id, name, phone="none", ref="none", is_stuff=False):
        self.id = id
        self.name = name
        self.phone = phone
        self.referer = ref
        self.is_stuff = is_stuff


