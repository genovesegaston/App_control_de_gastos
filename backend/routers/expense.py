from fastapi import FastAPI

app = FastAPI()


@app.get("/")
def expenses():
    return {"status": "ok", "route": "/expenses"}
