from fastapi import APIRouter, Request, Form, Depends
from fastapi.templating import Jinja2Templates
from fastapi.responses import RedirectResponse

router = APIRouter()
templates = Jinja2Templates(directory="templates")

tickets = []

def is_authenticated(request: Request):
    return request.cookies.get("auth") == "authenticated"

@router.get("/dashboard")
def dashboard(request: Request):
    if not is_authenticated(request):
        return RedirectResponse(url="/")
    return templates.TemplateResponse("dashboard.html", {"request": request, "tickets": tickets})

@router.get("/create")
def create_form(request: Request):
    if not is_authenticated(request):
        return RedirectResponse(url="/")
    return templates.TemplateResponse("create_ticket.html", {"request": request})

@router.post("/create")
def create_ticket(request: Request,
                  title: str = Form(...),
                  description: str = Form(...),
                  customer_name: str = Form(...),
                  customer_email: str = Form(...),
                  customer_phone: str = Form(...),
                  priority: str = Form(...),
                  category: str = Form(...)):

    tickets.append({
        "title": title,
        "description": description,
        "customer_name": customer_name,
        "customer_email": customer_email,
        "customer_phone": customer_phone,
        "priority": priority,
        "category": category,
        "status": "Open"
    })
    return RedirectResponse(url="/dashboard", status_code=302)
