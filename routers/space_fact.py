from fastapi import APIRouter
from typing import Optional
from models import SpaceFact
from nasa_client import fetch_space_fact

router = APIRouter(tags=["Space Facts"])

@router.get("/space-fact", response_model=SpaceFact)
async def get_space_fact(date: Optional[str] = None):
    return await fetch_space_fact(date)