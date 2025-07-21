from fastapi import Form
from db import SessionLocal, Ticket

@app.post("/create-ticket")
async def create_ticket(
    title: str = Form(...),
    description: str = Form(...),
    customer_name: str = Form(...),
    email: str = Form(...)
):
    db = SessionLocal()
    ticket = Ticket(
        title=title,
        description=description,
        customer_name=customer_name,
        email=email
    )
    db.add(ticket)
    db.commit()
    db.refresh(ticket)
    db.close()
    return RedirectResponse("/dashboard", status_code=303)
