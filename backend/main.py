from fastapi import FastAPI,APIRouter
from backend.routers.expense import expense

app = FastAPI(
    title= "Control de gastos API",
    description="API para registrar y analizar gastos corrientes.",
    version="0.1.0"
)

#Routes
app.include_router(expense, prefix="/expenses", tags=["Expenses"])

@app.get("/health")
def dummy():
    return {"status":"ok"}