from fastapi import FastAPI
from backend.routers import category, expense

# from models.database import session

app = FastAPI(
    title= "Control de gastos API",
    description="API para registrar y analizar gastos corrientes.",
    version="0.1.0"
)

#Routes
app.include_router(expense.router, prefix="/expenses", tags=["Expenses"])
app.include_router(category.router, prefix="/category", tags=["category"])



@app.get("/health")
def dummy():
    return {"status":"ok"}