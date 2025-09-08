from pydantic import BaseModel, ConfigDict
from datetime import date
from categories import CategoryOut


class ExpensesBase(BaseModel):
    amount: float
    category: CategoryOut
    date: date
    description: str | None = None


class ExpensesCreate(ExpensesBase):
    category_id: int


class Expenses(ExpensesBase):
    id: int
    category: CategoryOut
    model_config = ConfigDict(from_attributes=True)
