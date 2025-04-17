from fastapi import FastAPI
from starlette.staticfiles import StaticFiles

from nasa_client import fetch_space_fact
from models import SpaceFact
from typing import Optional

app = FastAPI(title="Space Facts API")

app.mount("/static", StaticFiles(directory="static", html=True), name="static")


@app.get("/space-fact", response_model=SpaceFact)
async def get_space_fact(date: Optional[str] = None):
    return await fetch_space_fact(date)
