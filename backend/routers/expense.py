from fastapi import APIRouter
from backend.models.database import session
from backend.schemas.expense import ExpensesCreate

router = APIRouter()



@router.get("/")
def expenses():
    return {"status": "ok", "route": "/expenses"}

@router.post("/")
def expenses_post(new_expense: ExpensesCreate):
    session.add(new_expense)