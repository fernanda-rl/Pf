from fastapi import FastAPI
from app.routes import router

app = FastAPI(title="API Academia Crossfit TDD")
app.include_router(router)
