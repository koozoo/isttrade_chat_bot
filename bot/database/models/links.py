from sqlalchemy import Column, Integer, String, Text, Boolean, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from bot.database.models import *
from bot.database.main import Base


class Links(Base):
    __tablename__ = "links"

    id: Mapped[int] = mapped_column(primary_key=True)
    product_id: Mapped[int] = mapped_column(ForeignKey("products.id", ondelete="CASCADE"))
    products: Mapped["Products"] = relationship(back_populates="links")
    link = Column(String)

    def __init__(self, prod_id, link):
        self.product_id = prod_id
        self.link = link



