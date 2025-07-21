from db import Base, engine

# Create tables on startup
Base.metadata.create_all(bind=engine)
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from auth import router as auth_router
from ticket_routes import router as ticket_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
app.include_router(auth_router)
app.include_router(ticket_router)
from fastapi import Request
from fastapi.templating import Jinja2Templates
from db import SessionLocal, Ticket

