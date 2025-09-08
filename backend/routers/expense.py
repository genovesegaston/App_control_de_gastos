from fastapi import APIRouter

app = FastAPI()


@expense.get("/")
def expenses():
    return {"status": "ok", "route": "/expenses"}
