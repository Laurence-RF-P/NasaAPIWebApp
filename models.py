from pydantic import BaseModel

class SpaceFact(BaseModel):
    title: str
    explanation: str
    url: str
    date: str
    media_type: str