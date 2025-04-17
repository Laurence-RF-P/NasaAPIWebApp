import httpx
from typing import Optional
from models import SpaceFact
import os
from dotenv import load_dotenv

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
NASA_URL = "https://api.nasa.gov/planetary/apod"

_cache: dict[str, SpaceFact] = {}

async def fetch_space_fact(date: Optional[str] = None) -> SpaceFact:
    key = date or "today"

    if key in _cache:
        print(f'[CACHE HIT] Returned cached data for {key}')
        return _cache[key]

    print(f"[CACHE MISS] Fetching data from NASA for {key}")
    params = {"api_key": NASA_API_KEY}
    if date:
        params['date'] = date

    async with httpx.AsyncClient() as client:
        response = await client.get(NASA_URL, params=params)
        response.raise_for_status()
        data = response.json()
        fact = SpaceFact(**data)
        _cache[key] = fact
        return fact
