import httpx
from typing import Optional, List
from models import SpaceFact, Asteroid
import os
from dotenv import load_dotenv

load_dotenv()

NASA_API_KEY = os.getenv("NASA_API_KEY", "DEMO_KEY")
NASA_URL = "https://api.nasa.gov/planetary/apod"

_cache: dict[str, SpaceFact] = {}

# Fetch SpaceFact Photo
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

# Fetch Asteroids
async def fetch_asteroids(date: str) -> List[Asteroid]:
    url = "https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        "start_date": date,
        "end_date": date,
        "api_key": NASA_API_KEY
    }

    async with httpx.AsyncClient() as client:
        response = await client.get(url, params=params)
        response.raise_for_status()
        data = response.json()

    raw_asteroids = data["near_earth_objects"].get(date, [])
    result = []

    for obj in raw_asteroids:
        approach = obj["close_approach_data"][0]
        est_diameter = obj["estimated_diameter"]["kilometers"]
        asteroid = Asteroid(
            name=obj["name"],
            close_approach_date=approach["close_approach_date"],
            estimated_diameter_km=(est_diameter["estimated_diameter_min"] + est_diameter["estimated_diameter_max"]) / 2,
            miss_distance_km=float(approach["miss_distance"]["kilometers"]),
            relative_velocity_kmh=float(approach["relative_velocity"]["kilometers_per_hour"]),
            is_potentially_hazardous=obj["is_potentially_hazardous_asteroid"]
        )
        result.append(asteroid)
    return result
