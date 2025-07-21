from fastapi import FastAPI, Form, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

# In-memory storage
users = {"admin@example.com": "admin123"}
tickets = []

@app.get("/", response_class=HTMLResponse)
def home(request: Request):
    return templates.TemplateResponse("login.html", {"request": request})

@app.post("/login")
def login(email: str = Form(...), password: str = Form(...)):
    if users.get(email) == password:
        return RedirectResponse("/create-ticket", status_code=302)
    return {"error": "Invalid credentials"}

@app.get("/create-ticket", response_class=HTMLResponse)
def create_ticket_page(request: Request):
    return templates.TemplateResponse("create_ticket.html", {"request": request})

@app.post("/create-ticket")
def create_ticket(title: str = Form(...), description: str = Form(...)):
    tickets.append({"title": title, "description": description})
    return RedirectResponse("/tickets", status_code=302)

@app.get("/tickets", response_class=HTMLResponse)
def list_tickets(request: Request):
    return templates.TemplateResponse("tickets.html", {"request": request, "tickets": tickets})
