from sqlalchemy import Column, Integer, String, Float, DateTime, ForeignKey
from backend.models.database import Base
from sqlalchemy.sql import func
from sqlalchemy.orm import relationship


class Expense(Base):
    __tablename__ = "expenses"

    id = Column(Integer, primary_key=True, index=True, autoincrement=True)
    amount = Column(Float, nullable=False)
    category_id = Column(Integer, ForeignKey("categories.id"), nullable=False)
    category = relationship("Category", back_populates="expenses")
    date = Column(DateTime(timezone=True), server_default=func.now())
    description = Column(String(255), nullable=True)
