from sqlalchemy import Column, Integer, String, Text, Boolean
from sqlalchemy.orm import Mapped, mapped_column, relationship
from bot.database.models import *
from bot.database.main import Base


class Products(Base):
    __tablename__ = "products"

    id: Mapped[int] = mapped_column(primary_key=True)
    links: Mapped[list["Links"]] = relationship(
        back_populates="products",
        cascade="all, delete",
        passive_deletes=True
    )
    title = Column(String(250), nullable=False)
    description = Column(Text)
    link_img = Column(String)
    is_active = Column(Boolean)
    category_id = Column(Integer)

    def __init__(self, title, img, is_active, category,):
        self.title = title
        self.category_id = category
        self.is_active = is_active
        self.link_img = img

    def __str__(self):
        return self.title

    def set_description(self, description):
        self.description = description



