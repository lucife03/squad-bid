from fastapi import FastAPI, Request, Depends, Form, HTTPException
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.responses import HTMLResponse, RedirectResponse
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
from . import models, database
import os

app = FastAPI()

# Mount static files
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Setup templates
templates = Jinja2Templates(directory="app/templates")

# Create database tables
models.Base.metadata.create_all(bind=database.engine)

@app.get("/", response_class=HTMLResponse)
async def home(request: Request, db: Session = Depends(database.get_db)):
    deals = db.query(models.GroupDeal).all()
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "deals": deals}
    )

@app.post("/create-deal")
async def create_deal(
    product_name: str = Form(...),
    description: str = Form(...),
    original_price: float = Form(...),
    discount_percentage: float = Form(...),
    min_participants: int = Form(...),
    hours_active: int = Form(...),
    db: Session = Depends(database.get_db)
):
    deal = models.GroupDeal(
        product_name=product_name,
        description=description,
        original_price=original_price,
        discount_percentage=discount_percentage,
        min_participants=min_participants,
        end_time=datetime.utcnow() + timedelta(hours=hours_active)
    )
    db.add(deal)
    db.commit()
    db.refresh(deal)
    return RedirectResponse(url="/", status_code=303)

@app.post("/join-deal/{deal_id}")
async def join_deal(
    deal_id: int,
    name: str = Form(...),
    email: str = Form(...),
    db: Session = Depends(database.get_db)
):
    deal = db.query(models.GroupDeal).filter(models.GroupDeal.id == deal_id).first()
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    
    if not deal.is_active:
        raise HTTPException(status_code=400, detail="Deal has expired")
    
    participant = models.Participant(
        name=name,
        email=email,
        deal_id=deal_id
    )
    db.add(participant)
    db.commit()
    return RedirectResponse(url="/", status_code=303)

@app.get("/deal-status/{deal_id}")
async def deal_status(deal_id: int, db: Session = Depends(database.get_db)):
    deal = db.query(models.GroupDeal).filter(models.GroupDeal.id == deal_id).first()
    if not deal:
        raise HTTPException(status_code=404, detail="Deal not found")
    
    return {
        "current_participants": deal.current_participants,
        "min_participants": deal.min_participants,
        "is_active": deal.is_active,
        "time_remaining": (deal.end_time - datetime.utcnow()).total_seconds()
    } 