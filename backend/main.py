from fastapi import FastAPI
from backend.routes import docs

app = FastAPI(title="My FastAPI Project")


app.include_router(docs.router)


@app.get("/hello")
def read_root():
    return {"message": "Welcome to FastAPI!"}
