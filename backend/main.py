from typing import Union
from fastapi import FastAPI

app = FastAPI(
    title= "Control de gastos API",
    description="API para registrar y analizar gastos corrientes.",
    version="0.1.0"
)

@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/health")
def dummy():
    return {"status":"ok"}