from fastapi import APIRouter, Request, Form
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

router = APIRouter()
templates = Jinja2Templates(directory="templates")

USERNAME = "admin@example.com"
PASSWORD = "admin123"

@router.get("/")
def login_page(request: Request):
    return templates.TemplateResponse("login.html", {"request": request, "msg": ""})

@router.post("/login")
def login(request: Request, username: str = Form(...), password: str = Form(...)):
    if username == USERNAME and password == PASSWORD:
        response = RedirectResponse(url="/dashboard", status_code=302)
        response.set_cookie("auth", "authenticated")
        return response
    return templates.TemplateResponse("login.html", {"request": request, "msg": "Invalid credentials"})

@router.get("/logout")
def logout():
    response = RedirectResponse(url="/")
    response.delete_cookie("auth")
    return response
