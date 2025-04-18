from fastapi import APIRouter
from typing import Optional, List
from models import Asteroid
from nasa_client import fetch_asteroids
from datetime import date as dt

router = APIRouter(tags=["Asteroids"])

@router.get("/asteroids", response_model=List[Asteroid])
async def get_asteroids(date: Optional[str] = None):
    query_date = date or str(dt.today())
    return await fetch_asteroids(query_date)