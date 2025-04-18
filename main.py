from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.responses import FileResponse
from pathlib import Path
from nasa_client import fetch_space_fact, fetch_asteroids
from models import SpaceFact, Asteroid
from typing import Optional, List
from datetime import date as dt

app = FastAPI(title="Space Dashboard 🚀")

@app.get("/")
def root():
    file_path = Path(__file__).parent / "static" / "index.html"
    print(f"Serving file from: {file_path.resolve()}")
    return FileResponse(file_path)

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/space-fact", response_model=SpaceFact)
async def get_space_fact(date: Optional[str] = None):
    return await fetch_space_fact(date)

@app.get("/asteroids", response_model=List[Asteroid])
async def get_asteroids(date: Optional[str] = None):
    query_date = date or str(dt.today())
    return await fetch_asteroids(query_date)

@app.get("/debug")
def debug_path():
    path = Path(__file__).parent / "static" / "index.html"
    return {"exists": path.exists(), "path": str(path.resolve())}