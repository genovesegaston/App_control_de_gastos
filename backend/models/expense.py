from importlib.metadata import requires
from sqlalchemy.orm import Session
from sqlalchemy import Column, Integer, String, Float, Date, ForeignKey
from database import Base, engine, SessionLocal
from dependencies import get_db
from categories import Category
from sqlalchemy.orm import relationship


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount = Column(Float,required = True)
    category_id = Column(Integer, ForeignKey("categories.id"),required = True)
    category = relationship("Category", back_populates="expenses")
    date = Column(Date)
    description = Column(String(255), nullable=True)
