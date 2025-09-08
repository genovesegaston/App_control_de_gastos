from fastapi import APIRouter

expense = APIRouter()

@expense.get("/")
def expenses():
    return {"status":"ok","route":"/expenses","hotReload":"ok"}