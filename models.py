from pydantic import BaseModel
from typing import List

class SpaceFact(BaseModel):
    title: str
    explanation: str
    url: str
    date: str
    media_type: str

class Asteroid(BaseModel):
    name: str
    close_approach_date: str
    estimated_diameter_km: float
    miss_distance_km: float
    relative_velocity_kmh: float
    is_potentially_hazardous: bool