from backend.models.database import Base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship()


class Category(Base):
    __tablename__ = "categories"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    expenses = relationship("Expense",back_populates="category")
