from fastapi import FastAPI
from app.routes import login, connect, check, close

app = FastAPI(title="LinkedIn Automation API")

app.include_router(login.router)
app.include_router(connect.router)
app.include_router(check.router)
app.include_router(close.router)
