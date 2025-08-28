from fastapi import FastAPI
from backend.routers import expense

app = FastAPI(
    title= "Control de gastos API",
    description="API para registrar y analizar gastos corrientes.",
    version="0.1.0"
)

#Routes
app.include_router(expense.router, prefix="/expenses", tags=["Expenses"])

@app.get("/health")
def dummy():
    return {"status":"ok"}